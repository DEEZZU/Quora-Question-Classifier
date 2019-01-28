#libraries required
import csv
import nltk
from nltk.tokenize import RegexpTokenizer

# ALGORITHM

# read csv of questions
with open('info_question.csv', 'r') as f:
    quoraDataset = list(csv.reader(f, delimiter=','))
quora=quoraDataset[0:300]

with open('opinion_question.csv', 'r') as f:
    quoraDataset = list(csv.reader(f, delimiter=','))
quora.extend(quoraDataset[0:300])

# convert each question to url format : https://www.quora.com/(question words separated by -) , remove punctuations
tokenizer = RegexpTokenizer(r'\w+')
len_quora = len(quora)
for i in range(0, len_quora) :
    quora[i][0] = quora[i][0].replace("'s","s")
    q = tokenizer.tokenize(quora[i][0])
    len_q = len(q)
    url = "https://www.quora.com/"
    url += q[0]
    for j in range(1, len_q):
        url += "-"
        url += q[j]
    quora[i].append(url)
    quora[i].append(0)




# write urls to a file for record
with open('questionUrl.csv', 'w') as csvFile:
    writer = csv.writer(csvFile)
    writer.writerows(quora)
