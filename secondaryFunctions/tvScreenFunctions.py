from requests import get  
import requests #pip install requests
from bs4 import BeautifulSoup #pip install beautifulsoup4
from time import sleep
from random import randint
from random import choice
from PIL import Image
import os
import secondaryFunctions.bannerFunctions as bf #need to use bannerURL function


userAgentsList = [
    'Mozilla/5.0 (iPad; CPU OS 12_2 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E148',
    'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.83 Safari/537.36',
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.51 Safari/537.36',
    'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/47.0.2526.111 Safari/537.36',
    'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:15.0) Gecko/20100101 Firefox/15.0.1',
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/42.0.2311.135 Safari/537.36 Edge/12.246',
    'Mozilla/5.0 (X11; CrOS x86_64 8172.45.0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.64 Safari/537.36',
    'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_2) AppleWebKit/601.3.9 (KHTML, like Gecko) Version/9.0.2 Safari/601.3.9' ]



#TV Screen Main
def getTVScreenAlter (container, titleXMLPic, years):

    check_file = os.path.isfile("images/imagesMovieTV_" + years + "/" + titleXMLPic + "_" + years +".png")
    if(check_file == False):

        bannerURLList = container.find('h3', class_ = 'lister-item-header')
        urlSecondPart = bf.getUrlFormatter(str(bannerURLList))
        # urlSecondPart = bf.getMovieBannerLink(bannerURL)

        if urlSecondPart != "DELETEME":
            screenLinkURL = getScreenSearchContainer(urlSecondPart)
            if screenLinkURL != "DELETEME":
                page_html = getScreenOriginContainerAlter(screenLinkURL)
                if page_html != "DELETEME":
                    screenOriginURL = getScreenContainerFilter(page_html)
                    if screenOriginURL != "DELETEME":
                        downloadScreen(screenOriginURL, titleXMLPic, years)
                        return "Downloaded"
                    else:
                        return "DELETEME"
                else:
                    return "DELETEME"
            else:
                return "DELETEME"
        else:
            return "DELETEME"
    else:
        sleep(2)



def getScreenSearchContainer(urlSecondPart):
    # connect_timeout = 0.1
    # read_timeout = 10
    try:
        response = get(f"https://www.moviestillsdb.com/search?query={urlSecondPart}", timeout = 10, headers={'User-Agent': choice(userAgentsList)})
        sleep(randint(12,18)) #anti rate limit
        page_html = BeautifulSoup(response.text, 'html.parser')
        screenList = str(page_html).split("<a href=\"" , 1)
        screenList = screenList[1].split("\" style")
        screenSearchURL = f"https://www.moviestillsdb.com{screenList[0]}"
    except:
        print(f"Error while trying to download tv Screen for https://www.moviestillsdb.com/search?query={urlSecondPart}")
        screenSearchURL = "DELETEME"
    return screenSearchURL



def getScreenOriginContainerAlter (screenLinkURL):
     
    try:
        response = get(screenLinkURL, timeout = 10, headers={'User-Agent': choice(userAgentsList)})  
        #sleep(randint(8,15))  we already wait during searchcontainer
        page_html = BeautifulSoup(response.text, 'html.parser')
        return str(page_html)
    except:
        return "DELETEME"




def getScreenContainerFilter (page_html):

    iterator = 1
    foundIt = 0

    if (str(page_html).find("\"preview\":{\"")) > 0:
        screenList = str(page_html).split("\"preview\":{\"")


        while(foundIt == 0):
            try:
                heightList = screenList[iterator].split("ght\":", 1)
                heightList = heightList[1].split(",", 1)
                height = int(heightList[0])

                widthList = screenList[iterator].split("th\":", 1)
                widthList = widthList[1].split(",\"", 1)
                width = int(widthList[0])

                if(height < width):
                    screenIteratingList = screenList[iterator].split("\"path\":\"", 1)
                    screenIteratingList = screenIteratingList[1].split("\"},\"", 1)
                    screenOriginURL = (screenIteratingList[0].replace("\\", "/")).replace("//" ,  "/")
                    return screenOriginURL
                else:
                    iterator += 1
            except:
                return("DELETEME")

    elif (str(page_html).find("{&quot;height&quot;:")) > 0 :
        screenList = str(page_html).split("{&quot;height&quot;:")


        while(foundIt == 0):
            try:
                heightList = screenList[iterator].split(",&quot;", 1)
                height = int(heightList[0])

                widthList = screenList[iterator].split(",&quot;width&quot;:", 1)
                widthList = widthList[1].split(",&quot;path&", 1)
                width = int(widthList[0])

                
                if(height < width):
                    screenIteratingList = screenList[iterator].split("path&quot;:&quot;", 1)
                    screenIteratingList = screenIteratingList[1].split("&quot;}", 1)
                    screenOriginURL = (screenIteratingList[0].replace("\\", "/")).replace("//" ,  "/")
                    return screenOriginURL
                else:
                    iterator += 1
            except:
                 return("DELETEME")

    else:
        screenList = str(page_html).split("{\"height\":")

        while(foundIt == 0):
            try:
                heightList = screenList[iterator].split(",\"", 1)
                height = int(heightList[0])

                widthList = screenList[iterator].split("th\":", 1)
                widthList = widthList[1].split(",", 1)
                width = int(widthList[0])
                
                if(height < width):
                    screenIteratingList = screenList[iterator].split("path\":\"", 1)
                    screenIteratingList = screenIteratingList[1].split("\"},", 1)
                    screenOriginURL = (screenIteratingList[0].replace("\\", "/")).replace("//" ,  "/")

                    return screenOriginURL
                else:
                    iterator += 1
            except:
                return("DELETEME")
            


def downloadScreen(screenOriginURL, titleXMLPic, years):
    try:
        img = Image.open(requests.get(screenOriginURL, stream = True, timeout= 20).raw)
        newImgSize = (374, 254)
        img = img.resize(newImgSize)

        image_path = f"images/imagesMovieTV_{years}"
        if(os.path.exists(image_path) == False):
            os.mkdir(image_path) ##creates folder as images

        saveName =  titleXMLPic + "_" + years

        try:
            img.save(f"{image_path}/{saveName}.png")
        except:
            print(f" problem while writing screenOriginalURL = {screenOriginURL}")
    except:
        print(f"Problem while downloading screenOriginalURL = {screenOriginURL}")


















    # foundIt = str(page_html).find("&quot;path&quot;:&quot;")

    # if foundIt > 0 :
    #     screenList = str(page_html).split("&quot;path&quot;:&quot;" , 1)
    #     try:
    #         screenList = screenList[1].split("&quot;}")
    #     except:
    #         return "DELETEME"
    #     screenOriginURL = (screenList[0].replace("\\", "/")).replace("//" ,  "/")
    # #"path":"
    # else:
    #     screenList = str(page_html).split("path\":\"" , 1)
    #     try:
    #         screenList = screenList[1].split("\"},")
    #     except:
    #         return "DELETEME"
    #     screenOriginURL = (screenList[0].replace("\\", "/")).replace("//" ,  "/")        

    # return(screenOriginURL)