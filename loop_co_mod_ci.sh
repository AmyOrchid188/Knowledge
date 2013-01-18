#!/bin/bash
#cleartool path
CLEARTOOL=/usr/atria/bin/cleartool
#cleartool setview 
#$CLEARTOOL setview krugle_integ_view
#$CLEARTOOL mkact check_cmd
#set the root foler where you want to do many times checkout and check in
#STATDIR=/xn-test/vobtags/vob_1/src/code
#STATDIR=/junhui/vobs/krugle_demo/all_k4_collection/k4_collection_second
STATDIR=/junhui/vobs/krugle_demo/all_k4_collection/k4_collection_second/cerner

#the text uou want to add to files
ADDTEXT='Apache Enterprise Social Messaging=========++++ //junhui_add 25 lines delete 15ines'

#ADDTEXT='package net.krugle.hubtools.similarity.algorithm;+++++++++===888888888 //ning'
#replaced text
REPLACED_TEXT='this line is replaced by shell script'
#the times you want to check out and check in
CO_CI_TIMES=200
# update lines times
REPLCE_Time=5
# start replace line number
START_REP=1
#loop to check out and check in 
for (( COUNTER=1; COUNTER<=$CO_CI_TIMES; COUNTER++))
  do
	echo $COUNTER
#recursively check out
  #/usr/atria/bin/cleartool find $STATDIR -version 'version(/main/LATEST)' -exec 'cleartool co -nc $CLEARCASE_PN'

  $CLEARTOOL find $STATDIR -version 'version(/main/LATEST)' -exec 'cleartool co -nc $CLEARCASE_PN'
# recursively add text to files
 find $STATDIR -type f -exec sed -i "1,19 a$ADDTEXT " {} \;
#recursively delete lines 
  find $STATDIR -type f -exec sed -i '20,29d' {} \;
#recursively insert text to top line and last line

#: << 'recursively comment '
#     for ((n=$START_REP; n<=$REPLCE_Time; n++))
#      do
#        find $STATDIR -type f -exec sed -i "$n c$REPLACED_TEXT" {} \;
#      done

#recursively check in
  #/usr/atria/bin/cleartool find $STATDIR -version 'version(/main/LATEST)' -exec 'cleartool ci -nc $CLEARCASE_PN'
  $CLEARTOOL find $STATDIR -version 'version(/main/LATEST)' -exec 'cleartool ci -ide -nc $CLEARCASE_PN'


done
 

