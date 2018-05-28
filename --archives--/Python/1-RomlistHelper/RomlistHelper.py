#!/usr/bin/python3.6
# -*-coding:Utf-8 -*

# ##################################################################################################
# Romlist Helper
# By Urukai
# Copyright 2018
# Licence GNU GENERAL PUBLIC LICENSE, Version 3, 29 June 2007
# ##################################################################################################

import glob
from lxml import etree
import Models.Rom

gamesHyperlist = []
gamesHyperpie = []
games = []
categs = []


def ConsolidateHyperlistAndHyperpie(gamesHyperlist, gamesHyperpie):
    for hpg in gamesHyperpie:
        isExist = False

        if not hpg.gamename == "":
            for g in games:
                if g.gamename == hpg.gamename and g.emulator == hpg.emulator:
                    isExist = True
                break

            if not isExist:
                print("Adding : " + hpg.gamename + " | Emulator : " + hpg.emulator)
                games.append(hpg)

    for hlg in gamesHyperlist:
        isExist = False

        if not hlg.gamename == "":
            for g in games:
                if g.gamename == hlg.gamename and g.emulator == hlg.emulator:
                    g.category = hlg.category

                    # if (g.gamename == hlg.gamename and g.filename == hlg.filename):
                    #     g.emulator == "Final Burn Alpha"

                    isExist = True
                break            

            if not isExist:
                print("Adding : " + hpg.gamename + " | Emulator : " + hpg.emulator)
                games.append(hlg)

    games.sort(key=lambda x: x.gamename, reverse = False)
    return ""


def LoadHyperlistFile(hyperlistPath):
    tree = etree.parse(hyperlistPath)

    for game in tree.xpath("/menu/game"):
        g =Models.Rom.Rom()
        g.filename = game.get("name")
        gameInfos = game.getchildren()

        for info in gameInfos:
            infoName = str(info)
            infoName = infoName[9:infoName.find(" at")]

            infoText = str(info.text)

            if infoName == "description":
                g.gamename = infoText
            elif infoName == "cloneof":
                g.cloneOf = infoText
            elif infoName == "crc":
                g.crc = infoText
            elif infoName == "manufacturer":
                g.manufacturer = infoText
            elif infoName == "year":
                g.year = infoText
            elif infoName == "genre":
                if infoText == "None":
                    infoText = ""
                g.category = infoText
            elif infoName == "rating":
                g.rating = infoText

            g.emulator = hyperlistPath[hyperlistPath.rfind("/") + 1:len(hyperlistPath) - 4]

        if not g.filename == "" or not g.gamename == "":

            if len(gamesHyperlist) == 0:
                gamesHyperlist.append(g)
            else:
                for test in gamesHyperlist:
                    isDone = False

                    if not (test.gamename == g.gamename and test.filename == g.filename and test.emulator == g.emulator):
                        gamesHyperlist.append(g)
                        break
                    else:
                        if (test.gamename == g.gamename and test.filename == g.filename) and (g.emulator == "Final Burn Alpha" and test.emulator == "MAME (Libretro)"):
                            test.emulator = g.emulator
                            break
    
    gamesHyperlist.sort(key=lambda x: x.gamename, reverse = False)

    return ""


