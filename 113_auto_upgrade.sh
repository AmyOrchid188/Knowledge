#!/bin/bash
echo "This script is to upgrade this server [ $HOSTNAME ]"
echo "Step1, Check up if there is others ssh connection, kick others ssh"
declare -a other_ips
i=0
localhost_ip=`ifconfig  | grep 'inet addr:'| grep -v '127.0.0.1' | cut -d: -f2 | awk '{ print $1}'`
echo $localhost_ip
my_own_ip=$1
my_email=$2
: ${my_own_ip:="192.168.100.250"}
: ${my_email:="liujunhui@cn-acg.com"}

who|while read LINE
do
cho "-------------------------------"
echo $LINE
ips=$(echo $LINE |awk '{ print $5 }')
item=$(echo $LINE | awk '{ print $2}' )
echo $item
ip2=${ips#"("}
ip2=${ip2%")"}
echo  "string after cuting" $ip2
if [ $ip2 != $my_own_ip ]
then
     echo $i
    other_ips[$i]=$item
    echo ${other_ips[$i]}
    pid=`ps aux|grep ${other_ips[$i]}|grep sshd|awk '{ print $2 }'`
     echo $pid
     kill -9 $pid
     if [ $? -eq 0 ]
     then
        echo "killed process $pid successfully"
     fi
    ((i++))
fi 
done
echo "all ips "  ${other_ips[@]}
if [ ${#ssh_conn_ips[@]} -ne 1 ]
then
   echo "Kick other ssh connections"
    
fi
# If there is tmuxs, kill tmux
tmux ls
if [ $? -eq 0 ]; then
tmux ls|awk '{print $1}'|while read t_name
do
tmux kill-session -t $t_name
if [ $? -eq 0 ];then
echo "kill session " $t_name "successfully."
fi
done
fi

echo "Step2, Stop all krugle service."
 #~/stop-krugle-service.sh
service monit stop
service kse stop
service hub stop
service nginx stop
service api stop
service memcached stop
service disk-monitor stop

ps aux|grep krugle|grep -v "hbase"|grep -v "hadoop"|grep -v "grep"| while read proc 
do
echo "Processes are lived after stop service" 
echo $proc
process_id=$(echo $proc | awk '{print $2}')
echo "process id"
echo $process_id
kill -9 $process_id
if [ $? -eq 0 ]
then
   echo "killed $process_id successfully"
else
   echo "killed $process_id failed, try again"
   kill -9 $process_id
   if [ $? -ne 0 ]
   then 
       echo "Try again to stop $process_id failed."
   fi
fi
done
echo "Step3, Mount upgrade server(131)'s /kb to local."
if [ -z $1 ]
then
   echo "upgrade krugle sever with latest version"
  if [ ! "$(ls -A /kb)" ]
  then
     echo "/kb not mounted, mounting it."
     mount 192.168.100.131:/kb /kb
     if [ "$(ls -A /kb)" ]
     then
      echo "mounting successfully."
     fi
  fi

myfiles=`ls /kb  -lt |grep zip |head -n 1|awk '{print $9}'`
  echo "The latest upgrade package is " $myfiles
  
else #use $1 version
myfiles=`ls /kb |grep $1|awk '{print $9}' `
fi
version="${myfiles%.*}"
echo $version
echo "Step4, Unzip the upgrade package to /tmp/upgrade_krugle/upgrade_package"
unzip /kb/$myfiles -d /tmp/upgrade_krugle/$version/
# echo "Step5, dump mysql user_data"
# timestamp=`date "+%Y%m%dt%H%M%S"`
# mysqldump user_data>~/krugle_user_data_backup/user-data-backup$timestamp.dump
# mysql user_data<~/drop-saved-search-tables.sql
echo "Step5, Go to /tmp/upgrade_krugle/upgrade_package to do upgrade"
# mail -s "$localhost_ip krugle server upgrade successfully" liujunhui@cn-acg.com </tmp/upgrade_krugle/$version/upgrade.out
/tmp/upgrade_krugle/$version/upgrade.sh
flag=0
tail -f /tmp/upgrade_krugle/$version/upgrade.out &
while [ $flag == 0 ]
do
succ=`grep "Ending stage3" /tmp/upgrade_krugle/$version/upgrade.out`
failed=`grep "FATAL ERROR" /tmp/upgrade_krugle/$version/upgrade.out`

if [ -n "$succ" ];
then
mail -s "$localhost_ip krugle server upgrade successfully" $my_email </tmp/upgrade_krugle/$version/upgrade.out
flag=1
fi
if [ -n "$failed" ];
then
mail -s "$localhost_ip krugle server upgrade failed" $my_email </tmp/upgrade_krugle/$version/upgrade.out
break
fi
done
tail_pid=`ps aux|grep tail|grep -v grep|awk '{print $2}'`
kill -9 $tail_pid
#timestamp2=`date "+%Y%m%dt%H%M%S"`
#
#mysqldump user_data>~/krugle_user_data_backup/after-upgrade-user-data-backup$timestamp2.dump
#mysql user_data<~/krugle_user_data_backup/user-data-backup$timestamp.dump
