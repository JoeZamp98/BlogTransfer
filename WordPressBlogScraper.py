from bs4 import BeautifulSoup
import requests
import csv

from requests.exceptions import ConnectTimeout

archivesOne = requests.get('https://josephzampitella.com/author/joezampitella/').text
archivesTwo = requests.get('https://josephzampitella.com/author/joezampitella/page/2').text

soupOne = BeautifulSoup(archivesOne, 'lxml')
soupTwo = BeautifulSoup(archivesTwo, 'lxml')

#Opens CSV file

csv_file = open('wordpress_scraped.csv', 'w')

csv_writer = csv.writer(csv_file)
csv_writer.writerow(['headline', 'date', 'full_text'])

#Retrieves headlines from posts

articleTitles = []

for article in soupOne.find_all('article'):
    headline = article.h2.a.text
    #print(headline)
    articleTitles.append(headline)

for article in soupTwo.find_all('article'):
    headline = article.h2.a.text
    #print(headline)
    articleTitles.append(headline)

del(articleTitles[3]) #this article was missing an HREF link; will investigate

#Retrieves body text from individual posts

hrefList = []
contentList =[]

for a in soupOne.find_all('a', href=True, class_='more-link'):
    if a.text:
        hrefList.append(a['href'])

for a in soupTwo.find_all('a', href=True, class_='more-link'):
     if a.text:
         hrefList.append(a['href'])

for link in hrefList:

    postLink = requests.get(link).text
    postSoup = BeautifulSoup(postLink, 'lxml')
    
    div = postSoup.find(class_='entry-content')

    contentContainer = str()

    concatCounter = 0

    for section in div.find_all('p'):

        contentText = section.get_text()

        #print(contentText)

        if concatCounter == 0:
            
            finalContainer = contentContainer + contentText

            concatCounter += 1

        elif concatCounter > 0:

            finalContainer = finalContainer + "  " + contentText

            concatCounter += 1

    contentList.append(finalContainer)

    del(finalContainer)
        
counter = 0

while counter <= 15: 

    writeTitle = articleTitles[counter]
    writeLink = hrefList[counter]
    writeContent = contentList[counter]

    csv_writer.writerow([writeTitle, writeLink, writeContent])

    counter += 1

csv_file.close()

print(contentText)

print(len(contentList))

for i in contentList:
    print(i + '\n')