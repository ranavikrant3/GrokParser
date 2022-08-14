import pickle
clf = pickle.load(open('model.bin', 'rb'))
vectorizer = pickle.load(open('vectorizer.bin', 'rb'))
X_predict = []
f = open("test.log", "r")
lines = f.readlines()
for line in lines:
    X_predict.append(line.strip().split("INFO")[1])
X_predict = vectorizer.transform(X_predict)
y_Predict = clf.predict(X_predict)
for i in range(len(y_Predict)):
    if y_Predict[i]==1:
        print(lines[i].strip())

