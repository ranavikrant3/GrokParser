import logging
logging.basicConfig(filename='test.log',
                    filemode='a',
                    format='%(asctime)s %(name)s %(levelname)s %(message)s',
                    datefmt='%Y-%m-%d %H:%M:%S',
                    level=logging.DEBUG)



logger = logging.getLogger('QueryLogger')
logger.info("test123")