# coding=utf-8
import os
import os.path
from whoosh import index
from whoosh.fields import Schema, TEXT, KEYWORD, ID, STORED
from whoosh.analysis import StemmingAnalyzer
from whoosh.qparser import QueryParser

# Création du schéma
schema = Schema(Name=TEXT(stored=True))

# Création de l'index
if not os.path.exists("indexdir"):
    os.mkdir("indexdir")

ix = index.create_in("indexdir", schema)
ix = index.open_dir("indexdir")

path = "../data/FranchiseList.txt"
file = open(path, "r")
fileContent = str(file.read())
file.close()

lines = fileContent.split("\n")

# Indexation des documents
writer = ix.writer()
for l in lines:
    writer.add_document(Name=l)
    print(l)
writer.commit()

with ix.searcher() as searcher:
    query = QueryParser("Name", ix.schema).parse(u'Zero')
    results = searcher.search(query)

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

# input("Press Enter to continue...")
