import logging
import time

logging.basicConfig(level=logging.INFO) 
logger = logging.getLogger("ten1")


def state():
    state = "success"
    return state

def is_success():
    if state not in ("success","fail"):
        logger.error(f"结果{state}")
    else:
        logger.info(f"结果{state}")    
    return state == "success"

print(is_success())