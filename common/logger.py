from loguru import logger

logger.add(
    sink='temu_login.log',
    level='INFO',
    encoding='utf-8',
    enqueue=True,
    format="{time:YYYY-MM-DD HH:mm:ss} | {level} | {module} | {file} | {message}"
)