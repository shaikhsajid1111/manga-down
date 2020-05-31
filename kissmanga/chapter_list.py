#!/usr/bin/env python
# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from bs4 import BeautifulSoup
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import re
import fake_useragent
class chapter_list:
    
    def __init__(self,anime):
        self.anime = anime
    
    
    def url_generator(self,anime_name):
        '''Make Keyword URL friendly'''
        
        anime_name = re.sub(r'[?|$|%|&|#]',r'-',anime_name)
        keyword_list = anime_name.split(" ")
        keyword = '-'.join(keyword_list)
        return keyword.capitalize()
       
   
    def scrap(self):
        """
        Gets all chapter of a manga available
        """
        try:
            #generating URL for manga givem
            URL = f'http://kissmanga.com/manga/{self.url_generator(self.anime)}'
            headers = fake_useragent.get_user_agent()
            #setting chrome capabilities
            chrome_options = Options()          #options for chrome to run as e.g in incognito tab

            chrome_options.add_argument('--headless')                   #don't open browser tab
            chrome_options.add_argument('--disable-extensions')     #don't use any extenstions
            chrome_options.add_argument('--incognito')              #open link in incognito tab
            chrome_options.add_argument('--disable-gpu')    #disable graphics for chrome
            chrome_options.add_argument('--log-level=3')        #disable all logs of selenium 
            chrome_options.add_argument(f'user-agent={headers}')    #change user agent
            #initializing webdriver
            driver = webdriver.Chrome('C:\\webdrivers\\chromedriver.exe',options=chrome_options)    #first parameter is webdriver's executive path, and chrome capabilities

            driver.get(URL)         #opening the link in browser
            #wait until the pages load so that element with divAds is visible
            element = WebDriverWait(driver, 10).until(
                    EC.presence_of_element_located((By.ID, "divAds"))
                )
            #converting page source code to utf-8
            response = driver.page_source.encode('utf-8').strip()
            soup =  BeautifulSoup(response,'html.parser')       #passed markup -> HTML 

            #finding chapter table in soup with class name 'listing'
            tables = soup.find('table',{'class' : "listing"})

            #finding anchor tag inside the above table
            childrens = tables.findChildren('a')

            #generating URL with anchor tags given
            links = [f'http://kissmanga.com{child["href"]}' for child in childrens]
            return links
        except Exception as error:
            print(error)
        except KeyboardInterrupt:       #Ctrl+C
            print("Bye")
            exit()


#usr = chapter_list('naruto')
#print(usr.scrap()) 
'''
author : Sajid Shaikh
updated on: 31-05-2020 
'''