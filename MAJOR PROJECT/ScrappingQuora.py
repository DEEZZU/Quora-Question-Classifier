#libraries required
import csv
import requests
from bs4 import BeautifulSoup

# ALGORITHM
# while creating url take care of apostrophes : old's in url is given as olds
# read csv of questions
with open('scrappedLabels.csv', 'r') as f:
    quora = list(csv.reader(f, delimiter=','))
#print(quora[0])

# pass each as url to get labels : append labels to each question
for i in range(0, 600):
    if quora[i][3] == '0' :
        #print("here")
        url = quora[i][2]
        #print(url)
        page = requests.get(url)
        soup = BeautifulSoup(page.content, 'html.parser')
        resultSpan = soup.find_all('span', attrs={'class':'TopicName TopicNameSpan'})
        if not resultSpan :
            resultSpan = soup.find_all('span', attrs={'class':'TopicNameSpan TopicName'})
        #it may be TopicNameSpan TopicName
        for j in range(len(resultSpan)):
            resultSpan[j]=str(resultSpan[j])
        newResult = []
        for k in range(len(resultSpan)):
            x = resultSpan[k].split('">')
            y = (x[1]).split('<')
            newResult.append(y[0])
            print(str(i)+" "+ str(newResult))
        if not not newResult :
            quora[i].extend(newResult)
            quora[i][3] = 1

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




