import requests
from time import sleep
from PIL import Image #pip install Pillow
import os
import movieposters as mp #ONLY USED FOR MOVIE BANNERS // pip install movieposters

#Banner main
def getBanner(container, titleXMLPic, years):

    #DONT ADD CHECK FILE HERE, WE NEED BANNER URL
    if container.find('h3', class_ = 'lister-item-header') is not None:
        bannerURLList = container.find('h3', class_ = 'lister-item-header')
        bannerURL = getUrlFormatter(str(bannerURLList))
        bannerRealURL = getMovieBannerLink(bannerURL)
        downloadBanner(bannerRealURL,titleXMLPic, years)
        return bannerURL
    else:
        return "DELETEME"



def getUrlFormatter(bannerURLList):

    bannerURLList = bannerURLList.split("/title/" , 1)
    bannerURLList = bannerURLList[1].split("/", 1)
    return bannerURLList[0]


def getMovieBannerLink (movieUrl):
    
    link = mp.get_poster(id= movieUrl)
    return link   



def downloadBanner(bannerURL, titleXMLPic, years):
    
    img_url = bannerURL
    try:
        img = Image.open(requests.get(img_url, stream = True, timeout = 10).raw)
        newImgSize = (112, 168)
        img = img.resize(newImgSize)
        image_path = f"images/imagesMoviePoster_{years}"
        if(os.path.exists("images/") == False):
            os.mkdir("images/")
        if(os.path.exists(image_path) == False):
            os.mkdir(image_path) ##creates folder as images

        saveName =  titleXMLPic + "_" + years +"_p.png"

        img.save(f"{image_path}/{saveName}")
    except:
        print(f"Timeout while trying to download banner for {img_url}")
        

    



     

#Anime Banner main

def getAnimeBanner(container, titleXMLPic, years):

    if container.find('div', class_ = 'image') is not None:
        animeBanner = container.find('div', class_ = 'image')
        animeBannerFix = animeBannerFormat(str(animeBanner))
        downloadBanner(animeBannerFix, titleXMLPic, years)    


def animeBannerFormat(animeBanner):

    try:
        animeBannerFix = animeBanner.split("src=\"", 1)
        animeBannerFix = animeBannerFix[1].split("\"", 1)
        return animeBannerFix[0]
    except:
        return ""




