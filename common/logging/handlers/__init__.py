import logging as py_logging
from mongo import MongoHandler

__all__ = [
    'create'
]


def __get_class(kls):
    parts = kls.split('.')
    module = ".".join(parts[:-1])
    m = __import__(module)
    for comp in parts[1:]:
        m = getattr(m, comp)

    return m


def __get_params(handler):
    params = {}
    for key, value in handler.iteritems():
        if key not in ['class', 'level']:
            params[key] = value

    return params


def create(config):
    handler_config = config.get('handler')

    params = __get_params(handler_config)
    handler = __get_class(handler_config.get('class'))(**params)
    handler.setLevel(getattr(py_logging, handler_config.get('level'), py_logging.INFO))

    return handler