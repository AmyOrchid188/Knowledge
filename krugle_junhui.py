#!/usr/bin/env python
import os
import time
from time import strftime
import csv
import sys
import unittest
import re
from pyvirtualdisplay import Display
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait


error_counter = 0
error_projects = []
cycle_staus = -1
starttime = None
endtime = None
print "before run test, starttime is %s , endtime is %s" % (starttime, endtime)
display = Display(visible=0, size=(1024,768))
class ParametrizedTestCase(unittest.TestCase):
    """ TestCase classes that want to be parametrized should
        inherit from this class.
    """
    def __init__(self, methodName='runTest', param=None):
        super(ParametrizedTestCase, self).__init__(methodName)
        self.param = param

    @staticmethod
    def parametrize(testcase_class, param=None):
        """ Creat a suite containing all tests taken from the given
            subclass, passing them the parameter 'param'.
        """
        testloader = unittest.TestLoader()
        testnames = testloader.getTestCaseNames(testcase_class)
        suite = unittest.TestSuite()
        for name in testnames:
            suite.addTest(testcase_class(name, param=param))
        return suite
class krugle_update(ParametrizedTestCase):
    def setUp(self):
        #display = Display(visible=0, size=(1024,768))
        display.start()
        self.driver = webdriver.Firefox()
        self.driver.maximize_window()
        #status_ok = "background-image:url('/gfx/step_OK_active.gif');"
    def isEveryOneFinish(self):

        elem_projecs_2 = WebDriverWait(self.driver, 10).until(lambda driver : driver.find_element_by_link_text("Projects"))
        elem_projecs_2.click()
        time.sleep(5)

