import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
from sklearn.svm import SVC
from sklearn import model_selection
from sklearn.metrics import classification_report

dataSet = pd.read_csv("/Users/deeps/Desktop/Quora-Question-Classifier/EXTRA/dataset.csv",sep= ',')
print("Dataset Lenght:: ", len(dataSet))
print("Dataset Shape:: ", dataSet.shape)
print("Dataset Head:: ", dataSet.head())

X = dataSet.values[1:,1:7]
Y = dataSet.values[1:,0]
X_train, X_test, y_train, y_test = train_test_split( X, Y, test_size = 0.3, random_state = 100)


svclassifier = SVC(kernel='rbf', gamma='auto')
print(type(X_train))
svclassifier.fit(X_train, y_train)
y_pred = svclassifier.predict(X_test)
print("Accuracy is ", accuracy_score(y_test,y_pred)*100)

