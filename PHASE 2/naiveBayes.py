import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import time
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import GaussianNB, BernoulliNB, MultinomialNB
from sklearn.metrics import accuracy_score
from sklearn.metrics import classification_report

dataSet = pd.read_csv('dataset.csv',sep= ',', header=0)
print(":::::Naive Bayes:::::")
print("Dataset Lenght:: ", len(dataSet))
print("Dataset Shape:: ", dataSet.shape)
print("Dataset Head::::::::\n ", dataSet.head())

X = dataSet.values[:, 1:6]
Y = dataSet.values[:,0]
X_train, X_test, y_train, y_test = train_test_split( X, Y, test_size = 0.3, random_state = 100)

gnb = GaussianNB()
gnb.fit(X_train,y_train)
y_pred = gnb.predict(X_test)
print("Accuracy is ", accuracy_score(y_test,y_pred)*100)

report = classification_report(y_test, y_pred)
print(report)
