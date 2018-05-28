#!/usr/bin/python3.6
# -*-coding:Utf-8 -*

# ##################################################################################################
# RomsWithoutCateg Helper
# By Urukai
# Copyright 2018
# Licence GNU GENERAL PUBLIC LICENSE, Version 3, 29 June 2007
# ##################################################################################################

import sys
import GlobalHelper

games = []
emulators = []
orphans = []

print("""
################################
# Import oprhan roms
################################
""")
games = GlobalHelper.ImportRomlist("RomsWithoutCateg.txt")
orphans = list(games)
print("Imported roms : " + str(len(games)))

GlobalHelper.ExportGamesWithoutCateg(orphans, "tmp.txt")


sys.exit()

print("""
################################
# Distinct Emulators impacted
################################
""")
prevEmu = ""
actualEmu = ""
count = 0

games.sort(key=lambda x: x.emulator, reverse=False)

for g in games:

    if not g.gamename == "":
        actualEmu = g.emulator

        if actualEmu != prevEmu:
            if not count == 0:
                emulators.append(prevEmu + " : " + str(count))

            count = 0
            prevEmu = actualEmu
        else:
            if g.category == "":
                count += 1

txt = ""
for e in emulators:
    txt = txt + e + "\n"

print("Opening Destination File")
fichier = open("EmulatorsConcernedByRomsWithoutCateg.txt", "a")
print("Wrinting Destination File")
fichier.write(txt)
fichier.close()

print("Numbers of emulators inpacted : " + str(len(emulators)))

print("""
################################
# Try to get categs from Master
################################
""")
master = []
games[:] = []
print("Loading Master File ...")
master = GlobalHelper.ImportRomlist("MasterRomList.txt")

print("\nNumbers of roms : " + str(len(master)))
print("\nChecking ...")

count = 0
found = False
nbFound = 0
for g in orphans:
    found = False
    for m in master:
        gameToSearch = ""
        masterGame = ""

        masterGame = m.gamename
        gameToSearch = g.gamename[0:g.gamename.find(" (")]

        if gameToSearch in masterGame and m.category != "":
            g.category = m.category
            found = True
            nbFound += 1
            break

    count += 1

    print(str(count) + " / " + str(len(orphans)) + " | Restant : " + str(len(orphans) - count) + " | Find : " + str(found) + " | Numbers of found : " + str(nbFound))

print("End\n")
print("Before : " + str(len(orphans)))

newCount = 0

for g in orphans:
    if g.category == "":
        newCount += 1
print("After : " + str(newCount))

GlobalHelper.ExportToCSV(orphans, "1-RomsWithoutCateg.txt")
