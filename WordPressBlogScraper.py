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

# for paragraph in soupThree.find_all('article'):
#     content = paragraph.p.a.text
#     print(content)

section = soupThree.findAll('div', attrs={"class":"entry-content"})

htmlParse = BeautifulSoup(testArticleOne, 'html.parser')

div = soupThree.find(class_='entry-content')

for article in div.find_all('p'):
     print(article.get_text())