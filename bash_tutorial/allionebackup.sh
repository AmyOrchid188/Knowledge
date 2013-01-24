#!/bin/bash
# A shell script to backup mysql, webserver and files to tape
# allionebackup.sh version 2.0
# ----------------------------------------------------------------
# Convert all passed arguments to lowercase using
# tr command and here strings

#opt=$( tr '[:upper:]' '[:lower:]'<<< "$1" )



opt=$1
#################################################################
# Use regex to match all command line arguments                 #
# [Tt][Aa][Rr] matches "Tar", "tar", "tAr", "TaR" etc           #
# [Ss][Qq][Ll] matches "sql", "SQL", "Sql","Sql" ect            #
#################################################################

case $opt in
    [Ss][Qq][Ll])
        echo "Running mysql backup using mysqldump tool...."
          ;;
    [Ss][Yy][Nn][Cc])
        echo "Running backup using rsync tool..."
        ;;
    [Tt][Aa][Rr])
        echo "Running tape backup using tar tool......"
        ;;
    *)
        echo "Bacup shell script utility"
        echo "Usage: $0 {sql|sync|tar}"
        echo "           sql: Run mysql backup utility"
        echo "           sync: Run webserver backup utility."
        echo "           tar: Run tape backup utility."
        ;;
esac
