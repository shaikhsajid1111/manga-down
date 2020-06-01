import requests 
from bs4 import BeautifulSoup
import sys
from chapter_reader import chapter_reader
import time
import random
from fake_headers import Headers
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
        try:
            chp_reader = chapter_reader(self.chapter_number,self.anime)
            page_links = chp_reader.scrap()

            print("Chapter found! ...")
            
            image_links = []
            print("Setting a new user agent...")
            headers = Headers(headers=False).generate()
            print("New user agent changed...")
            
            urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)  
            
            for i in range(len(page_links)):
                response = requests.get(page_links[i],verify = False,headers = headers)      #4 is page 5
                if response.status_code == 404:
                    print(f"Page not found! {page_links[i]}")

                if response.status_code == 200:
                    soup = BeautifulSoup(response.content,"html.parser")

                    image = soup.find("img",{
                    "id" : "img"
            })        
                    image_links.append(image['src'])

                    time.sleep(random.randint(2,13))
            return image_links
        except requests.exceptions.ConnectionError:
            print("Connection refused!")            
                    
#usr = image_fetcher()#
#print(usr.scrap()) 