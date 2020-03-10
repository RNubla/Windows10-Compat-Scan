import wget
import fire
import os
import platform
import sys
import re
from bs4 import BeautifulSoup

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options


opts = Options()
opts.add_argument('user-agent=Chrome -- Mac')
# driver = webdriver.Chrome('./chromedriver') for OSX
driver = webdriver.Chrome(chrome_options=opts, executable_path='./chromedriver.exe') #for Windows
# driver = webdriver.Safari()
class AutomateWeb(object):
    
    def winISO(self):
        driver.get('https://www.microsoft.com/en-us/software-download/windows10ISO')
        WebDriverWait(driver, 50).until(EC.visibility_of_element_located((By.ID, 'productEdition-validation')))
        src = driver.page_source

        parser = BeautifulSoup(src, 'lxml')
        list_of_attributes = {'id' : 'product-edition'}
        tag = parser.findAll('select', attrs=list_of_attributes)

        drpOS = driver.find_element_by_id('product-edition')
        for option in drpOS.find_elements_by_tag_name('option'):
            if option.text == 'Windows 10':
                option.click()
        
        driver.find_element_by_id('submit-product-edition').click()

        WebDriverWait(driver, 50).until(EC.visibility_of_element_located((By.ID, 'product-languages')))

        dropLang = driver.find_element_by_id('product-languages')
        for option in dropLang.find_elements_by_tag_name('option'):
            if option.text == 'English':
                option.click()

        driver.find_element_by_id('submit-sku').click()

    #TODO Have to user select between 32-bit or 64-bit OS or Both

    #TODO Download ISO by looking for the button class and have the driver click it

        WebDriverWait(driver, 50).until(EC.visibility_of_element_located((By.TAG_NAME, '64-bit')))

        driver.find_element_by_class_name('button button-long button-flat button-purple x-hidden-focus').click()

#For Debugging since I switch platform between Windows and OSX
# class Check_OS():
#     def os_check(self):
#         if platform == 'win32':
#             print('Windows')

class Program(object):

    def link(self, link):
        print('Downloading File')
        filename = wget.download(link)

if __name__ == '__main__':
    # Check_OS.os_check()
    fire.Fire(AutomateWeb)
