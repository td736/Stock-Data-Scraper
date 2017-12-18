import bs4 as bs
import urllib.request
import json
from Scraper import scrape


def make_url(tag):
    return 'http://quotes.wsj.com/CH/XVTX/%s/research-ratings'%tag


def main():
    file = open('tags.txt', 'r')
    raw_tags = file.read()
    file.close()

    tags_list = raw_tags.split('\n')

    final_data = {}

    for tag in tags_list:
        final_data[tag] = scrape(make_url(tag))

    out = open('out.txt', 'w')
    out.write(json.dumps(final_data))
