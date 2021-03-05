try:
    import requests 
    from bs4 import BeautifulSoup
    from fake_headers import Headers
    import urllib3
    import re
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
        self.URL = f"http://mangareader.cc/manga/{self.URLify(self.manga)}"

    def URLify(self,manga):
        return "-".join(manga.split(" "))
    
    def remove_trails(self,string):
        string = re.sub(r"\s", "", string)
        string = re.sub("([a-z])([A-Z])","\g<1> \g<2>",string)
        return string


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
    
            unorder_lists = soup.findAll("ul")
            all_spans = unorder_lists[2].findChildren('span',{'class' : 'leftoff'})
            all_chapters = list(reversed(list(map(self.remove_trails,[span.text for span in all_spans]))))                
            
            return all_chapters


    def get_links(self):
        """
        returns list of all chapter's link from https://mangareader.cc/
        """
        ua = Headers(headers = False) #change headers
        
        urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)         #hiding the warning
        
        response = requests.get(self.URL,headers = ua.generate(),verify = False)           #sending a request and storing the response inside response var
        
        if response.status_code >= 400 and response.status_code < 500:     #if server error
            print("Server Error\nTry again later")
        if response.status_code >= 200 and response.status_code < 300:
            soup = BeautifulSoup(response.content,"html.parser")

            unorder_list = soup.findAll("ul")[2]
            all_hyperlink_tags = unorder_list.findChildren('a') 
            all_hrefs = list(reversed([hyperlink.get('href') for hyperlink in all_hyperlink_tags]))

            return all_hrefs
