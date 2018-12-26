import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score
from sklearn import tree
from sklearn.metrics import classification_report
from sklearn.metrics import confusion_matrix

dataSet = pd.read_csv('dataset.csv',sep= ',', header= 0)
print(":::::Decision Tree:::::")
#X = dataSet.values[::2, 1:6]
#Y = dataSet.values[::2,0]
#print("Dataset Lenght:: ", len(X))
#print("Dataset Shape:: ", X.shape)
#print("Dataset Head:::::\n ", dataSet.head())

X = dataSet.values[:, 1:7]
Y = dataSet.values[:,0]
print("Dataset Lenght:: ", len(X))
print("Dataset Shape:: ", X.shape)
print("Dataset Head:::::\n ", dataSet.head())

X_train, X_test, y_train, y_test = train_test_split( X, Y, test_size = 0.3, random_state = 100)

print(":::::Gini Index:::::")
#gini Index
clf_gini = DecisionTreeClassifier(criterion = "gini", random_state = 100, max_depth=5, min_samples_leaf=1,  max_leaf_nodes=10)
clf_gini.fit(X_train, y_train)
'''
n_nodes = clf_gini.tree_.node_count
children_left = clf_gini.tree_.children_left
children_right = clf_gini.tree_.children_right
feature = clf_gini.tree_.feature
#print(feature)
threshold = clf_gini.tree_.threshold

#DecisionTreeClassifier(class_weight=None, criterion='gini', max_depth=3,max_features=None, max_leaf_nodes=None, min_samples_leaf=5,min_samples_split=2, min_weight_fraction_leaf=0.0, presort=False, random_state=100, splitter='best')
'''

y_pred = clf_gini.predict(X_test)
print("Accuracy:: ", accuracy_score(y_test,y_pred)*100)
m=confusion_matrix(y_test, y_pred)
print(m)

report = classification_report(y_test, y_pred)
print(report)

print(":::::Information Gain:::::")
# information gain
clf_entropy = DecisionTreeClassifier(criterion = "entropy", random_state = 100,
                                     max_depth=3, min_samples_leaf=1,  max_leaf_nodes=10)
clf_entropy.fit(X_train, y_train)

'''DecisionTreeClassifier(class_weight=None, criterion='entropy', max_depth=3,
                       max_features=None, max_leaf_nodes=None, min_samples_leaf=5,
                       min_samples_split=2, min_weight_fraction_leaf=0.0,
                       presort=False, random_state=100, splitter='best')
'''

y_pred_en = clf_entropy.predict(X_test)
print("Accuracy is ", accuracy_score(y_test,y_pred_en)*100)

m=confusion_matrix(y_test, y_pred_en)
print(m)

report = classification_report(y_test, y_pred_en)
print(report)

import graphviz
dot_data1 = tree.export_graphviz(clf_gini, out_file=None,feature_names=list(dataSet.columns.values)[1:7],label='all',class_names=['0','1'],filled='True',rounded='True')
graph = graphviz.Source(dot_data1)
graph.render("Gini") 

dot_data2 = tree.export_graphviz(clf_entropy, out_file=None,feature_names=list(dataSet.columns.values)[1:7],label='all',class_names=['0','1'],filled='True',rounded='True')
graph = graphviz.Source(dot_data2)
graph.render("Entropy")

