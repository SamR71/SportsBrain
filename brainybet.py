#BRAINYBET
#Sam Rackey
#2019

import os
import keras
import numpy as np
import matplotlib as plt
import csv
from statistics import mean
from statistics import stdev
from keras.models import Sequential
from keras.layers import Dense, Dropout
from keras.optimizers import RMSprop, SGD, Adagrad
from keras.models import load_model
from bettor import getDay
from mlbUtil import replaceTeamCodes
from mlbUtil import tokenizeTeamName
from random import randint
import game_profile_generator_file


#reads csv of game profiles, creates numpy array of inputs and outputs
def load_profiles(filename):
	#print("Loading profiles...")
	with open(filename) as game_profiles_file:
		game_profiles = csv.DictReader(game_profiles_file)
		
		games = []
		results = []
		
		for row in game_profiles:
			l = []
			o = []
			
			l.append(float(row["HOPS1"]))
			l.append(float(row["HOPS2"]))
			l.append(float(row["HOPS3"]))
			l.append(float(row["HOPS4"]))
			l.append(float(row["HOPS5"]))
			l.append(float(row["HWAR1"]))
			l.append(float(row["HWAR2"]))
			l.append(float(row["HWAR3"]))
			l.append(float(row["HFIELD1"]))
			l.append(float(row["HFIELD2"]))
			
			l.append(float(row["HWINYTD"]))
			l.append(float(row["HWINL5"]))
			l.append(float(row["HELO"]))
			l.append(float(row["HPITCH"]))
			l.append(float(row["HPRELO"]))
			l.append(tokenizeTeamName(row["HTEAM"]))
			
			l.append(float(row["AOPS1"]))
			l.append(float(row["AOPS2"]))
			l.append(float(row["AOPS3"]))
			l.append(float(row["AOPS4"]))
			l.append(float(row["AOPS5"]))
			l.append(float(row["AWAR1"]))
			l.append(float(row["AWAR2"]))
			l.append(float(row["AWAR3"]))
			l.append(float(row["AFIELD1"]))
			l.append(float(row["AFIELD2"]))
			
			l.append(float(row["AWINYTD"]))
			l.append(float(row["AWINL5"]))
			l.append(float(row["AELO"]))
			l.append(float(row["APITCH"]))
			l.append(float(row["APRELO"]))
			l.append(tokenizeTeamName(row["ATEAM"]))
			
			o.append(float(row["HRES"]))
			o.append(float(row["ARES"]))
			
			prof_array = np.array(l)
			res_array = np.array(o)
			
			games.append(prof_array)
			results.append(res_array)
	
	#print("Profiles loaded!")
	
	return np.array(games),np.array(results)
	return np.array(games)

#reads csv of game profiles, creates numpy array of inputs and outputs
def load_nate_profiles(filename):
	#print("Loading profiles...")
	with open(filename) as game_profiles_file:
		game_profiles = csv.DictReader(game_profiles_file)
		
		games = []
		results = []
		
		for row in game_profiles:
			l = []
			o = []
			
			if(row["pitcher1_adj"] != '' and row["pitcher2_adj"] != ''):
			
			
				l.append(tokenizeTeamName(row["team1"]))
				l.append(tokenizeTeamName(row["team2"]))
				
				l.append(float(row["elo1_pre"]))
				l.append(float(row["elo2_pre"]))
				l.append(float(row["elo_prob1"]))
				l.append(float(row["elo_prob2"]))
				l.append(float(row["rating1_pre"]))
				l.append(float(row["rating2_pre"]))
				l.append(float(row["pitcher1_rgs"]))
				l.append(float(row["pitcher2_rgs"]))
				l.append(float(row["pitcher1_adj"]))
				l.append(float(row["pitcher2_adj"]))
				l.append(float(row["rating_prob1"]))
				l.append(float(row["rating_prob2"]))
				
				if(int(row["score1"]) > int(row["score2"])):
					hres = 1.0
					ares = 0.0
				else:
					hres = 0.0
					ares = 1.0
				
				
				o.append(hres)
				o.append(ares)
				
				prof_array = np.array(l)
				res_array = np.array(o)
				
				games.append(prof_array)
				results.append(res_array)
	
	#print("Profiles loaded!")
	
	return np.array(games),np.array(results)
	return np.array(games)
	
def load_profiles28(filename):
	#print("Loading profiles...")
	with open(filename) as game_profiles_file:
		game_profiles = csv.DictReader(game_profiles_file)
		
		games = []
		results = []
		
		for row in game_profiles:
			l = []
			o = []
			
			l.append(float(row["HOPS1"]))
			l.append(float(row["HOPS2"]))
			l.append(float(row["HOPS3"]))
			l.append(float(row["HOPS4"]))
			l.append(float(row["HOPS5"]))
			l.append(float(row["HWAR1"]))
			l.append(float(row["HWAR2"]))
			l.append(float(row["HWAR3"]))
			l.append(float(row["HFIELD1"]))
			l.append(float(row["HFIELD2"]))
			l.append(float(row["HWINYTD"]))
			l.append(float(row["HWINL5"]))
			l.append(float(row["HELO"]))
			l.append(float(row["AOPS1"]))
			l.append(float(row["AOPS2"]))
			l.append(float(row["AOPS3"]))
			l.append(float(row["AOPS4"]))
			l.append(float(row["AOPS5"]))
			l.append(float(row["AWAR1"]))
			l.append(float(row["AWAR2"]))
			l.append(float(row["AWAR3"]))
			l.append(float(row["AFIELD1"]))
			l.append(float(row["AFIELD2"]))
			l.append(float(row["AWINYTD"]))
			l.append(float(row["AWINL5"]))
			l.append(float(row["AELO"]))
			
			l.append(float(row["MONTH"]))
			l.append(float(row["DAY"]))
			
			o.append(float(row["HRES"]))
			o.append(float(row["ARES"]))
			
			prof_array = np.array(l)
			res_array = np.array(o)
			
			games.append(prof_array)
			results.append(res_array)
	
	#print("Profiles loaded!")
	
	return np.array(games),np.array(results)
	return np.array(games)

	
