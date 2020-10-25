try:
    import requests 
    from bs4 import BeautifulSoup
    from fake_headers import Headers
    import urllib3
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
        self.URL = f"http://www.mangareader.net/{self.URLify(self.manga)}"

    def URLify(self,manga):
        return "-".join(manga.split(" "))
    
    def get_chapter_list(self):
        """
        returns list of all chapter's from given manga/
        """
        ua = Headers(headers = False) #change headers
        
        urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)         #hiding the warning
        
        response = requests.get(self.URL,headers = ua.generate(),verify = False)           #sending a request and storing the response inside response var
        
        if response.status_code >= 400 and response.status_code < 500:     #server error
            print("Server Error!\nTry again later")
        if response.status_code == 200:
            soup = BeautifulSoup(response.content,"html.parser")
    
            table = soup.find('table',{'class' : 'd48'})       #find all chapter table
            
            all_rows = table.find_all("tr")  #find all row in table                
            
            all_tables_data = [tr.find("td") for tr in all_rows]    #loop through all row and find td tag inside

            all_chapters = [data.get_text() for data in all_tables_data]    #loop through all td and store there text inside the list
            return all_chapters[1:]
            

        

    def get_links(self):
        """
        returns list of all chapter's link from https://mangareader.com/
        """
        ua = Headers(headers = False) #change headers
        
        urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)         #hiding the warning
        
        response = requests.get(self.URL,headers = ua.generate(),verify = False)           #sending a request and storing the response inside response var
        
        if response.status_code >= 400 and response.status_code < 500:     #if server error
            print("Server Error\nTry again later")
        if response.status_code >= 200 and response.status_code < 300:
            soup = BeautifulSoup(response.content,"html.parser")
    
            table = soup.find('table',{'class' : 'd48'})       #find table containing all chapter
            anchors = table.find_all("a")                   #all hyperlinks in table i.e all links for chapters available
    
            links = [f"https://www.mangareader.net{a['href']}" for a in anchors] #get href attribute of all anchor tags and store them in lists
            return links   