def LoadHyperpieFile(hyperpiePath):
    hyperpieFile = open(hyperpiePath, "r")
    hyperpie = str(hyperpieFile.read())
    hyperpieFile.close()

    columns = {}
    lines = hyperpie.split("\n")

    i = 0

    for l in lines:

        if l[0:1] == "#" and i == 0:
            columns = l.split(";")

            noColumns = 0

            for c in columns:
                if c[0:1] == "#":
                    c = c[1:]

                if c == "Name":
                    columns[noColumns] = "Name"
                elif c == "Title":
                    columns[noColumns] = "Title"
                elif c == "Emulator":
                    columns[noColumns] = "Emulator"
                elif c == "CloneOf":
                    columns[noColumns] = "CloneOf"
                elif c == "Year":
                    columns[noColumns] = "Year"
                elif c == "Manufacturer":
                    columns[noColumns] = "Manufacturer"
                elif c == "Category":
                    columns[noColumns] = "Category"
                elif c == "Players":
                    columns[noColumns] = "Players"
                elif c == "Rotation":
                    columns[noColumns] = "Rotation"
                elif c == "Control":
                    columns[noColumns] = "Control"
                elif c == "Status":
                    columns[noColumns] = "Status"
                elif c == "DisplayCount":
                    columns[noColumns] = "DisplayCount"
                elif c == "DisplayType":
                    columns[noColumns] = "DisplayType"
                elif c == "AltRomname":
                    columns[noColumns] = "AltRomname"
                elif c == "AltTitle":
                    columns[noColumns] = "AltTitle"
                elif c == "Extra":
                    columns[noColumns] = "Extra"
                elif c == "Buttons":
                    columns[noColumns] = "Buttons"

                noColumns += 1

        else:
            hyperpieGame = l.split(";")
            g =Models.Rom.Rom()

            iCol = 0

            for v in hyperpieGame:
                # print("#########################################\n NEW LINE")
                # print("game : " + v)
                # print("emulator : " + v)
                # print("iCol : " + str(iCol))
                # #print(columns + "\n")

                if not columns == {}:
                    if iCol < len(columns):
                        if columns[iCol] == "Name":
                            g.filename = v
                        elif columns[iCol] == "Title":
                            g.gamename = v
                        elif columns[iCol] == "Emulator":
                            g.emulator = v
                            # emulator = hyperlistPath[hyperlistPath.rfind("/") + 1:len(hyperlistPath) - 4]
                        elif columns[iCol] == "CloneOf":
                            g.cloneof = v
                        elif columns[iCol] == "Year":
                            g.year = v
                        elif columns[iCol] == "Manufacturer":
                            g.manufacturer = v
                        elif columns[iCol] == "Category":
                            if v == "None":
                                v = ""
                            g.category = v
                        elif columns[iCol] == "Players":
                            g.players = v
                        elif columns[iCol] == "Rotation":
                            g.rotation = v
                        elif columns[iCol] == "Control":
                            g.control = v
                        elif columns[iCol] == "Status":
                            g.status = v
                        elif columns[iCol] == "DisplayCount":
                            g.displayCount = v
                        elif columns[iCol] == "DisplayType":
                            g.DisplayType = v
                        elif columns[iCol] == "AltRomname":
                            g.AltRomname = v
                        elif columns[iCol] == "AltTitle":
                            g.altTitle = v
                        elif columns[iCol] == "Extra":
                            g.extra = v
                        elif columns[iCol] == "Buttons":
                            g.buttons = v

                    iCol += 1

            if not g.filename == "" or not g.gamename == "":                
                if len(gamesHyperpie) == 0:
                    gamesHyperpie.append(g)
                else:
                    for test in gamesHyperpie:
                        isDone = False

                        if not (test.gamename == g.gamename and test.filename == g.filename and test.emulator == g.emulator):
                            gamesHyperpie.append(g)
                            break
                        else:
                            if (test.gamename == g.gamename and test.filename == g.filename) and (g.emulator == "Final Burn Alpha" and test.emulator == "MAME (Libretro)"):
                                test.emulator = g.emulator
                                break


                #gamesHyperpie.append(g)

        i += 1
    gamesHyperpie.sort(key=lambda x: x.gamename, reverse = False)
    return ""


