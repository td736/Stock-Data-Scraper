import bs4 as bs
import urllib.request
from Scraper import scrape

import datetime

now = datetime.datetime.now()

file = open('tags.txt', 'r')
raw_tags = file.read()
file.close()

tags_list = raw_tags.split('\n')


def make_url(tag):
    return 'http://quotes.wsj.com/CH/XVTX/%s/research-ratings'%tag


def main():
    final_data = {}

    for tag in tags_list:
        final_data[tag] = scrape(make_url(tag))

    return final_data

