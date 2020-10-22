try:
    import requests
    from bs4 import BeautifulSoup
    from fake_headers import Headers
    import urllib3
except Exception as ex:
    print(ex)

class Chapter_list:
    def __init__(self,manga):
        self.manga = manga
        self.URL = f"https://mangapark.net/manga/{self.manga}/"
    
    def replace_ending(self,sentence, old, new):
        if sentence.endswith(old):
            return sentence[:-len(old)] + new
        return sentence
    
    def get_chapter_list(self):
        """returns list of all chapter available for given manga"""

        user_agent = Headers(os="win").generate() #fake user agent    
        urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning) 

        response = requests.get(self.URL,headers = user_agent,verify = False)

        if response.status_code < 500 and response.status_code > 400:
            print("Server error")
            exit()
        
        if response.status_code >= 200 and response.status_code < 300:
            soup = BeautifulSoup(response.content,"html.parser")
            
            table = soup.find("div",{"id" : "stream_3"})
            
            all_div_tags = table.find_all("div",{"class" : "d-none"})
            
            all_texts = [text.get_text().strip().replace("\n","").strip().replace(":","").strip() for text in all_div_tags]
            
            all_texts.reverse()

            return ["{} {} : {}".format(self.manga,index,value) for index,value in enumerate(all_texts,start=1)]


    def get_links(self):
        user_agent = Headers().generate()    
        urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)    
        response = requests.get(self.URL,headers = user_agent,verify = False)

        if response.status_code < 500 and response.status_code > 400:
            print("Server error")
            exit()
        
        if response.status_code >= 200 and response.status_code < 300:
            soup = BeautifulSoup(response.content,"lxml")
            
            table = soup.find("div",{"id" : "stream_3"})
            
            all_anchor_tags = table.find_all("a",{"class" : "ml-1 visited ch"})
            
            all_hrefs = [f"https://mangapark.net{self.replace_ending(anchor['href'],'/1','')}" for anchor in all_anchor_tags]

            return all_hrefs

