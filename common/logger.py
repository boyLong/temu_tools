from loguru import logger

logger.add(
    sink='log/temu.log',
    level='INFO',
    encoding='utf-8',
    enqueue=True,
    format="{time:YYYY-MM-DD HH:mm:ss} | {level} | {module} | {file} | {message}",
    rotation=1,
    retention=7
)