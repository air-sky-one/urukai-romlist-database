#!/usr/bin/python3.6
# -*-coding:Utf-8 -*

# ##################################################################################################
# Romlist Helper
# By Urukai
# Copyright 2018
# Licence GNU GENERAL PUBLIC LICENSE, Version 3, 29 June 2007
# ##################################################################################################

class Rom:

    def __init__(self):
        self._filename = "NULL"
        self._gamename = ""
        self._emulator = ""
        self._cloneOf = ""
        self._year = ""
        self._manufacturer = ""
        self._category = ""
        self._players = ""
        self._rotation = ""
        self._control = ""
        self._status = ""
        self._displayCount = ""
        self._displayType = ""
        self._altRomName = ""
        self._altTitle = ""
        self._extra = ""
        self._buttons = ""
        self._crc = ""
        self._rating = ""

    @property
    def filename(self):
        return self._filename

    @filename.setter
    def filename(self, v):
        self._filename = v

    @property
    def gamename(self):
        return self._gamename

    @gamename.setter
    def gamename(self, v):
        self._gamename = v

    @property
    def emulator(self):
        return self._emulator

    @emulator.setter
    def emulator(self, v):
        self._emulator = v

    @property
    def cloneOf(self):
        return self._cloneOf

    @cloneOf.setter
    def cloneOf(self, v):
        self._cloneOf = v

    @property
    def year(self):
        return self._year

    @year.setter
    def year(self, v):
        self._year = v

    @property
    def manufacturer(self):
        return self._manufacturer

    @manufacturer.setter
    def manufacturer(self, v):
        self._manufacturer = v

    @property
    def category(self):
        return self._category

    @category.setter
    def category(self, v):
        self._category = v

    @property
    def players(self):
        return self._players

    @players.setter
    def players(self, v):
        self._players = v

    @property
    def rotation(self):
        return self._rotation

    @rotation.setter
    def rotation(self, v):
        self._rotation = v

    @property
    def control(self):
        return self._control

    @control.setter
    def control(self, v):
        self._control = v

    @property
    def status(self):
        return self._status

    @status.setter
    def status(self, v):
        self._status = v

    @property
    def displayCount(self):
        return self._displayCount

    @displayCount.setter
    def displayCount(self, v):
        self._displayCount = v

    @property
    def displayType(self):
        return self._displayType

    @displayType.setter
    def displayType(self, v):
        self._displayType = v

    @property
    def altRomName(self):
        return self._altRomName

    @altRomName.setter
    def altRomName(self, v):
        self._altRomName = v

    @property
    def altTitle(self):
        return self._altTitle

    @altTitle.setter
    def altTitle(self, v):
        self._altTitle = v

    @property
    def extra(self):
        return self._extra

    @extra.setter
    def extra(self, v):
        self._extra = v

    @property
    def buttons(self):
        return self._buttons

    @buttons.setter
    def buttons(self, v):
        self._buttons = v

    @property
    def crc(self):
        return self._crc

    @crc.setter
    def crc(self, v):
        self._crc = v

    @property
    def rating(self):
        return self._rating

    @rating.setter
    def rating(self, v):
        self._crc = v