def load_profiles_sparse(filename):
	#print("Loading profiles...")
	with open(filename) as game_profiles_file:
		game_profiles = csv.DictReader(game_profiles_file)
		
		games = []
		results = []
		
		for row in game_profiles:
			l = []
			o = []
			
			l.append(float(row["HWINYTD"]))
			l.append(float(row["HWINL5"]))
			l.append(float(row["HELO"]))
			l.append(float(row["HPITCH"]))
			l.append(float(row["HPRELO"]))
			l.append(tokenizeTeamName(row["HTEAM"]))
			l.append(float(row["AWINYTD"]))
			l.append(float(row["AWINL5"]))
			l.append(float(row["AELO"]))
			l.append(float(row["APITCH"]))
			l.append(float(row["APRELO"]))
			l.append(tokenizeTeamName(row["ATEAM"]))
			
			o.append(float(row["HRES"]))
			o.append(float(row["ARES"]))

			
			prof_array = np.array(l)
			res_array = np.array(o)
			
			games.append(prof_array)
			results.append(res_array)
	
	#print("Profiles loaded!")
	
	return np.array(games),np.array(results)
	return np.array(games)

#def predict(file, model):
#	print()
#	print("Determining Predictions for ", file)
#	games,outcomes = load_profiles(file)
#	print(model.predict(games,batch_size=1,verbose=0,steps=None))
#	print()

def predict(day, model):
	#print()
	file = "profiles\\"+day+"_profiles.csv"
	#print("Determining Predictions for ", file)
	games,outcomes = load_profiles_sparse(file)
	#print(model.predict(games,batch_size=1,verbose=0,steps=None))
	predictions = model.predict(games,batch_size=1,verbose=0,steps=None)
	
	#print("Predictions:")
	toRet = {}
	with open(file) as game_profiles_file:
		game_profiles = csv.DictReader(game_profiles_file)
		
		i=0
		for row in game_profiles:
			toRet[row["HTEAM"]] = predictions[i][0]
			#print(row["HTEAM"]+": "+str(predictions[i][0]))
			toRet[row["ATEAM"]] = predictions[i][1]
			#print(row["ATEAM"]+": "+str(predictions[i][1]))
			i+=1
		
	#print(toRet)
	#print()
	#print("Moneylines:")
	
	
	##ODDSPORTAL -----------------------------------------
	#odds = {}
	#oddsFile = day+"moneyline.txt"
	#moneylineOddsFile = open(oddsFile,'r')
	#moneylineOdds = moneylineOddsFile.readlines()
	#for i in range(int((len(moneylineOdds)-1)/4)):
	#	l = replaceTeamCodes(moneylineOdds[(4*i)+1])
	#	home = l[7:10]
	#	away = l[13:16]
	#	homeodds = float(moneylineOdds[(4*i)+2])
	#	awayodds = float(moneylineOdds[(4*i)+3])
	#	odds[home] = homeodds
	#	#print(home+": "+str(homeodds))
	#	odds[away] = awayodds
	#	#print(away+": "+str(awayodds))
	##----------------------------------------------------
	
	##BET ONLINE -----------------------------------------
	oddsFile = "scrapedOdds\\"+day+".csv"
	odds = {}
	with open(oddsFile) as day_odds_file:
		dayOdds = csv.DictReader(day_odds_file)
		for row in dayOdds:
			odds[row["Team"]] = float(row["Moneyline"])
	##-----------------------------------------------------
	
	#print()
	#print("Expected values:")
	evs = {}
	for thing in odds:
		if(odds[thing]*toRet[thing] > 1.1):
			evs[thing] = odds[thing]*toRet[thing]
			#print(thing+": "+str(evs[thing]))
	
	#print()
	
	return toRet,odds,evs

def sbet(day, capital, model):
	
	results = {}
	
	with open("mlb-elo\\mlb_elo_latest_0712.csv") as day_results_file:
		dayResults = csv.DictReader(day_results_file)
		
		for row in dayResults:
			if(day == row["date"][5:7]+row["date"][8:10]):
				if(int(row["score1"]) > int(row["score2"])):
					hres = 1.0
					ares = 0.0
				else:
					hres = 0.0
					ares = 1.0
			
				results[row["team1"]] = hres
				results[row["team2"]] = ares
				
	print()
	print("Betting capital to work with today: $" + capital)
	#print("EVs we are working with:")
	preds,lines,evs = predict(day, model)
	#for ev in evs:
	#	print(ev +": "+ str(evs[ev]))
	
	#print()
	print("Bets to place:")
	
	weights = weightings(lines,preds,evs)
	bets = []
	for weight in weights:
		#print(weight+": "+str(float(capital)*weights[weight]))
		tup = (weight, float(capital)*weights[weight])
		bets.append(tup)
	
	bets.sort(key=lambda tup: tup[1], reverse=True)
	
	checkwork = 0
	winnings = 0
	for bet in bets:
		if(bet[1] > 1.0):
			print()
			print(bet[0]+": $"+str(round(bet[1],2)))
			print("   Moneyline: "+str(lines[bet[0]])+", Predicted: "+str(round(preds[bet[0]],3))+",  EV: "+str(round(evs[bet[0]],2))) 
			checkwork += round(bet[1],2)
			
			if(bet[0] not in results):
				#no action
				winnings += round(bet[1],2)
				print("   Won: $"+str(round(bet[1],2)))
			else:
				winnings += results[bet[0]]*round(bet[1],2)*lines[bet[0]]
				print("   Won: $"+str(round(results[bet[0]]*round(bet[1],2)*lines[bet[0]],2)))
			
	print()
	print("total bet: $", str(round(checkwork,2)))
	print("won: $", str(round(winnings,2))+", ($"+  str(round(winnings-checkwork,2))+ ")" )
	print("return: "+str(round(((winnings-checkwork)/checkwork)*100, 3))+"%")
	
