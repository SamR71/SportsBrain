from bs4 import BeautifulSoup
import csv
import requests

def scrape_batting(day):
	response = requests.get('https://www.baseball-reference.com/leagues/MLB/2019-standard-batting.shtml')
	data = str(response.content)
	#data = data.replace("</div>\n-->\n","</div>\n\n")
	data = data.replace("<!--\\n","\\n")
	
	soup = BeautifulSoup(data,features="html.parser")
	table = soup.find("table",attrs={"id" : "players_standard_batting"})
	
	print("scraped batting!")

	output_rows = []
	printedTop = False
	for table_row in table.findAll('tr'):
		columns = table_row.findAll('td')
		things = table_row.findAll('th')
		if(len(things) > 0 and things[0].text != "Rk"):
			output_row = []
			for thing in things:
				got = thing.find('a')
				if(got != None):
					output_row.append(got.text)
				else:
					output_row.append(thing.text)
			for column in columns:
				got = thing.find('a')
				if(got != None):
					output_row.append(got.text)
				else:
					output_row.append(column.text)
			output_rows.append(output_row)
		
	header_row = ['Rk','Name','Age','Tm','Lg','G','PA','AB','R','H','2B','3B','HR','RBI','SB','CS','BB','SO','BA','OBP','SLG','OPS','OPS+','TB','GDP','HBP','SH','SF','IBB','Pos Summary']
	with open('mlbBattingData\\'+day+'.csv', 'w', newline='') as csvfile:
		writer = csv.writer(csvfile)
		writer.writerow(header_row)
		for row in output_rows:
			if(row[1] == "LgAvg per 600 PA"):
				break
			writer.writerow(row)
			
	print("batting data written to file")
			