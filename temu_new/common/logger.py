from loguru import logger
from tenacity import _utils
from common.proxy import get_proxy

logger.add(
    sink='log/temu.log',
    level='INFO',
    encoding='utf-8',
    enqueue=True,
    format="{time:YYYY-MM-DD HH:mm:ss} | {level} | {module} | {file} | {message}",
    # rotation=1,
    # retention=7
)


def retry_loger(retry_state):
    sec_format = "%0.3f"
    if retry_state.fn is None:
        # NOTE(sileht): can't really happen, but we must please mypy
        fn_name = "<unknown>"
    else:
        fn_name = _utils.get_callback_name(retry_state.fn)
    logger.warning(
        f"函数 '{fn_name}' "
        f"耗时 {sec_format % retry_state.seconds_since_start}(s), "
        f"第{_utils.to_ordinal(retry_state.attempt_number)} 次重试"
        f"异常内容{retry_state.outcome.exception()}"
    )


def req_retry(session):

    class Retry():
        def __init__(self, session):
            self.session = session
        def retry_loger(self, retry_state):
            sec_format = "%0.3f"
            try:
                if session.proxies:
                    session.proxies = get_proxy(3)
                    logger.info(f"请求失败,切换代理>{session.proxies}")
                else:
                    logger.info(f"没有代理>{session.proxies}")

            except Exception as e:
                logger.error(f"请求失败,代理切换失败, {e}")
            if retry_state.fn is None:
                # NOTE(sileht): can't really happen, but we must please mypy
                fn_name = "<unknown>"
            else:
                fn_name = _utils.get_callback_name(retry_state.fn)
            logger.warning(
                f"函数 '{fn_name}' "
                f"耗时 {sec_format % retry_state.seconds_since_start}(s), "
                f"第{_utils.to_ordinal(retry_state.attempt_number)} 次重试"
                f"异常内容{retry_state.outcome.exception()}"
            )
    r = Retry(session)
    return r.retry_loger


def email_after_loger(retry_state):
    retry_state.outcome.exception()
    sec_format = "%0.3f"

    logger.warning(
        f"本次查询耗时 {sec_format % retry_state.seconds_since_start}(s), "
        f"查询失败原因 {retry_state.outcome.exception()}"
    )
def email_before_log(stats):
    logger.info(f"正在获取邮箱验证码..请稍后...第{stats.attempt_number}次查询")