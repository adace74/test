#!/usr/bin/env python
######################################################################
#
# $Id$
#
# Name: distribulator.py
#
# Description: The Distribulator.
# A detailed description can be found in the README file.
#
# Notes: Unfortunately, Python, like other shell-oriented langauges,
# requires that methods be defined before calling them.
# As such, main() will always be at the -bottom- of a file.
#
# Flow:
# 1) Fire up / validation
# 2) Load up Server / ServerGroup objectsets.
# 3) Report Load Summary
# 4) Interactive Mode (Parser object, Command objects?)
#
# Server object -- contains server hostname, username
# ServerGroup object -- contains many Server objects
######################################################################

# Version tag
__version__ = '$Revision$'[11:-2]

# Import modules
try:
    # Standard modules
    import getopt
    import getpass
    import os
    import os.path
    import socket
    import sys
    import syslog

    # Custom modules
    import engine.CommandLine
    import engine.ConfigLoader
    import generic.SysLogger

except ImportError:
    print "An error occured while loading Python modules, exiting..."
    sys.exit(1)

######################################################################

# Display a nice pretty header.
def title_header():
    print
    print "The Distribulator v0.10"
    print "-----------------------"
    print

def info_header(server_env, start_dir):
    print "Python Version:      " + sys.version.split()[0]
    print "Local Hostname:      " + socket.gethostname()
    print "Current Environment: " + server_env
    print "Current Directory:   " + start_dir
    print

# Good old main...
def main(argv):
    short_options = ':b:d:e:s:'
    long_options = ['batch=',
                    'directory=',
                    'env=',
                    'shell=']

    usage = """Usage: %s [options] --env=environment

The available options are:

    -b / --batch=filename
    Enables batch mode processing, requires a readable input file.
    Not yet implemented.
    OPTIONAL

    -d / --directory=start_dir
    Allows the wrapper script to pass in the user's real cwd.
    OPTIONAL

    -e / --env=
    Set the server environment we wish to operate in.
    REQUIRED

    -s / --shell=
    Sets the remote shell type we wish to use.  Defaults to ssh.
    Not yet implemented.
    OPTIONAL

""" % argv[0]

    title_header()

    server_env = 'sample'
    server_shell = 'ssh'
    start_dir = '/tmp/'

    try:
        if len(argv) < 2:
            print "ERROR: I need to know which environment I am to use!"
            print
            raise "CommandLineError"

        optlist, args = getopt.getopt(sys.argv[1:], short_options, long_options)

        if len(optlist) > 0:
            for opt in optlist:
                if (opt[0] == '-b') or (opt[0] == '--batch'):
                    batch_file = opt[1]
                elif (opt[0] == '-d') or (opt[0] == '--directory'):
                    start_dir = opt[1]
                elif (opt[0] == '-e') or (opt[0] == '--env'):
                    server_env = opt[1]
                elif (opt[0] == '-s') or (opt[0] == '--shell'):
                    server_shell = opt[1]
        else:
            print "ERROR: getopt failure!  This shouldn't even happen!"
            print
            raise "CommandLineError"

    except "CommandLineError":
        sys.stderr.write(usage)
        sys.exit(1)

    except getopt.GetoptError:
        print "ERROR: Erroneous flag(s) given.  Please check your syntax."
        print
        sys.stderr.write(usage)
        sys.exit(1)

    info_header(server_env, start_dir)

    config_dir = os.path.join(os.getcwd(), 'conf')

    # Log our startup.
    myLogger = generic.SysLogger.SysLogger(syslog.LOG_LOCAL1)
    myLogger.LogMsgInfo("Started by user " + getpass.getuser() + '.')

    # Create CommandLine instance, and pass it through to ConfigLoader.
    myCommLine = engine.CommandLine.CommandLine()

    # Create ConfigLoader instance and call that method!
    myLoader = engine.ConfigLoader.ConfigLoader()
    myPassThruList = myLoader.load(myCommLine, config_dir)

    # The main readline loop.
    myCommLine.processInput(myPassThruList)

    # Once it returns, we're done!
    myLogger.LogMsgInfo("Shutting down...")
    sys.exit(0)

######################################################################
#
# If called from the command line, invoke thyself!
#
######################################################################
if __name__=='__main__': main(sys.argv)
