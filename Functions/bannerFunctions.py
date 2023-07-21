import requests
from PIL import Image
import os
import time
from google_images_download import google_images_download #pip install google_images_download

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
    

    ##Banner Alter Main
def getBannerAlter(titleXMLPic, years):
    #https://pypi.org/project/google_images_download/2.0.1/ read for arguments and other needed stuff

    response = google_images_download.googleimagesdownload()
    image_path = "images"
    arguments = {"keywords": f"{titleXMLPic}_{years}_p.png",
                "format": "png",
                "limit":1,
                "print_urls":True,
                "size": "medium", #("large, medium, icon")
                "aspect_ratio":"tall",
                "output_directory": image_path,
                "specific_site" : "www.imdb.com"} #Possible values: tall, square, wide, panoramic
        
    response.download(arguments)
    #getBannerFixSize(titleXMLPic, years)
 
# def getBannerFixSize(titleXMLPic, years):

#     im = Image.open(fr"images\{titleXMLPic}_{years}_p\{titleXMLPic}_{years}_p.png")
#     width, height = im.size
#     newImgSize = (112, 168)
#     img = img.resize(newImgSize)





