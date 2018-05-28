#!/usr/bin/python3.6
# -*-coding:Utf-8 -*

import re
import sys
import GlobalHelper


def ClearName(name):
	tmp1 = name[0:name.find(" (") + 1]
	tmp2 = tmp1[0:tmp1.find(" [") + 1]
	tmp3 = tmp2[0:tmp2.find(" ~") + 1]

	if tmp3 != "":
		return tmp3
	elif tmp2 != "":
		return tmp2
	elif tmp1 != "":
		return tmp1
	else:
		return name

def ClearName2(name):
	tmp1 = name.lower()
	tmp2 = tmp1.replace("the", "")
	tmp3 = tmp2.replace("of", "")
	tmp4 = tmp3.replace("in", "")
	tmp5 = tmp4.replace("for", "")

	return tmp5


nom1 = "for of DArius the tubble IN"
nom2 = "Darius TUBBLE (2345678) [bootleg]"

tmpcleaned1 = ClearName(nom1)
tmpcleaned2 = ClearName(nom2)
cleaned1 = ClearName2(tmpcleaned1)
cleaned2 = ClearName2(tmpcleaned2)

search1 = ""
search2 = ""

search1 = cleaned1.split()
search2 = cleaned2.split()
print("#VALEURS : ")
print("nom1 : " + nom1)
print("nom2 : " + nom2)
print("cleaned1 : " + cleaned1)
print("cleaned2 : " + cleaned2)
print("search1 : " + str(search1))
print("search2 : " + str(search2))
print("# ---\n")

print("SEARCH nom1 in nom2")
if re.search(nom1, nom2, re.IGNORECASE):
	print(True)
else:
	print(False)

print("SEARCH nom2 in nom1")
if re.search(nom2, nom1, re.IGNORECASE):
	print(True)
else:
	print(False)

print("SEARCH search1 ~ into ~ search2")
r = []
for s1 in search1:
	found = False
	for s2 in search2:
		if re.search(s1, s2, re.IGNORECASE):
			found = True
			break
	if found:
		r.append(True)
	else:
		r.append(False)
			

cpt = 0
tot = len(r)

for b in r:
	if b:
		cpt += 1

perc = cpt * 100 / tot

percOK = 63

gameOK = False
if perc >= percOK:
	gameOK = True
else : 
	gameOK = False

txtDisplay = "compté : " + str(cpt)
txtDisplay += " total : " + str(tot)
txtDisplay += " poucentage : " + str(int(perc))
txtDisplay += " calcul : " + str(r)
txtDisplay += " OK ? " + str(gameOK)
print(txtDisplay) 


sys.exit()





print("""
################################
# Import First Master
################################
""")

master =  []
master = GlobalHelper.ImportRomlist("Input/MasterRomList.txt")
master.sort(key=lambda x: x.gamename, reverse = False)

print("- count : {0}".format(str(len(master))))

print("""
################################
# Gest games without categ
################################
""")

orphans =[]
orphans = GlobalHelper.GetRomsWithoutCateg(master)
orphans.sort(key=lambda x: x.gamename, reverse = False)

print("- count : {0}".format(str(len(orphans))))

print("""
################################
""")

count = 0

for o in orphans:
	if o .gamename != "":

		found = False
		categ = ""

		gamename = ClearName(o.gamename)

		masterName = ""
		for m in master:
			if m.gamename != "" and m.category != "":
				masterName = ClearName(m.gamename)

				if gamename in masterName:
					found = True
				if not found and masterName in gamename:
					found = True
				if not found and o.filename == m.filename:
					found = True
			if found:
				o.category = m.category
				categ = o.category
				break
		count += 1
		#print("game : {0}, file : {2}, found ? {3}".format(gamename, o.filename, str(found)))
		print("game : " + gamename + ", file : " + o.filename +", found ? " + str(found))

print("""
################################
# Export results : 
# - Output/oprhans-reworked-1.txt
################################
""")
GlobalHelper.ExportToCSV(orphans, "Output/oprhans-reworked-1.txt")