import urllib
from urllib.request import urlopen
from bs4 import BeautifulSoup, Comment
import html5lib
import pandas as pd
import sys
import numpy as np

teams=["crd", "atl", "rav", "buf", "car", "chi", "cin", "cle", "dal", "den", "det", "gnb", "htx", "clt", "jax", "kan", "mia", "min", "nwe", "nor", "nyg", "nyj",
		"rai", "phi", "pit", "sdg", "sfo", "sea", "ram", "tam", "oti", "was"]

years=["2008","2009","2010","2011","2012", "2013", "2014", "2015", "2016"]

teamstest=["crd", "atl"]

for team in teams:
	for year in years:
		
		urltest='https://www.pro-football-reference.com/teams/{0}/{1}_roster.htm' .format(team, year)
		#print(urltest)
		
		sauce=urllib.request.urlopen(urltest)
		soup=BeautifulSoup(sauce, 'lxml')
		#print(sauce)

		tables=soup.find('table')
		
		df=pd.read_html(str(soup))
		for dfs in df:	
			dfs.to_csv("C:/Users/whjac/Downloads/Term Paper Data/ExperienceData/{0}{1}.csv".format(team, year))