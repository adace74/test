######################################################################
#
# $Id$
#
# Name: GlobalConfig.py
#
######################################################################

# Version tag
__version__= '$Revision$'[11:-2]

try:
    # Standard modules
    import os
    import os.path
    import string
    import sys

except ImportError:
    print "An error occured while loading Python modules, exiting..."
    sys.exit(1)

######################################################################

class GlobalConfig:

    #
    # Global settings.
    #
    #
    # Unix command "pass through" list.
    #
    def getPassThruList(self):
        return self.thisPassThruList
    
    def setPassThruList(self, PassedPassThruList):
        self.thisPassThruList = PassedPassThruList
    #
    # Servers and ServerGroups
    #

######################################################################