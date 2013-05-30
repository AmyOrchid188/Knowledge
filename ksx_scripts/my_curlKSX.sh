#!/bin/bash

if [ $# -eq 1 ]

then

    reqNum=$1
else

    echo "Usage: ./curlKSX.sh [ReqNumber]"
    echo "Everytime request 2002 files, one file case insentive, one file none exist, the others should be successful"

    exit -1
    
fi

origin_response=`curl -X POST http://192.168.100.120:8082/login?username=Administrator\&password=Administrator\&starteamserver=192.168.100.120:49201`
echo $origin_response

my_token=${origin_response##*':'}
my_token=${my_token/\"/}
my_token=${my_token/\"/}
my_token=${my_token/\}/}

echo ${my_token}

#ksx_url=http://192.168.100.120:8082/download?filepath=Krugle_KSX/200MB_Files/first_folder/second_folder/third_folder/fouth_folder/fifth_folder/${c}.tar.gz&cpmsid=${c}_cpmsid&callbackur=http%3A%2F%2Flocalhost%3A8082%2Freq&authtoken=${my_token}


    
    ksx_url_3="http://192.168.100.120:8082/download?filepath=Krugle_KSX/200MB_Files/tree_1_200MB_1.zip&cpmsid=${c}_2_3_cpmsid&callbackurl=http%3A%2F%2Flocalhost%3A8082%2Freq&authtoken=${my_token}"
    ksx_url_1w_files="http://192.168.100.120:8082/download?filepath=Krugle_KSX/200MB_Files/first_folder/krugle_hui.zip&cpmsid=${c}_4_cpmsid&callbackurl=http%3A%2F%2Flocalhost%3A8082%2Freq&authtoken=${my_token}"
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
   
  case_insentive_1="http://192.168.100.120:8082/download?filepath=Krugle_KSX/200MB_Files/first_folder/second_folder/TREE_3_200MB.tar.gz&cpmsid=${c}_case_insentive_cpmsid&callbackurl=http%3A%2F%2Flocalhost%3A8082%2Freq&authtoken=${my_token}"

  none_exist_1="http://192.168.100.120:8082/download?filepath=Krugle_KSX/200MB_Files/first_folder/second_folder/treabe_200MB.tar.gz&cpmsid=${c}_none_exist_cpmsid&callbackurl=http%3A%2F%2Flocalhost%3A8082%2Freq&authtoken=${my_token}"

#for ((c=1;c<=$reqNum;c++))
#do
#    echo "Requested $c times"
#    for ((j=1;j<=100;j++)) 
#       do
 #        echo "Requested ${j}.tar.gz"
   
         ksx_url_1="http://192.168.100.120:8082/download?filepath=Krugle_KSX/200MB_Files/first_folder/second_folder/fourth_folder/fifth_folder/${j}.tar.gz&cpmsid=${c}_1_cpmsid&callbackurl=http%3A%2F%2Flocalhost%3A8082%2Freq&authtoken=${my_token}"
         ksx_url_2="http://192.168.100.120:8082/download?filepath=Krugle_KSX/200MB_Files/first_folder/Krugle%20ksx/${j}.tar.gz&cpmsid=${c}_2_cpmsid&callbackurl=http%3A%2F%2Flocalhost%3A8082%2Freq&authtoken=${my_token}"
#         curl -X POST $ksx_url_1
#         curl -X POST $ksx_url_2
#      done
#for ((i=1;i<=10;i++))
#do
#    for ((k=3;k<=20;k++))
#      do
#       echo "ksx_url_$k"  
#       eval "echo \$ksx_url_$k"
#       eval "curl -X POST \$ksx_url_$k"
#     done
# done
 
# echo "case_insentive_1 it should response successful"
#  curl -X POST $case_insentive_1
#  echo "none_exit_1 it should response failed"
#  curl -X POST $none_exist_1
#  echo "request 1w files"
#  curl -X POST $ksx_url_1w_files
#done
ksx_url_embed_three="http://192.168.100.120:8082/download?filepath=Krugle_test/200MB_Files/embed_files/4_folder.zip&cpmsid=113_three_cpmsid&callbackurl=http%3A%2F%2Flocalhost%3A8082%2Freq&authtoken=${my_token}"
ksx_url_embed_five="http://192.168.100.120:8082/download?filepath=Krugle_test/200MB_Files/embed_files/5_folder.zip&cpmsid=113_five_cpmsid&callbackurl=http%3A%2F%2Flocalhost%3A8082%2Freq&authtoken=${my_token}"
ksx_url_embed_sec_five="http://192.168.100.120:8082/download?filepath=Krugle_test/200MB_Files/embed_files/sec_5_folder.zip&cpmsid=113_sec_five_cpmsid&callbackurl=http%3A%2F%2Flocalhost%3A8082%2Freq&authtoken=${my_token}"
curl -X POST $ksx_url_embed_three
curl -X POST $ksx_url_embed_five
curl -X POST $ksx_url_embed_sec_five

#usage example
#./curlKSX.sh "http://localhost:8082/download?filepath=KSX+Test%2F120806-Krugle-Test-ClientPack-1.tar.gz&cpmsid=cpmsid&callbackurl=http%3A%2F%2Flocalhost%3A8082%2Freq&authtoken=A8EQjXU0AT0luUS3BXTn1354602083188" 1000
