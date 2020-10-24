try:
    import requests 
    from bs4 import BeautifulSoup
    from .chapter_list import Chapter_list
    from fake_headers import Headers
    import re
    import time
    import os
    import random
    import urllib3
except Exception as ex:
    print(ex)
    exit()

class Chapter_reader(Chapter_list):
    
    def __init__(self, manga):   #chapter_number and manga_name
        """
        instantiate chapter_reader class 
        """
        self.manga = self.URLify(manga)
        self.URL = f"http://www.mangareader.net/{self.URLify(self.manga)}"

    def get_image_links(self,chapter_number):
        """returns all image links present for manga chapter"""
        
        URLS = self.get_links()             #all chapters
   
        headers = Headers(headers=False).generate()        
        urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning) #disable warning
        response = requests.get(URLS[int(chapter_number)-1],headers = headers,verify = False)            #chapter number
        
        if response.status_code == 404:
            print("Error Occured!")
            exit()
        if response.status_code == 200:
            soup = BeautifulSoup(response.content,"html.parser")    

            all_tags = re.findall('"u":".*?"',soup.prettify())
            all_image_urls = ["https:"+url.split(":")[1].replace('"','').replace("\\","") for url in all_tags]
            return all_image_urls
            
    
    def create_folder(self,chapter_number):

        if os.path.isdir(os.path.join(os.getcwd(), f'{self.manga}')):
                # changing current directory to folder
                os.chdir(os.path.join(os.getcwd(), f'{self.manga}'))
            # if chapter folder exists
                if os.path.isdir(os.path.join(os.getcwd(), f'{chapter_number}')):
                    # just change the CWD to this folder
                    os.chdir(os.path.join(os.getcwd(), f'{chapter_number}'))
                    print("Starting download ...")
                else:
                    # create chapter folder
                    os.mkdir(f'{chapter_number}')
                # change directory to chapter folder
                    os.chdir(os.path.join(os.getcwd(), f'{chapter_number}'))
        else:

            # making folder with same manga name
            os.mkdir(f'{self.manga}')
            print(f"Folder created {self.manga}")
            # canging directory to that above created folder
            os.chdir(os.path.join(os.getcwd(), f'{self.manga}'))
            # ceating /manga/chapter_number
            os.mkdir(f'{chapter_number}')
            # ceating chapter folder inside current folder
            os.chdir(os.path.join(os.getcwd(), f'{chapter_number}'))
        return "Starting download ..."



    def download(self,URL,file_name):
        """expects image links,downloads them, if download was succesful,return True else False"""
        headers = Headers().generate()
        
        image_extension = URL.split(".")[-1]
        urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning) 
        response = requests.get(URL, stream=True,headers = headers,verify = False)
                
        if response.status_code == 200:
            with open(f'{self.manga} - {file_name}.{image_extension}', 'wb') as file:
                file.write(response.content)    
                return True
        return False
    

    def download_chapter(self,chapter_number,file_location = os.getcwd()):
        '''download the chapter'''
        try:
            if not os.path.exists(file_location):
                file_location = os.getcwd()

            print(f"Searching for {self.manga}")
            
            time.sleep(random.randint(1, 5))
            
            print(f"Succesfully fetched all images on the server...\nCreating Folder {self.manga}...")
            
            # folder creating process
            
            os.chdir(file_location)

            self.create_folder(chapter_number)
            
            # loops through all image links, send a response and if response is success,
            # write that response.content as binary as images

            urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)         #hiding the warning
            
            img_links = self.get_image_links(chapter_number)
            print(f'{len(img_links)+1} Pages to download...')
            
            for i in range(len(img_links)):
                download_result = self.download(img_links[i],f"{self.manga} - Page {i+1}")
                if download_result:
                        print(f"{self.manga} - Chapter : {chapter_number} Page :{i+1} downloaded...")
                        print(f'Remaining {len(img_links)-i}')    
                        time.sleep(random.randint(5, 10))
                else:
                    print(f"Could not able to download {i+1} page")

            return f"Successfully downloaded {self.manga} - {chapter_number}\nEnjoy the manga!:)\nBye"
        
        except IndexError:
            print(f"{chapter_number} does not exist!")
        except KeyboardInterrupt:
            print("Bye")
            exit()
        except Exception as ex:
            print(ex)
