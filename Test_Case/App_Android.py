# coding=utf-8
'''
    Class - App_Android
    
    @author: Tony Chang
'''
import unittest
import os
from appium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import time
from bs4 import BeautifulSoup

class App_Android(unittest.TestCase):
    #-------------------------- Setting for the environment --------------------------#
    def setUp(self):
        desired_caps = {
                        'platformName': 'Android',
                        'platformVersion': '10',
                        'deviceName': 'SM-N9750',
                        'appPackage': 'com.nhiApp.v1',
                        'appActivity': 'com.nhiApp.v1.ui.LaunchScreenActivity',
                        'app': os.path.abspath('./App/NHI.apk'),
                        'noReset': True,
                        'unicodeKeyboard': True,
#                         'resetKeyboard': True,
                        'chromedriverExecutableDir': os.path.abspath(os.getcwd())
                        }
        
        # Connect to Appium
        self.driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', desired_caps)
        self.wait = WebDriverWait(self.driver, 10, 0.5)



    def test_Case1(self):
        '''確認按鈕「口罩地圖」已加載於頁面DOM中且可見。'''
        print('【Case #1】')
        print('> Case description: 確認按鈕「口罩地圖」已加載於頁面DOM中且可見。')
        print('  Expected results: 手機畫面中，可見App首頁帶有按鈕「口罩地圖」。')
        # Checking the button "Mask Map" is present on the DOM of the page and visible.
        self.wait.until(EC.visibility_of_element_located((By.ID, 'com.nhiApp.v1:id/btnMask')))
        time.sleep(2)
              
        now = time.localtime(time.time())
        now_Date = time.strftime('%Y_%m_%d', now)
        now_DateTime = time.strftime('%Y_%m_%d %H_%M_%S', now)
        screenshot = './App_Test_Report/Images/{}/{}.png'.format(now_Date, now_DateTime)
              
        print('\n> Screenshot:', screenshot)
        self.driver.get_screenshot_as_file(screenshot)
            
            
            
    def test_Case2(self):
        '''點擊按鈕「口罩地圖」，並跳轉至WebView「口罩供需資訊平台」。'''
        print('【Case #2】')
        print('> Case description: 點擊按鈕「口罩地圖」，並跳轉至WebView「口罩供需資訊平台」。')
        print('  Expected results: 手機畫面中，可見瀏覽器呈現頁面「口罩供需資訊平台」。')
        # Click button "Mask Map" => Transfer to the "Information Platform of Mask Supply and Demand"
        self.wait.until(EC.element_to_be_clickable((By.ID, 'com.nhiApp.v1:id/btnMask')))
        self.driver.find_element_by_id('com.nhiApp.v1:id/btnMask').click()
        time.sleep(2)
                    
        # Switch to WebView
        contexts = self.driver.contexts
        print('\n> Contexts:', contexts)
        self.driver.switch_to.context(contexts[1])
                    
        now = time.localtime(time.time())
        now_Date = time.strftime('%Y_%m_%d', now)
        now_DateTime = time.strftime('%Y_%m_%d %H_%M_%S', now)
        screenshot = './App_Test_Report/Images/{}/{}.png'.format(now_Date, now_DateTime)
              
        print('\n> Screenshot:', screenshot)
        self.driver.get_screenshot_as_file(screenshot)
            
        # Assertion        
        print('  Title:', self.driver.title)
        self.assertEqual('口罩供需資訊平台', self.driver.title)
           
        self.driver.switch_to.context(contexts[0])    
                  
          
          
    def test_Case3(self):
        '''在WebView「口罩供需資訊平台」中下滑，並連結至應用界面「口罩即時查」，顯示方圓5公里以內的口罩供應商。'''
        print('【Case #3】')
        print('> Case description: 在WebView「口罩供需資訊平台」中下滑，並連結至應用界面「口罩即時查」，顯示方圓5公里以內的口罩供應商。')
        print('  Expected results: 手機畫面中，可見瀏覽器呈現頁面「口罩即時查」，並顯示方圓5公里以內的口罩供應商。')
        # Click button "Mask Map" => Transfer to the "Information Platform of Mask Supply and Demand"
        self.wait.until(EC.element_to_be_clickable((By.ID, 'com.nhiApp.v1:id/btnMask')))
        self.driver.find_element_by_id('com.nhiApp.v1:id/btnMask').click()
        time.sleep(2)
                    
        # Scroll down => Switch to WebView => Click 「口罩即時查」
        contexts = self.driver.contexts
        print('\n> Contexts:', contexts)                   
        
        self.driver.switch_to.context(contexts[0]) 
        window = self.driver.get_window_size()
        x = window['width']
        self.driver.swipe(x*1/2, 480, x*1/2, 0, 500)
        
        self.driver.switch_to.context(contexts[1])
         
        self.wait.until(EC.element_to_be_clickable((By.XPATH, '/html/body/div[2]/div/div/div[2]/div[1]/a/picture/img')))
        self.driver.find_element_by_xpath('/html/body/div[2]/div/div/div[2]/div[1]/a/picture/img').click()
        time.sleep(2)
                   
        # Switch to Interface 「口罩即時查」
        self.driver.switch_to_window(self.driver.window_handles[-1])
        print('\n> Current Url:', self.driver.current_url)
              
        self.wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="mask"]/article/section[5]/div/div/div[2]')))
        self.driver.find_element_by_xpath('//*[@id="mask"]/article/section[5]/div/div/div[2]').click()
        time.sleep(1)
                    
        self.wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="mask"]/article/section[5]/div/span')))
        self.driver.find_element_by_xpath('//*[@id="mask"]/article/section[5]/div/span').click()
        time.sleep(1)
           
        now = time.localtime(time.time())
        now_Date = time.strftime('%Y_%m_%d', now)
        now_DateTime = time.strftime('%Y_%m_%d %H_%M_%S', now)
        screenshot = './App_Test_Report/Images/{}/{}.png'.format(now_Date, now_DateTime)
              
        print('\n> Screenshot:', screenshot)
        self.driver.get_screenshot_as_file(screenshot)
         
        # Assertion        
        print('  Title:', self.driver.title)
        self.assertEqual('口罩即時查', self.driver.title)
     
        self.driver.switch_to.context(contexts[0]) 
        window = self.driver.get_window_size()
        x = window['width']
        y = window['height']
        for i in range(3):
            self.driver.swipe(x*1/2, y*3/4, x*1/2, y*2/4, 500)
            time.sleep(1)
         
        self.driver.switch_to.context(contexts[1])
        results = {}
        soup = BeautifulSoup(self.driver.page_source, 'html.parser')
        divs = soup.find_all('div', class_='name')
            
        if len(divs) > 0:
            for div in divs:
                name_Store = div.find_all('span')[0].text
                distance_Store = div.find_all('span')[1].text
                operation_Store = div.find_all('span')[2].text
                results.update({name_Store: '{}({})'.format(distance_Store, operation_Store)})
                    
            print('  Query Results:', results)
            for k, v in results.items():
                distance = float(v.split(' km')[0])
                self.assertTrue(distance <= 5)
             
        else:
            results.update({'Suppliers': soup.find_all('section')[2].find_all('p')[0].text})
                  
            print('  Query Results:', results)
            for k, v in results.items():
                self.assertEqual('No Result', v)
                 
        self.driver.switch_to.context(contexts[0])    
           
                 
     
    def test_Case4(self):
        '''在應用界面「口罩即時查」中搜尋口罩供應商(搜尋不含空白格)。'''
        print('【Case #4】')
        print('> Case description: 在應用界面「口罩即時查」中搜尋口罩供應商(搜尋不含空白格)。')
        print('  Expected results: 手機畫面中，可見應用界面「口罩即時查」呈現符合搜尋條件之口罩供應商。')
        # Click button "Mask Map" => Transfer to the "Information Platform of Mask Supply and Demand"
        self.wait.until(EC.element_to_be_clickable((By.ID, 'com.nhiApp.v1:id/btnMask')))
        self.driver.find_element_by_id('com.nhiApp.v1:id/btnMask').click()
        time.sleep(2)
                    
        # Scroll down => Switch to WebView => Click 「口罩即時查」
        contexts = self.driver.contexts
        print('\n> Contexts:', contexts)                   
        
        self.driver.switch_to.context(contexts[0]) 
        window = self.driver.get_window_size()
        x = window['width']
        self.driver.swipe(x*1/2, 480, x*1/2, 0, 500)
        
        self.driver.switch_to.context(contexts[1])
         
        self.wait.until(EC.element_to_be_clickable((By.XPATH, '/html/body/div[2]/div/div/div[2]/div[1]/a/picture/img')))
        self.driver.find_element_by_xpath('/html/body/div[2]/div/div/div[2]/div[1]/a/picture/img').click()
        time.sleep(2)
                   
        # Switch to Interface 「口罩即時查」
        self.driver.switch_to_window(self.driver.window_handles[-1])
        print('\n> Current Url:', self.driver.current_url)
              
        self.wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="mask"]/article/section[5]/div/div/div[2]')))
        self.driver.find_element_by_xpath('//*[@id="mask"]/article/section[5]/div/div/div[2]').click()
        time.sleep(1)
                    
        self.wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="mask"]/article/section[5]/div/span')))
        self.driver.find_element_by_xpath('//*[@id="mask"]/article/section[5]/div/span').click()
        time.sleep(1)
              
        # Query "Name of Pharmacy" => Return info of "the Pharmacy"
        query_Keyword = '博'
        query_Keyword_L = [query_Keyword]
        self.wait.until(EC.visibility_of_element_located((By.XPATH, '//*[@id="mask"]/article/section[1]/div[1]/input')))
        query_Store = self.driver.find_element_by_xpath('//*[@id="mask"]/article/section[1]/div[1]/input')
        query_Store.send_keys(query_Keyword)
        time.sleep(2)
            
        self.driver.keyevent(111)
            
        now = time.localtime(time.time())
        now_Date = time.strftime('%Y_%m_%d', now)
        now_DateTime = time.strftime('%Y_%m_%d %H_%M_%S', now)
        screenshot = './App_Test_Report/Images/{}/{}.png'.format(now_Date, now_DateTime)
              
        print('\n> Screenshot:', screenshot)
        self.driver.get_screenshot_as_file(screenshot)
            
        # Assertion  
        results = []
        soup = BeautifulSoup(self.driver.page_source, 'html.parser')
        divs = soup.find_all('div', class_='name')
            
        if len(divs) > 0:
            for div in divs:
                name_Store = div.find_all('span')[0].text
                results.append(name_Store)
                      
            print('  Query Keyword:', query_Keyword_L)
            print('  Query Results:', results)
            for result in results:
                self.assertIn(query_Keyword, result)
              
        else:
            results.append(soup.find_all('section')[2].find_all('p')[0].text)
                  
            print('  Query Keyword:', query_Keyword_L)
            print('  Query Results:', results)
            for result in results:
                    self.assertNotIn(query_Keyword, result)
                          
        self.driver.switch_to.context(contexts[0])    
                
               
   
    def test_Case5(self):
        '''在應用界面「口罩即時查」中搜尋口罩供應商(搜尋誤夾帶空白格)。'''
        print('【Case #5】')
        print('> Case description: 在應用界面「口罩即時查」中搜尋口罩供應商(搜尋誤夾帶空白格)。')
        print('  Expected results: 手機畫面中，可見應用界面「口罩即時查」呈現搜尋結果「No Result」。')
        # Click button "Mask Map" => Transfer to the "Information Platform of Mask Supply and Demand"
        self.wait.until(EC.element_to_be_clickable((By.ID, 'com.nhiApp.v1:id/btnMask')))
        self.driver.find_element_by_id('com.nhiApp.v1:id/btnMask').click()
        time.sleep(2)
                    
        # Scroll down => Switch to WebView => Click 「口罩即時查」
        contexts = self.driver.contexts
        print('\n> Contexts:', contexts)                   
        
        self.driver.switch_to.context(contexts[0]) 
        window = self.driver.get_window_size()
        x = window['width']
        self.driver.swipe(x*1/2, 480, x*1/2, 0, 500)
        
        self.driver.switch_to.context(contexts[1])
         
        self.wait.until(EC.element_to_be_clickable((By.XPATH, '/html/body/div[2]/div/div/div[2]/div[1]/a/picture/img')))
        self.driver.find_element_by_xpath('/html/body/div[2]/div/div/div[2]/div[1]/a/picture/img').click()
        time.sleep(2)
                   
        # Switch to Interface 「口罩即時查」
        self.driver.switch_to_window(self.driver.window_handles[-1])
        print('\n> Current Url:', self.driver.current_url)
              
        self.wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="mask"]/article/section[5]/div/div/div[2]')))
        self.driver.find_element_by_xpath('//*[@id="mask"]/article/section[5]/div/div/div[2]').click()
        time.sleep(1)
                    
        self.wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="mask"]/article/section[5]/div/span')))
        self.driver.find_element_by_xpath('//*[@id="mask"]/article/section[5]/div/span').click()
        time.sleep(1)
              
        # Query "Name of Pharmacy" => Return info of "the Pharmacy"
        query_Keyword = '博 '
        query_Keyword_L = [query_Keyword]
        self.wait.until(EC.visibility_of_element_located((By.XPATH, '//*[@id="mask"]/article/section[1]/div[1]/input')))
        query_Store = self.driver.find_element_by_xpath('//*[@id="mask"]/article/section[1]/div[1]/input')
        query_Store.send_keys(query_Keyword)
        time.sleep(2)
            
        self.driver.keyevent(111)
            
        now = time.localtime(time.time())
        now_Date = time.strftime('%Y_%m_%d', now)
        now_DateTime = time.strftime('%Y_%m_%d %H_%M_%S', now)
        screenshot = './App_Test_Report/Images/{}/{}.png'.format(now_Date, now_DateTime)
              
        print('\n> Screenshot:', screenshot)
        self.driver.get_screenshot_as_file(screenshot)
            
        # Assertion  
        results = []
        soup = BeautifulSoup(self.driver.page_source, 'html.parser')
        divs = soup.find_all('div', class_='name')
            
        if len(divs) > 0:
            for div in divs:
                name_Store = div.find_all('span')[0].text
                results.append(name_Store)
                      
            print('  Query Keyword:', query_Keyword_L)
            print('  Query Results:', results)
            for result in results:
                self.assertIn(query_Keyword, result)
              
        else:
            results.append(soup.find_all('section')[2].find_all('p')[0].text)
                  
            print('  Query Keyword:', query_Keyword_L)
            print('  Query Results:', results)
            for result in results:
                    self.assertNotIn(query_Keyword, result)
                          
        self.driver.switch_to.context(contexts[0]) 
        
        
                    
    def tearDown(self):
        self.driver.quit()
        
        
        