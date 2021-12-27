from bs4 import BeautifulSoup
import requests
import csv

archivesOne = requests.get('https://josephzampitella.com/author/joezampitella/').text
archivesTwo = requests.get('https://josephzampitella.com/author/joezampitella/page/2').text

soupOne = BeautifulSoup(archivesOne, 'lxml')
soupTwo = BeautifulSoup(archivesTwo, 'lxml')

csv_file = open('wordpress_scraped.csv', 'w')

csv_writer = csv.writer(csv_file)
csv_writer.writerow(['headline', 'date', 'full_text'])

for article in soupOne.find_all('article'):
    headline = article.h2.a.text
    print(headline)

for article in soupTwo.find_all('article'):
    headline = article.h2.a.text
    print(headline)