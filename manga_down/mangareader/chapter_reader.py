try:
    import requests 
    from bs4 import BeautifulSoup

    from . import chapter_list

    from fake_headers import Headers
    import argparse
    import re
except Exception as ex:
    print(ex)
    exit()
class Chapter_reader:
    
    def __init__(self, manga,chapter_number):   #chapter_number and manga_name
        """
        instantiate chapter_reader class 
        """
        self.manga = manga
        self.chapter_number = chapter_number

    def get_image_links(self):
        """returns all image links present for manga chapter"""
        chp_list = chapter_list.Chapter_list(self.manga) #Chapter_list(self.manga)

        URLS = chp_list.get_links()             #all chapters

        print("Changing user agent...")      
        headers = Headers(headers=False).generate()        
        print("User agent changed...")

        response = requests.get(URLS[int(self.chapter_number)-1],headers = headers,verify = False)            #chapter number
        
        if response.status_code == 404:
            print("Error Occured!")
            exit()
        if response.status_code == 200:
            soup = BeautifulSoup(response.content,"html.parser")    

            all_tags = re.findall('"u":".*?"',soup.prettify())
            all_image_urls = ["https:"+url.split(":")[1].replace('"','').replace("\\","") for url in all_tags]
            return all_image_urls
            

