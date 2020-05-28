import requests
from image_fetcher import image_fetcher
from chapter_list import chapter_list
import os
import time
import random
import sys
import fake_useragent

class downloader:

    '''downloader class downloads all images by sending response to the server, and writing them as 'wb' '''

    def __url_generator(self, keywords):
        '''private method to make anime names URL friendly'''
        
        all_words = keywords.split(" ")
        all_words = [all_words[i] for i in range(len(all_words)) if all_words[i] != '']
        
        keyword = '-'.join(all_words)

        return keyword.lower()

    def download_chapter(self, chp_number, anime_name):
        '''expected parameters are 
        chapter number-> chapter number for manga(int),
        anime_name -> manga name e.g naruto
        '''
        
        try:
            anime_name = self.__url_generator(anime_name)
         
            print(f"Searching for {anime_name}")
            
            img_fetch = image_fetcher(chp_number, anime_name)

            img_links = img_fetch.scrap()
            time.sleep(random.randint(1, 5))
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
            print("Changing user agent...")
            headers = fake_useragent.get_user_agent()
            print("User Agent changed...")
            print(f'{len(img_links)} Pages to download...')

            
            for i in range(len(img_links)):
                response = requests.get(img_links[i], stream=True,verify = False,headers = headers)
                if response.status_code == 200:
                    with open(f'{anime_name} - Page {i+1}.jpg', 'wb') as file:
                        file.write(response.content)
                        print(f"{anime_name} - Chapter : {chp_number} Page :{i+1} downloaded...")
                        print(f'Remaining {len(img_links) - (i+1)}...')
                    time.sleep(random.randint(6, 14))
                else:
                    print(f"Could not able to download {i+1} page")
            print(f"Successfully downloaded {anime_name} - {chp_number}\nEnjoy Reading the manga\nHave a great day! :)")

        except IndexError:
            print(f"{chp_number} does not exist!")
        except KeyboardInterrupt:
            print("Have a great day! :)\nBye")
            exit()
        except Exception as ex:
            print(ex)
        
    def download_all(self, anime_name):
        """expected parameters, anime_name -> anime's name"""
        try:
            anime_name = self.__url_generator(anime_name)
            print(f"Searching for {anime_name}")
            # finding all chapters present for manga
            chp_list = chapter_list(anime_name)
            chp_count = chp_list.scrap()
                
            for i in range(len(chp_count)):  # iterating over all chapters
                img_fetch = image_fetcher(i, anime_name)
                self.download_chapter(i, anime_name)
        except Exception as ex:
            print(ex)


d = downloader()
d.download_chapter((sys.argv[len(sys.argv)-2]), sys.argv[len(sys.argv)-1])#int(
