import requests
from PIL import Image
import pandas as pd


def bannerCodeClean(banner):
    bannerMod = str(banner) #bs4.element.Tag to str
    bannerMod = bannerMod.split("height=\"98\" loadlate=\"",1)[1]
    bannerMod = bannerMod.split("\" src=", 1)[0]

    return bannerMod

def downloadBanner(bannerURL, titles, years):
    img_url = bannerURL
    img = Image.open(requests.get(img_url, stream = True).raw)
    newImgSize = (112, 168)
    img = img.resize(newImgSize)

    pdOutput = pd.DataFrame({'movie': titles, 'year': years})
    numOutput = pdOutput.to_numpy()

    for titles, years in numOutput:
        saveName = str(titles) + str(years) + ".png"
        img.save(saveName)



