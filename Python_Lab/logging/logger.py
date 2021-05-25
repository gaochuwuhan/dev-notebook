import logging
import time

'''日志级别大小关系为：NOTSET < DEBUG < INFO < WARNING < ERROR < CRITICAL'''
logging.basicConfig(level=logging.INFO)  #logging 模块的基本默认等级，低于这个等级的日志不会被打印
logger = logging.getLogger("global")

# def add(x,y):
#     logger.info("START ADD")
#     print (x+y)
#     logger.info("finish add")

# add(1,3)

# while True:
#     for i in range(1,4):
#         logger.info('i为{}'.format(i))
#         print('第',i,'次:',1)
#         time.sleep(3)
#     if i==3:
#         break