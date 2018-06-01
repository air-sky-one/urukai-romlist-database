# coding=utf-8

import HelperFile
import HelperRomlist
import os
import os.path
from whoosh import index
from whoosh.fields import Schema, TEXT, KEYWORD, ID, STORED
from whoosh.analysis import StemmingAnalyzer
from whoosh.qparser import QueryParser

def GetDistinct(tab):
    result = []
    for e in tab:
        if not e in result:
            result.append(e)
    return result

def FormatHitResults(r):
    result = []
    for e in r:
        result.append(e["Name"])
    return result
'''
GOOOOOOOOOOOOOOOOOOOOOOOOOOOO !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
'''

# Set the Romlist file path
# romlistPath = input("Romlist file path (ex:/home/me/Documents/myFile.txt) : ")

#if romlistPath == "x":
romlistPath = "/home/urukai/Workspace/Retrogaming/Python scrap builders/urukai-romlist-database/--archives--/Python/1-RomlistHelper/Hyperpie/Nintendo Super Nintendo Entertainment System.txt"

# convert the romlist into a list of name
games = HelperRomlist.LoadRomListFile(romlistPath)

# Création du schéma
schema = Schema(Name=TEXT(stored=True))

# Création de l'index
if not os.path.exists("indexdir"):
    os.mkdir("indexdir")

ix = index.create_in("indexdir", schema)
ix = index.open_dir("indexdir")

# Indexation des documents (g.gamename)
print("Building index ...")
writer = ix.writer()
for g in games:
    writer.add_document(Name=g.gamename)
writer.commit()

# Load Universes list
tmpStr = HelperFile.GetFilecontent("data/FranchiseList.txt")
lines = tmpStr.split("\n")

'''with ix.searcher() as searcher:
    t = "Super Mario"
    print(t)
    query = QueryParser("Name", ix.schema).parse(t)
    results = searcher.search(query, groupedby="Name", limit=None)

    if len(results) > 0 :
        print("*Univers : " + t + " | Game : " + str(results[0]))

        print(results.groups("Name"))
        for r in results:
            print(r["Name"])
input("Please kill me ...")'''

for l in lines:
    with ix.searcher() as searcher:
        print(l)
        query = QueryParser("Name", ix.schema).parse(l)
        results = searcher.search(query, limit=None)

        if len(results) > 0 :
            formattedHits = FormatHitResults(results)
            r = GetDistinct(formattedHits)
            for e in r:
                print(e)
            input("Wait ...")
            # à ce stade on récupère la liste de jeux distincts par franchise
            # reste à trouver le format de sauvergarde et sauvegarder