def ExportToCSV():
    txt = "#Name;Title;Emulator;CloneOf;Year;Manufacturer;Category;Players;Rotation;Control;Status;DisplayCount;DisplayType;AltRomname;AltTitle;Extra;Buttons;\n"

    for g in games:
        if not g.gamename == "" or not g.filename == "":
            print("EMUL : " + g.emulator + " | CATEG : " + g.category + " | GAME : " + g.gamename)
            txt = txt + g.filename + ";"
            txt = txt + g.gamename + ";"
            txt = txt + g.emulator + ";"
            txt = txt + g.cloneOf + ";"
            txt = txt + g.year + ";"
            txt = txt + g.manufacturer + ";"
            txt = txt + g.category + ";"
            txt = txt + g.players + ";"
            txt = txt + g.rotation + ";"
            txt = txt + g.control + ";"
            txt = txt + g.status + ";"
            txt = txt + g.displayCount + ";"
            txt = txt + g.displayType + ";"
            txt = txt + g.altRomName + ";"
            txt = txt + g.altTitle + ";"
            txt = txt + g.extra + ";"
            txt = txt + g.buttons + ";"
            txt = txt + "\n"

    print("Opening Destination File")
    fichier = open("MasterRomList.txt", "a")
    print("Wrinting Destination File")
    fichier.write(txt)
    fichier.close()


def GetCategories():
    for g in games:
        tmp1 = g.category

        tmp2 = tmp1.split("/")

        for categ in tmp2:

            alreadyExist = False

            for c in categs:
                if categ == c:
                    alreadyExist = True
                    break

            if not alreadyExist:
                categs.append(categ)

    categs.sort()

# ###############################################
# # Get HyperList and HyperPie romlists files
# ###############################################
hyperlistFiles = glob.glob("Hyperlist/*.xml")
hyperpieFiles = glob.glob("Hyperpie/*.txt")

# ###############################################
# # Load HyperList romlists
# ###############################################

print("""
################################
# hyper - LIST
################################
""")

f = 0
for hyperlistFile in hyperlistFiles:
    # print(hyperlistFile)
    LoadHyperlistFile(hyperlistFile)
    f+=1
    # print("\n")
print("\nNumbers of hyperfile files : " + str(f) + "\n")

i = 0
for g in gamesHyperlist:
    # print(g.gamename)
    i+=1

print("\nNumbers of entries : " + str(i) + "\n")

# ###############################################
# # Load HyperPie romlists
# ###############################################
f = 0
for hyperpieFile in hyperpieFiles:
    # print(hyperpieFile)
    LoadHyperpieFile(hyperpieFile)
    f += 1
    # print("\n")

print("""
################################
# hyper - PIE
################################
""")

i = 0
for g in gamesHyperpie:
    # print(g.gamename)
    i+=1

print("\nNumbers of hyperpi files : " + str(f) + "\n")

print("\nNumbers of entries : " + str(i) + "\n")


# ###############################################
# # Consolidation of HyperList and HyperPie romlists
# ###############################################
print("""
################################
# Generating MasterRomlist
################################
""")
ConsolidateHyperlistAndHyperpie(gamesHyperlist, gamesHyperpie)

print("""
################################
# MasterRomlist
################################
""")

i = 0
for g in games:
    # print(g.gamename)
    i+=1

print("\nNumbers of entries : " + str(i) + "\n")

# ###############################################
# # Generate a MasterRomlist file
# ###############################################
print("""
################################
# Export MasterRomlist to file
################################
""")
ExportToCSV()

# ###############################################
# # Get the catgories list
# ###############################################
print("""
################################
# Categories listing
################################
""")
GetCategories()

print("\nListe des categs :\n")
for c in categs:
    print(c)

# ###########################################
# TESTS

print("""
################################
# Export roms without category
################################
""")
# Liste les jeux sans categ
romsWoCateg = []

for g in games:
    if g.category == "":
        romsWoCateg.append(g)

kocatgames = ""
for g in romsWoCateg:
    # print(g.gamename)
    kocatgames = kocatgames + "Game : " + g.gamename + " | Emulator : " + g.emulator + "\n" 

fichier = open("RomsWithourCateg.txt", "a")
fichier.write(kocatgames)
fichier.close()

print("""
################################
# Export roms without emulator
################################
""")
# Liste les jeux sans emulateur
romsWoEmul = []

for g in games:
    if g.emulator == "":
        romsWoEmul.append(g)

koemulgames = ""
for g in romsWoEmul :
    # print(g.gamename)
    koemulgames = koemulgames + "Game : " + g.gamename + "\n" 

fichier = open("RomsWithourCateg.txt", "a")
fichier.write(koemulgames)
fichier.close()