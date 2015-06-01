import logging as py_logging
from logging.config import dictConfig
from common.logging import handlers

__all__ = [
    'get_logger',
    'configure'
]


class LEVEL:
    CRITICAL = 50
    FATAL = CRITICAL
    ERROR = 40
    WARNING = 30
    WARN = WARNING
    INFO = 20
    DEBUG = 10
    NOTSET = 0


def get_logger(name=None):
    """
    Return a logger with the specified name, creating it if necessary.

    If no name is specified, return the root logger.
    :param name: The name of the logger instance
    :return: A log instance
    """
    return py_logging.getLogger(name)


def getLogger(name=None):
    """
    Return a logger with the specified name, creating it if necessary.

    If no name is specified, return the root logger.
    :param name: The name of the logger instance
    :return: A log instance
    """
    return get_logger(name)


def configure(logger, config, level=LEVEL.INFO):
    """
    Configures a logger instance from a configuration section.

    :param logger: The logger instance to configure
    :param config: A configuration dictionary instance
    :param level: The minimum logging level to listen for
    :return: The configured logger
    """
    if not logger.handlers:
        dictConfig(config)
        logger.setLevel(level)

    return logger