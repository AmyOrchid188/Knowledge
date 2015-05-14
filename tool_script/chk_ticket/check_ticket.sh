#!/bin/bash
# Author: Junhui Liu <liujunhui08@gmail.com>
# Created Time: 12/11/14 10:24:37 (CST)
# Modified Time: 12/18/14 17:20:29 (CST)

# Read tickets no from set_tickets.properties file

declare -a in_qa_tickets
current_path=`pwd`
FILE=$current_path'/''set_tickets.properties'
echo $FILE
user_name=`grep user_name $FILE`
user_password=`grep user_password $FILE`
trac_url=`grep trac_url $FILE`
user_name=${user_name#'user_name='}
user_password=${user_password#'user_password='}
trac_url=${trac_url#'trac_url='}
echo $user_name, $user_password,$trac_url

#IFS=","
declare -a tickets_array
if [ ! -s $FILE ]
then
    echo "set_tickets.properties file doesn't exist in current folder."
    exit 3
fi

# tickets
tickets=`cat ./set_tickets.properties|grep 'tickets='`
tickets=${tickets#'tickets='}
echo "tickets for checking is:"
tickets_array=(`echo $tickets | tr "," " "`)

#echo $tickets
for (( i=0; i<${#tickets_array[@]}; i++));
do
    echo ${tickets_array[i]}
done


# notification email

notify_email=`cat ./set_tickets.properties |grep my_email`
notify_email=${notify_email#'my_email='}
echo "notification email address is: " $notify_email


# Check these tickets' status, if some one tickets is In-QA status, send notification email
for (( j=0; j<${#tickets_array[@]}; j++));
do
   # curl --user $user_name:$user_password  $url${tickets_array[j]}
   ticket_url=$trac_url${tickets_array[j]}
   status=`curl -k --user $user_name:$user_password $trac_url${tickets_array[j]}|grep "be_status=In-QA"`
   # if status is in-qa, add this ticket to send notification email list
   if [ -n "$status" ];
   then
       echo "#${tickets_array[j]}'s status is in qa"
       in_qa_tickets[${#in_qa_tickets[*]}]=${tickets_array[j]}
   fi
#    curl  -k --user $user_name:$user_password $ticket_url

done

echo $in_qa_tickets>results
mail -s 'tickets is in qa' $notify_email </junhui/Knowledge/tool_script/chk_ticket/results
