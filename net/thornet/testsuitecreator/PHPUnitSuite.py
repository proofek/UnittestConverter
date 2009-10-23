#!/usr/bin/env python




##################################################
## DEPENDENCIES
import sys
import os
import os.path
from os.path import getmtime, exists
import time
import types
import __builtin__
from Cheetah.Version import MinCompatibleVersion as RequiredCheetahVersion
from Cheetah.Version import MinCompatibleVersionTuple as RequiredCheetahVersionTuple
from Cheetah.Template import Template
from Cheetah.DummyTransaction import DummyTransaction
from Cheetah.NameMapper import NotFound, valueForName, valueFromSearchList, valueFromFrameOrSearchList
from Cheetah.CacheRegion import CacheRegion
import Cheetah.Filters as Filters
import Cheetah.ErrorCatchers as ErrorCatchers
import os.path

##################################################
## MODULE CONSTANTS
try:
    True, False
except NameError:
    True, False = (1==1), (1==0)
VFFSL=valueFromFrameOrSearchList
VFSL=valueFromSearchList
VFN=valueForName
currentTime=time.time
__CHEETAH_version__ = '2.0.1'
__CHEETAH_versionTuple__ = (2, 0, 1, 'final', 0)
__CHEETAH_genTime__ = 1202423570.764852
__CHEETAH_genTimestamp__ = 'Thu Feb  7 22:32:50 2008'
__CHEETAH_src__ = '/home/proofek/workspace-pdt/UnittestConverter/src/net/plus/testsuitecreator/PHPUnitSuite.tmpl'
__CHEETAH_srcLastModified__ = 'Thu Feb  7 22:02:22 2008'
__CHEETAH_docstring__ = 'Autogenerated by CHEETAH: The Python-Powered Template Engine'

if __CHEETAH_versionTuple__ < RequiredCheetahVersionTuple:
    raise AssertionError(
      'This template was compiled with Cheetah version'
      ' %s. Templates compiled before version %s must be recompiled.'%(
         __CHEETAH_version__, RequiredCheetahVersion))

##################################################
## CLASSES

class PHPUnitSuite(Template):

    ##################################################
    ## CHEETAH GENERATED METHODS


    def __init__(self, *args, **KWs):

        Template.__init__(self, *args, **KWs)
        if not self._CHEETAH__instanceInitialized:
            cheetahKWArgs = {}
            allowedKWs = 'searchList namespaces filter filtersLib errorCatcher'.split()
            for k,v in KWs.items():
                if k in allowedKWs: cheetahKWArgs[k] = v
            self._initCheetahInstance(**cheetahKWArgs)
        

    def respond(self, trans=None):



        ## CHEETAH: main method generated for this template
        if (not trans and not self._CHEETAH__isBuffering and not callable(self.transaction)):
            trans = self.transaction # is None unless self.awake() was called
        if not trans:
            trans = DummyTransaction()
            _dummyTrans = True
        else: _dummyTrans = False
        write = trans.response().write
        SL = self._CHEETAH__searchList
        _filter = self._CHEETAH__currentFilter
        
        ########################################
        ## START - generated method body
        
        write("""<?php

if (!defined('PHPUnit_MAIN_METHOD')) {
    define('PHPUnit_MAIN_METHOD', '""")
        _v = VFFSL(SL,"dirName",True) # '${dirName}' on line 5, col 36
        if _v is not None: write(_filter(_v, rawExpr='${dirName}')) # from line 5, col 36.
        write("""_AllTests::main');
}
 
require_once 'PHPUnit/Framework.php';
require_once 'PHPUnit/TextUI/TestRunner.php';

""")
        for testFile in VFFSL(SL,"tests",True): # generated from line 11, col 1
            write("""require_once '""")
            _v = VFN(VFFSL(SL,"os.path",True),"basename",False)(VFFSL(SL,"testFile",True)) # '${os.path.basename($testFile)}' on line 12, col 15
            if _v is not None: write(_filter(_v, rawExpr='${os.path.basename($testFile)}')) # from line 12, col 15.
            write("""';
""")
        write('''
class ''')
        _v = VFFSL(SL,"dirName",True) # '${dirName}' on line 15, col 7
        if _v is not None: write(_filter(_v, rawExpr='${dirName}')) # from line 15, col 7.
        write("""_AllTests
{
    public static function main()
    {
        PHPUnit_TextUI_TestRunner::run(self::suite());
    }
 
    public static function suite()
    {
        $suite = new PHPUnit_Framework_TestSuite('Framework """)
        _v = VFFSL(SL,"dirName",True) # '${dirName}' on line 24, col 62
        if _v is not None: write(_filter(_v, rawExpr='${dirName}')) # from line 24, col 62.
        write("""');

""")
        for testClassName in VFFSL(SL,"classNames",True): # generated from line 26, col 3
            write("""\t\t$suite->addTestSuite('""")
            _v = VFFSL(SL,"testClassName",True) # '$testClassName' on line 27, col 26
            if _v is not None: write(_filter(_v, rawExpr='$testClassName')) # from line 27, col 26.
            write("""');
""")
        write(""" 
        return $suite;
    }
}
 
if (PHPUnit_MAIN_METHOD == '""")
        _v = VFFSL(SL,"dirName",True) # '${dirName}' on line 34, col 29
        if _v is not None: write(_filter(_v, rawExpr='${dirName}')) # from line 34, col 29.
        write("""_AllTests::main') {
    """)
        _v = VFFSL(SL,"dirName",True) # '${dirName}' on line 35, col 5
        if _v is not None: write(_filter(_v, rawExpr='${dirName}')) # from line 35, col 5.
        write('''_AllTests::main();
}
''')
        
        ########################################
        ## END - generated method body
        
        return _dummyTrans and trans.response().getvalue() or ""
        
    ##################################################
    ## CHEETAH GENERATED ATTRIBUTES


    _CHEETAH__instanceInitialized = False

    _CHEETAH_version = __CHEETAH_version__

    _CHEETAH_versionTuple = __CHEETAH_versionTuple__

    _CHEETAH_genTime = __CHEETAH_genTime__

    _CHEETAH_genTimestamp = __CHEETAH_genTimestamp__

    _CHEETAH_src = __CHEETAH_src__

    _CHEETAH_srcLastModified = __CHEETAH_srcLastModified__

    _mainCheetahMethod_for_PHPUnitSuite= 'respond'

## END CLASS DEFINITION

if not hasattr(PHPUnitSuite, '_initCheetahAttributes'):
    templateAPIClass = getattr(PHPUnitSuite, '_CHEETAH_templateClass', Template)
    templateAPIClass._addCheetahPlumbingCodeToClass(PHPUnitSuite)


# CHEETAH was developed by Tavis Rudd and Mike Orr
# with code, advice and input from many other volunteers.
# For more information visit http://www.CheetahTemplate.org/

##################################################
## if run from command line:
if __name__ == '__main__':
    from Cheetah.TemplateCmdLineIface import CmdLineIface
    CmdLineIface(templateObj=PHPUnitSuite()).run()

