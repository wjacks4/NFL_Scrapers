import urllib
from urllib.request import urlopen
from bs4 import BeautifulSoup
import html5lib
import pandas as pd
import sys
import numpy as np

teams=["arizona-cardinals", "atlanta-falcons", "baltimore-ravens", "buffalo-bills", "carolina-panthers", "chicago-bears", "cincinnati-bengals", "cleveland-browns", "dallas-cowboys", "denver-broncos",
		"detroit-lions", "green-bay-packers", "houston-texans", "indianapolis-colts", "jacksonville-jaguars", "kansas-city-chiefs", "los-angeles-rams", "los-angeles-chargers", "miami-dolphins", "minnesota-vikings", 
		"new-england-patriots", "new-orleans-saints", "new-york-giants", "new-york-jets", "oakland-raiders", "philadelphia-eagles", "pittsburgh-steelers", "san-diego-chargers", "san-francisco-49ers", "seattle-seahawks", "st.-louis-rams"
		"tampa-bay-buccaneers", "tennessee-titans", "washington-redskins"]

years=["2013","2014","2015","2016"]

teamstest=["arizona-cardinals", "atlanta-falcons"]

yearstest=["2013","2014"]

for team in teams:
		for year in years:	
				urltest='https://www.foxsports.com/nfl/%s-team-roster?season=%s' %(team,year)

				sauce=urllib.request.urlopen(urltest)
				soup=BeautifulSoup(sauce, 'lxml')
				print(soup)
				
				#rosterdfs = pd.read_html(urltest)
				#rosterdf = rosterdfs[0]
				#divs = soup.find_all("div", {"class": "wisbb_playerContainer"})
				#dfs=pd.read_html(urltest)
				#print(dfs)
				
				#for div in divs:
				#	spans = div.find_all("span", {"class": ""})
				#	for span in spans:
				#		#print(span.text)
				#		rosterdf = rosterdf.append({"Player":span.text,"Year":year,"Team":team}, ignore_index=True)
				
				#print(rosterdf)				
		
				#rosterdf.to_csv('C:/Users/whjac/Downloads/Term Paper Data/Rosters2/%s%s.csv' %(team,year))
				