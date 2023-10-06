import logging


def test_logging():
    logger = logging.getLogger(__name__)  # This will catch the test case name and prints the file name
    #logger.addHandler()  # pass fileHandler object here
    f_handler = logging.FileHandler('file.log')
    f_handler.setLevel(logging.DEBUG)
    f_format = logging.Formatter('%(asctime)s : %(levelname)s : %(name)s : %(message)s')
    f_handler.setFormatter(f_format)
    logger.addHandler(f_handler)
    logger.debug("This is a debug statment executed using logger")
    logger.info("This is Info logger")
    logger.error("This we use to mention data related to failed test")
    logger.warning("This is used to give warning message without failing a test")
    logger.critical("This will be used to print critical information")
    # logging.basicConfig(level=logging.DEBUG)
    # logging.debug('This will get logged')
