#autobettor

#import brainybet
#import game_profile_generator
import csv
import datetime
import fieldingScrape
import pitchingScrape
import battingScrape
import nateDownload
import oddsScrape


def preprocess(day):
	preprocess_batting(day)
	preprocess_pitching(day)
	preprocess_fielding(day)
	preprocess_elo(day)

def getDay():
	d = datetime.date.today()
	d1 = f"{d:%m}"
	d2 = f"{d:%d}"
	return d1+d2
	
def into(inty):
	if(inty == ''):
		return 0
	else:
		return int(inty)

def preprocess_batting(day):
	filename = "mlbBattingData\\"+day+".csv"
	
	print(filename)
	
	with open(filename, mode='r') as mlbBattingFile:
		
		reader = csv.DictReader(mlbBattingFile)
		
		sortedlist = sorted(reader, key=lambda row:into(row['AB']), reverse=True)
		sortedlist = sorted(sortedlist, key=lambda row:row['Tm'], reverse=False)
		
		for line in sortedlist:
			if(line["Tm"] == "LAA"):
				line["Tm"] = "ANA"
			
			if(line["Tm"] == "TBR"):
				line["Tm"] = "TBD"
			
			if(line["Tm"] == "MIA"):
				line["Tm"] = "FLA"
	
	filename = "mlbBattingData\\bet_"+day+".csv"
	with open(filename, 'w', newline='') as f:
		fieldnames = ['Rk','Name','Age','Tm','Lg','G','PA','AB','R','H','2B','3B','HR','RBI','SB','CS','BB','SO','BA','OBP','SLG','OPS','OPS+','TB','GDP','HBP','SH','SF','IBB','Pos Summary']
		writer = csv.DictWriter(f, fieldnames=fieldnames)
		writer.writeheader()
		for row in sortedlist:
			writer.writerow(row)
		 

def preprocess_pitching(day):
	filename = "mlbPitchingData\\"+day+".csv"
	
	print(filename)
	
	with open(filename, mode='r') as mlbPitchingFile:
		
		reader = csv.DictReader(mlbPitchingFile)
		
		sortedlist = sorted(reader, key=lambda row:float(row['IP']), reverse=True)
		sortedlist = sorted(sortedlist, key=lambda row:row['Tm'], reverse=False)
		
		for line in sortedlist:
			if(line["Tm"] == "LAA"):
				line["Tm"] = "ANA"
			
			if(line["Tm"] == "TBR"):
				line["Tm"] = "TBD"
			
			if(line["Tm"] == "MIA"):
				line["Tm"] = "FLA"
	
	filename = "mlbPitchingData\\bet_"+day+".csv"
	with open(filename, 'w', newline='') as f:
		fieldnames = ['Rk','Name','Age','Tm','IP','G','GS','R','RA9','RA9opp','RA9def','RA9role','PPFp','RA9avg','RAA','WAA','gmLI','WAAadj','WAR','RAR','waaWL%','162WL%','Salary','Acquired']
		writer = csv.DictWriter(f, fieldnames=fieldnames)
		writer.writeheader()
		for row in sortedlist:
			writer.writerow(row)

def preprocess_fielding(day):
	filename = "mlbFieldingData\\"+day+".csv"
	
	print(filename)
	
	with open(filename, mode='r') as mlbFieldingFile:
		
		reader = csv.DictReader(mlbFieldingFile)
		
		sortedlist = sorted(reader, key=lambda row:row['Tm'], reverse=False)
		
		for line in sortedlist:
			if(line["Tm"] == "LAA"):
				line["Tm"] = "ANA"
			
			if(line["Tm"] == "TBR"):
				line["Tm"] = "TBD"
			
			if(line["Tm"] == "MIA"):
				line["Tm"] = "FLA"
	
	filename = "mlbFieldingData\\bet_"+day+".csv"
	with open(filename, 'w', newline='') as f:
		fieldnames = ['Tm','#Fld','RA/G','DefEff','G','GS','CG','Inn','Ch','PO','A','E','DP','Fld%','Rtot','Rtot/yr','Rdrs','Rdrs/yr']
		writer = csv.DictWriter(f, fieldnames=fieldnames)
		writer.writeheader()
		for row in sortedlist:
			if(row["Tm"] != "LgAvg"):
				writer.writerow(row)

def preprocess_elo(day):
	filename = "mlb-elo\\mlb_elo_latest_"+day+".csv"
	
	m = int(day[0:2])
	d = int(day[2:4])
	
	print(filename)
	
	with open(filename, mode='r') as mlbEloFile:
		
		reader = csv.DictReader(mlbEloFile)
		
		dictlist = list(reader)
		
	#2019-09-29
	filename = "mlb-elo\\bet_"+day+".csv"
	with open(filename, 'w', newline='') as f:
		fieldnames = ['date','season','neutral','playoff','team1','team2','elo1_pre','elo2_pre','elo_prob1','elo_prob2','elo1_post','elo2_post','rating1_pre','rating2_pre','pitcher1','pitcher2','pitcher1_rgs','pitcher2_rgs','pitcher1_adj','pitcher2_adj','rating_prob1','rating_prob2','rating1_post','rating2_post','score1','score2']
		writer = csv.DictWriter(f, fieldnames=fieldnames)
		writer.writeheader()
		for row in dictlist:
			if(row["season"] == "2019"):
				if((int(row["date"][5:7]) == m and int(row["date"][8:10]) <= d) or int(row["date"][5:7]) < m):
					writer.writerow(row)


def pullData(day):
	print("scraping...")
	fieldingScrape.scrape_fielding(day)
	battingScrape.scrape_batting(day)
	pitchingScrape.scrape_pitching(day)
	nateDownload.downloadNate(day)
	oddsScrape.scrapeOdds(day)
	
	print("scraping complete")
	print()
	print("preprocessing...")
	preprocess_batting(day)
	preprocess_pitching(day)
	preprocess_fielding(day)
	preprocess_elo(day)
	print("preprocessing complete")

pullData("0803")