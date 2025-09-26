import logging
from ..config import BaseConfigs

def setup_logger(name: str) -> logging.Logger:
    """
    Настраивает логгер:
    - INFO выводится и в консоль, и в файл
    - остальные уровни только в файл
    """
    logger = logging.getLogger(name)
    logger.setLevel(logging.DEBUG)
    
    class InfoFilter(logging.Filter):
        def filter(self, record: logging.LogRecord) -> bool:
            return record.levelno == logging.INFO

    file_handler = logging.FileHandler(BaseConfigs.log_file_path, encoding="utf-8")
    file_handler.setLevel(logging.DEBUG)
    file_formatter = logging.Formatter(
        "%(asctime)s - %(name)s - %(levelname)s - %(message)s"
    )
    file_handler.setFormatter(file_formatter)

    console_handler = logging.StreamHandler()
    console_handler.setLevel(logging.INFO)
    console_handler.addFilter(InfoFilter())
    console_formatter = logging.Formatter("%(levelname)s: %(message)s")
    console_handler.setFormatter(console_formatter)

    if not logger.handlers:
        logger.addHandler(file_handler)
        logger.addHandler(console_handler)

    return logger
