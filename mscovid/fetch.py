#!/usr/bin/env python3

import requests
import re
from bs4 import BeautifulSoup
import pandas as pd
from io import StringIO


class CovidException:
    pass


class CovidGetData:
    def __init__(self):
        self.url = "https://opendatasus.saude.gov.br/dataset/casos-nacionais"
        self.links = []
        self.stateSymbols = ['go', 'ce', 'mt', 'ms', 'pe', 'sp', 'ro', 'ac', 'pr', 'rr', 'ap',
                             'df', 'rs', 'ba', 'al', 'se', 'es', 'pb', 'to', 'pa', 'mg', 'sc',
                             'rj', 'rn', 'ma', 'pi', 'am']
        self.stateData = dict((x, []) for x in self.stateSymbols)

    def list_csv(self):
        r = requests.get(self.url)
        soup = BeautifulSoup(r.text)
        state_parse = re.compile('dados-(\\w{2}).*\\.csv')
        for link in soup.find_all('a', attrs={'class': 'resource-url-analytics'}):
            link = link.get('href')
            if re.search('.*\\.csv$', link):
                self.links.append(link)
                self.stateData[state_parse.search(link).group(1)].append(link)

    def reporter_download(self, state='all'):

        file_name = re.compile('([^/]+)$')
        if state == all:
            for value in self.stateData.values():
                for v in values:
                    data = requests.get(v)
                    data = pd.read_csv(StringIO(data.text))
                    #data.to_csv(file_name(v))
                    data.to_csv(data, file_name(v))
        else:
            for v in self.stateData[state]:
                data = requests.get(v)
                data = pd.read_csv(StringIO(data.text))
                #data.to_csv(file_name(v))
                data.to_csv(data, file_name(v))

#    @property
#    def reporter_download(self, state='all'):
##        if state == 'all' :
#           for state
