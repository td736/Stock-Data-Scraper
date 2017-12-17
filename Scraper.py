import bs4 as bs
import urllib.request
'''
- Replace hardcoded parts with variables
- Tidy up.
'''
sauce = urllib.request.urlopen('http://quotes.wsj.com/CH/XVTX/NOVN/research-ratings').read()

soup = bs.BeautifulSoup(sauce, 'lxml')

out = []
for s in soup.find_all('span'):
    out.append(str(s))

data_loc = {}

for item in out:
    if 'Average' in item:
        data_loc['Avg'] = out.index(item) + 1

    if 'Current Price' in item:
        data_loc['Crn'] = out.index(item) + 1


def remove_tags(input_str):
    input_str = input_str.replace('<span class="data_data"><sup> </sup>', '')
    input_str = input_str.replace('</span>', '')
    return input_str

data_out = {}

data_out['Avg'] = float(remove_tags(out[data_loc['Avg']]))
data_out['Crn'] = float(remove_tags(out[data_loc['Crn']]))

