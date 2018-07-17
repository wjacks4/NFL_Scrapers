import urllib
from urllib.request import urlopen
from bs4 import BeautifulSoup
import html5lib
import pandas as pd
import sys
import numpy as np

teams=["crd", "atl", "rav", "buf", "car", "chi", "cin", "cle", "dal", "den", "det", "gnb", "htx", "clt", "jax", "kan", "mia", "min", "nwe", "nor", "nyg", "nyj",
		"rai", "phi", "pit", "sdg", "sfo", "sea", "ram", "tam", "oti", "was"]

years=["2011","2012", "2013", "2014", "2015", "2016"]

teamstest=["crd", "atl"]

for team in teams:
	for year in years:
		
		urltest='http://www.pro-football-reference.com/teams/{0}/{1}_injuries.htm' .format(team, year)
		#print(urltest)
		
		sauce=urllib.request.urlopen(urltest)
		soup=BeautifulSoup(sauce, 'lxml')

		tables=soup.find('table')
		datatable=soup.find_all('table', {"class": "datatable"})
		
		
		df=pd.read_html(str(soup))
		for dfs in df:	
			dfs.to_csv("C:/Users/whjac/Downloads/Term Paper Data/Injury Data/newdata/{0}{1}.csv".format(team, year))
		

