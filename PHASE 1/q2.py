import csv
import nltk
from nltk.tokenize import RegexpTokenizer
tokenizer = RegexpTokenizer(r'\w+')
l=[]
for i in range(0,35):
    l.append(0)

with open('/Users/deeps/Desktop/QUORA PROJECT/test.csv', 'r') as f:
    quoraDataset = list(csv.reader(f, delimiter=','))
quora=quoraDataset[0:250]
#print(quora[0])
len_quora=len(quora)

for i in range(0,len_quora):
    q=nltk.pos_tag(tokenizer.tokenize(quora[i][0]))
    len_q=len(q)
    ind=0
    for j in range(0, len_q):
        if q[j][1]=='PRP$' :
            ind=1
    quora[i].append(ind)
    if ind==0 :
        quora[i].append('Not Opinion')
    else :
        quora[i].append('Opinion')


with open('/Users/deeps/Desktop/QUORA/Possesive Rule.csv', 'w') as csvFile:
    writer = csv.writer(csvFile)
    writer.writerow(['Questions','Possesive ?'])
    writer.writerows(quora)

csvFile.close()
