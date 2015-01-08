from selenium import selenium
from BESPEEDTEST import get_url_from_excel
import unittest, time, re
import xlwt
from fractions import Fraction

class be_auto_python(unittest.TestCase):
    def setUp(self):
        self.verificationErrors = []
        #self.selenium = selenium("localhost", 4444, "*googlechrome c:\\Program Files\(x86\)\\Google\\Chrome\\Application\\chrome.exe", "http://tools.pingdom.com/fpt")
        self.selenium = selenium("localhost", 4444, "*googlechrome C:\\Program Files (x86)\\Google\\Chrome\\Application\chrome.exe", "http://tools.pingdom.com/fpt")
        self.selenium.start()
    
    def test_be_auto_python(self):
        # Open pingdom website
        sel = self.selenium
        sel.set_timeout(10000000000)
        sel.open("/")
        for i in range(180):
            try:
                if sel.is_element_present("id=Settings"): break
            except: pass
            time.sleep(180)
        else: self.fail("time out")
        #sel.click("//*[@id='settingsBox']/form/div[2]/label[2]/text()")
        sel.click("//*[@id='settingsBox']/form/div[3]/label/")
        #//*[@id="settingsBox"]/form/div[2]/label/text()

        for i in range(180):
            try:
                if sel.is_element_present("id=urlinput"): break
            except: pass
            time.sleep(20)
        else: self.fail("time out")
        # Get url from BESPEEDTEST.PY 
        URLlist = get_url_from_excel()      
