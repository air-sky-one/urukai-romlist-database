#!/usr/bin/python3.6
# -*-coding:Utf-8 -*

# ##################################################################################################
# fucking console
# By Urukai
# Copyright 2018
# Licence GNU GENERAL PUBLIC LICENSE, Version 3, 29 June 2007
# ##################################################################################################

import re
import sys
import GlobalHelper

print("""
################################
# Import MasterRomList
################################
""")

master = []
master = GlobalHelper.ImportRomlist("Output/MasterRomList.txt")
master.sort(key=lambda x: x.filename, reverse=False)
print("Imported roms : " + str(len(master)))

#print(">>> Exporting roms without categ ...")
#GlobalHelper.ExportGamesWithoutCateg(master, "Output-tmp/RomsWithoutCateg.csv")

print("""
################################
# Import Orphans roms
################################
""")

orphans = []
orphans = GlobalHelper.ImportRomlist("Output-tmp/RomsWithoutCateg - V3.txt")
orphans.sort(key=lambda x: x.filename, reverse=False)
print("Imported roms : " + str(len(orphans)))

print("""
################################
# 1- beginning traitment
################################
""")

actualGamename = ""
prevGamename = ""
count = 0

for o in orphans:
    found = False
    if o.filename != "":
        filename = o.filename
        if o.category != "":
            for m in master:
                if m.filename != "":
                    if m.category != "":
                        if filename == m.filename:
                            o.category = m.category
                            found = True
                if found:
                    break
    count += 1

# for o in orphans:
#     found = False
#     if o.filename != "":
#         tmp1 = ""
#         tmp2 = ""
#         tmp3 = ""
#         filename = o.filename[0:o.filename.find(" (") + 1]
#         tmp1 = filename
#         tmp2 = tmp1[0:tmp1.find(" [")]
#         tmp3 = re.sub("[!@#$+-~]", "", tmp2)
#         actualGamename = tmp3

#         go = False

#         if prevGamename == "":
#             #premier tour
#             go = True
#         elif prevGamename != "":
#             if prevGamename != actualGamename:
#                 go = True

#         if go:
#             prevGamename = actualGamename

#             for m in master:
#                 if m.filename != "":
#                     if m.category != "":
#                         print("- compare {0} avec {1}".format(actualGamename, m.gamename))

#                         tmpMas1 = m.filename[0:m.filename.find(" (") + 1]
#                         tmpMas2 = tmpMas1[0:tmpMas1.find(" [")]
#                         tmpMas3 = re.sub("[!@#$+-~]", "", tmpMas2)

#                         actualMasterGamename = tmpMas3

#                         if re.search(actualGamename, actualMasterGamename, re.IGNORECASE):
#                             o.category = m.category
#                             found = True

#                         if len(actualGamename) >= len(actualMasterGamename):
#                             if re.search(actualMasterGamename, actualGamename, re.IGNORECASE):
#                                 o.category = m.category
#                                 found = True
#                 if found:
#                     break

#         # if prevGamename == "" and count == 0:
#         #     prevGamename == actualGamename

#         # for m in master:
#         #     if m.category != "":
#         #         if re.search(actualGamename, m.gamename, re.IGNORECASE):
#         #             break
#     txtDisplay = """- jeu cherché : {0}
# - trouvé ? : {1}
# - {2} / {3}
#     """.format(actualGamename, str(found), str(count), str(len(orphans)))
#     print(txtDisplay)


#    count += 1

print("""
################################
# Result Export
################################
""")
GlobalHelper.ExportToCSV(orphans, "Output-tmp/RomsWithoutCateg - V4.txt")

print("""
################################
# Still KO
################################
""")
GlobalHelper.ExportGamesWithoutCateg(orphans, "Output-tmp/stillKO.txt")





















sys.exit()

print("""
################################
# Import oprhan roms
################################
""")

games = []
# le fichoer tmp.txt contient un premier passage déja sur Master par rapport au nom du jeu
# le fichoer tmp2.txt se base sur le fichier tmp.txt et contient un premier passage déja sur Master par rapport au nom du fichier (filename)
games = GlobalHelper.ImportRomlist("tmp2.txt")
games.sort(key=lambda x: x.gamename, reverse=False)
games.sort(key=lambda x: x.category, reverse=False)
print("Imported roms : " + str(len(games)))

