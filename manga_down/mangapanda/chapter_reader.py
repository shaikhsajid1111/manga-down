try:
    import requests
    import urllib3
    from fake_headers import Headers
    from .chapter_list import Chapter_list 
    from bs4 import BeautifulSoup
    import re
    import os
    import time
    import random
except Exception as ex:
    print(ex)

class Chapter_reader(Chapter_list):
    def __init__(self,manga):
        self.manga = self.URLify(manga)
        self.URL = f"https://mangapark.net/manga/{self.URLify(self.manga)}/"
    def get_image_links(self,chapter_number):
        """returns a list of image link for a given chapter"""
        #make a request to server and scrap all present chapter for manga
        manga_chapters = self.get_links()  #calling from base class Chapter_list
    
        #we get a list where chapter is listed in descending order, so we'll reverse it to ascending order
        manga_chapters.reverse()
        
        #store chapter that has to be scrapped
        chapter_to_scrap = manga_chapters[int(chapter_number)-1]
        
        urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning) #disable warning
        
        #send request to server with given chapter URL
        response = requests.get(chapter_to_scrap,headers = Headers().generate(),verify=False)

        if response.status_code >= 400 and response.status_code < 500:
            #if response status code is 400-499
            print("Server error,Please try again later")
            exit()
        if response.status_code >= 200 and response.status_code < 300:
            #if successful response 
            soup = BeautifulSoup(response.content,"html.parser")    
            
            all_tags = re.findall('"u":".*?"',soup.prettify())   #using regex find all url present in js code
            
        
            all_urls = [f"https:"+url.split(":")[2].replace('"','').replace("\\","") for url in all_tags]
            
            return all_urls      
    
    def create_folder(self,chapter_number):
        #if folder with name of given manga exists already
        if os.path.isdir(os.path.join(os.getcwd(), f'{self.manga}')):
                # changing current directory to given manga name folder
                os.chdir(os.path.join(os.getcwd(), f'{self.manga}'))
                
                # if folder with name as given chapter also exists in the folder
                if os.path.isdir(os.path.join(os.getcwd(), f'{chapter_number}')):
                    # just set the current working directory to this one, and exit function
                    os.chdir(os.path.join(os.getcwd(), f'{chapter_number}'))
                    
                    return "Starting download ..."   #exit
                else:
                    # create the chapter folder with given manga name
                    os.mkdir(f'{chapter_number}')
                    # change current working directory to newly created folder
                    os.chdir(os.path.join(os.getcwd(), f'{chapter_number}'))
                    return "Starting download ..."
        #if folder with name of given manga does not exist
        else:

            # making folder with same manga name
            os.mkdir(f'{self.manga}')
            # changing directory to that above created folder
            os.chdir(os.path.join(os.getcwd(), f'{self.manga}'))
            # ceating /manga/chapter_number folder
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
            # write that response.content as binary as images'''
            urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)         #hiding the warning
            
            img_links = self.get_image_links(chapter_number)
            print(f'{len(img_links)+1} Pages to download...')
            
            for i in range(len(img_links)):
                res = self.download(img_links[i],f"{self.manga} - Page {i+1}")
                if res:
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




