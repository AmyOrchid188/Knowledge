#!/bin/bash

if [ $# -eq 1 ]

then

    reqNum=$1
else

    echo "Usage: ./curlKSX.sh [ReqNumber]"

    exit -1

fi

#origin_response=`curl -X POST http://192.168.100.120:8082/login?username=admin&userpass=aragon&serverUri=192.168.100.169:9080/ram/`
origin_response=`curl -X POST "http://192.168.100.120:8082/login?username=rtcadmin&userpass=123456&serverURI=http://192.168.100.169:9080/ram/"`
#echo $origin_response

#my_token=`echo $origin_response|cut -d: -f 3|cut -d, -f 1`
#my_token=${origin_response##*'"'}
my_token=${origin_response#*'"result":'}
#my_token=${my_token##*'"'}
#echo $my_token
my_token=${my_token/\"/}
my_token=${my_token/\"/}
my_token=${my_token/\}/}
my_token=${my_token%%','*}
#echo $my_token

#ksx_url=http://192.168.100.120:8082/download?filepath=Krugle_KSX/200MB_Files/first_folder/second_folder/third_folder/fouth_folder/fifth_folder/${c}.tar.gz&cpmsid=${c}_cpmsid&callbackur=http%3A%2F%2Flocalhost%3A8082%2Freq&authtoken=${my_token}
for ((c=1;c<=$reqNum;c++))
do
    j=1
    echo "========================================================================================================="
    echo "Requested $c times for 27 files"
   # make the url has the different cpmsid
   
   #for   ((j=1;j<=27;j++))
   # do
    ksx_url_1="http://192.168.100.120:8082/download?artifactURI=http://192.168.100.169:9080/ram/artifact/11A5B4FF-F721-9A13-13A6-A5AEEFC67101/1.0/own_test_data/PKG_Files/P_Number/031813-EEG-E2013-SP10.tar.Z&cpmsid=${c}_$((j++))_cpmsid&callbackURI=http://192.168.100.120:8082/test/req&token=${my_token}"
    echo "Get the file $ksx_url_1"
   ksx_url_2="http://192.168.100.120:8082/download?artifactURI=http://192.168.100.169:9080/ram/artifact/11A5B4FF-F721-9A13-13A6-A5AEEFC67101/1.0/own_test_data/PKG_Files/P_Number/031813-EEG-E2013-SP16.zip&cpmsid=${c}_$((j++))_cpmsid&callbackURI=http://192.168.100.120:8082/test/req&token=${my_token}"
   ksx_url_3="http://192.168.100.120:8082/download?artifactURI=http://192.168.100.169:9080/ram/artifact/11A5B4FF-F721-9A13-13A6-A5AEEFC67101/1.0/own_test_data/PKG_Files/P_Number/031813-EEG-E2013-SP17.tar.Z&cpmsid=${c}_$((j++))_cpmsid&callbackURI=http://192.168.100.120:8082/test/req&token=${my_token}"
    ksx_url_4="http://192.168.100.120:8082/download?artifactURI=http://192.168.100.169:9080/ram/artifact/11A5B4FF-F721-9A13-13A6-A5AEEFC67101/1.0/own_test_data/PKG_Files/P_Number/031813-EEG-E2013-SP18.tar.Z&cpmsid=${c}_$((j++))_cpmsid&callbackURI=http://192.168.100.120:8082/test/req&token=${my_token}"
   ksx_url_5="http://192.168.100.120:8082/download?artifactURI=http://192.168.100.169:9080/ram/artifact/11A5B4FF-F721-9A13-13A6-A5AEEFC67101/1.0/own_test_data/PKG_Files/P_Number/031813-EEG-E2013-SP19.tar.Z&cpmsid=${c}_$((j++))_cpmsid&callbackURI=http://192.168.100.120:8082/test/req&token=${my_token}"
   ksx_url_6="http://192.168.100.120:8082/download?artifactURI=http://192.168.100.169:9080/ram/artifact/11A5B4FF-F721-9A13-13A6-A5AEEFC67101/1.0/own_test_data/PKG_Files/P_Number/031813-EEG-E2013-SP20.tar.Z&cpmsid=${c}_$((j++))_cpmsid&callbackURI=http://192.168.100.120:8082/test/req&token=${my_token}"
   ksx_url_7="http://192.168.100.120:8082/download?artifactURI=http://192.168.100.169:9080/ram/artifact/11A5B4FF-F721-9A13-13A6-A5AEEFC67101/1.0/own_test_data/PKG_Files/P_Number/031813-EEG-E2013-SP14.tar.gz&cpmsid=${c}_$((j++))_cpmsid&callbackURI=http://192.168.100.120:8082/test/req&token=${my_token}"
   ksx_url_8="http://192.168.100.120:8082/download?artifactURI=http://192.168.100.169:9080/ram/artifact/11A5B4FF-F721-9A13-13A6-A5AEEFC67101/1.0/own_test_data/PKG_Files/P_Number/031813-EEG-E2013-SP15.tar.bz2&cpmsid=${c}_$((j++))_cpmsid&callbackURI=http://192.168.100.120:8082/test/req&token=${my_token}"
   ksx_url_9="http://192.168.100.120:8082/download?artifactURI=http://192.168.100.169:9080/ram/artifact/11A5B4FF-F721-9A13-13A6-A5AEEFC67101/1.0/own_test_data/PKG_Files/P_Number/031813-EEG-E2013-SP13.tar&cpmsid=${c}_$((j++))_cpmsid&callbackURI=http://192.168.100.120:8082/test/req&token=${my_token}"
   ksx_url_10="http://192.168.100.120:8082/download?artifactURI=http://192.168.100.169:9080/ram/artifact/11A5B4FF-F721-9A13-13A6-A5AEEFC67101/1.0/own_test_data/Package_Type/062912-KP_NATL_HOC_COE-EPIC2010_IU6-ClientPack-1.tar&cpmsid=${c}_$((j++))_cpmsid&callbackURI=http://192.168.100.120:8082/test/req&token=${my_token}"
   ksx_url_11="http://192.168.100.120:8082/download?artifactURI=http://192.168.100.169:9080/ram/artifact/913101F5-18A2-B536-C924-80D0276A12D3/1.0/23T/062012-KP_SCALIFORNIA-EPIC2010_IU4-ClientPack-23T-test.zip&cpmsid=${c}_$((j++))_cpmsid&callbackURI=http://192.168.100.120:8082/test/req&token=${my_token}"
  # ksx_url_12="http://192.168.100.120:8082/download?artifactURI=http://192.168.100.169:9080/ram/artifact/11A5B4FF-F721-9A13-13A6-A5AEEFC67101/1.0/own_test_data/Package_Type/062912-KP_NATL_HOC_COE-EPIC2010_IU6-ClientPack-1.7z&cpmsid=${c}_$((j++))_cpmsid&callbackURI=http://192.168.100.120:8082/test/req&token=${my_token}"
   ksx_url_12="http://192.168.100.120:8082/download?artifactURI=http://192.168.100.169:9080/ram/artifact/11A5B4FF-F721-9A13-13A6-A5AEEFC67101/1.0/own_test_data/Package_Type/062912-KP_NATL_HOC_COE-EPIC2010_IU6-ClientPack-1.tar.bz2&cpmsid=${c}_$((j++))_cpmsid&callbackURI=http://192.168.100.120:8082/test/req&token=${my_token}"
   ksx_url_13="http://192.168.100.120:8082/download?artifactURI=http://192.168.100.169:9080/ram/artifact/11A5B4FF-F721-9A13-13A6-A5AEEFC67101/1.0/own_test_data/Package_Type/062912-KP_NATL_HOC_COE-EPIC2010_IU6-ClientPack-1.tar.gz&cpmsid=${c}_$((j++))_cpmsid&callbackURI=http://192.168.100.120:8082/test/req&token=${my_token}"
   ksx_url_14="http://192.168.100.120:8082/download?artifactURI=http://192.168.100.169:9080/ram/artifact/11A5B4FF-F721-9A13-13A6-A5AEEFC67101/1.0/KSX_Customer_Files/HC_C00000_CodeRepository/Epic/Client%20Packs/CO/032712-KP_COLORADO-SUM09_IU7-ClientPack-10.zip&cpmsid=${c}_$((j++))_cpmsid&callbackURI=http://192.168.100.120:8082/test/req&token=${my_token}"
   ksx_url_15="http://192.168.100.120:8082/download?artifactURI=http://192.168.100.169:9080/ram/artifact/11A5B4FF-F721-9A13-13A6-A5AEEFC67101/1.0/KSX_Customer_Files/HC_C00000_CodeRepository/Epic/Client%20Packs/CO/081712-KP_COLORADO-EPIC2010_IU7-ClientPack-1.zip&cpmsid=${c}_$((j++))_cpmsid&callbackURI=http://192.168.100.120:8082/test/req&token=${my_token}"
   ksx_url_16="http://192.168.100.120:8082/download?artifactURI=http://192.168.100.169:9080/ram/artifact/11A5B4FF-F721-9A13-13A6-A5AEEFC67101/1.0/KSX_Customer_Files/HC_C00000_CodeRepository/Epic/Client%20Packs/GA/011112-KP_GEORGIA-SUM09_IU4-ClientPack-22.zip&cpmsid=${c}_$((j++))_cpmsid&callbackURI=http://192.168.100.120:8082/test/req&token=${my_token}"
   ksx_url_17="http://192.168.100.120:8082/download?artifactURI=http://192.168.100.169:9080/ram/artifact/11A5B4FF-F721-9A13-13A6-A5AEEFC67101/1.0/KSX_Customer_Files/HC_C00000_CodeRepository/Epic/Client%20Packs/GA/020712-KP_GEORGIA-SUM09_IU4-ClientPack-23.zip&cpmsid=${c}_$((j++))_cpmsid&callbackURI=http://192.168.100.120:8082/test/req&token=${my_token}"
    ksx_url_18="http://192.168.100.120:8082/download?artifactURI=http://192.168.100.169:9080/ram/artifact/11A5B4FF-F721-9A13-13A6-A5AEEFC67101/1.0/KSX_Customer_Files/HC_C00000_CodeRepository/Epic/Client%20Packs/GA/042712-KP_GEORGIA-SUM09_IU4-ClientPack-24.zip&cpmsid=${c}_$((j++))_cpmsid&callbackURI=http://192.168.100.120:8082/test/req&token=${my_token}"
    ksx_url_19="http://192.168.100.120:8082/download?artifactURI=http://192.168.100.169:9080/ram/artifact/11A5B4FF-F721-9A13-13A6-A5AEEFC67101/1.0/KSX_Customer_Files/HC_C00000_CodeRepository/Epic/Client%20Packs/SCAL/061312-KP_SCALIFORNIA-EPIC2010_IU4-ClientPack-21T.tar.gz&cpmsid=${c}_$((j++))_cpmsid&callbackURI=http://192.168.100.120:8082/test/req&token=${my_token}"
    ksx_url_20="http://192.168.100.120:8082/download?artifactURI=http://192.168.100.169:9080/ram/artifact/11A5B4FF-F721-9A13-13A6-A5AEEFC67101/1.0/KSX_Customer_Files/HC_C00000_CodeRepository/Epic/Client%20Packs/SCAL/061312-KP_SCALIFORNIA-EPIC2010_IU4-ClientPack-21T-Contents.zip&cpmsid=${c}_$((j++))_cpmsid&callbackURI=http://192.168.100.120:8082/test/req&token=${my_token}"
    ksx_url_21="http://192.168.100.120:8082/download?artifactURI=http://192.168.100.169:9080/ram/artifact/11A5B4FF-F721-9A13-13A6-A5AEEFC67101/1.0/KSX_Customer_Files/HC_C00000_CodeRepository/Epic/Client%20Packs/SCAL/062012-KP_SCALIFORNIA-EPIC2010_IU4-ClientPack-23T.tar.gz&cpmsid=${c}_$((j++))_cpmsid&callbackURI=http://192.168.100.120:8082/test/req&token=${my_token}"
    ksx_url_22="http://192.168.100.120:8082/download?artifactURI=http://192.168.100.169:9080/ram/artifact/11A5B4FF-F721-9A13-13A6-A5AEEFC67101/1.0/KSX_Customer_Files/HC_C00000_CodeRepository/Epic/Client%20Packs/SCAL/062012-KP_SCALIFORNIA-EPIC2010_IU4-ClientPack-23T-Contents.zip&cpmsid=${c}_$((j++))_cpmsid&callbackURI=http://192.168.100.120:8082/test/req&token=${my_token}"
    ksx_url_23="http://192.168.100.120:8082/download?artifactURI=http://192.168.100.169:9080/ram/artifact/11A5B4FF-F721-9A13-13A6-A5AEEFC67101/1.0/KSX_Customer_Files/HC_C00000_CodeRepository/Epic/Client%20Packs/SCAL/120806-Krugle-Test-ClientPack-1.tar.gz&cpmsid=${c}_$((j++))_cpmsid&callbackURI=http://192.168.100.120:8082/test/req&token=${my_token}"
    ksx_url_24="http://192.168.100.120:8082/download?artifactURI=http://192.168.100.169:9080/ram/artifact/11A5B4FF-F721-9A13-13A6-A5AEEFC67101/1.0/customer_data/090612-KP_SCALIFORNIA-EPIC2010_IU4-ClientPack-35.tar.gz&cpmsid=${c}_$((j++))_cpmsid&callbackURI=http://192.168.100.120:8082/test/req&token=${my_token}"
    ksx_url_25="http://192.168.100.120:8082/download?artifactURI=http://192.168.100.169:9080/ram/artifact/11A5B4FF-F721-9A13-13A6-A5AEEFC67101/1.0/customer_data/Sample_PKG_Files/031813-EEG-E2010-SP14.tar.Z&cpmsid=${c}_$((j++))_cpmsid&callbackURI=http://192.168.100.120:8082/test/req&token=${my_token}"
    ksx_url_26="http://192.168.100.120:8082/download?artifactURI=http://192.168.100.169:9080/ram/artifact/11A5B4FF-F721-9A13-13A6-A5AEEFC67101/1.0/customer_data/Sample_PKG_Files/031813-EEG-E2012-SP14.tar.Z&cpmsid=${c}_$((j++))_cpmsid&callbackURI=http://192.168.100.120:8082/test/req&token=${my_token}"
    ksx_url_27="http://192.168.100.120:8082/download?artifactURI=http://192.168.100.169:9080/ram/artifact/913101F5-18A2-B536-C924-80D0276A12D3/1.0/061312-KP_SCALIFORNIA-EPIC2010_IU4-ClientPack-21T-test.zip&cpmsid=${c}_$((j++))_cpmsid&callbackURI=http://192.168.100.120:8082/test/req&token=${my_token}"
# done
   # curl the urls
    for ((k=1;k<=27;k++))
    do
       eval "curl -X GET \$ksx_url_$k"
       eval "echo Get the file [ \$ksx_url_$k ]"
    done
done
#usage example
#./curlKSX.sh "http://localhost:8082/download?filepath=KSX+Test%2F120806-Krugle-Test-ClientPack-1.tar.gz&cpmsid=cpmsid&callbackurl=http%3A%2F%2Flocalhost%3A8082%2Freq&authtoken=A8EQjXU0AT0luUS3BXTn1354602083188" 1000
