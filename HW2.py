import nltk
import pymorphy2
from nltk.collocations import *
from nltk.metrics.spearman import *

trigram_measures = nltk.collocations.TrigramAssocMeasures()

results_list = [('суд', 'слушать', 'дело'),('суд', 'удовлетворить', 'требование'),('суд', 'зачитать', 'приговор'),('суд', 'передать', 'дело'),
                ('суд', 'рассмотреть', 'ходатайство'),('суд', 'принять', 'решение'),('суд', 'вынести', 'решение'),('суд', 'удовлетворить', 'ходатайство'),
                ('суд', 'вынести', 'приговор'),('суд', 'изменить', 'решение')]
results_list1 = [(('суд', 'слушать', 'дело'), 0),(('суд', 'удовлетворить', 'требование'), 1),(('суд', 'зачитать', 'приговор'), 2),(('суд', 'передать', 'дело'), 3),
                (('суд', 'рассмотреть', 'ходатайство'), 4),(('суд', 'принять', 'решение'),5),(('суд', 'вынести', 'решение'), 6),(('суд', 'удовлетворить', 'ходатайство'), 7),
                (('суд', 'вынести', 'приговор'), 8),(('суд', 'изменить', 'решение'), 9)]

morph = pymorphy2.MorphAnalyzer()
punct = ','
words = [word.strip(punct) for word in open('court-V-N.csv', encoding="utf8").read().split()]
words_tagged = [morph.parse(word)[0].normal_form for word in words]
##print(len(words_tagged))

for i in results_list:
    finder = TrigramCollocationFinder.from_words(words_tagged)
    results_list_pmi = finder.nbest(trigram_measures.pmi, len(words_tagged))    
##    print(results_list_pmi.index(i))


for i1 in results_list:
    stopwords = nltk.corpus.stopwords.words('russian')
    results_list_likelihood = finder.nbest(trigram_measures.likelihood_ratio, len(words_tagged))
##    print(results_list_likelihood.index(i1))

results_list_pmi1 = [(('суд', 'слушать', 'дело'), 3413),(('суд', 'удовлетворить', 'требование'), 4045),
                     (('суд', 'зачитать', 'приговор'), 2979),
                     (('суд', 'передать', 'дело'), 3986),
                (('суд', 'рассмотреть', 'ходатайство'), 3720),
                     (('суд', 'принять', 'решение'),3756),
                     (('суд', 'вынести', 'решение'), 4008),(('суд', 'удовлетворить', 'ходатайство'), 3685),
                (('суд', 'вынести', 'приговор'), 3764),(('суд', 'изменить', 'решение'), 3782)]

results_list_likelihood1 = [(('суд', 'слушать', 'дело'), 1224),(('суд', 'удовлетворить', 'требование'), 155),
                     (('суд', 'зачитать', 'приговор'), 2466),
                     (('суд', 'передать', 'дело'), 1242),
                (('суд', 'рассмотреть', 'ходатайство'), 138),
                     (('суд', 'принять', 'решение'),36),
                     (('суд', 'вынести', 'решение'), 40),(('суд', 'удовлетворить', 'ходатайство'), 35),
                (('суд', 'вынести', 'приговор'), 266),(('суд', 'изменить', 'решение'), 169)]


print('%0.1f' % spearman_correlation(results_list1, results_list_pmi1))
print('%0.1f' % spearman_correlation(results_list1, results_list_likelihood1))

##-839361.0
##-56007.1, результаты оказались отрицательны, loglikelyhood ближе, чем pmi

