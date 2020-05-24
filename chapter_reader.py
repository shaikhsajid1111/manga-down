import requests 
from bs4 import BeautifulSoup
import sys
from chapter_list import chapter_list 

class chapter_reader:
    
    def scrap(self):
        """this method finds all pages and their links"""
        chp_list = chapter_list("miki-san-sukidesu")
        URLS = chp_list.scrap()

        response = requests.get(URLS[0])
        
        if response.status_code == 404:
            print("Error Occured!")
            exit()
        if response.status_code == 200:
            soup = BeautifulSoup(response.content,"html.parser")    
            
            last_page_number = soup.find('select',{'id':'pageMenu'})
            page_options = last_page_number.find_all('option')
            
            page_links = [f"https://mangareader.net{page_options[i]['value']}" for i in range(len(page_options))]
            return page_links
        
