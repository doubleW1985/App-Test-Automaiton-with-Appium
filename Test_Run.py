# coding=utf-8
'''
    App Test Automation with Appium.(Python)
    
    @author: Tony Chang
'''
import unittest
import time
import os
from HTMLTestReport import HTMLTestRunner
 
if __name__ == '__main__':
    #-------------------------- Find and return all test modules from the specified start directory --------------------------#
    tests = unittest.defaultTestLoader.discover(start_dir='./Test_Case', pattern='App*.py')



    #-------------------------- Test Report --------------------------#
    now = time.localtime(time.time())
    now_Date = time.strftime('%Y_%m_%d', now)
    now_DateTime = time.strftime('%Y_%m_%d %H_%M_%S', now)
    
    dir_AppTestReport = './App_Test_Report'
    dir_AppScreenshot = './App_Test_Report/Images/{}'.format(now_Date)
    os.makedirs(dir_AppTestReport, exist_ok=True)
    os.makedirs(dir_AppScreenshot, exist_ok=True)
     
    file_AppTestReport = '{}/{}.html'.format(dir_AppTestReport, 'App_Test_Report_{}'.format(now_DateTime))
  
    with open(file_AppTestReport, 'wb')as f:
        runner = HTMLTestRunner(stream=f, title='App自動化測試報告', description='1.平台：Android 10。 '+
                                                                              '2.裝置：Samsung Galaxy Note 10+。 '+
                                                                              '3.App：全民健保行動快易通│健康存摺APP。', tester='Tony Chang')
        runner.run(tests)