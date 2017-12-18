
class Scraper():

    def __init__(self, pages):
        self.output = {}
        self.pages = pages

        for page in pages:
            self.output[page.tag] = {}

    def scrape(self):
        for page in self.pages:
            locations = {'Avg': 0, 'Crn': 0}

            for item in page.raw_data:
                if 'Average' in item:
                    locations['Avg'] = page.raw_data.index(item) + 1

                elif 'Current Price' in item:
                    locations['Crn'] = page.raw_data.index(item) + 1

            self.output[page.tag]['Avg'] = page.raw_data[locations['Avg']].replace(
                '<span class="data_data"><sup> </sup>', '').replace('</span>', '')
            self.output[page.tag]['Crn'] = page.raw_data[locations['Crn']].replace(
                '<span class="data_data"><sup> </sup>', '').replace('</span>', '')


