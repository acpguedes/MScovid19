#!/usr/bin/env python3

from mscovid.fetch import CovidGetData

a = CovidGetData()
a.list_csv()
b = a.reporter('pa')