#        myprojects = {"1": "fbug",
#                      "2": "casacore",
#                      "3": "google-web-toolkit",
#                      "4": "flylinkdc", "5": "miranda",
#                       "6": "native_client", "7": "xe-core",
#                      "8": "geogebra",
#                      "9": "openmobster",
#                      "10": "tortoisesvn",
#                      "11": "cacheless_false_test","12": "cacheless_true_test",
#                      "13": "cacheless_false_test1","14": "cacheless_true_test1"}
#
        myprojects = {"1": "Project1",
                      "2": "Project2",
                      "3": "Project3",
                      "4": "Project4",
                      "5": "Project5",
                      "6": "Project6",
                      "7": "Project7",
                      "8": "Project8",
                      "9": "Project9",
                      "10": "Project10"}
        #for loop  check every project finish
        #table_projects = WebDriverWait(self.driver,15).until(lamdba my_driver : my_driver.find_element_by_xpath('//*[@id="projectListing"]/table[2]/tbody/tr[2]/td/table/tbody/tr[3]/td/table/tbody'))
        table_projects = self.driver.find_element_by_xpath('//*[@id="projectListing"]/table[2]/tbody/tr[2]/td/table/tbody/tr[3]/td/table/tbody')
        proj_step_ok='/gfx/OK.gif'
        proj_step_error='gfx/ERROR.gif'
        finish_counter=0
        global error_counter
        global error_projects
        error_projects=[]
        error_counter=0
        print "====================================================="
        for num in range(1,11):
            print "num is " + str(num)
            try:
               link = table_projects.find_element_by_link_text(myprojects[str(num)])
               href = link.get_attribute('href')
            except:
               try:
                   print "1 catche every one expcetion"
                   table_projects = self.driver.find_element_by_xpath('//*[@id="projectListing"]/table[2]/tbody/tr[2]/td/table/tbody/tr[3]/td/table/tbody')
                   link = table_projects.find_element_by_link_text(myprojects[str(num)])
                   href = link.get_attribute('href')
               except:
                   print "2 catche every one expcetion"
                   table_projects = self.driver.find_element_by_xpath('//*[@id="projectListing"]/table[2]/tbody/tr[2]/td/table/tbody/tr[3]/td/table/tbody')
                   link = table_projects.find_element_by_link_text(myprojects[str(num)])
                   href = link.get_attribute('href')
            projects_id = href.split('=')[1]
            print "project id is "+ projects_id
            xpath_table_icon = "statusContent_" + projects_id
            print "xpth table icon is "+ xpath_table_icon
            #every_proj_status = self.driver.find_element_by_id(xpath_table_icon)
            try:
               print "1.catch imag exception"
               every_proj_status = WebDriverWait(self.driver,20).until(lambda driver_1 : driver_1.find_element_by_id(xpath_table_icon))
               per_proj_status = every_proj_status.find_element_by_tag_name('img')
               str_status = per_proj_status.get_attribute('src')
            except:
               try:
                  print "2.catch imag exception"
                  every_proj_status = WebDriverWait(self.driver,20).until(lambda driver_1 : driver_1.find_element_by_id(xpath_table_icon))
                  per_proj_status = every_proj_status.find_element_by_tag_name('img')
                  str_status = per_proj_status.get_attribute('src')
               except:
                    try:
                        print "3.catch imag exception"
                        every_proj_status = WebDriverWait(self.driver,20).until(lambda driver_1 : driver_1.find_element_by_id(xpath_table_icon))
                        per_proj_status = every_proj_status.find_element_by_tag_name('img')
                        str_status = per_proj_status.get_attribute('src')
                    except:
                        every_proj_status = WebDriverWait(self.driver,20).until(lambda driver_1 : driver_1.find_element_by_id(xpath_table_icon))
                        per_proj_status = every_proj_status.find_element_by_tag_name('img')
                        str_status = per_proj_status.get_attribute('src')

            print "str_status is "+ str(str_status)
            is_finish = re.search(proj_step_ok,str(str_status))
            is_error = re.search(proj_step_error,str(str_status))
            if is_finish :
                finish_counter = finish_counter + 1
            elif is_error:
                error_counter = error_counter + 1
                print "error project is %s" % myprojects[str(num)]
                error_projects.append(myprojects[str(num)])
        sum=finish_counter + error_counter
        f = open('./log/error_projects.log','w')
        f.write("In cycle "+ self.param + "\n".join(error_projects))
        f.close()
        return sum
    def isPresent(self):
        time.sleep(60)
        elem_projects_1 = self.driver.find_element_by_link_text("Projects")
        elem_projects_1 = WebDriverWait(self.driver, 20).until(lambda driver : driver.find_element_by_link_text("Projects"))
        elem_projects_1.click()
        time.sleep(10)
        self.assertIn(u"Projects", self.driver.title)
        #print self.driver.find_element_by_xpath('//*[@id="snap"]/div/div[5]')
        try:
            snap_finish = WebDriverWait(self.driver, 20).until(lambda d : d.find_elements_by_class_name('processingstep'))
            snap_png=snap_finish[3].get_attribute("style")
        except:
            print '1.catch the snap_finish error, and try again'
            try:
                snap_finish = WebDriverWait(self.driver, 20).until(lambda d : d.find_elements_by_class_name('processingstep'))
                snap_png=snap_finish[3].get_attribute("style")
                pass
            except:
                print '2. catch the snap_finish error, and try again'

                snap_finish = WebDriverWait(self.driver, 20).until(lambda d : d.find_elements_by_class_name('processingstep'))
                snap_png=snap_finish[3].get_attribute("style")
                pass

        print "snap_png is %s " % snap_png
        finish_flag = re.search("step_ok_active", snap_png, re.IGNORECASE)
        print "finish_flag is  %s " % snap_finish
        error_flag = re.search("step_error_active", snap_png, re.IGNORECASE)
        #print "erro_flag is "+ not bool(error_flag)
        if bool(error_flag):
            return False
        else:
            if bool(finish_flag):
                return True
    def test_login_update(self):
        driver = self.driver
        driver.implicitly_wait(60)
        driver.set_script_timeout(60)
        #driver.get("http://192.168.100.191:8080")
        driver.get("http://192.168.100.192:8080")
        self.assertIn("Krugle", driver.title)
        elem_username = driver.find_element_by_name("j_username")
        elem_password = driver.find_element_by_name("j_password")
        elem_username.send_keys("admin")
        elem_password.send_keys("123456")
        elem_signin = driver.find_element_by_class_name("button")
        elem_signin.click()
        self.assertIn("Status", driver.title)
        #click projects link
        elem_projects = driver.find_element_by_link_text("Projects")
        elem_projects.click()
        self.assertIn(u"Projects", driver.title)
        #note the start time
        global starttime
        starttime = strftime('%Y-%m-%d %H:%M:%S',time.gmtime())
        #strftime("%a, %d %b %Y %H:%M:%S +0000", gmtime())

        #check "select all" checkbox after this  click update button
        WebDriverWait(driver, 10).until(lambda driver : driver.title.lower().startswith("krugle"))
        elem_chk_all = driver.find_element_by_name("cbx_all")
        elem_chk_all.click()
        elem_update = driver.find_elements_by_class_name("smallButton")[0]
        elem_update.click()
        #check every project is finish
        time.sleep(5)
        finish_everyone = self.isEveryOneFinish()
        while finish_everyone != 10:
            time.sleep(60)
            finish_everyone = self.isEveryOneFinish()
        running = True
