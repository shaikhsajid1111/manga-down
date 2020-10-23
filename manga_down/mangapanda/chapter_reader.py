try:
    import requests
    import urllib3
    from fake_headers import Headers
    from . import chapter_list 
    from bs4 import BeautifulSoup
    import re
    import os
    import time
    import random
except Exception as ex:
    print(ex)

class Chapter_reader:
    def __init__(self,manga,chapter_number):
        self.manga = manga
        self.chapter_number = chapter_number    

    def get_image_links(self):
        """returns a list of image link for a given chapter"""
        #make a request to server and scrap all present chapter for manga
        manga_chapters = chapter_list.Chapter_list(self.manga).get_links()
        #we get a list where chapter is listed in descending order, so we'll reverse it to ascending order
        manga_chapters.reverse()
        
        #store chapter that has to be scrapped
        chapter_to_scrap = manga_chapters[int(self.chapter_number)-1]
        
        urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning) 
        
        #send request to server with given chapter URL
        response = requests.get(chapter_to_scrap,headers = Headers().generate(),verify=False)

        if response.status_code >= 400 and response.status_code < 500:
            #if response was code is 400-499
            print("Server error,Please try again later")
            exit()
        if response.status_code >= 200 and response.status_code < 300:
            #if successful response 
            soup = BeautifulSoup(response.content,"html.parser")    
            
            all_tags = re.findall('"u":".*?"',soup.prettify())   #using regex find all url present in js code
            
        
            all_urls = [f"https:"+url.split(":")[2].replace('"','').replace("\\","") for url in all_tags]
            
            return all_urls      
    def __create_folder(self):

        if os.path.isdir(os.path.join(os.getcwd(), f'{self.manga}')):
                # changing current directory to folder
                os.chdir(os.path.join(os.getcwd(), f'{self.manga}'))
            # if chapter folder exists
                if os.path.isdir(os.path.join(os.getcwd(), f'{self.chapter_number}')):
                    # just change the CWD to this folder
                    os.chdir(os.path.join(os.getcwd(), f'{self.chapter_number}'))
                    print("Starting download ...")
                else:
                    # create chapter folder
                    os.mkdir(f'{self.chapter_number}')
                # change directory to chapter folder
                    os.chdir(os.path.join(os.getcwd(), f'{self.chapter_number}'))
        else:
                # making folder with same manga name
            os.mkdir(f'{self.manga}')
            print(f"Folder created {self.manga}")
            # canging directory to that above created folder
            os.chdir(os.path.join(os.getcwd(), f'{self.manga}'))
            # ceating /manga/chapter_number
            os.mkdir(f'{self.chapter_number}')
            # ceating chapter folder inside current folder
            os.chdir(os.path.join(os.getcwd(), f'{self.chapter_number}'))
        return "Starting download ..."



    def __download(self,URL,file_name):
        headers = Headers().generate()
        response = requests.get(URL, stream=True,headers = headers,verify = False)
                
        if response.status_code == 200:
            with open(f'{self.manga} - {file_name}.jpg', 'wb') as file:
                file.write(response.content)    
                return True
        return False
    

    def download_chapter(self,file_location = os.getcwd()):
        '''download the chapter'''
        try:
            if not os.path.exists(file_location):
                file_location = os.getcwd()

            print(f"Searching for {self.manga}")
            
            time.sleep(random.randint(1, 5))
            
            print(f"Succesfully fetched all images on the server...\nCreating Folder {self.manga}...")
            
            # folder creating process
            
            os.chdir(file_location)

            self.__create_folder()
            
            # loops through all image links, send a response and if response is success,
            # write that response.content as binary as images'''
            urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)         #hiding the warning
            #chapter_r = chapter_reader.Chapter_reader(manga_name,self.chapter_number)
            img_links = self.get_image_links()
            print(f'{len(img_links)+1} Pages to download...')
            
            for i in range(len(img_links)):
                res = self.__download(img_links[i],f"{self.manga} - Page {i+1}")
                if res:
                        print(f"{self.manga} - Chapter : {self.chapter_number} Page :{i+1} downloaded...")
                        print(f'Remaining {len(img_links)-i}')    
                        time.sleep(random.randint(5, 10))
                else:
                    print(f"Could not able to download {i+1} page")

            return f"Successfully downloaded {self.manga} - {self.chapter_number}\nEnjoy the manga!:)\nBye"
        
        except IndexError:
            print(f"{self.chapter_number} does not exist!")
        except KeyboardInterrupt:
            print("Bye")
            exit()
        except Exception as ex:
            print(ex)




