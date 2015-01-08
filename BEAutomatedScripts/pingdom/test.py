from selenium import selenium
from BESPEEDTEST import get_url_from_excel
import unittest, time, re
import xlwt


class be_auto_python(unittest.TestCase):
    def setUp(self):
        self.verificationErrors = []
        self.selenium = selenium("localhost", 4444, "*googlechrome c:\\Program Files\\Google\\Chrome\\Application\\chrome.exe", "http://tools.pingdom.com/")
        self.selenium.start()
    
    def test_be_auto_python(self):
        # Open pingdom website
        sel = self.selenium
        sel.set_timeout(1000000)
        sel.open("http://tools.pingdom.com")

        for i in range(180):
            try:
                if sel.is_element_present("id=urlinput"): break
            except: pass
            time.sleep(20)
        else: self.fail("time out")
        # Get url from BESPEEDTEST.PY 
        URLlist = get_url_from_excel()      
        Gradelist = []
        Requestslist = []
        Loadtimelist = []
        Pagesizelist = [] 
        # Test each url by pingdom     
        for url in URLlist:
            sel.type("id=urlinput", url)
            print url
            sel.click("css=button.large.TestButt")
            # Wait grade, requests, pagesize, loadtime display
            time.sleep(60)
            status = sel.get_text("//div[@id='feedbackMessage']/h4/text()")
            print status
            if status == "Unable to connect to test server" or status == "An error occured":
                # If there is error, will refresh and re-type the url
                sel.refresh()
                time.sleep(600)
                sel.type("id=urlinput", url)
                sel.click("css=button.large.TestButt")
                time.sleep(60)
            try: self.failUnless(sel.is_element_present("css=dl.last > dt"))
            except AssertionError, e: self.verificationErrors.append(str(e))
            try: self.failUnless(sel.is_element_present("//div[@id='rt_sumright']/dl[3]/dt"))
            except AssertionError, e: self.verificationErrors.append(str(e))
            try: self.failUnless(sel.is_element_present("//div[@id='rt_sumright']/dl[2]/dd"))
            except AssertionError, e: self.verificationErrors.append(str(e))
            try: self.failUnless(sel.is_element_present("css=#rt_sumright > dl.first > dt"))
            except AssertionError, e: self.verificationErrors.append(str(e))
            
            # Get grade, loadtime, requests, pagesize value
            grade = sel.get_text("css=dl.last > dd")
            print grade
            Gradelist.append(grade)   
                     
            requests = sel.get_text("//div[@id='rt_sumright']/dl[3]/dd")
            print requests
            Requestslist.append(requests)
            
            loadtime = sel.get_text("//div[@id='rt_sumright']/dl[2]/dd")
            print loadtime
            Loadtimelist.append(loadtime)
            
            pagesize = sel.get_text("css=#rt_sumright > dl.first > dd")
            print pagesize
            Pagesizelist.append(pagesize)  
            # Put the list value back to excel
        print Gradelist
        print Requestslist
        print Loadtimelist
        print Pagesizelist
        # Put the result to excel
        file = xlwt.Workbook()
        table = file.add_sheet('result')
        table.write(0,0,'URL')
        table.write(0,1,'Load time')
        table.write(0,2,'Page size')
        table.write(0,3,'Requests')
        table.write(0,4,'Perf. Grade')
        rownum = len(Loadtimelist)
        for i in range(1,rownum):
            table.write(i,0,URLlist[i])
            table.write(i,1,Loadtimelist[i])        
            table.write(i,2,Pagesizelist[i])
            table.write(i,3,Requestslist[i])   
            table.write(i,4,Gradelist[i])            
        file.save('D:\\be\\pingdomtest\\result.xls')
     

    def tearDown(self):
        self.selenium.stop()
        self.assertEqual([], self.verificationErrors)
        


if __name__ == "__main__":
    unittest.main()
