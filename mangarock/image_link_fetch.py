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
        #print(chap_list)
        print("Chapters founded")   
        headers = Headers().generate()

        chrome_options = Options()
        #chrome_options.add_argument('--headless')
        chrome_options.add_argument('--disable-extensions')
        chrome_options.add_argument('--incognito')
        chrome_options.add_argument('--disable-gpu')
        chrome_options.add_argument('--log-level=3')
        chrome_options.add_argument(f'user-agent={headers}')
        driver = webdriver.Chrome('C:\\webdrivers\\chromedriver.exe',options=chrome_options)
        url = chap_list[int(chp_number)]
        print(url)
        driver.get(url) 
        
        element = WebDriverWait(driver, 10).until(
                    EC.presence_of_element_located((By.ID,'page_image_zoom'))
                )
        select_box = Select(driver.find_element_by_id('sel_load'))
        select_box.select_by_visible_text('Load images: all images')       
        element = WebDriverWait(driver, 10).until(
                    EC.presence_of_element_located((By.ID,'img-1'))
                )
        print("page is loaded")        
        
        
        response = driver.page_source.encode('utf-8').strip()
        
        soup = BeautifulSoup(response,'html.parser')
        #print(soup.prettify())
        #with open('all.html','w',encoding='utf-8') as file:
        #    file.write(str(soup.prettify()))
        all_images = soup.find_all('img',{
            'class' : 'img'
        })
        #print(all_images)
        image_links = [anchor['src'] for anchor in all_images]
        #print(image_links)
        return image_links

#print(image_fetcher.image_links("bleach",4))
if __name__ == '__main__':
    print(image_fetcher.image_links("naruto",10))