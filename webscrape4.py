import urllib
from urllib.request import urlopen
from bs4 import BeautifulSoup
import html5lib
import pandas as pd
import sys
import numpy as np

years=["2011", "2012", "2013", "2014", "2015", "2016"]

positions=["qb", "rb", "wr", "te", "k", "dl", "lb", "db", "k"]

weeks=list(range(1,16))

teamstest=["crd", "atl"]

for year in years:
	for position in positions:
		for week in weeks:
		
			urltest='https://www.fantasypros.com/nfl/reports/leaders/{0}.php?year={1}&start={2}&end={3}' .format(position, year, week, week)
			#print(urltest)
		
			sauce=urllib.request.urlopen(urltest)
			soup=BeautifulSoup(sauce, 'lxml')

			tables=soup.find('table')
			
			output="C:/Users/whjac/Downloads/Term Paper Data/Individual Player Weekly Stats/{0}{1}{2}.csv".format(position, year, week)
			#print(output)
			
			#print(tables)
			df=pd.read_html(str(tables))
			for dfs in df:	
				dfs.to_csv("C:/Users/whjac/Downloads/Term Paper Data/Individual Player Weekly Stats/{0}-{1}-week{2}.csv".format(position, year, week))