def bet(day, capital, model):
	print()
	print("Pulling data...")
	game_profile_generator_file.main()

	print()
	print("Betting capital to work with today: $" + str(capital))
	#print("EVs we are working with:")
	preds,lines,evs = predict(day, model)
	#for ev in evs:
	#	print(ev +": "+ str(evs[ev]))
	
	#print()
	print("Bets to place:")
	weights = alt_weightings(evs)
	bets = []
	for weight in weights:
		#print(weight+": "+str(float(capital)*weights[weight]))
		tup = (weight, float(capital)*weights[weight])
		bets.append(tup)
	
	bets.sort(key=lambda tup: tup[1], reverse=True)
		
	
	checkwork = 0
	wagers = []
	for bet in bets:
		if(bet[1] > 1.0):
			print(bet[0]+": $"+str(round(bet[1],2)))
			print("   Moneyline: "+str(round(lines[bet[0]],2))+", Predicted: "+str(round(preds[bet[0]],3))+",  EV: "+str(round(evs[bet[0]],2))) 
			checkwork += round(bet[1],2)
			wager = [bet[0],round(bet[1],2),round(lines[bet[0]],2),round(preds[bet[0]],3),round(evs[bet[0]],2)]
			wagers.append(wager)
	
	print("total bet: $", str(round(checkwork,2)))
	
	
	header_row = ['Team','Wager','Moneyline','Predicted','EV']
	with open('betRecords\\'+day+'_bet_record.csv', 'w', newline='') as csvfile:
		writer = csv.writer(csvfile)
		writer.writerow(header_row)
		for row in wagers:
			writer.writerow(row)

def analyze_bet(day,iterations):
	
	print("starting analysis")
	
	bets = {}
	lines = {}
	predictions = {}
	teams = []
	avg = 0
	
	with open("betRecords\\"+day+"_bet_record.csv") as day_bet_record_file:
		dayWagers = csv.DictReader(day_bet_record_file)
		for b in dayWagers:
			teams.append(b["Team"])
			bets[b["Team"]] = round(float(b["Wager"]),2)
			lines[b["Team"]] = round(float(b["Moneyline"]),2)
			predictions[b["Team"]] = int(float(b["Predicted"])*100)
			
	winnings = {}
	for i in range(0,iterations):
		print("analysis:",i)
		simWin = 0
		for team in teams:
			luck = randint(1,100)
			if(luck <= predictions[team]):
				simWin += int(bets[team]*lines[team])
				avg+=(bets[team]*lines[team])
		simWin = str(simWin)
		if(simWin in winnings):
			winnings[simWin] += 1
		else:
			winnings[simWin] = 1
					
	with open("analyses\\"+day+"_bet_analysis.csv", 'w', newline='') as csvfile:
		writer = csv.writer(csvfile)
		for win in winnings:
			row = [win, winnings[win]]
			writer.writerow(row)
	
	avg = avg / iterations
	print("average return:", avg)
	print("analysis complete")
	
def analyze_bet_compounding(listDays, startBank, iterations):
	
	#print("starting analysis")
	days = {}
	
	for day in listDays:
		days[day] = {}
		
		days[day]["b"] = {}
		days[day]["l"] = {}
		days[day]["p"] = {}
		days[day]["t"] = []
		
		amountBet = 0.0
		with open("betRecords\\"+day+"_bet_record.csv") as day_bet_record_file:
			dayWagers = csv.DictReader(day_bet_record_file)
			for b in dayWagers:
				amountBet += round(float(b["Wager"]),2)
	
	
		with open("betRecords\\"+day+"_bet_record.csv") as day_bet_record_file:
			dayWagers = csv.DictReader(day_bet_record_file)
			for b in dayWagers:
				days[day]["t"].append(b["Team"])
				days[day]["b"][b["Team"]] = round(float(b["Wager"])/amountBet,2)
				days[day]["l"][b["Team"]] = round(float(b["Moneyline"]),2)
				days[day]["p"][b["Team"]] = int(float(b["Predicted"])*100)
	
	winnings = {}
	for i in range(iterations):
		bank = startBank
		
		for day in listDays:
			cap = bank*0.50
			#print(bank)
			for team in days[day]["t"]:
				luck = randint(1,100)
				if(luck <= days[day]["p"][team]):
					if(cap*days[day]["b"][team]<=10000):
						bank+=(cap*days[day]["b"][team]*days[day]["l"][team])
						bank-=(cap*days[day]["b"][team])
					else:
						bank+=(10000*days[day]["l"][team])
						bank-=10000
				else:
					if(cap*days[day]["b"][team]<=10000):
						bank-=(cap*days[day]["b"][team])
					else:
						bank-=10000
		
		bank = str(round(bank))
		if(bank in winnings):
			winnings[bank] += 1
		else:
			winnings[bank] = 1
						
	with open("analyses\\"+listDays[0]+"_to_"+listDays[len(listDays)-1]+"_bet_analysis.csv", 'w', newline='') as csvfile:
		writer = csv.writer(csvfile)
		for win in winnings:
			row = [win, winnings[win]]
			writer.writerow(row)
	
	print("analysis complete")
	
	
		
def weightings(Moneylines, Predictions,ExpectedValues):  #note that teams listed in Moneylines MUST match teams in Predictions
	#Logistics function parameters
	LSlope = 30
	LCenter = 0.6
	
	#plt.plot(LCurve[:,0],LCurve[:,1])
	#plt.xlabel('Confidence')
	#plt.ylabel('Weighting factor')
	#plt.title('Logistics Curve Weighting')
	#plt.show()
	

	LCurve= np.zeros([15,2])
	for count in range(1,16):
		Index = 1/15 * count
		LCurve[count-1,0]=Index
		LCurve[count-1,1]=1/(1+np.exp(-LSlope*(Index-LCenter)))
	

	BetsOfDay = {}

	SumConf=0
	NormFactor=0
	TotalBetsOfDay=0
	for Team in ExpectedValues:
		SumConf += Predictions[Team] * 1/(1+np.exp(-LSlope*(Predictions[Team]-LCenter)))
		
	NormFactor = 1/SumConf
	
	for Team in ExpectedValues:
		BetsOfDay[Team] = Predictions[Team] *  1/(1+np.exp(-LSlope*(Predictions[Team]-LCenter)))*NormFactor
		
	return BetsOfDay

