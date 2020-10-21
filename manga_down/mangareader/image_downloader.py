try:
    import requests
    from . import chapter_list
    from . import chapter_reader
    import os
    import time
    import random
    from fake_headers import Headers
    import urllib3
    import re
    import argparse
except Exception as ex:
    print(ex)
    exit()
class downloader:

    def __init__(self,manga,chp_number):
        '''downloader class downloads all images by sending response to the server, and writing them as 'wb' '''
        self.manga = manga
        self.chp_number = chp_number
    
    def __url_generator(self, keywords):
        '''private method to make anime names URL friendly'''
        all_words = re.sub(r'[?|$|%|&|#]',r'-',keywords)
        all_words = keywords.split(" ")
        all_words = [all_words[i] for i in range(len(all_words)) if all_words[i] != '']
       
        keyword = '-'.join(all_words)

        return keyword.lower()


    def download_chapter(self,file_location = os.getcwd()):
        '''expected parameters are 
        chapter number-> chapter number for manga(int),
        manga_name -> manga name e.g naruto
        '''

        try:
            manga_name = self.__url_generator(self.manga)

            print(f"Searching for {manga_name}")
            
            time.sleep(random.randint(1, 5))
            
            print(f"Succesfully fetched all images on the server...\nCreating Folder {manga_name}...")
            # folder creating process
            
            os.chdir(file_location)

            # if folder exists
            if os.path.isdir(os.path.join(os.getcwd(), f'{manga_name}')):
                # changing current directory to folder
                os.chdir(os.path.join(os.getcwd(), f'{manga_name}'))
            # if chapter folder exists
                if os.path.isdir(os.path.join(os.getcwd(), f'{self.chp_number}')):
                    # just change the CWD to this folder
                    os.chdir(os.path.join(os.getcwd(), f'{self.chp_number}'))
                    print("Starting download ...")
                else:
                    # create chapter folder
                    os.mkdir(f'{self.chp_number}')
                # change directory to chapter folder
                    os.chdir(os.path.join(os.getcwd(), f'{self.chp_number}'))

                print("Starting download ...")
            else:
                # making folder with same manga name
                os.mkdir(f'{manga_name}')
                print(f"Folder created {manga_name}")

            # changing directory to that above created folder
                os.chdir(os.path.join(os.getcwd(), f'{manga_name}'))

            # creating /manga/chapter_number
                os.mkdir(f'{self.chp_number}')

            # creating chapter folder inside current folder
                os.chdir(os.path.join(os.getcwd(), f'{self.chp_number}'))
                print("Starting download ...")

            # '''
             # loops through all image links, send a response and if response is success,
              #  write that response.content as binary as images'''
            headers = Headers(headers=False).generate()
            urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)         #hiding the warning
            chapter_r = chapter_reader.Chapter_reader(manga_name,self.chp_number)
            img_links = chapter_r.get_image_links()
            print(f'{len(img_links)} Pages to download...')
            
            for i in range(len(img_links)):
                response = requests.get(img_links[i], stream=True,headers = headers,verify = False)
                
                if response.status_code == 200:
                    with open(f'{manga_name} - Page {i+1}.jpg', 'wb') as file:
                        file.write(response.content)
                        print(
                            f"{manga_name} - Chapter : {self.chp_number} Page :{i+1} downloaded...")
                        print(f'Remaining {len(img_links)-i}')    
                    time.sleep(random.randint(5, 10))
                else:
            
                    print(f"Could not able to download {i+1} page")
            print(f"Successfully downloaded {manga_name} - {self.chp_number}\nEnjoy the manga!:)\nBye")

        except IndexError:
            print(f"{self.chp_number} does not exist!")
        except KeyboardInterrupt:
            print("Bye")
            exit()
        except Exception as ex:
            print(ex)

#    def download_all(self, anime_name):
#        """expected parameters, anime_name -> anime's name"""
#        try:
#            anime_name = self.__url_generator(anime_name)
#            print(f"Searching for {anime_name}")
#            # finding all chapters present for manga
#            chp_list = chapter_list(anime_name)
#            chp_count = chp_list.scrap()
#                
#            for i in range(len(chp_count)):  # iterating over all chapters
#                img_fetch = image_fetcher(i, anime_name)
#                self.download_chapter(i, anime_name)
#        except Exception as ex:
#            print(ex)

