import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score
from sklearn.model_selection import cross_val_score, cross_val_predict
from sklearn import metrics

dataSet = pd.read_csv('dataset.csv',sep= ',', header= 0)
print(":::::Decision Tree:::::")

X = dataSet.values[:, 1:7]
Y = dataSet.values[:,0]
#print("Dataset Lenght:: ", len(X))
print("Dataset Shape:: ", X.shape)
#print("Dataset Head:::::\n ", dataSet.head())

X_train, X_test, y_train, y_test = train_test_split( X, Y, test_size = 0.3, random_state = 100)

print(":::::Gini Index:::::")
clf_gini = DecisionTreeClassifier(criterion = "gini", random_state = 100, max_depth=5, min_samples_leaf=1,  max_leaf_nodes=10)
clf_gini.fit(X_train, y_train)
y_pred = clf_gini.predict(X_test)
print("Accuracy using 1 fold:: ", accuracy_score(y_test,y_pred)*100)


scores = cross_val_score(clf_gini, X, Y, cv=4)
#print("Cross-validated scores:", scores)
predictions = cross_val_predict(clf_gini,X,Y, cv=4)
#plt.scatter(Y, predictions)
print("Cross-Predicted Accuracy 4 folds :", scores.mean()*100) #accuracy_score(Y,predictions)*100)


scores = cross_val_score(clf_gini, X, Y, cv=3)
#print("Cross-validated scores:", scores)
predictions = cross_val_predict(clf_gini,X,Y, cv=3)
#plt.scatter(Y, predictions)
print("Cross-Predicted Accuracy 3 folds :", scores.mean()*100) #accuracy_score(Y,predictions)*100)

scores = cross_val_score(clf_gini, X, Y, cv=2)
#print("Cross-validated scores:", scores)
predictions = cross_val_predict(clf_gini,X,Y, cv=2)
#plt.scatter(Y, predictions)
print("Cross-Predicted Accuracy 2 folds :",  scores.mean()*100) #accuracy_score(Y,predictions)*100)


print(":::::Information Gain:::::")
# information gain
clf_entropy = DecisionTreeClassifier(criterion = "entropy", random_state = 100,
                                     max_depth=3, min_samples_leaf=1,  max_leaf_nodes=10)
clf_entropy.fit(X_train, y_train)
y_pred = clf_entropy.predict(X_test)
print("Accuracy using 1 fold:: ", accuracy_score(y_test,y_pred)*100)


scores = cross_val_score(clf_entropy, X, Y, cv=4)
#print("Cross-validated scores:", scores)
predictions = cross_val_predict(clf_entropy,X,Y, cv=4)
#plt.scatter(Y, predictions)
print("Cross-Predicted Accuracy 4 folds :", scores.mean()*100) #accuracy_score(Y,predictions)*100)


scores = cross_val_score(clf_entropy, X, Y, cv=3)
#print("Cross-validated scores:", scores)
predictions = cross_val_predict(clf_entropy,X,Y, cv=3)
#plt.scatter(Y, predictions)
print("Cross-Predicted Accuracy 3 folds :", scores.mean()*100) #accuracy_score(Y,predictions)*100)

scores = cross_val_score(clf_entropy, X, Y, cv=2)
#print("Cross-validated scores:", scores)
predictions = cross_val_predict(clf_entropy,X,Y, cv=2)
#plt.scatter(Y, predictions)
print("Cross-Predicted Accuracy 2 folds :",  scores.mean()*100) #accuracy_score(Y,predictions)*100)
