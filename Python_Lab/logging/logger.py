import logging

logger = logging.getLogger("django")

def add(x,y):
    logger.info("START ADD")
    print (x+y)
    logger.info("finish add")

add(1,3)