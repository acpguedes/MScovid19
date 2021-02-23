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

    def reporter(self, state='all', save=True, format='csv'):
        today = date.today()
        file = '.'.join(['_'.join([state, today.strftime('%m%d%Y')]), format])
        data = dict()
        if state == all:
            for key, value in self.stateData:
                for v in value:
                    data[key] = list()
                    data[key].append(requests.get(v))
        else:
            for v in self.stateData[state]:
                data[state] = list()
                data[state].append(requests.get(v))
#        return data
        if save:
            f = open(file, "a")
            for key in data.keys():
                for value in data[key]:
                    f.write(value)
            f.close()
        else:
            return data
