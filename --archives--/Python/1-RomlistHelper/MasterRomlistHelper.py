#!/usr/bin/python3.6
# -*-coding:Utf-8 -*

# ##################################################################################################
# MasterRomlist Helper
# By Urukai
# Copyright 2018
# Licence GNU GENERAL PUBLIC LICENSE, Version 3, 29 June 2007
# ##################################################################################################

import GlobalHelper

games = []

print("""
################################
# Import MasterRomListFile
################################
""")
games = GlobalHelper.ImportRomlist("MasterRomList.txt")

print("""
################################
# Export roms without category
################################
""")

txt = "#Name;Title;Emulator;CloneOf;Year;Manufacturer;Category;Players;Rotation;Control;Status;DisplayCount;DisplayType;AltRomname;AltTitle;Extra;Buttons;\n"

for g in games:
    if g.category == "":
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
fichier = open("RomsWithoutCateg.txt", "a")
print("Wrinting Destination File")
fichier.write(txt)
fichier.close()

print("""
################################
# Export roms without emulator
################################
""")
txt = ""
for g in games:
    if g.emulator == "":
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
fichier = open("RomsWithoutEmu.txt", "a")
print("Wrinting Destination File")
fichier.write(txt)
fichier.close()
