from image_link_fetch import image_fetcher
import os
from fake_headers import Headers
import urllib3
import random
import time
import requests
import sys
class image_downloader:
    @staticmethod
    def download_chapter(chp_number:int,anime_name):
        try:
            #anime_name = self.__url_generator(anime_name)
            print(f"Searching for {anime_name}")
            
            img_links = image_fetcher.image_links(anime_name,int(chp_number))
            print(img_links)
            print(f"Succesfully fetched all images on the server...\nCreating Folder {anime_name}...")
            # folder creating process
            # if folder exists
            if os.path.isdir(os.path.join(os.getcwd(), f'{anime_name}')):
                # changing current directory to folder
                os.chdir(os.path.join(os.getcwd(), f'{anime_name}'))
            # if chapter folder exists
                if os.path.isdir(os.path.join(os.getcwd(), f'{chp_number}')):
                    # just change the CWD to this folder
                    os.chdir(os.path.join(os.getcwd(), f'{chp_number}'))
                    print("Starting download ...")
                else:
                    # create chapter folder
                    os.mkdir(f'{chp_number}')
                # change directory to chapter folder
                    os.chdir(os.path.join(os.getcwd(), f'{chp_number}'))

                print("Starting download ...")
            else:
                # making folder with same anime name
                os.mkdir(f'{anime_name}')
                print(f"Folder created {anime_name}")

            # changing directory to that above created folder
                os.chdir(os.path.join(os.getcwd(), f'{anime_name}'))

            # creating /anime/chapter_number
                os.mkdir(f'{chp_number}')

            # creating chapter folder inside current folder
                os.chdir(os.path.join(os.getcwd(), f'{chp_number}'))
                print("Starting download ...")

            # '''
             # loops through all image links, send a response and if response is success,
              #  write that response.content as binary as images'''
            headers = Headers(headers=False).generate()
            urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)         #hiding the warning
            
            print(f'{len(img_links)} Pages to download...')
            
            for i in range(len(img_links)):
                response = requests.get(img_links[i], stream=True,headers = headers,verify = False)
                if response.status_code == 200:
                    with open(f'{anime_name} - Page {i+1}.jpg', 'wb') as file:
                        file.write(response.content)
                        print(
                            f"{anime_name} - Chapter : {chp_number} Page :{i+1} downloaded...")
                        print(f'Remaining {len(img_links)-i}')    
                    time.sleep(random.randint(5, 10))
                else:
            
                    print(f"Could not able to download {i+1} page")
            print(f"Successfully downloaded {anime_name} - {chp_number}\nEnjoy the manga!:)\nBye")

        except IndexError:
            print(f"{chp_number} does not exist!")
        except KeyboardInterrupt:
            print("Bye")
            exit()
        except Exception as ex:
            print(ex)

image_downloader.download_chapter(4,'bleach')   
   