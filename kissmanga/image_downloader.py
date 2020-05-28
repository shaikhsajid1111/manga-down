from image_link_fetcher import image_fetch
import sys
import os
import requests
import random
import time
import re
class image_downloader:
    def url_generator(self,anime_name):
        #anime_name.replace('?','-')
        anime_name = re.sub(r'[?|$|%|&|#]',r'-',anime_name)
        keyword_list = anime_name.split(" ")
        keyword = '-'.join(keyword_list)
        return keyword.capitalize()

    def download_chapter(self,chp_number,anime):
        '''Downloads a chater'''
        img_fetcher = image_fetch(chp_number,anime)     #image_fetch class object instantiation

        img_links = img_fetcher.scrap()             #fetching all image links
        #if all images links are found
        print("Image has been fetched on the server...")

        #folder creating process
        if os.path.isdir(os.path.join(os.getcwd(),f'{anime}')):    #if folder exists with name same as manga
            #changing current directory to the same manga folder
            os.chdir(os.path.join(os.getcwd(),f'{anime}'))
            #if chapter folder exists inside that folder as well
            if os.path.isdir(os.path.join(os.getcwd(),f'{chp_number}')):
                #than just change the CWD to this folder
                os.chdir(os.path.join(os.getcwd(),f'{chp_number}'))
                #and start downloading
                print(f"Folder created\nStarting download ...")
            else:
                #create chapter folder
                os.mkdir(f'{chp_number}')
                #change directory to chapter folder
                os.chdir(os.path.join(os.getcwd(),f'{chp_number}'))
                
                print("Folder created\nStarting download ...")
        else:
            #making folder with same anime name
            os.mkdir(f'{anime}')
            print(f"Folder created {anime}\nStarting download")

            #changing directory to that above created folder
            os.chdir(os.path.join(os.getcwd(),f'{anime}'))
            
            # creating /anime/chapter_number
            os.mkdir(f'{chp_number}')

            #creating chapter folder inside current folder
            os.chdir(os.path.join(os.getcwd(),f'{chp_number}'))         
            
            print("Folder created\nStarting download ...") 

            print(f'{len(img_links)} Pages to download...')
        
        for i in range(len(img_links)):     #iterating over all inage's link in the list
            response = requests.get(img_links[i],stream = True)         #sending response to that link
            if response.status_code == 200:         #if response is success
                #write image file with sructure of naming convention, [anime_name - Page - Page_number]
                with open(f'{anime} - Page {i+1}.jpg','wb') as file:
                    file.write(response.content)            #writing the content to the file
                    #status showing that it is downloaded
                    print(f"{anime} - Chapter : {chp_number} Page :{i+1} downloaded...")        
                    print(f'Remaining {len(img_links)-(i+1)} pages..')
                #stop the code execution between 5-10 secs randomly that server does not block 
                time.sleep(random.randint(5,10))
            else:
                print(f"Could not able to download {i+1} page")
        return f"Successfully downloaded {anime} - {chp_number}"
        
usr = image_downloader()
chapter_number = int(sys.argv[len(sys.argv)-2])-1
manga_name = sys.argv[len(sys.argv)-1]
print(usr.download_chapter(chapter_number,manga_name))        