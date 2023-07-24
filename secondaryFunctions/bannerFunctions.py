import requests
from PIL import Image
import os
import time

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
    




#Anime Banner main

def getAnimeBanner(container):

    if container.find('div', class_ = 'image') is not None:
        animeBanner = container.find('div', class_ = 'image')
        animeBannerFix = animeBannerFormat(str(animeBanner))
        print(animeBannerFix)
        return animeBannerFix
    else:
        return ""


def animeBannerFormat(animeBanner):

    try:
        animeBannerFix = animeBanner.split("src=\"", 1)
        animeBannerFix = animeBannerFix[1].split("\"", 1)
        return animeBannerFix[0]
    except:
        return ""



