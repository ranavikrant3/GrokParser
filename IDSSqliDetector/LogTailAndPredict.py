import time
import pickle
import logging
logging.basicConfig(filename='ids.log',
                    filemode='a',
                    format='%(asctime)s %(name)s %(levelname)s %(message)s',
                    datefmt='%Y-%m-%d %H:%M:%S',
                    level=logging.DEBUG)
logger = logging.getLogger('IDSLogger')


file = open("test.log", "r")
clf = pickle.load(open('model.bin', 'rb'))
vectorizer = pickle.load(open('vectorizer.bin', 'rb'))

while True:
    pos = file.tell()
    line = file.readline()
    if not line:
        time.sleep(1)
        file.seek(pos)
    else:
        X_predict = []
        query = line.strip().split("INFO")[1]
        X_predict.append(query)
        X_predict = vectorizer.transform(X_predict)
        y_Predict = clf.predict(X_predict)
        for i in range(len(y_Predict)):
            if y_Predict[i] == 1:
                logger.info('Possible SQLI Attempt: '+query)
            else:
                logger.info('Logging input: '+query)