#!/usr/bin/python3.6
# -*-coding:Utf-8 -*

import re
import sys
import GlobalHelper

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
orphans = GlobalHelper.ImportRomlist("Output/oprhans-reworked-2.txt")
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

print("""
################################
# Merge
################################
""")

count = 0
total = len(orphans) - orphansCount
for o in orphans:
	for m in master:
		if o.filename == m.filename and o.gamename == m.gamename and o.emulator == m.emulator and m.category == "" and o.category != "":
			m.category = o.category
			count +=1
			print("[MERGE] " + str(count) + "/" + str(total) + " [Game] : " + m.gamename + " [Categ] : " + m.category)

print("""
################################
# Export results : 
# - Output/NewMasterRomlist.txt
################################
""")
GlobalHelper.ExportToCSV(master, "Output/NewMasterRomlist.txt")