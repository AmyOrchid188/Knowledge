from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
import unittest, time, re 

class AutoWriteTimeForOrangePythonWebdriver(unittest.TestCase):
        def setUp(self):
            self.driver = webdriver.Firefox()
            self.driver.implicitly_wait(30)
            self.base_url = "https://hrm.aragoncs.com/"
            self.verificationErrors = []
            self.accept_next_alert = True
             
        def test_auto_write_time_for_orange_python_webdriver(self):
            driver = self.driver
            driver.get(self.base_url + "/login.php")
            driver.find_element_by_name("txtUserName").clear()
            driver.find_element_by_name("txtUserName").send_keys(UserName)
            driver.find_element_by_name("txtPassword").send_keys(Password)
            driver.find_element_by_name("Submit").click()
            driver.find_element_by_link_text("Time").click()
            driver.find_element_by_link_text("Timesheets").click()          
            driver.find_element_by_id("btnEdit").click()
            row_count=driver.findElement(By.tagName("tr")).size()
            print row_count        
            
        def tearDown(self):
            self.driver.quit()
            self.assertEqual([], self.verificationErrors)

if __name__ == "__main__":
    unittest.main()
