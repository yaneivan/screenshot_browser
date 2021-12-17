from bs4 import BeautifulSoup
import requests
import numpy as np
import cv2
import string    
import os   
os.system('mkdir folder')
def parse_website(link):
    html_text = requests.get(link, headers={'User-Agent': 'Chrome'}).text
    soup = BeautifulSoup(html_text, 'lxml')
    photo_part = soup.find('img', class_='no-click screenshot-image')
    return photo_part['src']

def get_picture(link):
    resp = requests.get(link, stream=True).raw
    image = np.asarray(bytearray(resp.read()), dtype="uint8")
    image = cv2.imdecode(image, cv2.IMREAD_COLOR)
    return image

print("Welcome to screenshot-browser. Use space to save image ")

flag = False
t = string.ascii_lowercase
for i in range(len(t)):
    i = t[i]
    for k in range(len(t)):
        k = t[k]
        for num in range(4, 10000):
            try:
            
                link_to_src = 'https://prnt.sc/'
                link_to_src = link_to_src + i + k+ ('0' * (4-len(str(num)))) + str(num)

                link = parse_website(link_to_src)
                img = get_picture(link)

                cv2.imshow('picture', img)
                a = cv2.waitKey(0)
                print(a)
                name = str(i)+str(k)+str(num)
                if a == 32:
                    path = __file__
                    path = path.replace('main.py', '')
                    path = path + 'folder\\'+name +'.png'
                    cv2.imwrite(path, img)
                    print(path)
                elif a == 27:                   
                    flag = True
            except:
                print('something broke: ' + link_to_src)
            if flag:
                exit()