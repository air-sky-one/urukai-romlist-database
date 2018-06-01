# coding=utf-8

import HelperFile
import HelperRomlist
import os
import os.path
from whoosh import index
from whoosh.fields import Schema, TEXT, KEYWORD, ID, STORED
from whoosh.analysis import StemmingAnalyzer
from whoosh.qparser import QueryParser

# Set the Romlist file path
romlistPath = input("Romlist file path (ex:/home/me/Documents/myFile.txt) : ")

if romlistPath == "x":
    romlistPath = "/home/akerbage/Workspace/Projects/RetroGaming/urukai-romlist-database/--archives--/Python/1-RomlistHelper/Hyperpie/Nintendo Super Nintendo Entertainment System.txt"

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
writer = ix.writer()
for g in games:
    writer.add_document(Name=g.gamename)
writer.commit()

# Load franchises list
tmpStr = HelperFile.GetFilecontent("data/FranchiseList.txt")
lines = tmpStr.split("\n")

for l in lines:
    with ix.searcher() as searcher:
        print(l)
        query = QueryParser("Name", ix.schema).parse(l)
        results = searcher.search(query)

        if len(results) > 0 :
            print("Franchise : " + l + " | Game : " + str(results[0]))

'''
        # Résultats
        found = results.scored_length()
        if results.has_exact_length():
            print("Scored", found, "of exactly", len(results), "documents")
        else:
            low = results.estimated_min_length()
            high = results.estimated_length()

            print("Scored", found, "of between", low, "and", high, "documents")

            for r in results:
                print(r)

'''
