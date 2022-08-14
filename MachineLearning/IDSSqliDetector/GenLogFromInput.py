import logging
import pandas as pd
logging.basicConfig(filename='test.log',
                    filemode='a',
                    format='%(asctime)s %(name)s %(levelname)s %(message)s',
                    datefmt='%Y-%m-%d %H:%M:%S',
                    level=logging.DEBUG)
logger = logging.getLogger('SQLQueryLogger')

if __name__ == '__main__':
    while True:
        logger.info(input('Enter SQL Query to Log: '))