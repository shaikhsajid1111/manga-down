try:
    import requests 
    from bs4 import BeautifulSoup
    from fake_headers import Headers
    import urllib3
    import argparse
#if module is not available
except Exception as ex:
    print(ex)
    exit()

class Chapter_list:
    def __init__(self,manga):
        """
        instantiate class with given manga name
        """
        
        self.manga = manga
        self.URL = f"http://www.mangareader.net/{self.manga}"
    
    def get_list(self):
        """
        returns list of all chapter's link from http://mangareader.com/
        """
        ua = Headers(headers = False) #change headers
        
        urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)         #hiding the warning
        
        response = requests.get(self.URL,headers = ua.generate(),verify = False)           #sending a request and storing the response inside response var
        
        if response.status_code == 404:     #if page does not exist
            print("Page not found!")
        if response.status_code == 200:
            soup = BeautifulSoup(response.content,"html.parser")
    
            table = soup.find('table',{'class' : 'd48'})       #find all chapter table
            anchors = table.find_all("a")                   #all hyperlinks in table i.e all links for chapters available
            links = [f"https://www.mangareader.net{a['href']}" for a in anchors]
            return links   


