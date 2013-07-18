#!/bin/bash
# this script is to add  local host folders to svn repository
# $1 is username $2 is password $3 is comments $4 is source folder $5 is remote svn repostory
# author Junhui Liu
# Date 2012-12-15
if [ $# -lt 5 ]; then
    echo 'parameters are absent '
    echo 'example svn_import.sh junhui junhui "example import" ./exapmle svn://localhost/test_import'
    exit -1
else
   if [ $# -gt 5 ]; then
      echo "parameters are too many"
      exit -1
    fi

if [ $# -eq 5 ]; then

svn --username $1 --password $2 import -m "$3" $4 $5
fi
fi
