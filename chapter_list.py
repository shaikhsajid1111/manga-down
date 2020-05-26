import requests 
from bs4 import BeautifulSoup
import sys

'''
- Need to find all chapter's link present for manga.
- Returns a list of all links of chapters e.g http://mangareader.com/chapter_number{int}

'''
class chapter_list:
    def __init__(self,anime = sys.argv[len(sys.argv)-1]):
        self.anime = anime
        self.URL = f"http://www.mangareader.net/{self.anime}"
    def scrap(self):
        """
        this method finds all chapters present for the manga
        """
        response = requests.get(self.URL)
        if response.status_code == 404:
            print("Page not found!")
        if response.status_code == 200:
            soup = BeautifulSoup(response.content,"html.parser")
    
            table = soup.find('table',{'id' : 'listing'})
            anchors = table.find_all("a")
        
            links = [f"https://www.mangareader.net{a['href']}" for a in anchors]
            return links   
#usr = chapter_list()
#print(usr.scrap())


