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
	tmp2 = tmp1.replace(" the ", " ")
	tmp3 = tmp2.replace(" of ", " ")
	tmp4 = tmp3.replace(" in ", " ")
	tmp5 = tmp4.replace(" for ", " ")
	tmp6 = tmp5.replace("&", "")
	tmp7 = tmp6.replace("+", "")
	tmp8 = tmp7.replace("$", "")	
	tmp9 = tmp8.replace("[", "")
	tmp10 = tmp9.replace("]", "")
	tmp11 = tmp10.replace("(", "")
	tmp12 = tmp11.replace(")", "")
	tmp13 = tmp12.replace("{", "")
	tmp14 = tmp13.replace("}", "")
	tmp15 = tmp14.replace("@", "")

	return tmp15


def Found(gamename, gamenameMaster):
	found = False

	cleaned1 = gamename
	cleaned2 = gamenameMaster

	# nom1 = gamename
	# nom2 = gamenameMaster

	# tmpcleaned1 = ClearName(nom1)
	# tmpcleaned2 = ClearName(nom2)
	# cleaned1 = ClearName2(tmpcleaned1)
	# cleaned2 = ClearName2(tmpcleaned2)

	search1 = ""
	search2 = ""

	search1 = cleaned1.split()
	search2 = cleaned2.split()

	r = []

	r1 = False
	try:
		r1 = re.search(cleaned1, cleaned2, re.IGNORECASE)
	except Exception as e:
		r1 = False	

	if r1:
		found = True
	else:
		r2 = False

		if len(cleaned2) >= len(cleaned1):
			try:
				r2 = re.search(cleaned2, cleaned1, re.IGNORECASE)
			except Exception as e:
				r2 = False

			if r2:
				found = True
			else:
				for s1 in search1:
					found = False
					for s2 in search2:
						
						r3 = False
						try:
							r3 = re.search(s1, s2, re.IGNORECASE)
						except Exception as e:
							r3 = False
							print("\ns1 : " + s1 + "\ns2 : " + s2)

						if r3:
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

				percOK = 70

				if perc >= percOK:
					found = True
				else : 
					found = False
	return found

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
# Import First Rework
################################
""")

orphans =  []
orphans = GlobalHelper.ImportRomlist("Output/oprhans-reworked-1.txt")
orphans.sort(key=lambda x: x.gamename, reverse = False)

print("- count : {0}".format(str(len(orphans))))

orphansCount = 0

for o in orphans:
	if o .gamename != "" and o.category == "":
		orphansCount += 1

print("- without categs : {0}".format(str(orphansCount)))

print("""
################################
""")

count = 0

for o in orphans:
	if o .gamename != "" and o.category == "":

		found = False
		categ = ""

		tmpgamename = ClearName(o.gamename)
		gamename = ClearName2(tmpgamename)

		gamesToSearch = []
		if " - " in gamename:
			gamesToSearch = gamename.split(" - ")
		else:
			gamesToSearch.append(gamename)

		for g in gamesToSearch:
			masterName = ""
			for m in master:
				if m.gamename != "" and m.category != "":
					tmpmasterName = ClearName(m.gamename)
					masterName = ClearName2(tmpmasterName)

					found = Found(g, masterName)
					
				if found:
					o.category = m.category
					categ = o.category
					break
			if found:
				break

		count += 1
		print("[COUNT] " + str(count) + "/" + str(orphansCount) + " [GAME] " + gamename + " [CATEG] " + o.category + " [FILE] " + o.filename +" [FOUND ?] " + str(found))

print("""
################################
# Export results : 
# - Output/oprhans-reworked-2.txt
################################
""")
GlobalHelper.ExportToCSV(orphans, "Output/oprhans-reworked-2.txt")