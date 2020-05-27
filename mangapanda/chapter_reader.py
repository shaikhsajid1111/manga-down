import requests 
from bs4 import BeautifulSoup
import sys
from chapter_list import chapter_list 

class chapter_reader:
    '''
- Need to iterate over chapter's link provided by chapter_list class
- Returns links of all pages present in the chapter 

'''
    def __init__(self, chapter_number = sys.argv[len(sys.argv)-2],anime = sys.argv[len(sys.argv)-1]):   #chapter_number and anime_name
        self.anime = anime
        self.chapter_number = chapter_number
    def scrap(self):
        """this method finds all pages and their links"""
        chp_list = chapter_list(self.anime)

        URLS = chp_list.scrap()             #all chapters
        
        response = requests.get(URLS[int(self.chapter_number)-1],verify = False)            #chapter number
        
        if response.status_code == 404:
            print("Error Occured!")
            exit()
        if response.status_code == 200:
            soup = BeautifulSoup(response.content,"html.parser")    
            
            last_page_number = soup.find('select',{'id':'pageMenu'})
            page_options = last_page_number.find_all('option')
            
            page_links = [f"https://mangapanda.com{page_options[i]['value']}" for i in range(len(page_options))]
            return page_links
