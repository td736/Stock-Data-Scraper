import bs4 as bs
import urllib.request


class Page():

    def __init__(self, tag, country, code):
        self.tag = tag
        self.country = country
        self.code = code
        self.url = 'http://quotes.wsj.com/%s/%s/%s/research-ratings' % (self.country, self.code, self.tag)

        sauce = urllib.request.urlopen(self.url).read()
        soup = bs.BeautifulSoup(sauce, 'lxml')

        self.raw_data = []

        for span_tag in soup.find_all('span'):
            self.raw_data.append(str(span_tag))

