from bs4 import BeautifulSoup
import csv
import requests

def scrape_fielding(day):
	response = requests.get('https://www.baseball-reference.com/leagues/MLB/2019-standard-fielding.shtml')
	soup = BeautifulSoup(response.content,features="html.parser")
	table = soup.find("table",attrs={"id" : "teams_standard_fielding"})

	output_rows = []
	for table_row in table.findAll('tr'):
		columns = table_row.findAll('td')
		things = table_row.findAll('th')
		output_row = []
		for thing in things:
			got = thing.find('a')
			if(got != None):
				output_row.append(got.text)
			else:
				output_row.append(thing.text)
		for column in columns:
			output_row.append(column.text)
		output_rows.append(output_row)
		
		
	with open('mlbFieldingData\\'+day+'.csv', 'w', newline='') as csvfile:
		writer = csv.writer(csvfile)
		for row in output_rows:
			if(row[0] == "LgAvg"):
				break
			writer.writerow(row)
			
	print("fielding data written to file")