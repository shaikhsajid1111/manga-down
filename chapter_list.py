import requests 
from bs4 import BeautifulSoup
import sys

class chapter_list:
    def __init__(self,anime):
        
        self.URL = f"http://www.mangareader.net/{anime}"
    def scrap(self):
        response = requests.get(self.URL)
        if response.status_code == 404:
            print("Page not found!")
        if response.status_code == 200:
            soup = BeautifulSoup(response.content,"html.parser")
    
            table = soup.find('table',{'id' : 'listing'})
            anchors = table.find_all("a")
        
            links = [f"https://www.mangareader.net{a['href']}" for a in anchors]
            return links

usr = chapter_list('naruto')
print(usr.scrap())             
