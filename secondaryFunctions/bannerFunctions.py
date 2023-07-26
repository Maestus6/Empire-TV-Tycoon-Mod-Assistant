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
    



#Banner Alter Main 

def getBannerAlter(bannerContainer, headers):
    
    for singleBanner in bannerContainer:
        for movieUrl, titleXMLPic, years in singleBanner:
            bannerFullHTML = getBannerConnection(movieUrl, headers)
            #print (f"bannerFullHTML = {bannerFullHTML}")
            #for singeBannerHTML in bannerFullHTML:

     



def getBannerConnection(movieUrl, headers):
    response = get(movieUrl, headers=headers)
    sleep(randint(8,15))


    page_html = BeautifulSoup(response.text, 'html.parser')
    print(f"page_html: {page_html}")
    bannerFullHTML = page_html.find_all('img', class_ = 'ipc-lockup-overlay__screen')
    return bannerFullHTML


# def getBannerFormatted(bannerContainer):
#     bannerFormatted = bannerContainer.find_all('div', class_ = 'ipc-media ipc-media--poster-27x40 ipc-image-media-ratio--poster-27x40 ipc-media--baseAlt ipc-media--poster-l ipc-poster__poster-image ipc-media__img')
#     print(f"bannerFormatted:{bannerFormatted}")





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




##KEEPING IT FOR POSSIBLE FUTURE SIMILAR CASES
