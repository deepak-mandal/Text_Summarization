# -*- coding: utf-8 -*-
"""
Created on Wed Jun  9 13:25:28 2021

@author: dkmii
"""

# -*- coding: utf-8 -*-
"""
Created on Wed Jun  9 12:03:18 2021

@author: dkmii
"""

import requests
from bs4 import BeautifulSoup
import os

#url = ""

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
        name = image.get("alt")#['alt']
        link = image.get("src")#['src']
        #imgName = imgTag.get("alt")
        #print(imgName)
        print(name, "---", link)
        with open(name.replace(' ', '-').replace('/', '') + '.jpg', 'wb') as f:     #write binary
            im = requests.get(link)
            f.write(im.content)
            print('writting', name)
   
            
if __name__ == "__main__":
    url = "https://www.airbnb.co.in/s/Ljubljana--Slovenia/homes?tab_id=home_tab&refinement_paths%5B%5D=%2Fhomes&flexible_trip_dates%5B%5D=july&flexible_trip_dates%5B%5D=june&flexible_trip_lengths%5B%5D=weekend_trip&date_picker_type=calendar&query=Ljubljana%2C%20Slovenia&place_id=ChIJ0YaYlvUxZUcRIOw_ghz4AAQ&checkin=2021-06-16&checkout=2021-06-17&disable_auto_translation=false&source=structured_search_input_header&search_type=autocomplete_click"
    imagedown(url, 'img_down')

        
        
        