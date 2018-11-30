import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
from xgboost import XGBClassifier
from sklearn import model_selection
from sklearn.metrics import classification_report

dataSet = pd.read_csv('dataset.csv',sep= ',', header= None)
print("Dataset Lenght:: ", len(dataSet))
print("Dataset Shape:: ", dataSet.shape)
print("Dataset Head:: ", dataSet.head())
X = dataSet.values[:, 1:6]
Y = dataSet.values[:,0]
X_train, X_test, y_train, y_test = train_test_split( X, Y, test_size = 0.3, random_state = 100)

model = XGBClassifier()
model.fit(X_train, y_train)
#Make predictions for test data
y_pred = model.predict(X_test)

print("Accuracy is ", accuracy_score(y_test,y_pred)*100)

seed=10
kfold = model_selection.KFold(n_splits=180, random_state=seed,shuffle=True)
scoring = 'accuracy'
results = model_selection.cross_val_score(model, X, Y, cv=kfold, scoring=scoring)
print(("Accuracy: %.3f (%.3f)")%(results.mean()*100, results.std()))

report = classification_report(y_test, y_pred)
print(report)
