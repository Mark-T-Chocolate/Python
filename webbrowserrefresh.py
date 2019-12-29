#!/usr/bin/python3
import webbrowser, sys
import os
import time
from selenium import webdriver

driver = webdriver.Firefox()
driver.maximize_window()
driver.get("http://10.162.87.212");
count = 0
    
while (count < 1000):
        driver.refresh();
        time.sleep(5)
        print ('The count is:', count)
        count = count + 1

print ("Good bye 1000 refreshes are done!")