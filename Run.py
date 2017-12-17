import bs4 as bs
import urllib.request

import os
import json

from Scraper import scrape
import Main


import datetime

if 'tags.txt' not in os.listdir():
    open('tags.txt', 'w')

if 'out.txt' not in os.listdir():
    open('out.txt', 'w')

Main.main()

now = datetime.datetime.now()
filename = '%s-%s.txt'%(now.day, now.month)
os.renames('out.txt', filename)
