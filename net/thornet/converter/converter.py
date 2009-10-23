"""
UnittestParser parser
"""
import os
import re
from net.thornet.converter.testFinder import UnittestFinder

class UnittestConverter:

    testFinder = None
    transformation = None

    def __init__(self, arguments):

        self.testFinder = UnittestFinder(arguments['workingDir'])
        self.transformation = arguments['transformation']
        self.testFinder.fetchFileList()

    def run(self):

        fileList = self.testFinder.getFileList()

        for file in fileList:
            print 'Converting ' + file
            self.convert(file)

    def convert(self, fileName):

            backupFileName = fileName + '.bak'
            os.rename(fileName, backupFileName)
            simpleTest = open(backupFileName, 'r')
            phpUnit = open(fileName, 'a+')

            for line in simpleTest:
                if (self.transformation is None or self.transformation == 'Extends') and self.convertExtends(line, phpUnit) is True:
                    continue
                if (self.transformation is None or self.transformation == 'AssertEqual') and self.convertAssertEqual(line, phpUnit) is True:
                    continue
                if (self.transformation is None or self.transformation == 'AssertNotEqual') and self.convertAssertNotEqual(line, phpUnit) is True:
                    continue
                if (self.transformation is None or self.transformation == 'AssertReference') and self.convertAssertReference(line, phpUnit) is True:
                    continue
                if (self.transformation is None or self.transformation == 'IsA') and self.convertIsA(line, phpUnit) is True:
                    continue
                if (self.transformation is None or self.transformation == 'Pass') and self.convertPass(line, phpUnit) is True:
                    continue
                if (self.transformation is None or self.transformation == 'Identical') and self.convertIdentical(line, phpUnit) is True:
                    continue
                if (self.transformation is None or self.transformation == 'ExpectException') and self.convertExpectException(line, phpUnit) is True:
                    continue
                phpUnit.write(line)

            simpleTest.close()
            phpUnit.close()

    def convertExtends(self, line, inputFile):

        converted = False

        p = re.compile('extends UnitTestCase')
        result = p.subn('extends PHPUnit_Framework_TestCase', line)

        if result[1] > 0:
            inputFile.write(result[0])
            converted = True

        return converted

    def convertAssertEqual(self, line, inputFile):

        converted = False

        p = re.compile('this->assertEqual')
        result = p.subn('this->assertEquals', line)

        if result[1] > 0:
            inputFile.write(result[0])
            converted = True

        return converted

    def convertAssertNotEqual(self, line, inputFile):

        converted = False

        p = re.compile('this->assertNotEqual')
        result = p.subn('this->assertNotEquals', line)

        if result[1] > 0:
            inputFile.write(result[0])
            converted = True

        return converted

    def convertAssertReference(self, line, inputFile):

        converted = False

        p = re.compile('this->assertReference')
        result = p.subn('this->assertSame', line)

        if result[1] > 0:
            inputFile.write(result[0])
            converted = True

        return converted

    def convertIsA(self, line, inputFile):

        converted = False

        p = re.compile("this->assertIsA\(([^,]+),[ \t]*(?P<quote>['\"])(.+)(?P=quote)\)")
        m = p.search(line)

        if m is not None:
            result = p.subn('this->assertType(\'' + m.group(3) + '\', ' + m.group(1) + ')', line)

            if result[1] > 0:
                inputFile.write(result[0])
                converted = True

        return converted

    def convertPass(self, line, inputFile):

        converted = False

        p = re.compile('this->pass')
        result = p.subn('this->anything', line)

        if result[1] > 0:
            inputFile.write(result[0])
            converted = True

        return converted

    def convertIdentical(self, line, inputFile):

        converted = False

        p = re.compile("this->assertIdentical\((.+),(.+)\)")
        m = p.search(line)

        if m is not None:
            print m.groups()
            result = p.subn('this->assertThat(' + m.group(2) + ', $this->identicalTo(' + m.group(1) +'))', line)

            if result[1] > 0:
                inputFile.write(result[0])
                converted = True

        return converted

    def convertExpectException(self, line, inputFile):

        converted = False

        p = re.compile('this->expectException')
        result = p.subn('this->setExpectedException', line)

        if result[1] > 0:
            inputFile.write(result[0])
            converted = True

        return converted
