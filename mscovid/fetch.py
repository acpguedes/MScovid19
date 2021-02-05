#!/usr/bin/env python3

import requests
import re
from bs4 import BeautifulSoup
import sqlite3 as sql
from pandas import read_csv
from pandas import DataFrame

class Covid:
    def __init__(self):
        self.url = "https://opendatasus.saude.gov.br/dataset/casos-nacionais"
        self.links = []

    def list_csv(self):
        r = requests.get(self.url)
        soup = BeautifulSoup(r.text)
        for link in soup.find_all('a', attrs={'class': 'resource-url-analytics'}):
            link = link.get('href')
            if re.search('.*\.csv$', link):
                self.links.append(link)

    def reporter_download(self, state='all'):

        if not self.links:
            for link in links
        else:


    def create_db(self, name = 'covid19_data', path = "."):
        conn = sql.connect(name)



