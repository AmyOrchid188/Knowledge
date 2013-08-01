#!/bin/bash
# This script is to sync the remote svn repository to localhost
# usage set array items for localhost svn repository name, every sync will
# sync
# author Junhui Liu
# Date 2012-12-15
array=( test_first test_sec )

for item in ${array[*]}
do
   echo $item
   temp=`svn info svn://localhost/$item |grep "Revision"`
   head_revision=${temp##*':'}
   increased_revision=3
   end_revision=`expr $head_revision + $increased_revision`
   flag=0
   pflag=0
 svnsync sync file:///home/svn/$item > sync.log &
  while [ $flag == 0 ]
    do
        #temp_revision_no=`tail -n 100 -f /junhui/scripts/sync.log|grep "Copied properties for revision $1\." `
        temp_revision_no=`grep "Copied properties for revision $end_revision\."  ./sync.log `
#        echo "grep results"
#       echo $temp_revision_no
        if [ -n "$temp_revision_no" ]; then

            temp_revision_no_1=${temp_revision_no##*'revision '}
            echo $temp_revision_no_1
            temp_revision_no_2=${temp_revision_no_1%\.*}
            echo $temp_revision_no_2
            flag=1
           # while [ $pflag == 0 ]
            #  do
               # sync_id=`pidof "svnsync sync file:///home/svn/$item"`
                killall "svnsync"

             #   pflag=`ps aux|grep "svnsync" |grep -v "grep" `
              #  echo "pflag value"
               # echo $pflag
             # done
            break
        fi

    done
done