##        Gradelist = []
##        Requestslist = []
##        Loadtimelist = []
##        Pagesizelist = []
        Grade_avg = 0
        Requests_avg = 0
        Loadtime_avg = 0
        Pagesize_avg = 0
        Gradelist_avg = []
        Requestslist_avg = []
        Loadtimelist_avg = []
        Pagesizelist_avg = []
        # Test each url by pingdom
        try:
            for url in URLlist:
                Gradelist = []
                Requestslist = []
                Loadtimelist = []
                Pagesizelist = []
                
                for k in range(0,5):
                    time.sleep(60)
                    if not sel.is_element_present("id=urlinput"):
                        time.sleep(120)
                    sel.type("id=urlinput", url)
                    print url
                    if not sel.is_element_present("//*[@id='settingsBox']/form/div[3]/label"):
                        time.sleep(60)
                        
                    sel.click("//*[@id='settingsBox']/form/div[3]/label/")
                    #//*[@id="settingsBox"]/form/div[3]/label/text()
                    sel.click("css=button.large.TestButt")
                    # Wait grade, requests, pagesize, loadtime display
                    time.sleep(60)
                    
                    try: self.failUnless(sel.is_element_present("//div[@id='feedbackMessage']/h4"))
                    except AssertionError, e: self.verificationErrors.append(str(e))
                    
                    status = sel.get_text("//div[@id='feedbackMessage']/h4/text()")
                    status_1 = sel.is_element_present("//*[@id='sumright']")
                    print status
                    if status == "Unable to connect to test server" or status == "An error occured" or status_1 == False:
                        # If there is error, will refresh and re-type the url
                        sel.refresh()
                        time.sleep(60)
                        sel.type("id=urlinput", url)
                        sel.click("css=button.large.TestButt")
                        time.sleep(180)
                    try: self.failUnless(sel.is_element_present("css=dl.last > dt"))  #grade
                    except AssertionError, e: self.verificationErrors.append(str(e))
                    #try: self.failUnless(sel.is_element_present("//div[@id='rt_sumright']/dl[3]/dt")) #request
                    try: self.failUnless(sel.is_element_present("//div[@id='rt_sumright']/dl[3]/dd"))
                    except AssertionError, e: self.verificationErrors.append(str(e))
                    try: self.failUnless(sel.is_element_present("//div[@id='rt_sumright']/dl[2]/dd"))  #loadtime
                    except AssertionError, e: self.verificationErrors.append(str(e))
                    #try: self.failUnless(sel.is_element_present("css=#rt_sumright > dl.first > dt"))    #pagesize
                    try: self.failUnless(sel.is_element_present("css=#rt_sumright > dl.first > dd"))
                    except AssertionError, e: self.verificationErrors.append(str(e))
                    
                    # Get grade, loadtime, requests, pagesize value
                    time.sleep(30)
                    grade = sel.get_text("css=dl.last > dd")
                    print grade
                    result = grade.find('?')
                    if result != -1:
                        sel.click("css=button.large.TestButt")
                        time.sleep(120)
                    grade = sel.get_text("css=dl.last > dd")
                    print grade
                    if grade.find('?') != -1:
                        time.sleep(120)
                    if grade.find('?') != -1:
                        Gradelist.append('fail')
                        break
                    try: grade=Fraction(grade)
                    except AssertionError, e: self.verificationErrors.append(str(e))
                        
                    Gradelist.append(grade)   
                             
                    requests = sel.get_text("//div[@id='rt_sumright']/dl[3]/dd")
                    print requests
                    Requestslist.append(requests)
                    
                    loadtime = sel.get_text("//div[@id='rt_sumright']/dl[2]/dd")
                    print loadtime
                    print loadtime[:-1]
                    Loadtimelist.append(loadtime[:-1])
                    
                    pagesize = sel.get_text("css=#rt_sumright > dl.first > dd")
                    print pagesize
                    print pagesize[:-2]
                    Pagesizelist.append(pagesize[:-2])
                # get grade average
                Gradelist_1 = map(str, Gradelist)
                res=[x for x in Gradelist_1 if 'fail' in x]
                print "res is %s " % res
                if  not res: #no contains fail
                    Gradelist=map(float,Gradelist)
                    print "float Gradelist is %s" % Gradelist
                    Grade_avg=reduce(lambda x,y:x+y,Gradelist) / len(Gradelist)
                    print "Grade_avg is %s" % Grade_avg
                    Gradelist_avg.append(Grade_avg)                
                    #get request average
                    Requestslist = map(float,Requestslist)
                    Requests_avg=reduce(lambda x,y:x+y,Requestslist) / len(Requestslist)
                    print "Requests_avg is %s" % Requests_avg
                    Requestslist_avg.append(Requests_avg)
                    #get loadtime average
                    Loadtimelist = map(float,Loadtimelist)
                    Loadtime_avg=reduce(lambda x,y:x+y,Loadtimelist) / len(Loadtimelist)
                    print "Loadtime_avg is %s" % Loadtime_avg
                    Loadtimelist_avg.append(Loadtime_avg)
                    #get pagesize average (unit is MB)
                    Pagesizelist = map(float,Pagesizelist)
                    Pagesize_avg=reduce(lambda x,y:x+y,Pagesizelist) / len(Pagesizelist)
                    print "Pagesize_avg is %s" % Pagesize_avg
                    Pagesizelist_avg.append(Pagesize_avg)
                else:
                    Gradelist_avg.append('fail')
                    Requestslist_avg.append('fail')
                    Loadtimelist_avg.append('fail')
                    Pagesizelist_avg.append('fail')         
        finally:
            print "finally ************"
            print Gradelist_avg
            print Requestslist_avg
            print Loadtimelist_avg
            print Pagesizelist_avg
##            print Gradelist
##            print Requestslist
##            print Loadtimelist
##            print Pagesizelist
            print "==================="
            #png = self.capture_entire_page_screenshot('D:\\be\\pingdomtest\\screenshot.png')
            
            print Gradelist_avg
            print Requestslist_avg
            print Loadtimelist_avg
            print Pagesizelist_avg
            # Put the result to excel
            file = xlwt.Workbook()
            table = file.add_sheet('result')
            table.write(0,0,'URL')
            table.write(0,1,'Load time(s)')
            table.write(0,2,'Page size(MB)')
            table.write(0,3,'Requests')
            table.write(0,4,'Perf. Grade')
            rownum = len(Loadtimelist_avg)
            rownum1 = rownum+1
            for i in range(1,rownum1):
                table.write(i,0,URLlist[i-1])
                table.write(i,1,Loadtimelist_avg[i-1])        
                table.write(i,2,Pagesizelist_avg[i-1])
                table.write(i,3,Requestslist_avg[i-1])   
                table.write(i,4,Gradelist_avg[i-1])
                #table.write(i,4,Gradelist[i-1])
            file.save('D:\\be\\pingdomtest\\result.xls')
     

    def tearDown(self):
        self.selenium.stop()
        self.assertEqual([], self.verificationErrors)
        


if __name__ == "__main__":
    unittest.main()
