# -*- coding: utf-8 -*-
"""
Created on Sat Jul  7 12:09:44 2018

@author: TushaR
"""
import os
os.chdir('C:/Users/TushaR/Documents/Machine Learning/Pandas Tutorial')

import pandas as pd
import numpy as np
from sklearn import preprocessing, cross_validation, neighbors

df = pd.read_csv('breast-cancer-wisconsin.data')
df.replace('?',-99999,inplace=True)
df.drop(['id'],1, inplace=True)

X = np.array(df.drop(['class'],1))
y = np.array(df['class'])

X_train, X_test, y_train, y_test = cross_validation.train_test_split(X,y,test_size=0.2)
clf = neighbors.KNeighborsClassifier()
clf.fit(X_train, y_train)

accuracy = clf.score(X_test, y_test)
print(accuracy)
