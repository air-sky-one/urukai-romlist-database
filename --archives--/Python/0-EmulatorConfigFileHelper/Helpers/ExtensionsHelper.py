#!/usr/bin/python3.6
# -*-coding:Utf-8 -*

# ##################################################################################################
# Emulator Config File Helper
# By Urukai
# Copyright 2018
# Licence GNU GENERAL PUBLIC LICENSE, Version 3, 29 June 2007
# ##################################################################################################

def Get_Extensions(emulatorCfgPath):
    emulatorCfgFile = open(emulatorCfgPath, "r")
    emulatorCfg = str(emulatorCfgFile.read())
    emulatorCfgFile.close()

    # Get roms allowed extensions into Array

    extensionsBegin = emulatorCfg.find("romext")
    extensionsEnd = emulatorCfg.find("system")
    extensionsList = emulatorCfg[extensionsBegin:extensionsEnd]
    extensionsList = extensionsList[extensionsList.find("."):]

    extensions = extensionsList.split(";")

    return extensions
