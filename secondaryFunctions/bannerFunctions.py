import requests
from PIL import Image
import os
from requests import get  #pip install requests
from bs4 import BeautifulSoup #pip install beautifulsoup4
from time import sleep
from random import randint

#Banner main
def getBanner(container, titleXMLPic, years):
     
    if container.find(class_ = 'loadlate') is not None:
        banner = container.find(class_ = 'loadlate')
        bannerUrl = bannerCodeClean(banner)
        downloadBanner(bannerUrl,titleXMLPic, years)


def bannerCodeClean(banner):

    bannerMod = str(banner) #bs4.element.Tag to str
    bannerMod = bannerMod.split("height=\"98\" loadlate=\"",1)[1]
    bannerMod = bannerMod.split("\" src=", 1)[0]

    return bannerMod


def downloadBanner(bannerURL, titleXMLPic, years):
    img_url = bannerURL
    img = Image.open(requests.get(img_url, stream = True).raw)
    newImgSize = (112, 168)
    img = img.resize(newImgSize)

    image_path = "images"
    if(os.path.exists(image_path) == False):
        os.mkdir(image_path) ##creates folder as images

    saveName =  titleXMLPic + "_" + years +"_p.png"

    ##Looks horrible, need to find another source
    img.save(f"{image_path}/{saveName}")
    



#Banner Alter Main --- DOESNT WORK

def getBannerAlter(bannerContainer, headers):
    
    for singleBanner in bannerContainer:
        for title, titleXMLPic, years in singleBanner:
            bannerContainer = getBannerConnection(title, years, headers)
            getBannerFormatted(bannerContainer)
     

def getBannerConnection(title, years, headers):
    response = get(f"https://www.movieposters.com/collections/shop?q={title}+{years}", headers=headers)
    sleep(randint(8,15))

    if response.status_code != 200:
    #warn('Request: {}; Status code: {}'.format(requests, response.status_code)) gets issues with requests
        print ("beep boop, not 200!!!")
    

    page_html = BeautifulSoup(response.text, 'html.parser')
    return page_html
    #bannerContainer = page_html.find_all('div', class_ = 'js-anime-category-producer')


def getBannerFormatted(bannerContainer):
    bannerFormatted = bannerContainer.find_all('div', class_ = 'grid grid--uniform')
    print(f"bannerFormatted:{bannerFormatted}")







#Anime Banner main

def getAnimeBanner(container, titleXMLPic, years):

    if container.find('div', class_ = 'image') is not None:
        animeBanner = container.find('div', class_ = 'image')
        animeBannerFix = animeBannerFormat(str(animeBanner))
        #print(animeBannerFix)
        downloadBanner(animeBannerFix, titleXMLPic, years)    


def animeBannerFormat(animeBanner):

    try:
        animeBannerFix = animeBanner.split("src=\"", 1)
        animeBannerFix = animeBannerFix[1].split("\"", 1)
        return animeBannerFix[0]
    except:
        return ""