def alt_weightings(ExpectedValues):  #note that teams listed in Moneylines MUST match teams in Predictions
	#print(ExpectedValues)
	#Logistics function parameters
	LSlope = 30
	LCenter = 0.6
	
	#plt.plot(LCurve[:,0],LCurve[:,1])
	#plt.xlabel('Confidence')
	#plt.ylabel('Weighting factor')
	#plt.title('Logistics Curve Weighting')
	#plt.show()
	

	LCurve= np.zeros([15,2])
	for count in range(1,16):
		Index = 1/15 * count
		LCurve[count-1,0]=Index
		LCurve[count-1,1]=1/(1+np.exp(-LSlope*(Index-LCenter)))
	

	BetsOfDay = {}

	SumConf=0
	NormFactor=0
	TotalBetsOfDay=0
	for Team in ExpectedValues:
		SumConf += ExpectedValues[Team] * 1/(1+np.exp(-LSlope*(ExpectedValues[Team]-LCenter)))
		
	NormFactor = 1/SumConf
	
	for Team in ExpectedValues:
		BetsOfDay[Team] = ExpectedValues[Team] *  1/(1+np.exp(-LSlope*(ExpectedValues[Team]-LCenter)))*NormFactor
		
	return BetsOfDay

#def flat_weightings(ExpectedValues):
	
	
def test(file,model):
	print()
	print("Determining accuracy of model on", file)
	games,outcomes = load_profiles(file)
	oddsPairs = model.predict(games,batch_size=1,verbose=0,steps=None)
	
	occurances = {}
	confidence = []
	
	i=0
	for op in oddsPairs:
		if(op[0] > op[1]):
			winner = 0
			confidence.append(float(op[0]*100))
			winP = str(int(round(op[0]*100)))
		elif(op[1] > op[0]):
			winner = 1
			confidence.append(float(op[1]*100))
			winP = str(int(round(op[1]*100)))
			
		if(winP in occurances):
			occurances[winP].append(float(outcomes[i][winner]))
		else:
			occurances[winP] = []
			occurances[winP].append(float(outcomes[i][winner]))
		
		i+=1
	
	deviations = []
	for pPair in occurances:
		deviation = (mean(occurances[pPair])*100) - int(pPair)
		deviations.append(deviation)
		print(str(int(pPair))+",",str(round((mean(occurances[pPair])*100),2)))
	
	print("Test Results:")
	print("Average Deviation: ", mean(deviations))
	print("StdDev of Deviations: ", stdev(deviations))
	print("Average confidence: ", mean(confidence))
	print()
			
	
def simbet(gameFile, oddsFile, model):
	print("Determining how to bet on ", gameFile, " considering ", oddsFile)
	
	daysOdds = {}
	
	moneylineOddsFile = open(oddsFile,'r')
	moneylineOdds = moneylineOddsFile.readlines()
	for i in range(int((len(moneylineOdds)-1)/4)):
		home = moneylineOdds[(4*i)+1][6:9]
		away = moneylineOdds[(4*i)+1][12:15]
		homeodds = float(moneylineOdds[(4*i)+2])
		awayodds = float(moneylineOdds[(4*i)+3])
		daysOdds[home] = homeodds
		daysOdds[away] = awayodds
	
	#for key in daysOdds:
	#	print(key,":",daysOdds[key])
	
	
	games,outcomes = load_profiles(gameFile)
	oddsPairs = model.predict(games,batch_size=1,verbose=0,steps=None)
	
	expectedValuesList = []
	results = {}
	
	with open(gameFile) as game_profiles_file:
		game_profiles = csv.DictReader(game_profiles_file)
		
		i = 0
		for row in game_profiles:
			homeExpectedVal = float(daysOdds[row["HTEAM"]])*oddsPairs[i][0]
			awayExpectedVal = float(daysOdds[row["ATEAM"]])*oddsPairs[i][1]
			
			homeBet = (homeExpectedVal,row["HTEAM"],daysOdds[row["HTEAM"]],oddsPairs[i][0])
			awayBet = (awayExpectedVal,row["ATEAM"],daysOdds[row["ATEAM"]],oddsPairs[i][1])
			
			expectedValuesList.append(homeBet)
			expectedValuesList.append(awayBet)
			
			if(str(row["HRES"]) == "1.0"):
				results[row["HTEAM"]] = (1.0, "(W)")
				results[row["ATEAM"]] = (0.0, "(L)")
			elif(str(row["ARES"]) == "1.0"):
				results[row["HTEAM"]] = (0.0, "(L)")
				results[row["ATEAM"]] = (1.0, "(W)")
			else:
				results[row["HTEAM"]] = (0.0, "(?)")
				results[row["ATEAM"]] = (0.0, "(?)")
			
			i+=1
	
	toBet = sorted(expectedValuesList, key=lambda x: x[0])
	toBet.reverse()
	toBet = toBet[:10]
	
	print("\nGames bet on:")
	runTot = 0.0
	for tup in toBet:
		print(tup[0]," Expected Value, ",tup[1]," actual moneyline: ",tup[2],", Machine odds: ",tup[3])
		runTot += tup[0]
		
	avgExpected = runTot/10.0
	
	print()
	print("Expected Value betting on all 10 equally:")
	print(avgExpected)
	print()
	print("Betting $1000 ($83.33 each)")
	print("\nReality:")
	winnings = 0.0
	for tup in toBet:
		print(tup[1],results[tup[1]][1])
		print("$"+str(round(tup[2]*results[tup[1]][0]*100.00)))
		winnings += tup[2]*results[tup[1]][0]*100.00 
	
	print()
	print("Spent: $1000")
	print("Got Back: $"+str(winnings))
	print("Deviation from expected:", winnings-(avgExpected*1000))
	
	
