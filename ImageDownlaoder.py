'''
The program name is ImageDownlaoder

Program is used to downlaod oimages of Aamir Khan from aweb page and store in folder

main modules used are 
    1.bs4: Beautiful Soup(bs4)=> is a Python library for pulling data out of HTML and XML files. This module does not come built-in with Python.
    2.requests=>Requests allows you to send HTTP/1.1 requests extremely easily. This module also does not come built-in with Python.
    3.OS=>The OS module in python provides functions for interacting with the operating system. OS, comes under Python’s standard utility modules. 



'''




from urllib.request import urlopen
from bs4 import BeautifulSoup
import requests
import os



#Function for creating folder
def create_folder(images):
    try: 
        folder_name = input("Enter Folder Name:- ") 
        # folder creation 
        os.mkdir(folder_name) 
  
    # if folder exists with that name, ask another name 
    except: 
        print("Folder Exist with that name!") 
        create_folder(images) 
  
    # image downloading start 
    download_images(images, folder_name) 
  
#function for downloading images into folder
def download_images(images,folder_name):
    for i, image in enumerate(images):  
        #check wether the image is Aamir Khan's
        try: 
                # In image tag ,searching for "data-srcset" 
                image_link = image["data-srcset"] 
                  
            # then we will search for "data-src" in img  
            # tag and so on.. 
        except: 
            try: 
                # In image tag ,searching for "data-src" 
                image_link = image["data-src"] 
            except: 
                try: 
                    # In image tag ,searching for "data-fallback-src" 
                    image_link = image["data-fallback-src"] 
                except: 
                    try: 
                        # In image tag ,searching for "src" 
                        image_link = image["src"] 
  
                    # if no Source URL found 
                    except: 
                        pass

        if 'aamirkhan' in image:
            try: 
                    #request for link for downlaoding          
                    r = requests.get(image_link).content 
                    try: 
  
                        # possibility of decode 
                        r = str(r, 'utf-8') 
  
                    except UnicodeDecodeError: 
  
                        # After checking above condition, Image Download start 
                        with open(f"{folder_name}/images{i+1}.jpg", "wb+") as f: 
                            #downlaod image into folder
                            f.write(r) 
  
            except: 
                pass
    



url="https://www.indiaglitz.com/aamir-khan-photos-hindi-actor-2628990-7950"
r=requests.get(url)
soup=BeautifulSoup(r.text,'html.parser')
images=bs.soup.findAll('img')
create_folder(images)