import logging
import logging.handlers as handlers
import time

logger = logging.getLogger('my_app')
logger.setLevel(logging.INFO)

logHandler = handlers.RotatingFileHandler('RotatingFileHandler.log', maxBytes=500, backupCount=2)
# logHandler = handlers.TimedRotatingFileHandler('TimedRotatingFileHandler.log',
                        # when='S', interval=5,backupCount=2)
logHandler.setLevel(logging.INFO)
logger.addHandler(logHandler)

def main():
    while True:
        time.sleep(1)
        logger.info("A Sample Log Statement")

main()