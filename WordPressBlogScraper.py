from bs4 import BeautifulSoup
import requests
import csv

archivesOne = requests.get('https://josephzampitella.com/author/joezampitella/').text
archivesTwo = requests.get('https://josephzampitella.com/author/joezampitella/page/2').text

testArticleOne = requests.get('https://josephzampitella.com/2020/12/16/winter-storm-expected-thursday-12-17/').text

soupOne = BeautifulSoup(archivesOne, 'lxml')
soupTwo = BeautifulSoup(archivesTwo, 'lxml')
soupThree = BeautifulSoup(testArticleOne, 'lxml')

csv_file = open('wordpress_scraped.csv', 'w')

csv_writer = csv.writer(csv_file)
csv_writer.writerow(['headline', 'date', 'full_text'])

for article in soupOne.find_all('article'):
    headline = article.h2.a.text
    print(headline)

for article in soupTwo.find_all('article'):
    headline = article.h2.a.text
    print(headline)

moreLink = soupTwo.find_all(class_='more-link')

for a in soupTwo.find_all('a', href=True, class_='more-link'):
    if a.text:
        print(a['href'])

#PULLS TEXT ONLY FROM PRIMARY CONTENT AREA (ARTICLE)

div = soupThree.find(class_='entry-content')

for article in div.find_all('p'):
     print(article.get_text())