def toCode(date):
	#print(date)
	#print(date[3:6])
	#print(date[:2])

	if(date[3:6] == "Oct"):
		toReturn = "10" + date[:2]
	elif(date[3:6] == "Sep"):
		toReturn = "09" + date[:2]
	elif(date[3:6] == "Aug"):
		toReturn = "08" + date[:2]
	elif(date[3:6] == "Jul"):
		toReturn = "07" + date[:2]
	elif(date[3:6] == "Jun"):
		toReturn = "06" + date[:2]
	elif(date[3:6] == "May"):
		toReturn = "05" + date[:2]
	elif(date[3:6] == "Apr"):
		toReturn = "04" + date[:2]
	elif(date[3:6] == "Mar"):
		toReturn = "03" + date[:2]
		
	return toReturn
	
def write_data(gameFile, oddsFile, write_file, model):
	
	seasonOdds = {}
	
	moneylineOddsFile = open(oddsFile,'r')
	moneylineOdds = moneylineOddsFile.readlines()
	j = 0
	for line in moneylineOdds:
		i = 1
		if(len(line) == 12):
			
			key = toCode(line[:6])
			seasonOdds[key] = {}
			
			while((i+j) < len(moneylineOdds) and len(moneylineOdds[j+i]) != 12):
				home = moneylineOdds[j+i][6:9]
				away = moneylineOdds[j+i][12:15]
				homeodds = float(moneylineOdds[j+i+1])
				awayodds = float(moneylineOdds[j+i+2])
				seasonOdds[key][home] = homeodds
				seasonOdds[key][away] = awayodds
				
				#print(key,home,homeodds)
				#print(key,away,awayodds)
				
				i+=4
		
		j+=1
		
	games,outcomes = load_profiles_sparse(gameFile)
	oddsPairs = model.predict(games,batch_size=1,verbose=0,steps=None)
	
	game_profiles_file = open(gameFile,'r')
	profiles = csv.DictReader(game_profiles_file)
	
	resultsCSV = open(write_file,'w')
	
	i = 0
	for row in profiles:
		currentday = row["MONTH"]+row["DAY"]
		if(currentday in seasonOdds):
			line = ""
			
			if(row["HTEAM"] in seasonOdds[currentday]):
				line+=str(seasonOdds[currentday][row["HTEAM"]])
				line+=","
				line+=str(oddsPairs[i][0])
				line+=","
			if(row["ATEAM"] in seasonOdds[currentday]):
				line+=str(seasonOdds[currentday][row["ATEAM"]])
				line+=","
				line+=str(oddsPairs[i][1])
				line+=","
			line+=row["HRES"]
			line+=","
			line+=row["MONTH"]
			line+=","
			line+=row["DAY"]
			line+=","
			line+=row["HTEAM"]
			line+=","
			line+=row["ATEAM"]
			line+="\n"
			
			if(line.count(',') == 8):
				resultsCSV.write(line)
		i+=1
		
def write_nate_data(gameFile, oddsFile, write_file):
	
	seasonOdds = {}
	
	moneylineOddsFile = open(oddsFile,'r')
	moneylineOdds = moneylineOddsFile.readlines()
	j = 0
	for line in moneylineOdds:
		i = 1
		if(len(line) == 12):
			
			key = toCode(line[:6])
			seasonOdds[key] = {}
			
			while((i+j) < len(moneylineOdds) and len(moneylineOdds[j+i]) != 12):
				home = moneylineOdds[j+i][6:9]
				away = moneylineOdds[j+i][12:15]
				homeodds = float(moneylineOdds[j+i+1])
				awayodds = float(moneylineOdds[j+i+2])
				seasonOdds[key][home] = homeodds
				seasonOdds[key][away] = awayodds
				
				#print(key,home,homeodds)
				#print(key,away,awayodds)
				
				i+=4
		
		j+=1
		
	
	game_profiles_file = open(gameFile,'r')
	profiles = csv.DictReader(game_profiles_file)
	
	resultsCSV = open(write_file,'w')
	
	i = 0
	for row in profiles:
		currentday = row["MONTH"]+row["DAY"]
		if(currentday in seasonOdds):
			line = ""
			
			if(row["HTEAM"] in seasonOdds[currentday]):
				line+=str(seasonOdds[currentday][row["HTEAM"]])
				line+=","
				line+=str(row["HELO"])
				line+=","
			if(row["ATEAM"] in seasonOdds[currentday]):
				line+=str(seasonOdds[currentday][row["ATEAM"]])
				line+=","
				line+=str(row["AELO"])
				line+=","
			line+=row["HRES"]
			line+="\n"
			
			if(line.count(',') == 4):
				resultsCSV.write(line)
		i+=1
	
def simulate_from_existing(listDays, startBank, betProp, model):
	
	dayResults = {}
	
	gameFile = "mlb-elo\\test_0727.csv"
	
	with open(gameFile) as game_profiles_file:
		game_profiles = csv.DictReader(game_profiles_file)
		
		for row in game_profiles:
			day = row["date"][5:7]+row["date"][8:10]
			if(day not in dayResults):
				dayResults[day] = {}
			
			
			if(int(row["score1"]) > int(row["score2"])):
				hwin = 1
				awin = 0
			else:
				hwin = 0
				awin = 1
				
			dayResults[day][row["team1"]] = hwin
			dayResults[day][row["team2"]] = awin
	
	bank = startBank
	
	for day in listDays:
		print(day)
		preds,odds,evs = predict(day,model)
		weights = alt_weightings(evs)
		
		
		dayCap = bank*betProp
		
		dayWin = 0
		
		for weight in weights:
			
			if(weight in dayResults[day]):
				dayWin += weights[weight]*dayCap*odds[weight]*dayResults[day][weight]
				print("     ",weight,": ",round(weights[weight]*dayCap,2),", moneyline:",round(odds[weight],2),",won? ",dayResults[day][weight])
			else:
				dayWin += weights[weight]*dayCap
				print("     ",weight,": ",round(weights[weight]*dayCap,2),", moneyline:",round(odds[weight],2),",no action")
		
		dayWin = dayWin - dayCap
		
		
		
		bank+=dayWin
		
		print("winnings on ",day,": ",round(dayWin,2), ", bank: ", round(bank,2))
		
	print(round(bank,2))
		
		
		
			

