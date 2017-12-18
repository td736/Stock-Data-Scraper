from Page import Page
from Scraper import Scraper

from pandas import DataFrame

import datetime

save_type = int(input("Select how you want to save the output\n1. txt\n2. csv\nEnter selection: "))

file = open('tags.txt', 'r')
tags = file.read()
file.close()

tags_list = tags.split('\n')

pages = []

for tag in tags_list:
    pages.append(Page(tag))

scraper = Scraper(pages)
scraper.scrape()

output = DataFrame(scraper.output)
output = output.T

if save_type == 1:
    output.to_csv('output/%s-%s.txt'%(datetime.datetime.now().day,datetime.datetime.now().month))

elif save_type == 2:
    output.to_csv('output/%s-%s.csv' % (datetime.datetime.now().day, datetime.datetime.now().month))

