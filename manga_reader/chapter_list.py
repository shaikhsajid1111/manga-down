import requests 
from bs4 import BeautifulSoup
import sys
from fake_headers import Headers
import urllib3
class chapter_list:
    '''
- Need to find all chapter's link present for manga.
- Returns a list of all links of chapters e.g http://mangareader.com/chapter_number{int}

'''
    def __init__(self,anime = sys.argv[len(sys.argv)-1]):
        self.anime = anime
        self.URL = f"http://www.mangareader.net/{self.anime}"
    def scrap(self):
        """
        this method finds all chapters present for the manga
        """
        ua = Headers(headers = False)
        

        urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)         #hiding the warning
        
        response = requests.get(self.URL,headers = ua.generate(),verify = False)           #sending a request and storing the response inside response var
        
        if response.status_code == 404:     #if page does not exist
            print("Page not found!")
        if response.status_code == 200:
            soup = BeautifulSoup(response.content,"html.parser")
    
            table = soup.find('table',{'id' : 'listing'})       #find all chapter table
            anchors = table.find_all("a")                   #all hyperlinks in table i.e all links for chapters available
            links = [f"https://www.mangareader.net{a['href']}" for a in anchors]
            return links   
#usr = chapter_list()
#print(usr.scrap())


