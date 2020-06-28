import requests
from bs4 import BeautifulSoup
from fake_headers import Headers

class chapter_list:
    @staticmethod
    def scrap(anime_name):
        response = requests.get(f"https://mangapark.net/manga/{anime_name}")
        soup = BeautifulSoup(response.content,"html.parser")
        #    file.write(str(soup.prettify()))
        list_duck = soup.find("div",{
            "class" : "mt-3 stream collapsed",
            "id" : "stream_1"
        })
        all_anchors = list_duck.findChildren('a',{'class' : 'ml-1 visited ch'})
        chapters = [f'https://mangapark.net{anchor["href"]}' for anchor in all_anchors]
        return chapters[::-1]
if __name__ == '__main__':
    print(chapter_list.scrap('bleach'))