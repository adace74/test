######################################################################
#
# $Id$
#
# Name: ConfigLoader.py
#
######################################################################

# Version tag
__version__= '$Revision$'[11:-2]

# Standard modules
import os
import os.path
import string
import sys

# Custom modules
import engine.CommandLine
import engine.XMLFileParser
import engine.data.GlobalConfig

######################################################################

class ConfigLoader:

    def __init__(self, PassedGlobalConfig):
        self._globalConfig = PassedGlobalConfig

    def loadGlobalConfig(self, PassedCommLine):
        # Load GNU Readline history.
        if (self._globalConfig.isBatchMode() == False):
            print('Loading configuration...')

        thisLinesLoaded = PassedCommLine.initHistory()
        #
        # Try to print status -after- actions so as to be
        # more accurate.
        #
        if (self._globalConfig.isBatchMode() == False):
            print("- GNU Readline history:        %d lines loaded." % \
                  (thisLinesLoaded))
        #
        # Unix "pass through" commands.
        #
        thisPassThruList = []
        
        try:
            thisFilename = os.path.join(self._globalConfig.getConfigDir(), \
                                        'pass_through_cmds.txt')
            thisFile = open(thisFilename, 'r')
            
            for thisLine in thisFile:
                thisLine = thisLine.strip()
                thisPassThruList.append(thisLine)

            thisFile.close()

        except IOError, (errno, strerror):
            thisError = "ERROR:[Errno %s] %s: %s" % \
                        (errno, strerror, thisFilename)
            print(thisError)
            self._globalConfig.getSysLogger().LogMsgError(thisError)
            sys.exit(1)

        self._globalConfig.setPassThruList(thisPassThruList)

        # Status.
        if (self._globalConfig.isBatchMode() == False):
            print( "- Unix pass-through commands:  %d lines loaded." \
                   % (len(thisPassThruList)) )

        # Parse XML...ouchies.
        thisParser = engine.XMLFileParser.XMLFileParser()
        self._globalConfig = thisParser.parse(self._globalConfig)

        if (self._globalConfig.isBatchMode() == False):
            print( "- Global options and settings: %d lines loaded." %
                   (self._globalConfig.getConfigLines()) )

        self._globalConfig.setCurrentServerGroup(
            self._globalConfig.getServerGroupList()[0] )

        thisServerGroupStr = '- '
        thisTotalServerCount = 0
        thisColumnCount = 0

        for thisServerGroup in self._globalConfig.getServerGroupList():
            thisColumnCount = thisColumnCount + 1
            thisTotalServerCount = thisTotalServerCount + \
                                   thisServerGroup.getServerCount()
            thisServerGroupStr = thisServerGroupStr + '%10s (%2d) ' % \
                                 (thisServerGroup.getName(), thisServerGroup.getServerCount())

            if (thisColumnCount == 4):
                thisColumnCount = 0
                thisServerGroupStr = thisServerGroupStr + '\n- '

        if (self._globalConfig.isBatchMode() == False):
            print("- Available Server Groups:")
            print("-")
            print(thisServerGroupStr)        
            print
            print("Confused?  Need help?  Try typing 'help' and see what happens!")
            print

        return self._globalConfig

######################################################################
