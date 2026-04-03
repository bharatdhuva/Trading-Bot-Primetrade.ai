import logging
import sys

def setup_logger():
    logger = logging.getLogger("TradingBot")
    if logger.handlers:
        return logger
        
    logger.setLevel(logging.DEBUG)

    # File handler (Logs everything including DEBUG)
    file_handler = logging.FileHandler("bot.log")
    file_handler.setLevel(logging.DEBUG)
    file_formatter = logging.Formatter(
        '%(asctime)s - %(name)s - %(levelname)s - %(message)s'
    )
    file_handler.setFormatter(file_formatter)

    # Console handler (Only warnings/errors if any)
    console_handler = logging.StreamHandler(sys.stdout)
    console_handler.setLevel(logging.WARNING)
    console_formatter = logging.Formatter(
        '%(levelname)s: %(message)s'
    )
    console_handler.setFormatter(console_formatter)

    logger.addHandler(file_handler)
    logger.addHandler(console_handler)

    return logger

logger = setup_logger()
