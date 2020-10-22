try:
    import requests
    import urllib3
    from fake_headers import Headers
    from . import chapter_list 
    from fake_headers import Headers
    from bs4 import BeautifulSoup
    import re
except Exception as ex:
    print(ex)

class Chapter_reader:
    def __init__(self,manga,chapter_number):
        self.manga = manga
        self.chapter_number = chapter_number    

    def get_image_links(self):
        """returns a list of image link for a given chapter"""
        #make a request to server and scrap all present chapter for manga
        manga_chapters = chapter_list.Chapter_list(self.manga).get_links()
        #we get a list where chapter is listed in descending order, so we'll reverse it to ascending order
        manga_chapters.reverse()
        
        #store chapter that has to be scrapped
        chapter_to_scrap = manga_chapters[int(self.chapter_number)-1]
        
        urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning) 
        
        #send request to server with given chapter URL
        response = requests.get(chapter_to_scrap,headers = Headers().generate(),verify=False)

        if response.status_code >= 400 and response.status_code < 500:
            #if response was code is 400-499
            print("Server error,Please try again later")
            exit()
        if response.status_code >= 200 and response.status_code < 300:
            #if successful response 
            soup = BeautifulSoup(response.content,"html.parser")    
            
            all_tags = re.findall('"u":".*?"',soup.prettify())   #using regex find all url present in js code
            
        
            all_urls = [f"https:"+url.split(":")[2].replace('"','').replace("\\","") for url in all_tags]
            
            return all_urls      



