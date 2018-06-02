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
romlistPath = "/home/urukai/Workspace/Retrogaming/Python scrap builders/urukai-romlist-database/--archives--/Python/1-RomlistHelper/Hyperpie/Nintendo Super Nintendo Entertainment System.txt"

# convert the romlist into a list of name
games = []
games = HelperRomlist.LoadRomListFile(romlistPath)

alreadyLinkedRomsPath = "/home/urukai/Workspace/Retrogaming/Python scrap builders/urukai-romlist-database/Output/2-test-univers-snes_roms with universe.csv"
alreadyLinkedRoms = HelperFile.GetFilecontent(alreadyLinkedRomsPath)

lines = alreadyLinkedRoms.split("\n")

# Création du schéma
schema = Schema(Name=TEXT(stored=True))

# Création de l'index
if not os.path.exists("indexdir"):
    os.mkdir("indexdir")

ix = index.create_in("indexdir", schema)
ix = index.open_dir("indexdir")

# Indexation des documents (alreadyLinkedRoms)
print("Building index ...")
writer = ix.writer()
for l in lines:
    cols = l.split(";")
    writer.add_document(Name=cols[0])
    print(l)
writer.commit()

for g in games:
    with ix.searcher() as searcher:
        query = QueryParser("Name", ix.schema).parse(g.gamename)
        results = searcher.search(query, limit=None)

        if not len(results) > 0 :
            print(";" + g.gamename)
