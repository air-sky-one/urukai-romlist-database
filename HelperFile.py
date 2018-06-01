# coding=utf-8
import os
import os.path

'''
' Return the content of a file
'''
def GetFilecontent(path):
    file = open(path, "r")
    fileContent = str(file.read())
    file.close()
    return fileContent
