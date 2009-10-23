#!/usr/bin/python
"""
SimpleTest to PHPUnit Converter v.0.1 by Sebastian Marek
Copyright (C) 2008 Sebastian Marek
This software comes with ABSOLUTELY NO WARRANTY. This is free software,
and you are welcome to modify and redistribute it

Usage: UnittestConverter -a -h [-d]

  OPTIONS:
  -h, --help             Display this help and exit.
  -a, --action           convert - Converts SimpleTest tests to PHPUnit tests
                         create  - Creates test suites
  -d, --dir              Convert unit tests in given directory.
  -t, --transformation   Use only one type of transformation.
                         Valid transformation keywords: 
                          - Extends
                          - AssertEqual
                          - AssertNotEqual
                          - AssertReference
                          - IsA
                          - Pass
                          - Identical
                          - ExpectException

"""
import sys
import getopt
import os
from net.thornet.actionWizard.actionWizard import ActionWizard

class Usage(Exception):
    def __init__(self, msg):
        self.msg = msg

def main(argv=None):

    workingDir = '.'
    actionCalled = None
    transformation = None

    if argv is None:
        argv = sys.argv    
    
    try:
        try:
            opts, args = getopt.getopt(argv[1:], "hd:a:t:", ["help","dir=","action=","transformation="])
        except getopt.error, msg:
            raise Usage(msg)
        
        # process options
        for o, a in opts:
            if o in ("-h", "--help"):
                print __doc__
                sys.exit(0)
            if o in ("-a", "--action"):
                actionCalled = a
            if o in ("-d", "--dir"):
                workingDir = a
            if o in ("-t", "--transformation"):
                transformation = a

        if actionCalled is None:
            raise Usage('Missing argument - specify valid action to use')

        arguments = {'workingDir': workingDir, 'transformation': transformation}
        action = ActionWizard(actionCalled)
        action.run(arguments)

        # run Forest, run!
        #testFinder = UnittestFinder(workingDir)
        #testFinder.fetchFileList()
        
        #converter = UnittestConverter()
        
        #fileList = testFinder.getFileList()
        #for file in fileList:
        #    print 'Converting ' + file
        #    converter.convert(file)

    except Usage, err:
        print >>sys.stderr, err.msg
        print >>sys.stderr, "for help use --help"    
        return 2


##################### Main application start point #####################
if __name__ == "__main__":
    sys.exit(main())
