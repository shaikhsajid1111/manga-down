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
    '''
    base class is Chapter_list, so,
    - URLify() method is inherited from Chapter_list
    - get_links() method is inherited as well
    '''
    def __init__(self, manga):   #constructor needs manga by default
        """
        instantiate chapter_reader class 
        """
        self.manga = self.URLify(manga)
        self.URL = f"http://mangareader.cc/manga/{self.URLify(self.manga)}"

    def get_image_links(self,chapter_number):
        """returns all image links present for manga chapter"""
        
        URLS = self.get_links()             #all chapters, method from Chapter_list class(base class)
   
        headers = Headers(headers=False).generate()        
        
        urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning) #disable warning
        
        response = requests.get(URLS[int(chapter_number)],headers = headers,verify = False)            #chapter number
        
        if response.status_code < 500 and response.status_code >= 400:   #if server error 
            print("Server Error!\nTry Again later")
            exit()

        if response.status_code >= 200 and response.status_code < 300:
            #if response is success

            soup = BeautifulSoup(response.content,"html.parser") #make bs4 object with response's content and parser is html.parser   
            
            paragraph = soup.find("p",{"id":"arraydata"})

            all_image_hrefs = paragraph.text.split(',')

            return all_image_hrefs
            
    
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
            #if given directory is invalid than download in current directory
            if not os.path.exists(file_location):
                file_location = os.getcwd()

            print(f"Searching for {self.manga}")
            
            time.sleep(random.randint(1, 5))
            
            print(f"Succesfully fetched all images on the server...\nCreating Folder {self.manga}...")
            
            # folder creating process
            
            os.chdir(file_location)

            self.create_folder(chapter_number) #change directory to where image has to been downloaded
            
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
