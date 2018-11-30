import csv
import nltk
from nltk.tokenize import RegexpTokenizer
tokenizer = RegexpTokenizer(r'\w+')
l=[]
for i in range(0,36):
    l.append(0)

with open('info_question.csv', 'r') as f:
    quoraDataset = list(csv.reader(f, delimiter=','))

quora=quoraDataset[0:300]

with open('opinion_question.csv', 'r') as f:
    quoraDataset = list(csv.reader(f, delimiter=','))

quora.extend(quoraDataset[0:300])

quoraCopy=quora

#print(quora)
len_quora=len(quora)
for i in range(0,len_quora):
    q=nltk.pos_tag(tokenizer.tokenize(quora[i][0]))
    len_q=len(q)
    quora[i].append(len_q)
    quora[i].append(q)
    quora[i].extend(l)

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
        x=36
    
    return x

#print(quora[70])
for i in range(0,len_quora):
    len_q=quora[i][2]
    #print(i)
    for j in range(0, len_q):
        #print(quora[i][3][j])
        ind=switchFun(quora[i][3][j][1])
        #print(ind)
        #print(len(quora[i]))
        quora[i][3+ind]=quora[i][3+ind]+1

#print(quora)

with open('ruleBased2Classes.csv', 'w') as csvFile:
    writer = csv.writer(csvFile)
    writer.writerows(quora)

csvFile.close()


list1 = [1,4,7,12,14,21,22] #4,7
newList = [[l[i] for i in list1] for l in quora]

for i in range(0,len(newList)) :
    if newList[i][0] == "information" :
        newList[i][0]=0
    else :
        newList[i][0]=1
           
with open('dataset.csv', 'w') as csvFile:
    writer = csv.writer(csvFile)
    writer.writerow(["Label","CC","EX","JJS","MD","PRP","PRP$"])#,"EX"
    writer.writerows(newList)

csvFile.close()


