"""
TestSuite creator
"""

import os
import re

from net.thornet.converter.testFinder import UnittestFinder
from Cheetah.Template import Template
from net.thornet.testsuitecreator.PHPUnitSuite import PHPUnitSuite

class TestSuiteCreator:

    testFinder = None

    def __init__(self, arguments):

        self.testFinder = UnittestFinder(arguments['workingDir'])
        self.testFinder.fetchDirList()

    def extractClassNames(self, fileName, classNames):
        p = re.compile('class(.+)extends.+PHPUnit_Framework_TestCase')
        unitTestFile = open(fileName, 'r')
        for line in unitTestFile:
             m = p.search(line)
             if m is not None:
                 className = m.group(1).strip()
                 if className is not None:
                     classNames.append(className)
        unitTestFile.close()

    def saveSuite(self, dirName, content):
        newSuite = open(dirName + '/AllTests.php', 'w')
        newSuite.write(content)
        newSuite.close()

    def run(self):

        dirList = self.testFinder.getDirList()

        for dirName in dirList:

            self.testFinder.clearFileList()
            self.testFinder.fetchFileList(dirName, False)
            print 'Creating suite for ' + os.path.basename(dirName)

            template = PHPUnitSuite()
            template.dirName = os.path.basename(dirName)
            template.tests = self.testFinder.getFileList()
            template.classNames = []

            for fileName in self.testFinder.getFileList():
                self.extractClassNames(fileName, template.classNames)
            
            self.saveSuite(dirName, str(template))
 