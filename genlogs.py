import logging
import pandas as pd
logging.basicConfig(filename='test.log',
                    filemode='a',
                    format='%(asctime)s %(name)s %(levelname)s %(message)s',
                    datefmt='%Y-%m-%d %H:%M:%S',
                    level=logging.DEBUG)


df = pd.read_csv("sqli.csv",encoding='utf-16', delimiter=',')
for row in df['Sentence'].to_list():
    print(row[1])
logger = logging.getLogger('QueryLogger')
logger.info("test123")
