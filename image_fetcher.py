import requests 
from bs4 import BeautifulSoup
import sys
from chapter_reader import chapter_reader
import time
class image_fetcher:
    def scrap(self):
        """this method finds images present in pages"""
        chp_reader = chapter_reader()
        page_links = chp_reader.scrap()
        image_links = []
        for i in range(len(page_links)):
            response = requests.get(page_links[i])      #4 is page 5
            if response.status_code == 404:
                print(f"Page not found! {page_links[i]}")
                
            if response.status_code == 200:
                soup = BeautifulSoup(response.content,"html.parser")

                image = soup.find("img",{
                "id" : "img"
            })    
                image_links.append(image['src'])
                print(image_links)
                time.sleep(5)
usr = image_fetcher()
print(usr.scrap())        
