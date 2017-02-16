import re
import numpy as np
from matplotlib import pyplot as plt
from matplotlib import mlab
import time
from pymystem3 import Mystem
from sklearn import grid_search, svm
m = Mystem()

def mystem(sentence):
    sentence = sentence.strip()
    anas = m.analyze(sentence)
    return anas

with open('anna.txt', encoding='utf-8') as f:
    anna = f.read()
    for i in anna:
        if not i.isspace():
            i.replace('\n', '')
            
with open('sonets.txt', encoding='utf-8') as f:
    sonets = f.read()
    for i in anna:
        if not i.isspace():
            i.replace('\n', '')

        
anna_sentences = re.split(r'(?:[.]\s*){3}|[.?!]', anna)
sonet_sentences = re.split(r'(?:[.]\s*){3}|[.?!]', sonets)

def lenwords(sentence):    
    return [len(word) for word in sentence.split()]

def find_dif(sent):
    a = ['-',',',';']
    d = {}
    for word in sent.split():
        for letter in word.lower():
            if letter not in a:
                if letter not in d:
                    d[letter] = 1
                else:
                    d[letter] += 0
    return len(d)

def find_vow(sent): 
    d = {}
    vowel = ['а', 'о', 'у', 'я', 'и', 'ю', 'э', 'ы', 'ё', 'е']
    for word in sent.split():
        for letter in word.lower():
            if letter in vowel:
                if letter not in d:
                    d[letter] = 1
                else:
                    d[letter] += 0
    return len(d)

def find_vow2(sent):
    x = 0
    mass = list(sent)
    vowel = ['а', 'о', 'у', 'я', 'и', 'ю', 'э', 'ы', 'ё', 'е']
    for letter in mass:
        letter = letter.lower()
        if letter in vowel:
            x += 1
    return x
        
def med(sent):
    mass = []
    for word in sent.split():
        word = word.lower()
        letter = find_vow2(word)
        if letter != 0:
            mass.append(letter)
    if len(mass) > 0:
        return mass

anna_data=[]
sonet_data=[]

for sent in anna_sentences:
    sentence = mystem(sent)
    for sentence in anna_sentences:
        if len(lenwords(sentence)) > 0:
            if med(sentence) != None:
                anna_data.append([1, sum(lenwords(sentence)), find_dif(sentence), find_vow(sentence),
                                  np.median(lenwords(sentence)), np.median(med(sentence))])

for sent in sonet_sentences:
    sentence = mystem(sent)
    for sentence in anna_sentences:
        if len(lenwords(sentence)) > 0:
                if med(sentence) != None:
                    sonet_data.append([2, sum(lenwords(sentence)), find_dif(sentence), find_vow(sentence),
                                       np.median(lenwords(sentence)), np.median(med(sentence))])

anna_data = np.array(anna_data)
sonet_data = np.array(sonet_data)
data = np.vstack((anna_data, sonet_data))

parameters = {'C': (.1, .6, 1.7, 1.5, 1.7, 1.3, 0.9)}
gs = grid_search.GridSearchCV(svm.LinearSVC(), parameters)
gs.fit(data[:, 1:], data[:, 0])

clf = svm.LinearSVC(C=gs.best_estimator_.C)
clf.fit(data[::2, 1:], data[::2, 0])

wrong = 0
for obj in data[1::2, :]:
    label = clf.predict(obj[1:])
    if label != obj[0] and wrong < 3:
        print('Пример ошибки машины: class = ', obj[0], ', label = ', label, ', экземпляр ', obj[1:])
        wrong += 1
    if wrong > 3:
        break

##Пример ошибки машины: class =  2.0 , label =  [ 1.] , экземпляр  [ 26.   15.    4.    4.    2.5]
##Пример ошибки машины: class =  2.0 , label =  [ 1.] , экземпляр  [ 109.   21.    6.    6.    2.]    
##Пример ошибки машины: class =  2.0 , label =  [ 1.] , экземпляр  [ 52.  21.   6.   4.   2.]
