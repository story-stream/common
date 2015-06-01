import logging as py_logging
import pymongo
from datetime import datetime


class MongoHandler(py_logging.Handler):

    def __init__(self, connection, level=py_logging.NOTSET):
        client = pymongo.MongoClient(connection)
        self.__connection = connection
        self.db = client.get_default_database()

        super(MongoHandler, self).__init__(level)

    def connection(self):
        return self.__connection

    def emit(self, record):
        log_model = {
            'created': datetime.utcnow(),
            'name': record.name,
            'module': record.module,
            'func_name': record.funcName,
            'line_no': record.lineno,
            'thread': record.thread,
            'thread_name': record.threadName,
            'process': record.process,
            'message': record.msg,
            'args': str(record.args)
        }

        self.db[record.levelname.lower()].insert(log_model)