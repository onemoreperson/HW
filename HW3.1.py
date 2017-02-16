import re
import numpy as np
from matplotlib import pyplot as plt
from matplotlib import mlab

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


anna_data = [(sum(lenwords(sentence)), find_dif(sentence), find_vow(sentence),
              np.median(lenwords(sentence)), np.median(med(sentence))) 
             for sentence in anna_sentences if len(lenwords(sentence)) > 0
             if med(sentence) != None]
sonet_data = [(sum(lenwords(sentence)), find_dif(sentence), find_vow(sentence),
               np.median(lenwords(sentence)), np.median(med(sentence))) 
             for sentence in sonet_sentences if len(lenwords(sentence)) > 0
              if med(sentence) != None]
##print(anna_data[:10])

anna_data = np.array(anna_data)
sonet_data = np.array(sonet_data)
plt.figure()
c1, c2 = 0, 1
plt.plot(anna_data[:,c1], anna_data[:,c2], 'og', 
         sonet_data[:,c1], sonet_data[:,c2], 'sb')
plt.show()


 



