import urllib
from urllib.request import urlopen
from bs4 import BeautifulSoup
import html5lib
import pandas as pd

teams=["arizona-cardinals", "atlanta-falcons", "baltimore-ravens", "buffalo-bills", "carolina-panthers", "chicago-bears", "cincinnati-bengals", "cleveland-browns", "dallas-cowboys", "denver-broncos",
		"detroit-lions", "green-bay-packers", "houston-texans", "indianapolis-colts", "jacksonville-jaguars", "kansas-city-chiefs", "los-angeles-rams", "miami-dolphins", "minnesota-vikings", 
		"new-england-patriots", "new-orleans-saints", "new-york-giants", "new-york-jets", "oakland-raiders", "philadelphia-eagles", "pittsburgh-steelers", "san-diego-chargers", "san-francisco-49ers", "seattle-seahawks", "tampa-bay-buccaneers", "st.-louis-rams", 
		"tennessee-titans", "washington-redskins"]

years=["2011","2012","2013","2014","2015","2016"]
		
#moneytypes=["full-cap", "full-cash", "full-aav", "active-cap", "active-cash", "active-aav", "starters-cap", "starters-cash", "starters-aav"]


teamstest=["arizona-cardinals"]

yearstest=["2011"]

for team in teamstest:
	for year in yearstest:

		urltest='http://www.spotrac.com/nfl/%s/cap/%s' %(team, year)

		sauce=urllib.request.urlopen(urltest)
		soup=BeautifulSoup(sauce, 'lxml')

		tables=soup.find('table')
		datatable=soup.find_all('table', {"class": "datatable"})
		title=soup.find_all("h2")
		df=pd.read_html(str(datatable))
		elements=(len(df))
		for i in range(elements-1):
			label=(title[i].text)
			label=label.replace("/", "-")
			print(label)
			elementdf=df[i+1]
			#print(elementdf)
			#elementdf.to_csv('C:/Users/whjac/Downloads/Term Paper Data/Contract Information/Total Cap Hits/%s%s.csv' %(label, team))
			
		
		
		#for i in range(elements):
			#label=(title[i].text)
			#label=label.replace("/", "-")
			#print(label)
			#elementdf=df[i]
			#print(elementdf)
			#elementdf.to_csv('C:/Users/whjac/Downloads/Term Paper Data/Contract Information/Total Cap Hits/%s%s.csv' %(label, team))
	
		#activecap=df[0]
		#activecap.to_csv('C:/Users/whjac/Downloads/Term Paper Data/Contract Information/Total Cap Hits/Active Rosters/%s%s.csv' %(year, team))


#for team in teams:
#		for year in years:	
#				urltest='http://www.spotrac.com/nfl/%s/cap/%s/' %(team,year)
#				df='data%s' %(year)
#				print(urltest)
#
#				sauce=urllib.request.urlopen(urltest)
#				soup=BeautifulSoup(sauce, 'lxml')
#				print(soup)
#
#				tables = soup.find('table')
#				datatable = soup.find_all('table', {"class": "datatable"})
#				#print(df)
#				df=pd.read_html(str(datatable))
#				
#				for dfs in df:
#					title=soup.find("h2")
#				
#				active=df[0]
#				Practice Squad=df[1]
#				dead=df[2]
#				
#				active.to_csv('C:/Users/whjac/Downloads/Term Paper Data/Contract Information/Total Cap Hits/Active Rosters/%s%sdata.csv' %(year,team))
#				IR.to_csv('C:/Users/whjac/Downloads/Term Paper Data/Contract Information/Total Cap Hits/Injured Reserve/%s%sdata.csv' %(year,team))
#				dead.to_csv('C:/Users/whjac/Downloads/Term Paper Data/Contract Information/Total Cap Hits/Dead Cap Hits/%s%sdata.csv' %(year,team))
#				
#			
#				dfs = pd.read_html(urltest)
#				print(dfs)
#				for df in dfs:
#					dim=df.shape
#					nrow=dim[0]
#					df['Team']=(team)
#					df['Year']=(year)
#					#df.drop(['Rank','Unnamed: 5','Unnamed: 6','Unnamed: 7','Unnamed: 8','Unnamed: 9'],axis=1,inplace=True)
#		
#				print(df)
#				dfs.to_csv('C:/Users/whjac/Downloads/Term Paper Data/Contract Information/Total Cap Hit by position test/%s%sdata.csv' %(year,team))

	
#for tr in table_rows:
#	td = tr.find_all('td')
#	row = [i.text for i in td]
#	print(row)