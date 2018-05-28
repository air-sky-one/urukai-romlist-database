#!/usr/bin/python3.6
# -*-coding:Utf-8 -*

import re
import sys
import GlobalHelper

print("""
################################
# Import New MasterRomlist
################################
""")

master = []
master = GlobalHelper.ImportRomlist("Output/NewMasterRomlist3.txt")
master.sort(key=lambda x: x.gamename, reverse = False)

print("- count : {0}".format(str(len(master))))

masterCount = 0

print("""
################################
# Get categories
################################
""")
categs = []
categs = GlobalHelper.GetCategories(master)

print("- count : {0}".format(str(len(categs))))

txtDisplay = ""
for c in categs:
	txtDisplay += c + "\n"

path = "Output/Categs-MRLF-3.txt"
GlobalHelper.WriteToFile(txtDisplay, path)
print("- exported to : {0}".format(path))

print("""
################################
# Get distinct categories
################################
""")
dcategs = []
dcategs = GlobalHelper.GetDistinctCategories(master)

print("- count : {0}".format(str(len(dcategs))))

txtDisplay = ""
for c in dcategs:
	txtDisplay += c + "\n"

path = "Output/Distinct-Categs-MRLF-3.txt"
GlobalHelper.WriteToFile(txtDisplay, path)
print("- exported to : {0}".format(path))
