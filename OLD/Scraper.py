import bs4 as bs
import urllib.request
'''
- Replace hardcoded parts with variables
- Tidy up.
'''


def scrape(url):

    sauce = urllib.request.urlopen(url).read()

    soup = bs.BeautifulSoup(sauce, 'lxml')

    out = []
    for s in soup.find_all('span'):
        out.append(str(s))

    data_loc = {'Avg': 0, 'Crn': 0}

    for item in out:
        if 'Average' in item:
            data_loc['Avg'] = out.index(item) + 1

        if 'Current Price' in item:
            data_loc['Crn'] = out.index(item) + 1

    def remove_tags(input_str):
        input_str = input_str.replace('<span class="data_data"><sup> </sup>', '')
        input_str = input_str.replace('</span>', '')
        return input_str

    data_out = {'Avg': 0, 'Crn': 0}

    data_out['Avg'] = remove_tags(out[data_loc['Avg']])
    data_out['Crn'] = remove_tags(out[data_loc['Crn']])

    return data_out

