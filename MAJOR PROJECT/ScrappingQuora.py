#libraries required
import csv
import nltk
from nltk.tokenize import RegexpTokenizer
import requests
from bs4 import BeautifulSoup
import pprint

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
    q = tokenizer.tokenize(quora[i][0])
    len_q = len(q)
    url = "https://www.quora.com/"
    url += q[0]
    for j in range(1, len_q):
        url += "-"
        url += q[j]
    quora[i].append(url)

print(quora[0])


# write urls to a file for record
with open('questionUrl.csv', 'w') as csvFile:
    writer = csv.writer(csvFile)
    writer.writerows(quora)

# pass each as url to get labels : append labels to each question
for i in range(0, len_quora):
    url = quora[i][2]
    page = requests.get(url)
    soup = BeautifulSoup(page.content, 'html.parser')
    resultSpan = soup.find_all('span', attrs={'class':'TopicName TopicNameSpan'})
    for j in range(len(resultSpan)):
        resultSpan[j]=str(resultSpan[j])
    newResult = []
    for k in range(len(resultSpan)):
        x = resultSpan[k].split('">')
        y = (x[1]).split('<')
        quora[i].extend(y[0])

# write labels into the file
with open('scrappedLabels.csv', 'w') as csvFile:
    writer = csv.writer(csvFile)
    writer.writerows(quora)


'''
    ONE - QUESTION SCRAPPING :

    #specify the url
    url = 'https://www.quora.com/If-you-summed-up-your-life-in-one-sentence-what-would-that-sentence-be'
    
    #returning the website html to the page variable
    page = requests.get(url)

    soup = BeautifulSoup(page.content, 'html.parser')
    resultSpan = soup.find_all('span', attrs={'class':'TopicName TopicNameSpan'})
    # resultSpan = soup.find_all('span')
    print(len(resultSpan))

    for i in range(len(resultSpan)):
        resultSpan[i]=str(resultSpan[i])

    newResult = []

    for i in range(len(resultSpan)):
        x = resultSpan[i].split('">')
        y = (x[1]).split('<')
        newResult.append(y[0])

    print(newResult)
'''




