from nltk.corpus import wordnet

#print(wordnet.synsets('plant')) #1

set1 = wordnet.synset('plant.n.01') 
set2 = wordnet.synset('plant.n.02')

#print(set1.definition()) #2
#set2.definition()

#print(set1.hypernyms()) #4
#set2.hypernyms()

i = wordnet.synsets('industry')
l = wordnet.synsets('leaf')
r = wordnet.synsets('rattlesnake\'s master')
o = wordnet.synsets('organism')
w = wordnet.synsets('whole')

mass = []
mass1 = []
mass3 = []
mass4 = []

for sets in i:  #5
    for sett in l:
        s1 = set1.path_similarity(sets)
        mass.append(s1)
        mass3.append(s1)
        s2 = set2.path_similarity(sett)
        s3 = set1.path_similarity(sett)
        s4 = set2.path_similarity(sets) 
        if s2 is not None:
            mass1.append(s2)
            mass4.append(s2)
        if s3 is not None:
            mass3.append(s3)
        if s4 is not None:
            mass4.append(s4)
#print(min(mass))
#print(min(mass1))
#print(min(mass3))
#print(min(mass4))

for r1 in r:#6
    dist1 = set2.wup_similarity(r1)
    print(dist1)         
for o1 in o:
    for w1 in w:
        dist2 = o1.wup_similarity(w1)
        if dist2 is not None:
           print(dist2)

for r1 in r:
    dist1 = set2.path_similarity(r1)
    print(dist1)          
for o1 in o:
    for w1 in w:
        dist2 = o1.path_similarity(w1)
        if dist2 is not None:
           print(dist2)

#Ответ: для первого случая одинаково, во втором - первый вариант:wup

from nltk.wsd import lesk  #3

man = ['they', 'built', 'a', 'large', 'plant', 'to', 'manufacture', 'automobiles']
lesk(man, 'plant').definition()
wordnet.synsets('plant', 'n')
lesk(man, 'plant', 'n')

green = ['plant', 'with', 'hispid', 'stems']
lesk(green, 'plant').definition()
wordnet.synsets('plant', 'n')
lesk(green, 'plant', 'n')
#print(lesk(green, 'plant', 'n'))
#print(lesk(man, 'plant', 'n'))