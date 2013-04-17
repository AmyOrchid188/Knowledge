#!/bin/bash

if [ $# -eq 1 ]

then

    reqNum=$1
else

    echo "Usage: ./curlKSX.sh [ReqNumber]"

    exit -1
    
fi

ksx_url_1=1
ksx_url_2=2
origin_response=`curl -X POST http://192.168.100.120:8082/login?username=Administrator\&password=Administrator\&starteamserver=192.168.100.121:49201`
echo $origin_response

my_token=${origin_response##*':'}
my_token=${my_token/\"/}
my_token=${my_token/\"/}
my_token=${my_token/\}/}

echo ${my_token}

#ksx_url=http://192.168.100.120:8082/download?filepath=Krugle_KSX/200MB_Files/first_folder/second_folder/third_folder/fouth_folder/fifth_folder/${c}.tar.gz&cpmsid=${c}_cpmsid&callbackur=http%3A%2F%2Flocalhost%3A8082%2Freq&authtoken=${my_token}

for ((c=1;c<=$reqNum;c++))
do
    echo "Requested $c times"
   for   ((j=1;j<=100;j++)) 
#    for   ((j=1;j<=1;j++)) 
     do
    #shift
    ksx_url_1="http://192.168.100.120:8082/download?filepath=Krugle_KSX/200MB_Files/first_folder/second_folder/fourth_folder/fifth_folder/${j}.tar.gz&cpmsid=${c}_1_cpmsid&callbackurl=http%3A%2F%2Flocalhost%3A8082%2Freq&authtoken=${my_token}"
    ksx_url_2="http://192.168.100.120:8082/download?filepath=Krugle_KSX/200MB_Files/first_folder/Krugle%20ksx/${j}.tar.gz&cpmsid=${c}_2_cpmsid&callbackurl=http%3A%2F%2Flocalhost%3A8082%2Freq&authtoken=${my_token}"
    
    ksx_url_3="http://192.168.100.120:8082/download?filepath=Krugle_KSX/200MB_Files/tree_1_200MB_1.zip&cpmsid=${c}_2_3_cpmsid&callbackurl=http%3A%2F%2Flocalhost%3A8082%2Freq&authtoken=${my_token}"
    ksx_url_4="http://192.168.100.120:8082/download?filepath=Krugle_KSX/200MB_Files/first_folder/tree_2_200MB.zip&cpmsid=${c}_4_cpmsid&callbackurl=http%3A%2F%2Flocalhost%3A8082%2Freq&authtoken=${my_token}"
    ksx_url_5="http://192.168.100.120:8082/download?filepath=Krugle_KSX/200MB_Files/first_folder/second_folder/tree_3_200MB.zip&cpmsid=${c}_5_cpmsid&callbackurl=http%3A%2F%2Flocalhost%3A8082%2Freq&authtoken=${my_token}"
    ksx_url_6="http://192.168.100.120:8082/download?filepath=Krugle_KSX/200MB_Files/first_folder/second_folder/fourth_folder/tree_4_200MB.zip&cpmsid=${c}_6_cpmsid&callbackurl=http%3A%2F%2Flocalhost%3A8082%2Freq&authtoken=${my_token}"
     
    ksx_url_7="http://192.168.100.120:8082/download?filepath=Krugle_KSX/200MB_Files/first_folder/second_folder/fourth_folder/fifth_folder/sixth_folder/tree_6_200MB.zip&cpmsid=${c}_7_cpmsid&callbackurl=http%3A%2F%2Flocalhost%3A8082%2Freq&authtoken=${my_token}"
    ksx_url_8="http://192.168.100.120:8082/download?filepath=Krugle_KSX/200MB_Files/first_folder/second_folder/fourth_folder/fifth_folder/sixth_foler/seventh_folder/tree_7_200MB.zip&cpmsid=${c}_8_cpmsid&callbackurl=http%3A%2F%2Flocalhost%3A8082%2Freq&authtoken=${my_token}"
    ksx_url_9="http://192.168.100.120:8082/download?filepath=Krugle_KSX/200MB_Files/first_folder/second_folder/fourth_folder/fifth_folder/sixth_foler/seventh_folder/eighth_folder/tree_8_200MB.zip&cpmsid=${c}_9_cpmsid&callbackurl=http%3A%2F%2Flocalhost%3A8082%2Freq&authtoken=${my_token}"
    ksx_url_10="http://192.168.100.120:8082/download?filepath=Krugle_KSX/200MB_Files/first_folder/second_folder/fourth_folder/fifth_folder/sixth_foler/seventh_folder/eighth_folder/ninth_folder/tree_9_200MB.zip&cpmsid=${c}_10_cpmsid&callbackurl=http%3A%2F%2Flocalhost%3A8082%2Freq&authtoken=${my_token}"
    ksx_url_11="http://192.168.100.120:8082/download?filepath=Krugle_KSX/200MB_Files/first_folder/second_folder/fourth_folder/fifth_folder/sixth_folder/seventh_folder/eighth_folder/ninth_folder/tenth_folder/tree_8_200MB.zip&cpmsid=${c}_11_cpmsid&callbackurl=http%3A%2F%2Flocalhost%3A8082%2Freq&authtoken=${my_token}"
    ksx_url_12="http://192.168.100.120:8082/download?filepath=Krugle_KSX/200MB_Files/first_folder/tree_2_200MB.tar.gz&cpmsid=${c}_12_cpmsid&callbackurl=http%3A%2F%2Flocalhost%3A8082%2Freq&authtoken=${my_token}"
    ksx_url_13="http://192.168.100.120:8082/download?filepath=Krugle_KSX/200MB_Files/first_folder/tree_2_200MB.tar.bz2&cpmsid=${c}_13_cpmsid&callbackurl=http%3A%2F%2Flocalhost%3A8082%2Freq&authtoken=${my_token}"



    ksx_url_14="http://192.168.100.120:8082/download?filepath=Krugle_KSX/200MB_Files/first_folder/second_folder/fourth_folder/fifth_folder/sixth_folder/tree_6_200MB.tar.gz&cpmsid=${c}_14_cpmsid&callbackurl=http%3A%2F%2Flocalhost%3A8082%2Freq&authtoken=${my_token}"
    ksx_url_15="http://192.168.100.120:8082/download?filepath=Krugle_KSX/200MB_Files/first_folder/second_folder/fourth_folder/fifth_folder/sixth_folder/tree_6_200MB.tar&cpmsid=${c}_15_cpmsid&callbackurl=http%3A%2F%2Flocalhost%3A8082%2Freq&authtoken=${my_token}"
    ksx_url_16="http://192.168.100.120:8082/download?filepath=Krugle_KSX/200MB_Files/first_folder/second_folder/fourth_folder/fifth_folder/sixth_folder/tree_6_200MB.tar.bz2&cpmsid=${c}_16_cpmsid&callbackurl=http%3A%2F%2Flocalhost%3A8082%2Freq&authtoken=${my_token}"
    ksx_url_17="http://192.168.100.120:8082/download?filepath=Krugle_KSX/200MB_Files/first_folder/second_folder/fourth_folder/fifth_folder/KSX-1.0.9.T1-release.zip&cpmsid=${c}_17_cpmsid&callbackurl=http%3A%2F%2Flocalhost%3A8082%2Freq&authtoken=${my_token}"
    ksx_url_18="http://192.168.100.120:8082/download?filepath=Krugle_KSX/200MB_Files/first_folder/second_folder/fourth_folder/tree_4_200MB.tar.gz&cpmsid=${c}_18_cpmsid&callbackurl=http%3A%2F%2Flocalhost%3A8082%2Freq&authtoken=${my_token}"
    ksx_url_19="http://192.168.100.120:8082/download?filepath=Krugle_KSX/200MB_Files/first_folder/second_folder/fourth_folder/tree_4_200MB.tar.bz2&cpmsid=${c}__19cpmsid&callbackurl=http%3A%2F%2Flocalhost%3A8082%2Freq&authtoken=${my_token}"
    ksx_url_20="http://192.168.100.120:8082/download?filepath=Krugle_KSX/200MB_Files/first_folder/second_folder/tree_3_200MB.tar.gz&cpmsid=${c}_20_cpmsid&callbackurl=http%3A%2F%2Flocalhost%3A8082%2Freq&authtoken=${my_token}"
    prefix=ksx_url_
     echo $ksx_url_1
     echo $ksx_url_2
     echo "Requested ${j}.tar.gz"
     for ((k=1;k<=20;k++))
    do
      
     echo $ksx_url_$k
   #curl -X POST ${ksx_url_$k}
    done
    curl -X POST $ksx_url_1
   curl -X POST $ksx_url_2
     done
done
#usage example
#./curlKSX.sh "http://localhost:8082/download?filepath=KSX+Test%2F120806-Krugle-Test-ClientPack-1.tar.gz&cpmsid=cpmsid&callbackurl=http%3A%2F%2Flocalhost%3A8082%2Freq&authtoken=A8EQjXU0AT0luUS3BXTn1354602083188" 1000
