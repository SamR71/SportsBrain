#Game Profile Generator
#BrainyBet component
#Sam Rackey
#2019

import csv
from statistics import mean

def main():
	mlb_batting_ops = {}
	mlb_pitching_war = {}
	mlb_team_fielding = {}

	startYear = 2018
	
	#Fill batting dictionary
	print("Loading batting data...")
	for y in range(1):
		filename = "mlbBattingData\mlb-batting-"+str(startYear+y)+".csv"
		#print()
		print("opening ",filename)
		with open(filename, mode='r') as mlbBattingFile:
			mlb_batting_ops[str(startYear+y)] = {}
			mlbBatting = csv.DictReader(mlbBattingFile)
			currteam = "XXX"
			r=0
			ops = []
			for row in mlbBatting:
				if(currteam != row["Tm"]):
					currteam = row["Tm"]
					r=1
					#print()
				if(r>0 and r<6):
					#print(startYear+y," ",row["Tm"]," #",r,": ",row["OPS"])
					ops.append(row["OPS"])
					r+=1
					if(r == 6):
						mlb_batting_ops[str(startYear+y)][currteam] = tuple(ops)
						ops = []
	
	#Fill pitching dictionary
	print("Loading pitching data...")
	for y in range(1):
		filename = "mlbPitchingData\mlb-pitching-"+str(startYear+y)+".csv"
		#print()
		print("opening ",filename)
		with open(filename, mode='r') as mlbPitchingFile:
			mlb_pitching_war[str(startYear+y)] = {}
			mlbPitching = csv.DictReader(mlbPitchingFile)
			currteam = "XXX"
			r=0
			war = []
			for row in mlbPitching:
				if(currteam != row["Tm"]):
					currteam = row["Tm"]
					r=1
					#print()
				if(r>0 and r<4):
					#print(startYear+y," ",row["Tm"]," #",r,": ",row["WAR"])
					war.append(row["WAR"])
					r+=1
					if(r == 4):
						mlb_pitching_war[str(startYear+y)][currteam] = tuple(war)
						war = []
	
	#Fill fielding dictionary
	print("Loading fielding data...")
	for y in range(1):
		filename = "mlbFieldingData\mlb-fielding-"+str(startYear+y)+".csv"
		#print()
		print("opening ",filename)
		with open(filename, mode='r') as mlbFieldingFile:
			mlb_team_fielding[str(startYear+y)] = {}
			mlbFielding = csv.DictReader(mlbFieldingFile)
			for row in mlbFielding:
				#print(startYear+y," ",row["Tm"]," DefEff: ",row["DefEff"],", Fld%: ",row["Fld%"])
				mlb_team_fielding[str(startYear+y)][row["Tm"]] = (row["DefEff"],row["Fld%"])
						
						
	#Generate per-game data
	print("writing game_profiles.csv...")
	game_profile_file = open("profiles\\2018_dumb_profiles.csv","w")
	game_profile_file.write("HOPS1,HOPS2,HOPS3,HOPS4,HOPS5,HWAR1,HWAR2,HWAR3,HFIELD1,HFIELD2,HWINYTD,HWINL5,HPITCH,HPRELO")
	game_profile_file.write(",HELO,AOPS1,AOPS2,AOPS3,AOPS4,AOPS5,AWAR1,AWAR2,AWAR3,AFIELD1,AFIELD2,AWINYTD,AWINL5,APITCH,APRELO,AELO,HRES,ARES")
	game_profile_file.write(",HTEAM,ATEAM,MONTH,DAY,YEAR\n")
	
	print("opening mlb_elo_training.csv")
	with open('mlb-elo\mlb_elo_training_2018.csv', mode='r') as mlb_elo_file:
		mlb_elo = csv.DictReader(mlb_elo_file)
		currentYear = -1
		records = {}
		for row in reversed(list(mlb_elo)):
			if(row["season"] != currentYear):
				currentYear = row["season"] 
				records[currentYear] = {}
			homeT = row["team1"]
			awayT = row["team2"]
			month = row["date"][5:7]
			day = row["date"][8:10]
			
			HRes = 0.0
			ARes = 0.0
			#determine YTD wins and last 5 wins
			if(row["score1"] != "" and int(row["score1"]) > int(row["score2"])):
				HRES = 1.0
				ARES = 0.0
			elif(row["score1"] != "" and int(row["score1"]) < int(row["score2"])):
				HRES = 0.0
				ARES = 1.0
				
			if(float(row["rating_prob1"]) > float(row["rating_prob2"])):
				HRes = 1.0
				ARes = 0.0
			elif(float(row["rating_prob1"]) < float(row["rating_prob2"])):
				HRes = 1.0
				ARes = 0.0
			
			if(homeT in records[currentYear] and row["score1"] != ""):
				records[currentYear][homeT].append(HRes)
			elif(row["score1"] != ""):
				records[currentYear][homeT] = []
				records[currentYear][homeT].append(HRes)
				
			if(awayT in records[currentYear] and row["score1"] != ""):
				records[currentYear][awayT].append(ARes)
			elif(row["score1"] != ""):
				records[currentYear][awayT] = []
				records[currentYear][awayT].append(ARes)
				
				
			
			#get rest of information
			home_ops = mlb_batting_ops[str(currentYear)][homeT]
			away_ops = mlb_batting_ops[str(currentYear)][awayT]
			home_war = mlb_pitching_war[str(currentYear)][homeT]
			away_war = mlb_pitching_war[str(currentYear)][awayT]
			home_fie = mlb_team_fielding[str(currentYear)][homeT]
			away_fie = mlb_team_fielding[str(currentYear)][awayT]
			
			if(len(records[currentYear][homeT]) > 1):
				#home_ytd = mean(records[currentYear][homeT][:-1])
				home_ytd = mean(records[currentYear][homeT])
			else:
				home_ytd = 0.0
				
			if(len(records[currentYear][awayT]) > 1):
				#away_ytd = mean(records[currentYear][awayT][:-1])
				away_ytd = mean(records[currentYear][awayT])
			else:
				away_ytd = 0.0
			
			if(row["score1"] != "" and len(records[currentYear][awayT])>5 and len(records[currentYear][homeT])>5):
				home_l5g = mean(records[currentYear][homeT][len(records[currentYear][homeT])-6:-1])
				away_l5g = mean(records[currentYear][awayT][len(records[currentYear][awayT])-6:-1])
			elif(row["score1"] == ""):
				home_l5g = mean(records[currentYear][homeT][-5:])
				away_l5g = mean(records[currentYear][awayT][-5:])
			else:
				home_l5g = 0.0
				away_l5g = 0.0
			home_elo = row["rating_prob1"]
			away_elo = row["rating_prob2"]
			
			home_pitch = row["pitcher1_rgs"]
			away_pitch = row["pitcher2_rgs"]
			
			home_prelo = row["elo_prob1"]
			away_prelo = row["elo_prob2"]
			
			#compile into line,write to file
			
			line = str(home_ops[0])+","+str(home_ops[1])+","+str(home_ops[2])+","+str(home_ops[3])+","+str(home_ops[4])+","
			line2 = str(home_war[0])+","+str(home_war[1])+","+str(home_war[2])+","+str(home_fie[0])+","+str(home_fie[1])+","
			line3 = str(home_ytd)+","+str(home_l5g)+","+str(home_pitch)+","+str(home_prelo)+","+str(home_elo)+","+str(away_ops[0])+","+str(away_ops[1])+","+str(away_ops[2])+","
			line4 = str(away_ops[3])+","+str(away_ops[4])+","+str(away_war[0])+","+str(away_war[1])+","+str(away_war[2])+","
			line5 = str(away_fie[0])+","+str(away_fie[1])+","+str(away_ytd)+","+str(away_l5g)+","+str(away_pitch)+","+str(away_prelo)+","+str(away_elo)+","
			line6 = str(HRES)+","+str(ARES)+","+str(homeT)+","+str(awayT)+","+str(month)+","+str(day)+","+str(currentYear)+"\n"
			
			game_profile_file.write(line)
			game_profile_file.write(line2)
			game_profile_file.write(line3)
			game_profile_file.write(line4)
			game_profile_file.write(line5)
			game_profile_file.write(line6)
			
	print("Successfully generated game profiles!")
				
main()