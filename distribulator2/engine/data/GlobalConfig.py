######################################################################
#
# $Id$
#
# Name: GlobalConfig.py
#
######################################################################

# Version tag
__version__= '$Revision$'[11:-2]

# Standard modules
import os
import os.path
import string
import sys

######################################################################

class GlobalConfig:
    #
    # Global settings.
    #
    # Which mode we're operating in.
    #
    def isBatchMode(self):
        return self._isbatchflag

    def setBatchMode(self, PassedBatchMode):
        self._isbatchflag = PassedBatchMode
    #
    # Which mode we're operating in.
    #
    def getBatchFile(self):
        return self._batchFile

    def setBatchFile(self, PassedBatchFile):
        self._batchFile = PassedBatchFile
    #
    # Our configuration directory path.
    #
    def getConfigDir(self):
        return self._configDir

    def setConfigDir(self, PassedConfigDir):
        self._configDir = PassedConfigDir
    #
    # Our helpfiles path.
    #
    def getHelpDir(self):
        return self._helpDir

    def setHelpDir(self, PassedHelpDir):
        self._helpDir = PassedHelpDir
    #
    # Number of config lines loaded.
    #
    def getConfigLines(self):
        return self._configLines

    def setConfigLines(self, PassedConfigLines):
        self._configLines = PassedConfigLines
    #
    # System binary locations.
    #
    def getLognameBinary(self):
        return self._lognameBinary

    def setLognameBinary(self, PassedLognameBinary):
        self._lognameBinary = PassedLognameBinary

    def getPingBinary(self):
        return self._pingBinary

    def setPingBinary(self, PassedPingBinary):
        self._pingBinary = PassedPingBinary

    def getScpBinary(self):
        return self._scpBinary

    def setScpBinary(self, PassedScpBinary):
        self._scpBinary = PassedScpBinary

    def getSshBinary(self):
        return self._sshBinary

    def setSshBinary(self, PassedSshBinary):
        self._sshBinary = PassedSshBinary
    #
    # Syslog Facility.
    #
    def getSyslogFacility(self):
        return self._syslogFacility

    def setSyslogFacility(self, PassedSyslogFacility):
        self._syslogFacility = PassedSyslogFacility
    #
    # Syslogger Object.
    #
    def getSysLogger(self):
        return self._sysLogger

    def setSysLogger(self, PassedSysLogger):
        self._sysLogger = PassedSysLogger
    #
    # Server Environment.
    #
    def getServerEnv(self):
        return self._serverEnv

    def setServerEnv(self, PassedServerEnv):
        self._serverEnv = PassedServerEnv
    #
    # Unix command "pass through" list.
    #
    def getPassThruList(self):
        return self._passThruList

    def setPassThruList(self, PassedPassThruList):
        self._passThruList = PassedPassThruList
    #
    # Local Unix username.
    #
    def getUsername(self):
        return self._username

    def setUsername(self, PassedUsername):
        self._username = PassedUsername
    #
    # Local effective Unix username.
    #
    def getRealUsername(self):
        return self._realUsername

    def setRealUsername(self, PassedRealUsername):
        self._realUsername = PassedRealUsername
    #
    # Servers and ServerGroups
    #
    def getCurrentServerGroup(self):
        return self._currentServerGroup

    def setCurrentServerGroup(self, PassedServerGroup):
        self._currentServerGroup = PassedServerGroup

    def getServerGroupList(self):
        return self._serverGroupList

    def setServerGroupList(self, PassedServerGroupList):
        self._serverGroupList = PassedServerGroupList

    def addServerGroup(self, PassedServerGroup):
        self._serverGroupList.append(PassedServerGroup)

    def getServerGroupByName(self, PassedServerGroupName):
        for thisServerGroup in self._serverGroupList:
            if (PassedServerGroupName == thisServerGroup.getName()):
                return thisServerGroup

        return False

######################################################################
