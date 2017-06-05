# -*- coding: utf-8 -*-
"""
Created on Mon May 15 22:52:21 2017

@author: Ivan
"""
import pos

#sentence = sys.argv[1].split(' ')
sentence = str.split('Он наставил на меня свое дуло.')

tagger = pos.Tagger()
tagger.load('tmp/svm.model', 'tmp/ids.pickle')

rus = {
    'NOUN': 'сущ.', 
    'ADJF': 'прил. полн', 
    'ADJS': 'прил. кратк', 
    'COMP': 'компаратив', 
    'VERB': 'глаг.', 
    'INFN': 'инфинитив', 
    'PRTF': 'причастие полн', 
    'PRTS': 'причастие кратк', 
    'GRND': 'деепричастие', 
    'NUMR': 'числительное', 
    'ADVB': 'наречие', 
    'NPRO': 'местоимение-сущ.', 
    'PRED': 'предикатив', 
    'PREP': 'предлог', 
    'CONJ': 'союз', 
    'PRCL': 'частица', 
    'INTJ': 'междометие', 
    'PNCT': 'знак препинания',
    'LATN': 'латиница',
    'NUBM': 'число',
    'SYMB': 'математика',
    'ROMN': 'римские числа'
}

tagged = []
for word, label in tagger.label(sentence):
    tagged.append((word, rus[tagger.get_label(label)]))
    
print(tagged)
#o = open('test.txt', 'w')
#print(tagged, file = o)
#o.close()