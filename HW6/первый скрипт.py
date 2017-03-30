# -*- coding: utf-8 -*-
"""
Created on Tue Mar 28 21:08:53 2017

@author: Оля
"""
#from sklearn import cross_validation
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
import sys, os
import gensim, logging
import pandas as pd
import numpy as np
from sklearn.metrics import f1_score
from sklearn.metrics import accuracy_score
from sklearn.metrics import precision_score

m = 'ruscorpora_1_300_10.bin.gz'
if m.endswith('.vec.gz'):
    model = gensim.models.KeyedVectors.load_word2vec_format(m, binary=False)
elif m.endswith('.bin.gz'):
    model = gensim.models.KeyedVectors.load_word2vec_format(m, binary=True)
else:
    model = gensim.models.Word2Vec.load(m)


def for_file(filename, model):
    m=[]
    f = open(filename,  encoding='utf-8')
    for line in f:
        line = line.split('\n')      
        for word in line:
            if word != '':
                if word in model:
                    m.append(model[word])
    return m

    
ane = []
files = os.listdir('C:\\Users\\Оля\\Desktop\\hw4\\ane\\')
for filename in files:
    aa = for_file('C:\\Users\\Оля\\Desktop\\hw4\\ane\\' + filename, model)
    ane.append(aa)
   
iz = []
files = os.listdir('C:\\Users\\Оля\\Desktop\\hw4\\iz\\')
for filename in files:
    ai = for_file('C:\\Users\\Оля\\Desktop\\hw4\\iz\\' + filename, model)
    iz.append(ai)
        
tech = []   
files = os.listdir('C:\\Users\\Оля\\Desktop\\hw4\\tech\\')
for filename in files:
    at = for_file('C:\\Users\\Оля\\Desktop\\hw4\\tech\\' + filename, model)
    tech.append(at)


def for_vec(i):
    mass = []
    for word in i:
        for nu in word:
            mass.append(nu)
    return sum(mass)

ane_vec = []
for i in ane:
    sa = for_vec(i)
    ane_vec.append(sa)
     

iz_vec = []
for i in iz:
    si = for_vec(i)
    iz_vec.append(si)

   
tech_vec = []
for i in tech:
    st = for_vec(i)
    tech_vec.append(st)


d = {'name'  : pd.Series('anecdote', index = range(125)),
     'num' : pd.Series(ane_vec, index = range(125))}
d1 = {'name'  : pd.Series('izvest', index = range(125, 250)),
     'num' : pd.Series(iz_vec, index = range(125, 250))}
d2 = {'name'  : pd.Series('tech', index = range(250,375)),
     'num' : pd.Series(tech_vec, index = range(250,375))}

df = pd.DataFrame(d, columns = ['name', 'num'])
df1 = pd.DataFrame(d1, columns = ['name', 'num'])
df2 = pd.DataFrame(d2, columns = ['name', 'num'])
df_new = [df, df1, df2]
result = pd.concat(df_new)

#чтобы комп меньше думал, уйдем в другой скрипт, a датафрейм сделаем csv файлом


