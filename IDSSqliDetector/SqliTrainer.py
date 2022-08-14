import numpy as np
import pandas as pd
import re
import nltk
import pickle
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.feature_extraction.text import TfidfTransformer
from sklearn.feature_extraction.text import TfidfVectorizer
df = pd.read_csv("sqli.csv",encoding='utf-16')
# df = df.sample(n=10000)
from io import StringIO
col = ['Label','Sentence']
df = df[col]
#Deleting nulls
df = df[pd.notnull(df['Sentence'])]
#more settings for our data manipulation
df.columns = ['Label', 'Sentence']
df['category_id'] = df['Label'].factorize()[0]
category_id_df = df[['Label', 'category_id']].drop_duplicates().sort_values('category_id')
category_to_id = dict(category_id_df.values)
id_to_category = dict(category_id_df[['category_id', 'Label']].values)

def getTokens(input):
    tokensBySpace = str(input.encode('utf-8')).split(' ')
    return tokensBySpace

y = [d[1]for d in df] #labels
myUrls = [d[0]for d in df] #urls
# vectorizer = TfidfVectorizer( tokenizer=getTokens ,use_idf=True, smooth_idf=True, sublinear_tf=False)
vectorizer = CountVectorizer()
features = vectorizer.fit_transform(df.Sentence).toarray()
labels = df.Label
features.shape

from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
model = LogisticRegression(random_state=0)
X_train, X_test, y_train, y_test, indices_train, indices_test = train_test_split(features, labels, df.index, test_size=0.20, random_state=0)
# print(df)
model.fit(X_train, y_train)
y_pred_proba = model.predict_proba(X_test)
y_pred = model.predict(X_test)
clf = LogisticRegression(random_state=0) 
clf.fit(X_train,y_train)
train_score = clf.score(X_train, y_train)
test_score = clf.score(X_test, y_test)
print ('train accuracy =', train_score)
print ('test accuracy =', test_score)
#saving the model
pickle.dump(model, open('model.bin', 'wb'))
pickle.dump(vectorizer, open('vectorizer.bin', 'wb'))

X_predict = ["' UNION SELECT 1,2", "a random text from somewhere"]
X_predict = vectorizer.transform(X_predict)
y_Predict = clf.predict(X_predict)
print(y_Predict)

X_predict.shape

