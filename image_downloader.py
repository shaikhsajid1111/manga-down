import requests
from image_fetcher import image_fetcher
from chapter_list import chapter_list
import os
import time
import random
import sys

class downloader:
    def download_chapter(self,chp_number,anime_name):
        
        img_fetch = image_fetcher(chp_number,anime_name)
        
        img_links = img_fetch.scrap() #['https://i1.imggur.net/miki-san-sukidesu/1/miki-san-sukidesu-13610923.jpg', 'https://i9.imggur.net/miki-san-sukidesu/1/miki-san-sukidesu-13610929.jpg', 'https://i5.imggur.net/miki-san-sukidesu/1/miki-san-sukidesu-13610935.jpg', 'https://i3.imggur.net/miki-san-sukidesu/1/miki-san-sukidesu-13610941.jpg', 'https://i5.imggur.net/miki-san-sukidesu/1/miki-san-sukidesu-13610947.jpg', 'https://i3.imggur.net/miki-san-sukidesu/1/miki-san-sukidesu-13610953.jpg', 'https://i5.imggur.net/miki-san-sukidesu/1/miki-san-sukidesu-13610959.jpg', 'https://i8.imggur.net/miki-san-sukidesu/1/miki-san-sukidesu-13610965.jpg', 'https://i6.imggur.net/miki-san-sukidesu/1/miki-san-sukidesu-13610971.jpg', 'https://i10.imggur.net/miki-san-sukidesu/1/miki-san-sukidesu-13610977.jpg', 'https://i8.imggur.net/miki-san-sukidesu/1/miki-san-sukidesu-13610983.jpg', 'https://i2.imggur.net/miki-san-sukidesu/1/miki-san-sukidesu-13610989.jpg', 'https://i6.imggur.net/miki-san-sukidesu/1/miki-san-sukidesu-13610995.jpg', 'https://i8.imggur.net/miki-san-sukidesu/1/miki-san-sukidesu-13611001.jpg', 'https://i4.imggur.net/miki-san-sukidesu/1/miki-san-sukidesu-13611007.jpg', 'https://i8.imggur.net/miki-san-sukidesu/1/miki-san-sukidesu-13611013.jpg']
        time.sleep(random.randint(1,5))
        print(f"Succesfully fetched all images on the server...\nCreating Folder {anime_name}...")
        #folder creating process
        if os.path.isdir(os.path.join(os.getcwd(),f'{anime_name}')):    #if folder exists
            #changing current directory to folder
            os.chdir(os.path.join(os.getcwd(),f'{anime_name}'))
            #if chapter folder exists
            if os.path.isdir(os.path.join(os.getcwd(),f'{chp_number}')):
                #just change the CWD to this folder
                os.chdir(os.path.join(os.getcwd(),f'{chp_number}'))
                
                print("Starting download ...")
            else:
                #create chapter folder
                os.mkdir(f'{chp_number}')
                #change directory to chapter folder
                os.chdir(os.path.join(os.getcwd(),f'{chp_number}'))
                
                print("Starting download ...")
        else:
            #making folder with same anime name
            os.mkdir(f'{anime_name}')
            print(f"Folder created {anime_name}")

            #changing directory to that above created folder
            os.chdir(os.path.join(os.getcwd(),f'{anime_name}'))
            
            # creating /anime/chapter_number
            os.mkdir(f'{chp_number}')

            #creating chapter folder inside current folder
            os.chdir(os.path.join(os.getcwd(),f'{chp_number}'))         
            print("Starting download ...")
            
            
        
        '''loops through all image links, send a response and if response is success, 
        write that response.content as binary as images'''
        print(f'{len(img_links)} Pages to download...')
        for i in range(len(img_links)):
            response = requests.get(img_links[i],stream = True)
            if response.status_code == 200:
                with open(f'{anime_name} - Chapter: {chp_number} Page {i+1}.jpg','wb') as file:
                    file.write(response.content)
                    print(f"{anime_name} - Chapter : {chp_number} Page :{i+1} downloaded...")
                time.sleep(random.randint(5,10))
            else:
                print(f"Could not able to download {i+1} page")
        print(f"Successfully downloaded {anime_name} - {chp_number}")
        
        
        
    def download_all(self,anime_name):
        chp_list = chapter_list(anime_name) #finding all chapters present for manga
        chp_count = chp_list.scrap()
        for i in range(len(chp_count)):  #iterating over all chapters 
            img_fetch = image_fetcher(i,anime_name)     
            self.download_chapter(i,anime_name)
d = downloader()
d.download_chapter(sys.argv[len(sys.argv)-2],sys.argv[len(sys.argv)-1])