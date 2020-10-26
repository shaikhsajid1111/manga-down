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
        self.URL = f"https://mangapark.net/manga/{self.URLify(self.manga)}/"
        
    def URLify(self,manga):
        """replaces space with '-' """
        return "-".join(manga.split(" "))

    def __replace_ending(self,sentence, old, new):
        if sentence.endswith(old):
            return sentence[:-len(old)] + new
        return sentence
    
    def get_chapter_list(self):
        """returns list of all chapter available for given manga"""

        user_agent = Headers(os="win").generate() #fake user agent    
        urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning) 
        
        #send request and store them to response var
        response = requests.get(self.URL,headers = user_agent,verify = False)

        if response.status_code < 500 and response.status_code >= 400:
            #if server error occured
            print("Server error")
            exit()
        
        if response.status_code >= 200 and response.status_code < 300:
            soup = BeautifulSoup(response.content,"html.parser")
            
            #find table tag with id named as "stream_3"
            table = soup.find("div",{"id" : "stream_3"})
            
            if table is None:
                print("Cannot find the manga on MangaPanda")
                exit()
            #find div with class name "d-none" inside table tag
            all_div_tags = table.find_all("div",{"class" : "d-none"})

            #extract text between those div tags,replace \n escape character,":" and spaces as well
            all_texts = [text.get_text().strip().replace("\n","").strip().replace(":","").strip() for text in all_div_tags]
            #if div tags inside table was not found
            if len(all_texts) == 0:
                #find all anchor tag
                all_anchor_tags = table.find_all("a",{"class" : "visited"})
                all_texts = [text.get_text() for text in all_anchor_tags]   #extract text between anchor tags

            #we get list in descending order,so reverse it to make it ascending order
            all_texts.reverse()
            
            return [f"{self.manga} {index} : {value}" for index,value in enumerate(all_texts,start=1)]


    def get_links(self):
        user_agent = Headers().generate()    
        urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)    
        response = requests.get(self.URL,headers = user_agent,verify = False)

        if response.status_code < 500 and response.status_code > 400:
            print("Server error")
            exit()
        
        if response.status_code >= 200 and response.status_code < 300:
            soup = BeautifulSoup(response.content,"html.parser")

            #find table that contains all chapters 
            table = soup.find("div",{"id" : "stream_3"})
            #all anchor tags inside tables
            all_anchor_tags = table.find_all("a",{"class" : "ml-1 visited ch"})
            #extract all href values from anchor tags
            all_hrefs = [f"https://mangapark.net{self.__replace_ending(anchor['href'],'/1','')}" for anchor in all_anchor_tags]

            return all_hrefs

