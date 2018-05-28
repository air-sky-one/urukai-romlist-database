#!/usr/bin/python3.6
# -*-coding:Utf-8 -*

# ##################################################################################################
# Emulator Config File Helper
# By Urukai
# Copyright 2018
# Licence GNU GENERAL PUBLIC LICENSE, Version 3, 29 June 2007
# ##################################################################################################

import glob
import Helpers.ExtensionsHelper

emulFiles = glob.glob("Config/Emulators/*.cfg")

for emuFile in emulFiles:
	print("\n##########\n" + emuFile[emuFile.rfind("/") + 1:] + "\n##########")
	extensions = Helpers.ExtensionsHelper.Get_Extensions(emuFile)
	print(extensions)