print("""
################################
# Import MasterRomList
################################
""")

master = []
master = GlobalHelper.ImportRomlist("Output/MasterRomList.txt")
master.sort(key=lambda x: x.gamename, reverse=False)
print("Imported roms : " + str(len(master)))

percent = 60

print("""
################################
# Last Chance ?
# 2 - recherche sur les mots composant le ou les noms du jeu
# si au moins {0} pourcents des mots ont été trouvés
# pour au moins 1 des noms du jeu
# comparé au noms du master
################################
""".format(percent))

count = 0
found = 0

actualGamename = ""
prevGamename = ""

for g in games:

    if g.filename == "1944ad":
        print("\n\n\n\n\n\ 19944ad \n\n\n\n\n\n\n")

    if g.gamename != "" and g.category == "":
        actualGamename = g.gamename[0:g.gamename.find(" (")]
        wasFound = False

        print("\n###########################\nNew game : {0}".format(actualGamename))

        # if prevGamename == "":
        #     prevGamename = actualGamename

        if prevGamename != actualGamename:
            
            print(" - prevGame : {0}".format(prevGamename))

            prevGamename=actualGamename

            gameToSearch = ""
            gameToSearch = actualGamename
            gamesToSearch = gameToSearch.split(" - ")
            wasFound = False

            # print("###########################\nNew game : {0}".format(g.gamename))
            # print(" - wasFound : {0}".format(str(wasFound)))
            txtTmp = ""
            for gts in gamesToSearch:
                txtTmp += " / " + gts
                print(" - games to search : {0}".format(txtTmp))

            for gts in gamesToSearch:
                wordsToSearch = []
                wordsToSearch = gts.split()
                result = []

                actualMasterGamename = ""
                prevMasterGamename = ""

                # print(" - Actual game to search : {0}".format(gts))

                # print(" - name to search : {0}".format(gts))
                master.sort(key=lambda x: x.gamename, reverse=False)
                for m in master:
                    masterGame = ""
                    masterGame = m.gamename

                    # actualMasterGamename = m.gamename[0:m.gamename.find(" (")]
                    tmpDisplay = m.gamename[0:m.gamename.find(" (")]


                    percTot = count * 100 / len(games)
                    percFound = found * 100 / len(games)

                    # sys.stdout.write("[I] : {0} \r".format(str(count)))
                    txtDisplay = "[I] : " + str(count) + " | "
                    txtDisplay += "[TOT] : " + str(len(games)) + " | "
                    txtDisplay += "[PERC] TOT : " + str(percTot) + " | "
                    txtDisplay += "[FOUND] : " + str(found) + " | "
                    txtDisplay += "[PERC] : " + str(percFound) + " | "
                    txtDisplay += "[GAME] : " + str(gts) + " | "
                    txtDisplay += "[MASTER] : " + tmpDisplay + "\r"
                    sys.stdout.write(txtDisplay)

                    # sys.stdout.write("[I] : {0} | [TOT] : {1} | [PERC] : {2} | [FOUND] : {3} | [PERC] : {4} | [Game] : {5} | [MASTER] : {6} \r".format(str(count), str(len(games)), str(percTot),str(found), str(percFound), str(gts[0:50]), actualMasterGamename))
                    sys.stdout.flush()

                    if m.category != "":
                        # print(" --> master name to search in : {0}".format(actualMasterGamename))
                        # actualMasterGamename = m.gamename[0:m.gamename.find(" (")]
                        #actualMasterGamename.sub(r'\d+$', '', actualMasterGamename)

                        new_s = ""
                        for word in actualMasterGamename.split(' '):
                            if any(char.isdigit() for char in word) and any(c.isalpha() for c in word):
                                new_s += ''.join([i for i in word if not i.isdigit()])
                            else:
                                new_s += word
                            new_s += ' '
                        actualMasterGamename = new_s

                        re.sub(r'\d+$', '', actualMasterGamename)

                        if prevMasterGamename != "" and prevMasterGamename != actualMasterGamename:
                            # print(" ---> master name to search in : {0}".format(actualMasterGamename))
                            # print("Words to seatch : {0} in {1} \n".format(str(wordsToSearch), actualMasterGamename))
                            for wts in wordsToSearch:
                                if wts in actualMasterGamename:
                                    result.append(True)
                                else:
                                    result.append(False)

                            total = len(result)
                            innerCount = 0

                            for ok in result:
                                if ok:
                                    innerCount += 1

                            percentOK = innerCount / total * 100
                            if innerCount >= total:
                                wasFound = True
                                percentOK = 100
                                break
                            else:
                                if percentOK >= percent:
                                    wasFound = True
                                    break
                            print(" - wasFound : {0}".format(str(wasFound)))
                            print(" - percentOK : {0}".format(str(percentOK)))
                        #else:
                        prevMasterGamename = actualMasterGamename
                        #print("Master NEXT >>>>>>>>")
                    if wasFound:
                        break
                if wasFound:
                    break
        else:
            prevGamename=actualGamename
        if wasFound:
            print("FOUND : " + g.gamename + "\n")
            g.category = m.category
            found += 1

    count += 1





