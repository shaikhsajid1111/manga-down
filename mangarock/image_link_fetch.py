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
        '''fetch all image links in a chapter'''
        chap_list = chapter_list.scrap(anime_name)      #fetch all chapters available for manga
    
        print("Chapters founded")   
        headers = Headers().generate()
        
        chrome_options = Options()
        chrome_options.add_argument('--headless')   #run browser headlessly
        chrome_options.add_argument('--disable-extensions')     #disable all extensions
        chrome_options.add_argument('--incognito')              #runs in incognito mode
        chrome_options.add_argument('--disable-gpu')
        chrome_options.add_argument('--log-level=3')            #do not show log of process
        chrome_options.add_argument(f'user-agent={headers}')    #change user agents
        driver = webdriver.Chrome('C:\\webdrivers\\chromedriver.exe',options=chrome_options)    #initialization
        url = chap_list[int(chp_number)]            #chapter_list[chapter_number]
        driver.get(url)             #open URL
        
        element = WebDriverWait(driver, 10).until(
                    EC.presence_of_element_located((By.ID,'page_image_zoom'))
                )       #wait until there is element with ID page_image_zoom
        select_box = Select(driver.find_element_by_id('sel_load'))  #select that select tag
        select_box.select_by_visible_text('Load images: all images')        #after selection, check option to show all iimages
        element = WebDriverWait(driver, 10).until(
                    EC.presence_of_element_located((By.ID,'img-1'))
                )   #wati until at least first image shows up
        print("page is loaded")        
        
        
        response = driver.page_source.encode('utf-8').strip()   #get page Source
        
        soup = BeautifulSoup(response,'html.parser')
        
        all_images = soup.find_all('img',{
            'class' : 'img'
        })              #find all image with className 'img'
    
        image_links = [img['src'] for img in all_images]    #extract SRC urls from all image tags
        
        return image_links

if __name__ == '__main__':
    print(image_fetcher.image_links("naruto",10))