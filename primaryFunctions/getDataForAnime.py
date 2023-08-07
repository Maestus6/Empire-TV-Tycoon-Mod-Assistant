#Libraries
from requests import get  #pip install requests
from bs4 import BeautifulSoup #pip install beautifulsoup4
from time import sleep
from random import randint
import pandas as pd


#Functions
from secondaryFunctions.genreFunctions import *
from secondaryFunctions.runtimeFunctions import *
from secondaryFunctions.outputFunctions import *
#from secondaryFunctions.ratingFunctions import *
from secondaryFunctions.bannerFunctions import *
from secondaryFunctions.titleFunctions import *
from secondaryFunctions.pageScoreFunctions import *
from secondaryFunctions.additionalFilterFunctions import *
from secondaryFunctions.episodesFunctions import *
from secondaryFunctions.storylineFunctions import *
from secondaryFunctions.tvScreenFunctions import *



def animeLoops():

    headers = {'Accept-Language': 'en-US,en;q=0.8'} # the default language is mandarin
    yearVal = "2022"
    seasonVal = "summer"
    animeFilteredList = []
    animeCounter = 0


    #get request for anime series
    response = get(f"https://myanimelist.net/anime/season/{yearVal}/{seasonVal}", timeout = 10, headers=headers)
    

    sleep(randint(8,15)) #anti rate limit

    if response.status_code != 200:
    #warn('Request: {}; Status code: {}'.format(requests, response.status_code)) gets issues with requests
        print ("beep boop, not 200!!!")
    

    page_html = BeautifulSoup(response.text, 'html.parser')
    animeContainers = page_html.find_all('div', class_ = 'js-anime-category-producer')
    
    for container in animeContainers:

        #Anime Title Main
        (animeTitle),(animeXMLTitle) = getAnimeTitle(container)

        #Anime Storyline Main
        animeStoryline = getAnimeStoryline(container)

        #Anime Year Main
        animeYears = yearVal

        #Anime Genre Main
        animeGenres = str(getAnimeGenre(container))

        #Anime Type Main
        animeType = "1"

        #Anime Episodes Main
        animeEpisodes = str(getAnimeEpisode(container))

        #Anime Score Main
        animePageScore = str(getAnimeScore(container))

        #Anime Rating Main
        animeRatings = "5"

        #Anime Runtime Main
        animeRuntime = animeGetRuntime(container)
        
        #Anime List Main
        animeCounter += 1 

        #Anime Banner Main
        getAnimeBanner(container, animeXMLTitle, animeYears)

        animeFilteredList.append(dataArrAnimeSaver(animeTitle, animeStoryline, animeYears, animeGenres, animeType, animeEpisodes, animePageScore,
        animeRatings, animeRuntime, animeXMLTitle, animeCounter))

        if(animeCounter > 3):  #To make loop iterate 3 times
            break
        
    
    #print(f"Anime list: {animeFilteredList}")
    dataFramer(animeFilteredList, animeYears)
    #print(f"Loop iterated {animeCounter} times")