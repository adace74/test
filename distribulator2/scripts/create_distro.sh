#!/bin/sh
#
# $Id$
#
# Description:  Creates distribution tar/gzip archives.
#
# (c) Copyright 2003 Adam W. Dace <adam@turing.com>  All Rights Reserved. 
# Please see the accompanying LICENSE file for license information.
#
# Sourcecode location.
#
CVSWORK_DIR="/home/awd/cvswork-sf"
PROJECT_DIR="distribulator2"
PROJECT_NAME="distribulator"
#
# Binary locations.
#
FIND_BIN="/usr/bin/find"
RM_BIN="/bin/rm"
TAR_BIN="/usr/bin/tar"
XARGS_BIN="/usr/bin/xargs"
#
# Make sure the user passed in a version to package.
#
if [ $# -lt 1 ]; then
	echo "ERROR: Please specify a version to package."

	exit 1
else
	echo "INFO:  Starting to archive..."
fi
#
# Step 1: Clean up any compiled python objects.
#
$FIND_BIN $CVSWORK_DIR/$PROJECT_DIR -name '*.pyc' | $XARGS_BIN $RM_BIN
#
# Step 2: Clean up any emacs temp files.
#
$FIND_BIN $CVSWORK_DIR/$PROJECT_DIR -name '*~' | $XARGS_BIN $RM_BIN
#
# Step 3: Clean up the config.xml symlink.
#
$RM_BIN $CVSWORK_DIR/$PROJECT_DIR/conf/config.xml
#
# Step 4: Create the distribution tar/gzip archive.
#
$TAR_BIN --create --gzip --file $PROJECT_NAME-$1.tar.gz \
	$PROJECT_DIR
#
#
#
echo "INFO:  All done!"
