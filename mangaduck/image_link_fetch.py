from chapter_list import chapter_list
import requests
from bs4 import BeautifulSoup
from fake_headers import Headers
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.select import Select
class image_fetcher:
    @staticmethod
    def image_links(anime_name,chp_number):
        chap_list = chapter_list.scrap(anime_name)
        print("Chapters founded")   
        headers = Headers().generate()

        chrome_options = Options()
        chrome_options.add_argument('--headless')
        chrome_options.add_argument('--disable-extensions')
        chrome_options.add_argument('--incognito')
        chrome_options.add_argument('--disable-gpu')
        chrome_options.add_argument('--log-level=3')
        chrome_options.add_argument(f'user-agent={headers}')
        driver = webdriver.Chrome('C:\\webdrivers\\chromedriver.exe',options=chrome_options)
        
        driver.get(chap_list[chp_number]) 
        
        element = WebDriverWait(driver, 10).until(
                    EC.presence_of_element_located((By.ID,'page_image_zoom'))
                )
        select_box = Select(driver.find_element_by_id('sel_load'))
        select_box.select_by_visible_text('Load images: all images')       
        print("page is loaded")        
        driver.implicitly_wait(10)
        
        response = driver.page_source.encode('utf-8').strip()
        
        soup = BeautifulSoup(response,'html.parser')
        
        all_images = soup.find_all('a',{
            'class' : 'img-num'
        })
        image_links = [anchor['href'] for anchor in all_images]
        return image_links

#print(image_fetcher.image_links("naruto",4))