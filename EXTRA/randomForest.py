import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
from sklearn.ensemble import RandomForestRegressor
from sklearn import model_selection
from sklearn.metrics import classification_report

dataSet = pd.read_csv("/Users/deeps/Desktop/Quora-Question-Classifier/PHASE 2/dataset.csv",sep= ',', header= None)
print("Dataset Lenght:: ", len(dataSet))
print("Dataset Shape:: ", dataSet.shape)
print("Dataset Head:: ", dataSet.head())

X = dataSet.values[1:, 1:7]
Y = dataSet.values[1:,0]
X_train, X_test, y_train, y_test = train_test_split( X, Y, test_size = 0.3, random_state = 100)


rf = RandomForestRegressor(n_estimators = 1000, random_state = 42)
rf.fit(X_train, y_train)
y_pred = rf.predict(X_test)
'''print(float(y_test))
errors = abs(y_pred - y_test)
# Print out the mean absolute error (mae
print('Mean Absolute Error:', round(np.mean(errors), 2), 'degrees.')
'''
'''print("Accuracy is ", accuracy_score(y_test,y_pred)*100)

seed=10
kfold = model_selection.KFold(n_splits=180, random_state=seed,shuffle=True)
scoring = 'accuracy'
results = model_selection.cross_val_score(rf, X, Y, cv=kfold, scoring=scoring)
print(("Accuracy: %.3f (%.3f)")%(results.mean()*100, results.std()))

report = classification_report(y_test, y_pred)
print(report)
'''
