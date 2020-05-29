from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from bs4 import BeautifulSoup
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import re
class chapter_list:
    
    def __init__(self,anime):
        self.anime = anime
    
    
    def url_generator(self,anime_name):
        '''Generates URL passed to it as a a paremeter'''
        #anime_name.replace('?','-')
        anime_name = re.sub(r'[?|$|%|&|#]',r'-',anime_name)
        keyword_list = anime_name.split(" ")
        keyword = '-'.join(keyword_list)
        return keyword.capitalize()
       
        return keyword.capitalize()
   
    def scrap(self):
        """
        Gets all chapter of a manga available
        """
        try:
            #generating URL for manga givem
            URL = f'http://kissmanga.com/manga/{self.url_generator(self.anime)}'
            
            #setting chrome capabilities
            chrome_options = Options()          #options for chrome to run as e.g in incognito tab

            chrome_options.add_argument('--headless')                   #don't open browser tab
            chrome_options.add_argument('--disable-extensions')     #don't use any extenstions
            chrome_options.add_argument('--incognito')              #open link in incognito tab
            chrome_options.add_argument('--disable-gpu')    #disable graphics for chrome
            chrome_options.add_argument('--log-level=3')
            #initializing webdriver
            driver = webdriver.Chrome('C:\\webdrivers\\chromedriver.exe',options=chrome_options)    #first parameter is webdriver's executive path, and chrome capabilities

            driver.get(URL)         #opening the link in browser
            #wait until the pages load so that element with divAds is visible
            element = WebDriverWait(driver, 10).until(
                    EC.presence_of_element_located((By.ID, "divAds"))
                )
            #converting page source code to utf-8
            response = driver.page_source.encode('utf-8').strip()
            soup =  BeautifulSoup(response,'html.parser')

            #finding chapter table in soup
            tables = soup.find('table',{'class' : "listing"})

            #finding anchor tag inside table
            childrens = tables.findChildren('a')
            #generating URL with anchor tags given
            links = [f'http://kissmanga.com{child["href"]}' for child in childrens]
            return links
        except Exception as error:
            print(error)
        except KeyboardInterrupt:       #Ctrl+C
            print("Bye")
            exit()


usr = chapter_list('naruto')
print(usr.scrap()) 