def simulate(gameFile, oddsFile, model):
	print("Simulating betting on season from", gameFile, "considering", oddsFile," betting 50%")
	
	seasonOdds = {}
	
	moneylineOddsFile = open(oddsFile,'r')
	moneylineOdds = moneylineOddsFile.readlines()
	j = 0
	for line in moneylineOdds:
		i = 1
		if(len(line) == 12):
			
			key = toCode(line[:6])
			seasonOdds[key] = {}
			
			while((i+j) < len(moneylineOdds) and len(moneylineOdds[j+i]) != 12):
				home = moneylineOdds[j+i][6:9]
				away = moneylineOdds[j+i][12:15]
				homeodds = float(moneylineOdds[j+i+1])
				awayodds = float(moneylineOdds[j+i+2])
				seasonOdds[key][home] = homeodds
				seasonOdds[key][away] = awayodds
				
				
				i+=4
		
		j+=1
	
	#print(list(seasonOdds))
	gameFile = "mlb-elo\\"+gameFile
	games,outcomes = load_nate_profiles(gameFile)
	oddsPairs = model.predict(games,batch_size=1,verbose=0,steps=None)
	
	bank = 1000.0
	capFactor = 0.75
	daysBet = 0
	dailyReturns = []
	winningDays = 0
	losingDays = 0
	
	numPosEV = 0
	numBetEV = 0
	
	winningReturns = []
	losingReturns = []
	
	with open(gameFile) as game_profiles_file:
		game_profiles = csv.DictReader(game_profiles_file)
		
		currentday = "0528"
		dayExpectedValues = []
		dayResults = {}
		
		i=0
		for row in game_profiles:
			if(str(row["MONTH"])+str(row["DAY"]) != currentday):
				if(len(dayExpectedValues) > 5):
					dayExpectedValues = sorted(dayExpectedValues, key=lambda x: x[0])
					toBet = {}
					
					for ltup in dayExpectedValues:
						if(ltup[0] >= 1.00):
							toBet[ltup[1]] = ltup[0]
							numPosEV+=1
					
					if(len(toBet) > 11):
						betWeights = alt_weightings(toBet)
						numBetEV+=len(toBet)
						dayWinnings = 0.0
						dayWager = bank*capFactor
						for tup in dayExpectedValues:
							if(tup[1] in betWeights):
								dayWinnings += tup[2]*dayResults[tup[1]][0]*(dayWager)*betWeights[tup[1]]
								if(dayResults[tup[1]][0] > 0):
									print("   ",tup[1],", GAIN: ",tup[2]*(dayWager)*betWeights[tup[1]])
								else:
									print("   ",tup[1],", LOSS: ",(dayWager)*betWeights[tup[1]])
						dayWinnings = dayWinnings-(dayWager)
						
						
						dayRet = dayWinnings/(dayWager)
						dailyReturns.append(dayRet)
						
						if(dayWinnings > 0):
							winningDays+=1
							winningReturns.append(dayRet)
						else:
							losingDays+=1
							losingReturns.append(dayRet)
						
						bank += round(dayWinnings,2)

						daysBet+=1
						
						if(dayWinnings > 0):
							print("Winnings on",currentday,":",round(dayWinnings,2),", Bet: ",round(dayWager,2)," Bank:",round(bank,2),", Return: ",round(dayRet*100,2),"%")
						else:
							print("Losings  on",currentday,":",round(dayWinnings,2),", Bet: ",round(dayWager,2),", Bank:",round(bank,2),", Return: ",round(dayRet*100,2),"%")
					
					
				currentday = str(row["MONTH"])+str(row["DAY"])
				dayExpectedValues = []
				dayResults = {}
			
			####ODDS ADJUSTED####
			if(row["HTEAM"] in seasonOdds[currentday]):
				if(seasonOdds[currentday][row["HTEAM"]] >= 2.0):
					if(oddsPairs[i][0] > 0.50):
						homeExpectedVal = (float(seasonOdds[currentday][row["HTEAM"]])+0.00)*oddsPairs[i][0]
						homeBet = (homeExpectedVal,row["HTEAM"],seasonOdds[currentday][row["HTEAM"]],oddsPairs[i][0],0.0)
						dayExpectedValues.append(homeBet)
					else:
						homeExpectedVal = (float(seasonOdds[currentday][row["HTEAM"]])+0.00)*oddsPairs[i][0]
						homeBet = (homeExpectedVal,row["HTEAM"],seasonOdds[currentday][row["HTEAM"]],oddsPairs[i][0],0.0)
						dayExpectedValues.append(homeBet)
				else:
					if(oddsPairs[i][0] > 0.50):
						homeExpectedVal = (float(seasonOdds[currentday][row["HTEAM"]])-0.00)*oddsPairs[i][0]
						homeBet = (homeExpectedVal,row["HTEAM"],seasonOdds[currentday][row["HTEAM"]],oddsPairs[i][0],0.0)
						dayExpectedValues.append(homeBet)
					else:
						homeExpectedVal = (float(seasonOdds[currentday][row["HTEAM"]])-0.00)*oddsPairs[i][0]
						homeBet = (homeExpectedVal,row["HTEAM"],seasonOdds[currentday][row["HTEAM"]],oddsPairs[i][0],0.0)
						dayExpectedValues.append(homeBet)
			
			if(row["ATEAM"] in seasonOdds[currentday]):
				if(seasonOdds[currentday][row["ATEAM"]] >= 2.0):
					if(oddsPairs[i][1] > 0.50):
						awayExpectedVal = (float(seasonOdds[currentday][row["ATEAM"]])+0.00)*oddsPairs[i][1]
						awayBet = (awayExpectedVal,row["ATEAM"],seasonOdds[currentday][row["ATEAM"]],oddsPairs[i][1],1.0)
						dayExpectedValues.append(awayBet)
					else:
						awayExpectedVal = (float(seasonOdds[currentday][row["ATEAM"]])+0.00)*oddsPairs[i][1]
						awayBet = (awayExpectedVal,row["ATEAM"],seasonOdds[currentday][row["ATEAM"]],oddsPairs[i][1],1.0)
						dayExpectedValues.append(awayBet)
				else:
					if(oddsPairs[i][1] > 0.50):
						awayExpectedVal = (float(seasonOdds[currentday][row["ATEAM"]])-0.00)*oddsPairs[i][1]
						awayBet = (awayExpectedVal,row["ATEAM"],seasonOdds[currentday][row["ATEAM"]],oddsPairs[i][1],1.0)
						dayExpectedValues.append(awayBet)
					else:
						awayExpectedVal = (float(seasonOdds[currentday][row["ATEAM"]])-0.00)*oddsPairs[i][1]
						awayBet = (awayExpectedVal,row["ATEAM"],seasonOdds[currentday][row["ATEAM"]],oddsPairs[i][1],1.0)
						dayExpectedValues.append(awayBet)
			##############################
					
				
			###CURRENT EV CALCULATIONS###
			#if(row["HTEAM"] in seasonOdds[currentday]):
			#	homeExpectedVal = float(seasonOdds[currentday][row["HTEAM"]])*oddsPairs[i][0]
			#	homeBet = (homeExpectedVal,row["HTEAM"],seasonOdds[currentday][row["HTEAM"]],oddsPairs[i][0],0.0)
			#	dayExpectedValues.append(homeBet)
			#if(row["ATEAM"] in seasonOdds[currentday]):
			#	awayExpectedVal = float(seasonOdds[currentday][row["ATEAM"]])*oddsPairs[i][1]
			#	awayBet = (awayExpectedVal,row["ATEAM"],seasonOdds[currentday][row["ATEAM"]],oddsPairs[i][1],1.0)
			#	dayExpectedValues.append(awayBet)
			##################################
			
			if(str(row["HRES"]) == "1.0"):
				dayResults[row["HTEAM"]] = (1.0, "(W)")
				dayResults[row["ATEAM"]] = (0.0, "(L)")
			else:
				dayResults[row["HTEAM"]] = (0.0, "(L)")
				dayResults[row["ATEAM"]] = (1.0, "(W)")
			
			i+=1
	
	print()
	print("Simulation Results:")
	print()
	print("Money at beginning: $1000")
	print("Money at end: $"+str(round(bank,2)))
	print("Return: "+str(round(((bank-1000)/1000)*100,2))+"%")
	print()
	print("Winning days: ",str(winningDays))
	print("Average winning return: ",str(round(mean(winningReturns),2)))
	print("Losing days: ",str(losingDays))
	print("Average losing return: ",str(round(mean(losingReturns),2)))
	print("Percent winning days: ",str(round((winningDays/(winningDays+losingDays))*100,2)))
	print()
	print("Average daily return: "+str(round(mean(dailyReturns)*100,2))+"%")
	print("StdDev of daily return: "+str(round(stdev(dailyReturns)*100,2)))
	print("Highest daily return: "+str(round(max(dailyReturns)*100,2))+"%")
	print("Lowest daily return: "+str(round(min(dailyReturns)*100,2))+"%")
	print()
	print("Days Bet:",daysBet);
	print()
	print("Num pos EVS",numPosEV)
	print("Num EVs we bet on",numBetEV)
	print("Num potential days",numPosEV/12)
	
