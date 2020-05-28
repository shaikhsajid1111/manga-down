from chapter_list import chapter_list
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from bs4 import BeautifulSoup
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import sys
class image_fetch:
    def __init__(self,chapter_number = sys.argv[len(sys.argv)-2],anime = sys.argv[len(sys.argv)-1]):
        self.anime = anime
        self.chapter_number = chapter_number
    def scrap(self):
        try:
            chp_list= chapter_list(self.anime)
            print(f"Searching {self.anime}...")
            chapter_links = chp_list.scrap()

            chrome_options = Options()

            chrome_options.add_argument('--headless')
            chrome_options.add_argument('--disable-extensions')
            chrome_options.add_argument('--incognito')
            chrome_options.add_argument('--disable-gpu')

            driver = webdriver.Chrome('C:\\webdrivers\\chromedriver.exe',options=chrome_options)

            driver.get(chapter_links[int(self.chapter_number)])            #pass the chapter number

            element = WebDriverWait(driver, 10).until(
                    EC.presence_of_element_located((By.ID, "divImage"))
                )

            response = driver.page_source.encode('utf-8').strip()
            soup =  BeautifulSoup(response,'html.parser')

            divs = soup.find('div',{'id' : 'divImage'})

            childrens = divs.findChildren('img')
            image_links = [child['src'] for child in childrens]
        except KeyboardInterrupt:
            print("Bye!")
            exit()    
        except Exception as ex:
            print(ex)
            print("If problem persists, try VPN or Proxy. You can even try other mangareader or mangapanda\nBye!")
            exit()        
        
        return image_links

#usr = image_fetch()
#print(usr.scrap())        
