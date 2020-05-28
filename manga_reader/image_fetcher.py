import requests 
from bs4 import BeautifulSoup
import sys
from chapter_reader import chapter_reader
import time
import random
import fake_useragent
import urllib3
'''
- Finds the image on the page, provided by chapter reader class
- returns a list of all image links present in an chapter
'''
class image_fetcher:
    def __init__(self,chapter_number = sys.argv[len(sys.argv)-2],anime = sys.argv[len(sys.argv)-1]):
        self.chapter_number = chapter_number
        self.anime = anime
    def scrap(self):
        """this method finds images present in pages"""
        chp_reader = chapter_reader(self.chapter_number,self.anime)
        page_links = chp_reader.scrap()
        image_links = []

        headers = fake_useragent.get_user_agent()
        urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)         #hiding the warning
        for i in range(len(page_links)):
            response = requests.get(page_links[i],headers = headers,verify = False)      #4 is page 5
            if response.status_code == 404:
                print(f"Page not found! {page_links[i]}")
                
            if response.status_code == 200:
                soup = BeautifulSoup(response.content,"html.parser")

                image = soup.find("img",{
                "id" : "img"
            })    
                image_links.append(image['src'])
                
                time.sleep(random.randint(1,5))
        return image_links        
#usr = image_fetcher()
#print(usr.scrap()) 