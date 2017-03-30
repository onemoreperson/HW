# -*- coding: utf-8 -*-
"""
Created on Thu Mar 30 07:51:57 2017

@author: Оля
"""
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
import pandas as pd
from sklearn.metrics import f1_score
from sklearn.metrics import accuracy_score
from sklearn.metrics import precision_score


db0 = pd.read_csv('vectors.csv', sep = ';', names = ['A', 'B'])

x = db0['B']
y = db0['A']

xtrain, xtest, ytrain, ytest = train_test_split(x, y)
clf = LogisticRegression(penalty="l2", solver="lbfgs", multi_class="multinomial", max_iter=300, n_jobs=4)
cvtrain = clf.fit_transform(xtrain)
cvtest = clf.transform(xtest)
y_pred = clf.fit(cvtrain, ytrain).predict(cvtest) 
print(f1_score(ytest, y_pred))          
print(accuracy_score(ytest, y_pred))        
print(precision_score(ytest, y_pred))  