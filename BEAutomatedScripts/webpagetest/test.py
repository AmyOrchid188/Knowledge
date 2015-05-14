from selenium import selenium
from BESPEEDTEST import get_url_from_excel
import unittest, time, re
import xlwt


class be_auto_python(unittest.TestCase):
    def setUp(self):
        self.verificationErrors = []
        self.selenium = selenium("localhost", 4444, "*googlechrome c:\\Program Files\\Google\\Chrome\\Application\\chrome.exe", "http://www.webpagetest.org")
        self.selenium.start()
    
    def test_be_auto_python(self):
        # Open pingdom website
        sel = self.selenium
        sel.set_timeout(1000000)
        sel.open("/")

        for i in range(600):
            try:
                if sel.is_element_present("id=location"): break
            except: pass
            time.sleep(20)
        else: self.fail("time out")
        sel.select("id=location", "label=New York, NY USA (IE 11,Chrome,Firefox)")
        sel.select("id=browser", "label=Chrome")
        # Get url from BESPEEDTEST.PY 
        URLlist = get_url_from_excel()      
        FirstLoadTimeList = []
        RepeatLoadTimeList = []
        FirstByteTimeList = []
        KeepAliveEnabledList = []
        CompressTransferList = []
        CompressImagesList = []
        ProgressiveJPEGsList = []
        CacheStaticContentList = []
        EffectiveUseofCDNList = []
        msFirstPaintList = []
        domContentLoadedList = []
        
        # Test each url by pingdom
        try:
            for url in URLlist:
                sel.type("id=url", url)
                print url
                sel.click("name=submit")
                time.sleep(30)        
                try: self.assertEqual("Testing...", sel.get_text("css=h3"))
                except AssertionError, e: self.verificationErrors.append(str(e))
                for i in range(600):
                    try:
                        if "Web Page Performance Test" in sel.get_text("css=h2.alternate.cufon-dincond_regular"): break
                    except: pass
                    time.sleep(1)
                else: self.fail("time out")
                GetResultStatus = sel.get_text("//table[@id='table1']/tbody/tr[2]/td")
 
                if "Timed Out" in GetResultStatus:
                    sel.click("css=input[value='Re-run the test']")
                    time.sleep(30)        
                    try: self.assertEqual("Testing...", sel.get_text("css=h3"))
                    except AssertionError, e: self.verificationErrors.append(str(e))
                    for i in range(600):
                        try:
                            if "Web Page Performance Test" in sel.get_text("css=h2.alternate.cufon-dincond_regular"): break
                        except: pass
                        time.sleep(1)
                    else: self.fail("time out")         
    ##            try: self.assertEqual("Repeat View", sel.get_text("css=td.even"))
    ##            except AssertionError, e: self.verificationErrors.append(str(e))
    ##            try: self.assertEqual("First View", sel.get_text("css=td"))
    ##            except AssertionError, e: self.verificationErrors.append(str(e))

                # Get loadtime value
                time.sleep(30)           
                FirstLoadTime = sel.get_text("id=fvLoadTime")
                print FirstLoadTime
                FirstLoadTimeList.append(FirstLoadTime)
                
                RepeatLoadTime = sel.get_text("id=rvLoadTime")
                print RepeatLoadTime
                RepeatLoadTimeList.append(RepeatLoadTime)

                FirstByteTime = sel.get_text("css=li.first_byte_time > a > h2")
                print FirstByteTime
                FirstByteTimeList.append(FirstByteTime)
                
                KeepAliveEnabled = sel.get_text("css=li.keep_alive_enabled > a > h2")
                print KeepAliveEnabled
                KeepAliveEnabledList.append(KeepAliveEnabled)
                
                CompressTransfer = sel.get_text("css=li.compress_text > a > h2")
                print CompressTransfer
                CompressTransferList.append(CompressTransfer)

                CompressImages = sel.get_text("css=li.compress_images > a > h2")
                print CompressImages
                CompressImagesList.append(CompressImages)
                
##                ProgressiveJPEGs = sel.get_text("css=li.progressive_jpeg > a > h2")
##                print ProgressiveJPEGs
##                ProgressiveJPEGsList.append(ProgressiveJPEGs)
                
                CacheStaticContent = sel.get_text("css=li.cache_static_content > a > h2")
                print CacheStaticContent
                CacheStaticContentList.append(CacheStaticContent)
                
                EffectiveUseofCDN = sel.get_text("css=li.use_of_cdn > a > h2")
                print EffectiveUseofCDN
                EffectiveUseofCDNList.append(EffectiveUseofCDN)
                
                sel.click("link=Details")
##                sel.wait_for_page_to_load("30000")
##                
##                self.assertEqual("msFirstPaint", sel.get_text("css=#tableW3CTiming > tbody > tr > th"))
                for i in range(600):
                    try:
                        if sel.is_element_present("css=#tableW3CTiming > tbody > tr > th"): break
                    except: pass
                    time.sleep(1)
                else: self.fail("time out")
                
                msFirstPaint = sel.get_text("css=#tableW3CTiming > tbody > tr:nth-child(2) > td:nth-child(1)")
                print msFirstPaint
                msFirstPaintList.append(msFirstPaint)

                domContentLoaded = sel.get_text("css=#tableW3CTiming > tbody > tr:nth-child(2) > td:nth-child(2)")
                print domContentLoaded
                domContentLoadedList.append(domContentLoaded)
                
                # Go Back to Home

                sel.click("link=Home")
                for i in range(600):
                    try:
                        if sel.is_element_present("id=location"): break
                    except: pass
                    time.sleep(20)
                else: self.fail("time out")
                        
        finally: 
            # Put the list value back to excel
            print FirstLoadTimeList
            print RepeatLoadTimeList

            # Put the result to excel
            file = xlwt.Workbook()
            table = file.add_sheet('result')
            table.write(0,0,'URL')
            table.write(0,1,'FirstLoadtime')
            table.write(0,2,'RepeatLoadTime')
            table.write(0,3,'FirstByteTime')
            table.write(0,4,'KeepAliveEnabled')
            table.write(0,5,'CompressTransfer')
            table.write(0,6,'CompressImages')
           # table.write(0,7,'ProgressiveJPEGs')
            table.write(0,8,'CacheStaticContent')
            table.write(0,9,'EffectiveUseofCDN')
            table.write(0,10,'msFirstPaint')
            table.write(0,11,'domContentLoaded')            
            rownum = len(FirstLoadTimeList)
            rownum1 = rownum+1
            for i in range(1,rownum1):
                table.write(i,0,URLlist[i-1])
                table.write(i,1,FirstLoadTimeList[i-1])        
                table.write(i,2,RepeatLoadTimeList[i-1])
                table.write(i,3,FirstByteTimeList[i-1])
                table.write(i,4,KeepAliveEnabledList[i-1])
                table.write(i,5,CompressTransferList[i-1])
                table.write(i,6,CompressImagesList[i-1])
               # table.write(i,7,ProgressiveJPEGsList[i-1])
                table.write(i,8,CacheStaticContentList[i-1])
                table.write(i,9,EffectiveUseofCDNList[i-1])
                table.write(i,10,msFirstPaintList[i-1])
                table.write(i,11,domContentLoadedList[i-1])  
            
            file.save('D:\\be\\webpagetest\\result.xls')
         

    def tearDown(self):
        self.selenium.stop()
        self.assertEqual([], self.verificationErrors)
        


if __name__ == "__main__":
    unittest.main()
