# coding=utf-8
import os, os.path
from whoosh import index
from whoosh.fields import Schema, TEXT, KEYWORD, ID, STORED
from whoosh.analysis import StemmingAnalyzer
from whoosh.qparser import QueryParser

# Création du schéma
schema = Schema(Name=TEXT(stored=True),
                Title=TEXT(analyzer=StemmingAnalyzer()))

# Création de l'index
if not os.path.exists("indexdir"):
    os.mkdir("indexdir")

ix = index.create_in("indexdir", schema)
ix = index.open_dir("indexdir")

# Indexation des documents
writer = ix.writer()
writer.add_document(Name=u"Super Mario World (USA)", Title=u"Super Mario World (USA)")
writer.add_document(Name=u"Frogger 2 - Swampy's Revenge (USA)", Title=u"Frogger 2 - Swampy's Revenge (USA)")
writer.add_document(Name=u"akumajou", Title=u"Akuma-Jou Dracula (Japan ver. N)")
writer.commit()

with ix.searcher() as searcher:
    query = QueryParser("Name", ix.schema).parse(u'World Super')
    results = searcher.search(query)

    # Résultats
    found = results.scored_length()
    if results.has_exact_length():
        print("Scored", found, "of exactly", len(results), "documents")
    else:
        low = results.estimated_min_length()
        high = results.estimated_length()

        print("Scored", found, "of between", low, "and", high, "documents")

input("Press Enter to continue...")
