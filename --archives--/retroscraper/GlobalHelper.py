#!/usr/bin/python3.6
# -*-coding:Utf-8 -*

# ##################################################################################################
# Global Helper
# By Urukai
# Copyright 2018
# Licence GNU GENERAL PUBLIC LICENSE, Version 3, 29 June 2007
# ##################################################################################################

import Models.Rom


def ImportRomlist(path):
    games = []
    romFile = open(path, "r")
    masterRoms = str(romFile.read())
    romFile.close()

    columns = {}
    lines = masterRoms.split("\n")

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
            game = l.split(";")
            g = Models.Rom.Rom()

            iCol = 0

            for v in game:
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
            games.append(g)

    games.sort(key=lambda x: x.gamename, reverse=False)

    return games


def GetDistinctCategories(games):
    categs = []

    for g in games:
        tmp1 = g.category

        if tmp1 != "":
            tmp2 = tmp1.split("/")

            alreadyExist = False

            for categ in tmp2:
                tmp3 = categ

                for c in categs:
                    if tmp3 == c:
                        alreadyExist = True
                        break
                if alreadyExist:
                    break

            if not alreadyExist:
                print("    >>>>    adding : {0}".format(categ))
                categs.append(categ)

    categs.sort()

    return categs


def GetCategories(games):
    categs = []

    for g in games:
        categ = g.category
        alreadyExist = False

        for c in categs:
            if categ == c:
                alreadyExist = True
                break

        if not alreadyExist:
            categs.append(categ)

    categs.sort()

    return categs


def ExportToCSV(games, path):
    txt = "#Name;Title;Emulator;CloneOf;Year;Manufacturer;Category;Players;Rotation;Control;Status;DisplayCount;DisplayType;AltRomname;AltTitle;Extra;Buttons;\n"

    for g in games:
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

    fichier = open(path, "a")
    fichier.write(txt)
    fichier.close()


def WriteToFile(content, path):
    tmp = str(content)
    fichier = open(path, "a")
    fichier.write(tmp)
    fichier.close()


def GetRomsWithoutCateg(games):
    result = []

    for g in games:
        if g.category == "":
            result.append(g)
    return result
