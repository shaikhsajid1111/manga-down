import requests 
from bs4 import BeautifulSoup
import sys
from fake_headers import Headers

class chapter_list:
    '''
- Need to find all chapter's link present for manga.
- Returns a list of all links of chapters 

'''
    def __init__(self,anime = sys.argv[len(sys.argv)-1]):
        self.anime = anime
        self.URL = f"http://www.mangapanda.com/{self.anime}"
    def scrap(self):
        """
        this method finds all chapters present for the manga
        """
        headers = Headers(headers=False).generate()
        response = requests.get(self.URL,verify = False,headers = headers)           #sending a request and storing the response inside response var
        if response.status_code == 404:     #if page does not exist
            print("Manga not found! :(")
            exit()
        if response.status_code == 200:
            soup = BeautifulSoup(response.content,"html.parser")
    
            table = soup.find('table',{'id' : 'listing'})       #find all chapter table
            anchors = table.find_all("a")                   #all hyperlinks in table i.e all links for chapters available
        
            links = [f"https://www.mangapanda.com{a['href']}" for a in anchors]
            return links   
#usr = chapter_list()
#print(usr.scrap())


