import requests
from image_fetcher import image_fetcher
import os
import time
import random
import sys
class downloader:
    def __init__(self,chapter_number = sys.argv[len(sys.argv)-2],anime = sys.argv[len(sys.argv)-1]):
        self.anime = anime
        self.chapter_number = chapter_number
    def download(self):
        img_fetch = image_fetcher(self.chapter_number,self.anime)
        img_links = img_fetch.scrap() #['https://i1.imggur.net/miki-san-sukidesu/1/miki-san-sukidesu-13610923.jpg', 'https://i9.imggur.net/miki-san-sukidesu/1/miki-san-sukidesu-13610929.jpg', 'https://i5.imggur.net/miki-san-sukidesu/1/miki-san-sukidesu-13610935.jpg', 'https://i3.imggur.net/miki-san-sukidesu/1/miki-san-sukidesu-13610941.jpg', 'https://i5.imggur.net/miki-san-sukidesu/1/miki-san-sukidesu-13610947.jpg', 'https://i3.imggur.net/miki-san-sukidesu/1/miki-san-sukidesu-13610953.jpg', 'https://i5.imggur.net/miki-san-sukidesu/1/miki-san-sukidesu-13610959.jpg', 'https://i8.imggur.net/miki-san-sukidesu/1/miki-san-sukidesu-13610965.jpg', 'https://i6.imggur.net/miki-san-sukidesu/1/miki-san-sukidesu-13610971.jpg', 'https://i10.imggur.net/miki-san-sukidesu/1/miki-san-sukidesu-13610977.jpg', 'https://i8.imggur.net/miki-san-sukidesu/1/miki-san-sukidesu-13610983.jpg', 'https://i2.imggur.net/miki-san-sukidesu/1/miki-san-sukidesu-13610989.jpg', 'https://i6.imggur.net/miki-san-sukidesu/1/miki-san-sukidesu-13610995.jpg', 'https://i8.imggur.net/miki-san-sukidesu/1/miki-san-sukidesu-13611001.jpg', 'https://i4.imggur.net/miki-san-sukidesu/1/miki-san-sukidesu-13611007.jpg', 'https://i8.imggur.net/miki-san-sukidesu/1/miki-san-sukidesu-13611013.jpg']
        time.sleep(random.randint(1,5))
        if os.path.isdir(os.path.join(os.getcwd(),f'{self.anime}')):
            os.chdir(os.path.join(os.getcwd(),f'{self.anime}'))
            os.mkdir(f'{self.chapter_number}')
            os.chdir(os.path.join(os.getcwd(),f'{self.chapter_number}'))
        
        else:
            os.mkdir(f'{self.anime}')
            os.chdir(os.path.join(os.getcwd(),f'{self.anime}'))
        
        for i in range(len(img_links)):
            response = requests.get(img_links[i],stream = True)
            with open(f'{self.anime} - Page {i+1}.jpg','wb') as file:
                file.write(response.content)
                print(f"Downloaded Page {i}")
            time.sleep(random.randint(5,10))
d = downloader()
d.download()