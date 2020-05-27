from image_link_fetcher import image_fetch
import sys
import os
import requests
import random
import time
class image_downloader:
    def url_generator(self,anime_name):
        keyword_list = anime_name.split(" ")
        keyword = '-'.join(keyword_list)
    
        return keyword.capitalize()

    def download_chapter(self,chp_number,anime):
        
        img_fetcher = image_fetch(chp_number,anime)

        img_links = img_fetcher.scrap()

        #folder creating process
        if os.path.isdir(os.path.join(os.getcwd(),f'{anime}')):    #if folder exists
            #changing current directory to folder
            os.chdir(os.path.join(os.getcwd(),f'{anime}'))
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
            os.mkdir(f'{anime}')
            print(f"Folder created {anime}")

            #changing directory to that above created folder
            os.chdir(os.path.join(os.getcwd(),f'{anime}'))
            
            # creating /anime/chapter_number
            os.mkdir(f'{chp_number}')

            #creating chapter folder inside current folder
            os.chdir(os.path.join(os.getcwd(),f'{chp_number}'))         
            print("Starting download ...")     
            print(f'{len(img_links)} Pages to download...')
        for i in range(len(img_links)):
            response = requests.get(img_links[i],stream = True)
            if response.status_code == 200:
                with open(f'{anime} - Page {i+1}.jpg','wb') as file:
                    file.write(response.content)
                    print(f"{anime} - Chapter : {chp_number} Page :{i+1} downloaded...")
                    print(f'Remaining {len(img_links)-(i+1)}')
                time.sleep(random.randint(5,10))
            else:
                print(f"Could not able to download {i+1} page")
        return f"Successfully downloaded {anime} - {chp_number}"
        
usr = image_downloader()
print(usr.download_chapter(221,'naruto'))        