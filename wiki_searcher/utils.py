import logging
import sys


def configure_logger(name: str) -> logging.Logger:
    logger = logging.getLogger(name)
    logger.setLevel(logging.DEBUG)

    ch = logging.StreamHandler(sys.stdout)
    ch.setLevel(logging.DEBUG)

    formatter = logging.Formatter('%(asctime)s %(name)s %(levelname)s [%(filename)s:%(lineno)d] %(message)s')
    ch.setFormatter(formatter)

    logger.addHandler(ch)

    return logger
