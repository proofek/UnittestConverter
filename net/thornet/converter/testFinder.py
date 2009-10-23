"""
UnittestFinder
"""
import os
import re

class UnittestFinder:

    fileList = []
    dirList = []
    ignoreDirs = ['CVS', 'testdata', 'TestData']
    currentDir = ''

    def __init__(self, workingDir):
        self.currentDir = workingDir

    def fetchFileList(self, Dir=None, recursive=True):

        searchDir = self.currentDir
        if Dir is not None:
            searchDir = Dir + '/'

        for fileName in os.listdir(searchDir):

            fullFileName = searchDir + fileName

            if os.path.isfile(fullFileName) is True and self.matchTestName(fullFileName) is True:
                self.fileList.append(fullFileName)

            if os.path.isdir(fullFileName) is True and recursive is True:
                self.fetchFileList(fullFileName)

    def fetchDirList(self, Dir=None, recursive=True):

        searchDir = self.currentDir
        if Dir is not None:
            searchDir = Dir + '/'

        for fileName in os.listdir(searchDir):

            fullFileName = searchDir + fileName
            
            if os.path.isdir(fullFileName) is True and recursive is True and not self.ignoreDirs.__contains__(os.path.basename(fullFileName)):
                self.dirList.append(fullFileName)
                self.fetchDirList(fullFileName)

    def getFileList(self):
        return self.fileList

    def getDirList(self):
        return self.dirList

    def matchTestName(self, fileName):
        m = re.search("\.test\.php$", fileName)
        if m is None:
            return False
        else:
            return True
    def clearFileList(self):
        self.fileList = []


    