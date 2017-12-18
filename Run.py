from Page import Page
from Scraper import Scraper

import json
import datetime

file = open('tags.txt', 'r')
tags = file.read()
file.close()

tags_list = tags.split('\n')

pages = []

for tag in tags_list:
    pages.append(Page(tag))

scraper = Scraper(pages)
scraper.scrape()

with open('output/%s-%s.txt'%(datetime.datetime.now().day,datetime.datetime.now().month), 'w') as out:
    out.write(json.dumps(scraper.output))

