# coding=utf-8

import HelperFile
import Models.Rom

def LoadRomListFile(path):
    romListFile = HelperFile.GetFilecontent(path)

    columns = {}
    lines = romListFile.split("\n")

    i = 0
    results = []

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
            g =Models.Rom.Rom()

            iCol = 0

            for v in game:
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
                results.append(g)
        i += 1
    results.sort(key=lambda x: x.gamename, reverse = False)
    return results