print("""
################################
# Result Export
################################
""")
GlobalHelper.ExportToCSV(games, "tmp3.txt")

print("""
################################
# Still KO
################################
""")
GlobalHelper.ExportGamesWithoutCateg(games, "stillKO-2.txt")




sys.exit()


print("""
################################
# Still KO
################################
""")
games.sort(key=lambda x: x.category, reverse=False)
for g in games:
    if g.category == "":
        puzzle = [" in 1", "13 Ma Jiang", "16 Ton", "16 Zhang Ma Jiang", "21 Emon - Mezase Hotel ou!", "6-Pak", "Aq Renkan Awa", "Bad Omen", "Be Ball", "Chibi Maruko-chan - Wakuwaku Shopping ", "Circus Lido", "Columns", "Dial Q o Mawase!", "Dong Gu Ri Te Chi Jak Jeon", "Doraemon - Meikyuu Dai Sakusen", "Drop Rock Hora Hora"]
        bootlegs = ["4 player input test"]
        schmups = ["1944", "Aero Blasters", "Barunba", "Burning Angels", "Codename - Blut Engel", "Coryoon - Child of Dragon", "Crying - Aseimei Sensou", "Darius", "Dead Moon - Tsuki Sekai no Akumu", "Deep Blue - Kaitei Shinwa", "Dragon Saber - After Story of Dragon Spirit"]
        sports = ["Super Baseball", "Appare! Gateball", "Bari Bari Densetsu", "Beastball", "Boogie Woogie Bowling", "Soccer", "Bull Fight - Ring no Haja", "NBA", "Cyber Dodge", "Tennis", "Davis Cup", "Digital Champ", "Ronaldinho 98", "Basketball"]
        action = ["The Adventures of Batman", "Akumajou Dracula", "Alex Kidd", "Disney's Ariel the Little Mermaid", "Bad Omen", "Shadow of the Beast", "Disney's Beauty and the Beast", "Be Ball", "Ben 10", "Chouzetsu Rinjin - Bravoman", "Caliber Fifty", "Captain Lang", "The Chaos Engine", "City Hunter", "The Incredible Crash Dummies", "Castlevania", "Busou Keiji - Cyber Cross", "Dai Makai-Mura", "Tom Mason's Dinosaurs for Hire", "A Dinosaur's Tale", "Doom Troopers - The Mutant Chronicles", "Doraemon - Meikyuu Dai Sakusen", "Jashin Draxos", "DarkWing Duck"]
        simulation = ["Air Management", "A Ressha de Ikou MD", "Daikoukai Jidai"]
        plateform = ["Aladdin II", "The Adventures of Batman", "Akumajou Dracula", "Alex Kidd", "Fushigi no Yume no Alice", "Ankoku Densetsu", "Disney's Ariel the Little Mermaid", "Bang 2 Busters", "The Simpsons - Bart's Nightmare", "Battle Lode Runner", "Disney's Beauty and the Beast", "The Berenstain Bears", "Bubble Bobble", "Captain Lang", "Castle of Illusion", "Chip n Dale", "Dai Makai-Mura", "A Dinosaur's Tale", "The Disney Collection - Mickey and Donald", "Ikazuse! Koi no Doki Doki Penguin Land MD", "Dragon Egg!", "Jashin Draxos", "DarkWing Duck"]
        party = ["The Aquatic Games Starring James Pond and the Aquabats"]
        cheat = ["Action Replay"]
        unknown = ["Art Tool", "Chaos Demo (CPS-1)"]
        adventure = ["Assassins Creed", "Blue Almanac", "Bubblegum Crash!", "Chikudenya Toubei - Kubikiri Yakata Yori", "Crouching Poney Hidden Dragon", "Daichi Kun Crisis - Do Natural", "Dragon Slayer - Eiyuu Densetsu"]
        wargame = ["Bahamut Senki"]
        strategy = ["Tsuru Teruhito no Jissen Kabushiki Bai Bai Game", "Caesar no Yabou", "Carmen Sandiego", "Commandos", "Dune II"]
        race = ["Bari Bari Densetsu", "Tachki"]
        moto = ["Bari Bari Densetsu"]
        fight = ["Beast Warriors", "Ben 10", "Battletoads", "Double Dragon", "The Death and Return of Superman"]
        beatemall = ["Ben 10", "Battletoads", "Double Dragon", "The Death and Return of Superman"]
        shooter = ["1944", "Aero Blasters", "Barunba", "Beyond Zero Tolerance", "Cal.50", "Caliber Fifty", "Narazumono Sentai Butai", "Bloodshot ~ Battle Frenzy", "Crying - Aseimei Sensou", "Counter Strike", "Darius", "Dead Moon - Tsuki Sekai no Akumu", "Death Caliber (Rus)", "Deep Blue - Kaitei Shinwa", "Cadillacs and Dinosaurs", "Doom Troopers - The Mutant Chronicles", "Dragon Saber - After Story of Dragon Spirit"]
        fps = ["Beyond Zero Tolerance", "Bloodshot ~ Battle Frenzy", "Counter Strike"]
        role = ["Blue Almanac", "Body Conquest", "Crouching Poney Hidden Dragon", "Dragon Slayer - Eiyuu Densetsu"]
        bowling = ["Boogie Woogie Bowling"]
        billiards = ["Break In"]
        casual = ["Break In", "Chao Ji Da Fu Weng", "Devil Crash MD", "Dial Q o Mawase!", "Chou Touryuu Retsuden - Dino Land"]
        soccer = ["Soccer", "Ronaldinho 98"]
        boxe = ["Bull Fight - Ring no Haja", "Digital Champ"]
        basket = ["NBA", "Basketball"]
        runandgun = ["Chouzetsu Rinjin Bravoman", "Caliber Fifty", "Cal.50", "The Chaos Engine", "Cadillacs and Dinosaurs", "Doom Troopers - The Mutant Chronicles"]
        educational = ["Carmen Sandiego"]
        cars = ["Tachki"]
        table = ["Break In", "Chao Ji Da Fu Weng"]
        brick = ["Columns"]
        dodgeball = ["Cyber Dodge"]
        tennis = ["Tennis", "Davis Cup"]
        pinball = ["Devil Crash MD", "Chou Touryuu Retsuden - Dino Land"]
        mahjong = ["Dial Q o Mawase!"]
        adult = ["Dial Q o Mawase!"]
    else:
        break


sys.exit()




























toExport = []

for g in games:
    if g.emulator == "Final Burn Alpha":
        toExport.append(g)

GlobalHelper.ExportToCSV(toExport, "tmp2.txt")

print("""
################################
# Import only FBA oprhan roms
################################
""")

games[:] = []
games = GlobalHelper.ImportRomlist("tmp2.txt")
print("Imported roms : " + str(len(games)))

print("""
################################
# Import MasterRomList
################################
""")

master = []
master = GlobalHelper.ImportRomlist("Output/MasterRomList.txt")
master.sort(key=lambda x: x.filename, reverse=False)
print("Imported roms : " + str(len(master)))

games.sort(key=lambda x: x.filename, reverse=False)

for g in games:
    for m in master:
        if g.filename == m.filename and m.category != "":
            g.category == m.category
            break

