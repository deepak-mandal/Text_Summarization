import requests
from bs4 import BeautifulSoup
import os

def imagedown(url, folder):
    try:
        os.mkdir(os.path.join(os.getcwd(), folder))
    except:
        pass
    os.chdir(os.path.join(os.getcwd(), folder))
    
    r = requests.get(url)
    soup = BeautifulSoup(r.text, 'html.parser')
    images = soup.find_all('img')
    for image in images:
        name = image['alt']
        link = image['src']
        with open(name.replace(' ', '-').replace('/', '') + '.jpg', 'wb') as f:     #write binary
            im = requests.get(link)
            f.write(im.content)
            print('writting', name)






# -*- coding: utf-8 -*-
"""
Created on Wed Jun  9 13:26:42 2021

@author: dkmii
"""

import bs4
import requests
import shutil

#url=input("enter your URL: ")
url = "https://www.airbnb.co.in/s/Ljubljana--Slovenia/homes?tab_id=home_tab&refinement_paths%5B%5D=%2Fhomes&flexible_trip_dates%5B%5D=july&flexible_trip_dates%5B%5D=june&flexible_trip_lengths%5B%5D=weekend_trip&date_picker_type=calendar&query=Ljubljana%2C%20Slovenia&place_id=ChIJ0YaYlvUxZUcRIOw_ghz4AAQ&checkin=2021-06-16&checkout=2021-06-17&disable_auto_translation=false&source=structured_search_input_header&search_type=autocomplete_click"
response = requests.get(url)

print(type(response))
print(response.text)

filename = "temp.html"

bs = bs4.BeautifulSoup(response.text, "html.parser")
formatted_text = bs.prettify()

print(formatted_text)


#To get the formatted HTML file for source code
try:
    with open(filename, "w+", encoding="utf-8") as f:    #w: write; w+ : if not then create
        f.write(formatted_text)
except Exception as e:
    print(e)
    
list_imgs = bs.find_all("img")

#print(list_imgs)

no_of_imgs = len(list_imgs)
list_as = bs.find_all("a")  #anchor tags

no_of_as = len(list_as)

#print("number of img tags ", no_of_imgs)
#print("number of anchor tags ", no_of_as)

j = 1
for imgTag in list_imgs:
    #print(imgTag)
    try:
        imgLink = imgTag.get("src")
        print(imgLink)
        imgName = imgTag.get("alt")
        print(imgName)
    
        #for image extention
        ext = imgLink[imgLink.rindex('.'): ]
        if ext.startswith(".png"):
            ext=".png"
        elif ext.startswith(".jpeg"):
            ext = ".jpeg"
        elif ext.startswith(".jpg"):
            ext=".jpg"
        elif ext.startswith(".svg"):
            ext=".svg"
        
        #print(ext)
        filen = str(j)+ext
        res = requests.get(imgLink, stream = True)
        
        with open(filen, "wb") as file:
            shutil.copyfileobj(res.raw, file)
    except Exception as e:
        print(e)
            
    j+=1































    

            
if __name__ == "__main__":
    url = "https://www.airbnb.co.in/s/Ljubljana--Slovenia/homes?tab_id=home_tab&refinement_paths%5B%5D=%2Fhomes&flexible_trip_dates%5B%5D=july&flexible_trip_dates%5B%5D=june&flexible_trip_lengths%5B%5D=weekend_trip&date_picker_type=calendar&query=Ljubljana%2C%20Slovenia&place_id=ChIJ0YaYlvUxZUcRIOw_ghz4AAQ&checkin=2021-06-16&checkout=2021-06-17&disable_auto_translation=false&source=structured_search_input_header&search_type=autocomplete_click"
    imagedown(url, 'img_down')



