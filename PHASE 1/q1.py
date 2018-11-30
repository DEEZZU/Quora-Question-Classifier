import csv
import nltk
from nltk.tokenize import RegexpTokenizer
tokenizer = RegexpTokenizer(r'\w+')
l=[]
for i in range(0,35):
    l.append(0)

with open('Quora 2.csv', 'r') as f:
    quoraDataset = list(csv.reader(f, delimiter=','))
quora=quoraDataset[1:31]
#print(quora)
len_quora=len(quora)
for i in range(0,len_quora):
    q=nltk.pos_tag(tokenizer.tokenize(quora[i][1]))
    len_q=len(q)
    quora[i].append(len_q)
    quora[i].extend(q)
    quora[i].extend(l)

'''
1 CC    coordinating conjunction
2 CD    cardinal digit
3 DT    determiner
4 EX    existential there (like: "there is" ... think of it like "there exists")
5 FW    foreign word
6 IN    preposition/subordinating conjunction
7 JJ    adjective    'big'
8 JJR    adjective, comparative    'bigger'
9 JJS    adjective, superlative    'biggest'
10 LS    list marker    1)
11 MD    modal    could, will
12 NN    noun, singular 'desk'
13 NNS    noun plural    'desks'
14 NNP    proper noun, singular    'Harrison'
15 NNPS    proper noun, plural    'Americans'
16 PDT    predeterminer    'all the kids'
17 POS    possessive ending    parent's
18 PRP    personal pronoun    I, he, she
19 PRP$    possessive pronoun    my, his, hers
20 RB    adverb    very, silently,
21 RBR    adverb, comparative    better
22 RBS    adverb, superlative    best
23 RP    particle    give up
24 TO    to    go 'to' the store.
25 UH    interjection    errrrrrrrm
26 VB    verb, base form    take
27 VBD    verb, past tense    took
28 VBG    verb, gerund/present participle    taking
29 VBN    verb, past participle    taken
30 VBP    verb, sing. present, non-3d    take
31 VBZ    verb, 3rd person sing. present    takes
32 WDT    wh-determiner    which
33 WP    wh-pronoun    who, what
34 WP$    possessive wh-pronoun    whose
35 WRB    wh-abverb    where, when
'''

def switchFun(val):
    
    if val=='CC':
        x=1
    elif val=='CD':
        x=2
    elif val=='DT':
        x=3
    elif val=='EX':
        x=4
    elif val=='FW':
        x=5
    elif val=='IN':
        x=6
    elif val=='JJ':
        x=7
    elif val=='JJR':
        x=8
    elif val=='JJS':
        x=9
    elif val=='LS':
        x=10
    elif val=='MD':
        x=11
    elif val=='NN':
        x=12
    elif val=='NNS':
        x=13
    elif val=='NNP':
        x=14
    elif val=='NNPS':
        x=15
    elif val=='PDT':
        x=16
    elif val=='POS':
        x=17
    elif val=='PRP':
        x=18
    elif val=='PRP$':
        x=19
    elif val=='RB':
        x=20
    elif val=='RBR':
        x=21
    elif val=='RBS':
        x=22
    elif val=='RP':
        x=23
    elif val=='TO':
        x=24
    elif val=='UH':
        x=25
    elif val=='VB':
        x=26
    elif val=='VBD':
        x=27
    elif val=='VBG':
        x=28
    elif val=='VBN':
        x=29
    elif val=='VBP':
        x=30
    elif val=='VBZ':
        x=31
    elif val=='WDT':
        x=32
    elif val=='WP':
        x=33
    elif val=='WP$':
        x=34
    elif val=='WRB':
        x=35
    else :
        x=0

    return x

print(quora[0])
for i in range(0,len_quora):
    len_q=quora[i][3]
    for j in range(0, len_q):
        #print(quora[i][4+j][1])
        ind=switchFun(quora[i][4+j][1])
        #print(ind)
        #print(len(quora[i]))
        #print(3+len_q+ind)
        quora[i][3+len_q+ind]=quora[i][3+len_q+ind]+1

print(quora)

with open('quora 3.csv', 'w') as csvFile:
    writer = csv.writer(csvFile)
    writer.writerows(quora)

csvFile.close()
