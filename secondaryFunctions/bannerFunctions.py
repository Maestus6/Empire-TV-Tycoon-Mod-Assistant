import requests
from PIL import Image
import os
import movieposters as mp #ONLY USED FOR MOVIE BANNERS

#Banner main
def getBanner(container, titleXMLPic, years):

    check_file = os.path.isfile(titleXMLPic + "_" + years +"_p.png")
    if(check_file == False):
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
    img = Image.open(requests.get(img_url, stream = True).raw)
    newImgSize = (112, 168)
    img = img.resize(newImgSize)
    image_path = f"images/imagesMoviePoster_{years}"
    if(os.path.exists("images/") == False):
        os.mkdir("images/")
    if(os.path.exists(image_path) == False):
        os.mkdir(image_path) ##creates folder as images

    saveName =  titleXMLPic + "_" + years +"_p.png"

    img.save(f"{image_path}/{saveName}")
    



     

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




