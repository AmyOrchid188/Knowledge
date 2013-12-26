import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait

class krugle_update(unittest.TestCase):
   
    def setUp(self):
        self.driver = webdriver.Firefox()
#        selenium = new WebDriverBackedSelenium(driver,url);
#       selenium.windowMaximize();
        self.driver.maximize_window()
    def test_login(self):
        driver = self.driver
        #driver.maximize_window()
        driver.get("http://192.168.100.191:8080")
        self.assertIn("Krugle", driver.title)
        elem_username = driver.find_element_by_name("j_username")
        elem_password = driver.find_element_by_name("j_password")
        elem_username.send_keys("admin")
        elem_password.send_keys("123456")
#        elem_signin = driver.find_element_by_xpath("//*[@id="login"]/table/tbody/tr[2]/td/table/tbody[3]/tr/td[2]/input")
        elem_signin = driver.find_element_by_class_name("button") 
        elem_signin.click()
        self.assertIn("Status", driver.title)
        #click projects link
        elem_projects = driver.find_element_by_link_text("Projects")
        elem_projects.click()
        self.assertIn("Projects", driver.title)
        #check "select all" checkbox
        WebDriverWait(driver, 10).until(lambda driver : driver.title.lower().startswith("krugle"))
        elem_chk_all = driver.find_element_by_name("cbx_all")
        elem_chk_all.click()
       # elem_update = driver.find_element
        elem_update = driver.find_element_by_xpath('//*[@id="projectListing"]/table[2]/tbody/tr[2]/td/table/tbody/tr[2]/td/table/tbody/tr[2]/td[1]/table/tbody/tr/td[1]/input')
        elem_update.click()
        WebDriverWait(driver, 1000000000).until(lambda driver : driver.find_element_by_xpath('//*[@id="snap"]/div/div[5]/div'))
    def tearDown(self):
        self.driver.close()

if __name__ == "__main__":
    unittest.main()        
        