def sim_no_day(gameFile, oddsFile, model):
	print("Simulating betting on season from", gameFile, "considering", oddsFile," betting 50%")
	
	seasonOdds = {}
	
	moneylineOddsFile = open(oddsFile,'r')
	moneylineOdds = moneylineOddsFile.readlines()
	j = 0
	for line in moneylineOdds:
		i = 1
		if(len(line) == 12):
			
			key = toCode(line[:6])
			seasonOdds[key] = {}
			
			while((i+j) < len(moneylineOdds) and len(moneylineOdds[j+i]) != 12):
				home = moneylineOdds[j+i][6:9]
				away = moneylineOdds[j+i][12:15]
				homeodds = float(moneylineOdds[j+i+1])
				awayodds = float(moneylineOdds[j+i+2])
				seasonOdds[key][home] = homeodds
				seasonOdds[key][away] = awayodds
				
				
				i+=4
		
		j+=1
	
	#print(list(seasonOdds))
	gameFile = "mlb-elo\\"+gameFile
	games,outcomes = load_nate_profiles(gameFile)
	oddsPairs = model.predict(games,batch_size=1,verbose=0,steps=None)
	
	benchMark = 10
	
	bank = 1000.0
	capFactor = .60/benchMark
	cyclesBet = 0
	
	with open(gameFile) as game_profiles_file:
		game_profiles = csv.DictReader(game_profiles_file)
		
		currentday = "0000"
		
		betQueue = []
		
		i=0
		for row in game_profiles:
		
			#if(row["MONTH"]+row["DAY"] != currentday):
			if(row["date"][5:7]+row["date"][8:10] != currentday):
				if(len(betQueue) >= benchMark):
					bank+=sum(betQueue)
					print("cycle ",cyclesBet+1)
					for bet in betQueue:
						print("    ",bet)
					
					print(len(betQueue),"  ",bank)
					cyclesBet+=1
					betQueue = []
					
				#currentday = row["MONTH"]+row["DAY"]
				currentday = row["date"][5:7]+row["date"][8:10]
				
				
			
			#if(row["HTEAM"] in seasonOdds[currentday] and row["ATEAM"] in seasonOdds[currentday]):
			if(row["team1"] in seasonOdds[currentday] and row["team2"] in seasonOdds[currentday]):
				homeOdds = oddsPairs[i][0]
				awayOdds = oddsPairs[i][1]
				
				#homeOdds = float(row["HELO"])
				#awayOdds = float(row["AELO"])
				
				#homeOdds = float(row["HPRELO"])
				#awayOdds = float(row["APRELO"])
				
				homeLine = float(seasonOdds[currentday][row["team1"]])
				awayLine = float(seasonOdds[currentday][row["team2"]])
				
				#homeLine = float(seasonOdds[currentday][row["HTEAM"]])
				#awayLine = float(seasonOdds[currentday][row["ATEAM"]])
				
				homeEV = homeOdds*homeLine
				awayEV = awayOdds*awayLine
				
				if(len(betQueue) < 15):
					if(homeEV > 1.4):
						#if(float(row["HRES"]) == 1.0):
						if(int(row["score1"]) > int(row["score2"])):
							bet = bank*capFactor*(homeLine-1)
							betQueue.append(bet)
						else:
							bet = bank*capFactor*-1
							betQueue.append(bet)
					
					if(awayEV > 1.4):
						#if(float(row["ARES"]) == 1.0):
						if(int(row["score1"]) < int(row["score2"])):
							bet = bank*capFactor*(awayLine-1)
							betQueue.append(bet)
						else:
							bet = bank*capFactor*-1
							betQueue.append(bet)
			
			i+=1
			
	
	print()
	print("Simulation Results:")
	print()
	print("Money at beginning: $1000")
	print("Money at end: $"+str(round(bank,2)))
	print("Return: "+str(round(((bank-1000)/1000)*100,2))+"%")
	print()
	print("Cycles bet: ",cyclesBet)
	
