#Libraries
from requests import get  #pip install requests
from bs4 import BeautifulSoup #pip install beautifulsoup4
from time import sleep
from random import randint
import numpy as np
import fnmatch


#Functions
from secondaryFunctions.genreFunctions import *
from secondaryFunctions.runtimeFunctions import *
#from secondaryFunctions.yearFunctions import *
from secondaryFunctions.outputFunctions import *
#from secondaryFunctions.ratingFunctions import *
from secondaryFunctions.bannerFunctions import *
from secondaryFunctions.titleFunctions import *
from secondaryFunctions.pageScoreFunctions import *



def animeLoops():

    headers = {'Accept-Language': 'en-US,en;q=0.8'} # the default language is mandarin
    counter = 0 #to Count loop iterations
    numOutputFull = []

    yearVal = "2022"
    seasonVal = "summer"

    #https://myanimelist.net/anime/season/2023/fall
    #get request for anime series
    response = get(f"https://myanimelist.net/anime/season/{yearVal}/{seasonVal}", headers=headers)
    

    sleep(randint(8,15)) #anti rate limit

    if response.status_code != 200:
    #warn('Request: {}; Status code: {}'.format(requests, response.status_code)) gets issues with requests
        print ("beep boop, not 200!!!")
    

    page_html = BeautifulSoup(response.text, 'html.parser')
    animeContainers = page_html.find_all('div', class_ = 'js-anime-category-producer')

    for container in animeContainers:

        #Anime Title Main
        (animeTitle),(animeXMLTitle) = getAnimeTitle(container)

        #Anime Year Main
        animeYears = str(yearVal)

        #Anime Genre Main
        animeGenres = getAnimeGenre(container)

        #Anime Rating Main
        animeRatings = "5"

        #Anime Runtime Main
        animeRuntime = getAnimeRuntime(container)