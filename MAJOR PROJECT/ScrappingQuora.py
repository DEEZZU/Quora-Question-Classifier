#libraries required
import requests
from bs4 import BeautifulSoup
import pprint

#speicfy the url
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