def main():
	print("BrainyBet!, By Sam Rackey. 2019")
	
	if(os.path.isfile('mlb_prob.h5')):
		model = load_model('mlb_prob.h5')
		print()
		print("------------------------------------------------------------")
		print("                  MODEL LOADED FROM DISK                    ")
		print("------------------------------------------------------------")
		print()
	else:
	


		games,outcomes = load_nate_profiles("mlb-elo\mlb_elo_training.csv")
		model = Sequential()
		model.add(Dense(1024, activation='tanh', input_shape=(14,)))
		model.add(Dense(1024, activation='tanh'))
		model.add(Dense(1024, activation='tanh'))
		model.add(Dense(1024, activation='tanh'))
		model.add(Dense(1024, activation='tanh'))
		model.add(Dense(1024, activation='tanh'))
		model.add(Dense(1024, activation='tanh'))
		model.add(Dense(1024, activation='tanh'))
		model.add(Dense(2, activation='softmax'))
		
		
		
		model.summary()

		model.compile(loss='mean_squared_error',
			optimizer=SGD(),
			metrics=['accuracy'])
		
		model.fit(games, outcomes,
			batch_size=128,
			epochs=50,
			verbose=3)
		
		model.save('mlb_prob.h5')
		
		print()
		print("------------------------------------------------------------")
		print("                     TRAINING COMPLETE                      ")
		print("                    MODEL SAVED TO DISK                     ")
		print("------------------------------------------------------------")
		print()
		
	
	g = ""
	while(g != "quit"):
		g = input("Enter a command:")
		if(g == "p"):
			#d = getDay()
			d = input("Enter day:")
			predict(d,model)
		elif(g == "test"):
			f = input("Enter the filename:")
			test(f,model)
		elif(g == "simbet"):
			f1 = input("Enter day game profile filename:")
			f2 = input("Enter day odds filename:")
			simbet(f1,f2,model)
		elif(g == "sbet"):
			f1 = input("Enter day:")
			f2 = input("Enter daily betting capital:")
			sbet(f1,f2,model)
		elif(g == "bet"):
			f1 = input("Enter day:")
			f2 = input("Enter daily betting capital:")
			bet(f1,f2,model)
		elif(g == "bet test"):             #TEMP
			listDays = ["0529","0530","0531","0601","0602","0604","0605","0606","0607","0608"]
			for day in listDays:
				bet(day, 100, model)
		elif(g == "a test"):               #TEMP
			listDays = ["0714","0715","0716","0717","0718","0719","0721","0722","0723","0724"]
			analyze_bet_compounding(listDays,1000.0,10000)
		elif(g == "file sim"):
			listDays = ["0529","0530","0531","0601","0602","0604","0605","0606","0607","0608","0713","0714","0715","0716","0717","0718","0719","0721","0722","0723","0724"]
			simulate_from_existing(listDays,1000,0.5,model)
		elif(g == "a"):
			f1 = input("Enter day:")
			f2 = input("Enter num iterations:")
			analyze_bet(f1,int(f2))
		elif(g == "ac"):
			dayz = ["0722","0723"]
			analyze_bet_compounding(dayz,40.54,10000)
		elif(g == "d"):
			f1 = "profiles\\2019_game_profiles.csv"
			f2 = "2019moneyline.txt"
			f3 = "moneylinemachine\\2019__sparser_192_2.csv"
			write_data(f1,f2,f3,model)
		elif(g == "data"):
			mod = input("enter model spec: ")
			f1 = "profiles\\2016_large_profiles.csv"
			f11 = "profiles\\2017_large_profiles.csv"
			f12 = "profiles\\2018_large_profiles.csv"
			f2 = "2016moneyline.txt"
			f21 = "2017moneyline.txt"
			f22 = "2018moneyline.txt"
			f3 = "moneylinemachine\\2016__"+mod+".csv"
			f31 = "moneylinemachine\\2017__"+mod+".csv"
			f32 = "moneylinemachine\\2018__"+mod+".csv"
			write_data(f1,f2,f3,model)
			write_data(f11,f21,f31,model)
			write_data(f12,f22,f32,model)
		elif(g == "nate"):
			f1 = "2016profiles.csv"
			f12 = "2017profiles.csv"
			f13 = "2018profiles.csv"
			f2 = "2016moneyline.txt"
			f22 = "2017moneyline.txt"
			f23 = "2018moneyline.txt"
			f3 = "nate2016.csv"
			f32 = "nate2017.csv"
			f33 = "nate2018.csv"
			write_nate_data(f1,f2,f3)
			write_nate_data(f12,f22,f32)
			write_nate_data(f13,f23,f33)
		elif(g == "sim"):
			f1 = input("Enter season game profile filename:")
			#f1 = "2018test.csv"
			f2 = input("Enter season odds filename:")
			#f2 = "2018moneyline.txt"
			simulate(f1,f2,model)
		elif(g == "nd"):
			f1 = input("Enter season game profile filename:")
			f2 = input("Enter season odds filename:")
			sim_no_day(f1,f2,model)

main()
