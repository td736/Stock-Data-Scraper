from Page import Page
from Scraper import Scraper

from pandas import DataFrame

import datetime

save_type = int(input("Select how you want to save the output\n1. txt\n2. csv\nEnter selection: "))

''' Load Switzerland  CH/XVTK'''
file = open('ch.txt', 'r')
ch = file.read()
file.close(

''' Load Germany  DE/XFRA'''
file = open('de.txt', 'r')
de = file.read()
file.close()

ch_list = ch.split('\n')
de_list = de.split('\n')

pages = []

for tag in ch_list:
    pages.append(Page(tag, 'CH', 'XVTK'))

for tag in de_list:
    pages.append(Page(tag, 'DE', 'XFRA'))

scraper = Scraper(pages)
scraper.scrape()

output = DataFrame(scraper.output)
output = output.T

if save_type == 1:
    output.to_csv('output/%s-%s.txt'%(datetime.datetime.now().day,datetime.datetime.now().month))

elif save_type == 2:
    output.to_csv('output/%s-%s.csv' % (datetime.datetime.now().day, datetime.datetime.now().month))

