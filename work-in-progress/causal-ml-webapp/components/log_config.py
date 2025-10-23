import logging
from typing import Final

def get_logger(name: str) -> logging.Logger:
    logging.basicConfig(
        level=logging.INFO,
        format="%(asctime)s %(levelname)s %(message)s",
        datefmt="%Y-%m-%d %H:%M:%S",
        filename="file.log",
        filemode="a",
        force=True,
    )
    logger: Final = logging.getLogger(name)
    logger.setLevel(level=logging.WARNING)

    return logger