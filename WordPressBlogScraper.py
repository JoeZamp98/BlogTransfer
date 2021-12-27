from bs4 import BeautifulSoup
import requests
import csv

archivesOne = requests.get('https://josephzampitella.com/author/joezampitella/').text
archivesTwo = requests.get('https://josephzampitella.com/author/joezampitella/page/2').text

testArticleOne = requests.get('https://josephzampitella.com/2020/12/16/winter-storm-expected-thursday-12-17/').text

soupOne = BeautifulSoup(archivesOne, 'lxml')
soupTwo = BeautifulSoup(archivesTwo, 'lxml')
soupThree = BeautifulSoup(testArticleOne, 'lxml')

#Opens 

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

#Retrieves body text from individual posts

hrefList = []
contentList =[]

for a in soupTwo.find_all('a', href=True, class_='more-link'):
     if a.text:
         hrefList.append(a['href'])

for link in hrefList:

    postLink = requests.get(link).text
    postSoup = BeautifulSoup(postLink, 'lxml')
    
    div = postSoup.find(class_='entry-content')

    for section in div.find_all('p'):

        contentText = section.get_text()

        contentList.append(contentText)

csv_file.close()