#        f = open('/home/huangkun/i44test/junhui/automated_script/log/cycle_' + self.param + '.log','w')
        global endtime
        #check the top process if finish
        while  running :
             time.sleep(60)
             flag = self.isPresent()
             print 'flag is', flag
             if flag :
                 endtime = strftime('%Y-%m-%d %H:%M:%S',time.gmtime())
                 time.sleep(10)
#                 msg= self.param+"="+str(flag)
#                 f.write(msg)
#                 f.close()
                 screenshot_name ="./screenshot/" + self.param + "_cycle.png"
                 driver.save_screenshot(screenshot_name)
                 break

             if flag == False:
#                 msg = self.param + "=" +"Error"
#                 f.write(msg)
#                 f.close()
                 break
                 print "---------flag is false------"
                 #if flag is None  go on loop

        #check if there is some project failed
       # global starttime, endtime
        print "starttime is %s, endtime is %s" % (starttime, endtime)
        with open('./log/cycle_data.csv','ar+') as cvsfile:
                spamwriter = csv.writer(cvsfile,delimiter=',',
                                        quotechar='|', quoting=csv.QUOTE_MINIMAL)
                if error_counter != 0:
                    spamwriter.writerow([self.param, starttime,endtime,'error',error_projects])
                else:
                    spamwriter.writerow([self.param, starttime,endtime])
        if error_counter !=0:
            mail_subject='mail -s "cycle '+str(self.param)+' failed some projects" liujunhui@cn-acg.com < ./log/error_projects.log'
            #os.system('mail -s "failed projects" liujunhui@cn-acg.com < ./log/error_projects.log')
            os.system(mail_subject)
        if flag == True:
            mail_subject='mail -s "cycle '+ str(self.param)+' complete successfully" liujunhui@cn-acg.com <./log/cycle_data.csv'
        else:
            mail_subject='mail -s "cycle ' + str(self.param) + ' complete failed" liujunhui@cn-acg.com < ./log/cycle_data.csv'

            #os.system('mail -s "failed projects" liujunhui@cn-acg.com < ./log/error_projects.log')
        os.system(mail_subject)
        if error_counter !=0:
            raise RuntimeError("some projects were failed in this cycle %s, failed projects is %s" % (self.param,error_projects))
    def tearDown(self):
        #display.stop()
        self.driver.close()
        display.stop()


if __name__ == "__main__":
    suite =unittest.TestSuite()
    suite.addTest(ParametrizedTestCase.parametrize(krugle_update,param=sys.argv[1]))
    print sys.argv[1]
    unittest.TextTestRunner(verbosity=2).run(suite)
