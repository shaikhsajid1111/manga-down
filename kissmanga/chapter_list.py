from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from bs4 import BeautifulSoup
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class chapter_list:
    def __init__(self,anime):
        self.anime = anime
    def url_generator(self,anime_name):
        keyword_list = anime_name.split(" ")
        keyword = '-'.join(keyword_list)
        #keyword = keyword[0].upper()
        return keyword.capitalize()
    def scrap(self):
        URL = f'http://kissmanga.com/manga/{self.url_generator(self.anime)}'
        print(URL)
        chrome_options = Options()
    
        chrome_options.add_argument('--headless')
        chrome_options.add_argument('--disable-extensions')
        chrome_options.add_argument('--incognito')
        chrome_options.add_argument('--disable-gpu')

        driver = webdriver.Chrome('C:\\webdrivers\\chromedriver.exe',options=chrome_options)

        driver.get(URL)
        element = WebDriverWait(driver, 10).until(
                EC.presence_of_element_located((By.ID, "divAds"))
            )

        response = driver.page_source.encode('utf-8').strip()
        soup =  BeautifulSoup(response,'html.parser')

        tables = soup.find('table',{'class' : "listing"})

        childrens = tables.findChildren('a')
        links = [f'http://kissmanga.com{child["href"]}' for child in childrens]
        return links
#usr = chapter_list('naruto')
#print(usr.scrap())