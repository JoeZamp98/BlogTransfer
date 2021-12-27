from bs4 import BeautifulSoup
import requests
import csv

source = requests.get('https://josephzampitella.com/author/joezampitella/').text

soup = BeautifulSoup(source, 'lxml')

csv_file = open('wordpress_scraped.csv', 'w')

csv_writer = csv.writer(csv_file)
csv_writer.writerow(['headline', 'date', 'full_text'])

