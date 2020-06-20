import requests
from bs4 import BeautifulSoup
from fake_headers import Headers

class chapter_list:
    @staticmethod
    def scrap(anime_name):
        response = requests.get(f"https://mangapark.net/manga/{anime_name}")
        soup = BeautifulSoup(response.content,"html.parser")
        list_duck = soup.find("div",{
            "class" : "mt-3 stream collapsed",
            "id" : "stream_4"
        })
        all_anchors = list_duck.findChildren('a',{'class' : 'ml-1 visited ch'})
        chapters = [f'https://mangapark.net/manga/naruto{anchor["href"]}' for anchor in all_anchors]
        return chapters

#print(chapter_list.scrap('bleach'))