from requests import get  
import requests #pip install requests
from bs4 import BeautifulSoup #pip install beautifulsoup4
from time import sleep
from random import randint
from random import choice
from PIL import Image
import os


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
def getTVScreenAlter (urlSecondPart, titleXMLPic, years):

    check_file = os.path.isfile("images/imagesMovieTV_" + years + "/" + titleXMLPic + "_" + years +".png")
    if(check_file == False):
        if urlSecondPart != "DELETEME":
            screenLinkURL = getScreenSearchContainer(urlSecondPart)
            page_html = getScreenOriginContainerAlter(screenLinkURL)
            screenOriginURL = getScreenContainerFilter(page_html)
            if screenOriginURL != "DELETEME":
                downloadScreen(screenOriginURL, titleXMLPic, years)



def getScreenSearchContainer(urlSecondPart):

    response = get(f"https://www.moviestillsdb.com/search?query={urlSecondPart}", headers={'User-Agent': choice(userAgentsList)})
        
    sleep(randint(8,15)) #anti rate limit

    page_html = BeautifulSoup(response.text, 'html.parser')
    
    screenList = str(page_html).split("<a href=\"" , 1)
    screenList = screenList[1].split("\" style")
    screenSearchURL = f"https://www.moviestillsdb.com{screenList[0]}"
    return screenSearchURL



def getScreenOriginContainerAlter (screenLinkURL):
     
    response = get(screenLinkURL, headers={'User-Agent': choice(userAgentsList)})  
    #sleep(randint(8,15))  we already wait during searchcontainer
    page_html = BeautifulSoup(response.text, 'html.parser')
    return str(page_html)




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
    img_url = screenOriginURL
    img = Image.open(requests.get(img_url, stream = True).raw)
    newImgSize = (374, 254)
    img = img.resize(newImgSize)

    image_path = f"images/imagesMovieTV_{years}"
    if(os.path.exists(image_path) == False):
        os.mkdir(image_path) ##creates folder as images

    saveName =  titleXMLPic + "_" + years

    try:
        img.save(f"{image_path}/{saveName}.png")
    except: #due to CMYK error
        img.save(f"1111_{image_path}/{saveName}")


















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