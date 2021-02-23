#!/usr/bin/env python3

import requests
import re
from bs4 import BeautifulSoup
import pandas as pd
from io import StringIO
from datetime import date



class CovidException:
    pass


class CovidGetData:
    '''Class to get data from Ministério da Saúde (health ministry) about Covid in Brazil'''

    def __init__(self):
        self.url = "https://opendatasus.saude.gov.br/dataset/casos-nacionais"
        self.links = []
        self.stateSymbols = ['go', 'ce', 'mt', 'ms', 'pe', 'sp', 'ro', 'ac', 'pr', 'rr', 'ap',
                             'df', 'rs', 'ba', 'al', 'se', 'es', 'pb', 'to', 'pa', 'mg', 'sc',
                             'rj', 'rn', 'ma', 'pi', 'am']
        self.stateData = dict((x, []) for x in self.stateSymbols)
        self.file = ''

    def list_csv(self):
        '''Metod to list files'''
        r = requests.get(self.url)
        soup = BeautifulSoup(r.text)
        state_parse = re.compile('dados-(\\w{2}).*\\.csv')
        for link in soup.find_all('a', attrs={'class': 'resource-url-analytics'}):
            link = link.get('href')
            if re.search('.*\\.csv$', link):
                self.links.append(link)
                self.stateData[state_parse.search(link).group(1)].append(link)

    def reporter(self, state='all', format='csv'):
        today = date.today()
        self.file = '.'.join(['_'.join([state, today.strftime('%m%d%Y')]), format])
        if state == all:
            for value in self.stateData.values():
                for v in value:
                    data = requests.get(v)
        else:
            for v in self.stateData[state]:
                data = requests.get(v)
        return data
