import inspect
import logging


class BaseClass:
    def getLogger(self):
        loggerName = inspect.stack()[1][3]
        logger = logging.getLogger(loggerName)
        f_handler = logging.FileHandler('file.log')
        f_handler.setLevel(logging.DEBUG)
        f_format = logging.Formatter('%(asctime)s : %(levelname)s : %(name)s : %(message)s')
        f_handler.setFormatter(f_format)
        logger.addHandler(f_handler)
        return logger
