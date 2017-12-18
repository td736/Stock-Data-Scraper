import bs4 as bs
import urllib.request


class Page:

    def __init__(self, tag):
        self.tag = tag
        self.url = 'http://quotes.wsj.com/CH/XVTX/%s/research-ratings' % self.tag

        sauce = urllib.request.urlopen(self.url).read()
        soup = bs.BeautifulSoup(sauce, 'lxml')

        self.raw_data = []

        for span_tag in soup.find_all('span'):
            self.raw_data.append(str(span_tag))

