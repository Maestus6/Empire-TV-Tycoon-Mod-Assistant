#Libraries
from requests import get  #pip install requests
from bs4 import BeautifulSoup #pip install beautifulsoup4
from time import sleep
from random import randint
import numpy as np


#Functions
from secondaryFunctions.genreFunctions import *
from secondaryFunctions.runtimeFunctions import *
from secondaryFunctions.yearFunctions import *
from secondaryFunctions.outputFunctions import *
from secondaryFunctions.ratingFunctions import *
from secondaryFunctions.bannerFunctions import *
from secondaryFunctions.titleFunctions import *
from secondaryFunctions.pageScoreFunctions import *
from secondaryFunctions.additionalFilterFunctions import *
from secondaryFunctions.episodesFunctions import *
from secondaryFunctions.storylineFunctions import *


def movieLoops():

    pages = np.arange(1, 2, 1) #entry (start, stop), lines between each entry 
    headers = {'Accept-Language': 'en-US,en;q=0.8'} # the default language is mandarin
    counter = 0 #to Count loop iterations
    numOutputFull = []
    numBannerFull = []
    yearVal = 2022
    endYearVal = yearVal + 1


    for page in pages:
    # https://www.imdb.com/search/title/?release_date=2022-01-01,2023-01-01&languages=en&start=51&ref_=adv_nxt
    #get request for sci-fi
        response = get(f"https://www.imdb.com/search/title/?release_date={str(yearVal)}-01-01,{str(endYearVal)}-01-01&languages=en&start={str(page)}&ref_=adv_nxt", headers=headers)
        
        sleep(randint(8,15)) #anti rate limit

        if response.status_code != 200:
        #warn('Request: {}; Status code: {}'.format(requests, response.status_code)) gets issues with requests
            print ("beep boop, not 200!!!")
        

        page_html = BeautifulSoup(response.text, 'html.parser')
        movie_containers = page_html.find_all('div', class_ = 'lister-item mode-advanced')
        
        for container in movie_containers:

            #Title Main
            (titles),(titleXMLPic) = getTitle(container)

            #Storyline Main
            storyline = getStoryline(container)

            #Year Main
            years = str(yearVal)

            #Genre Main
            genres,genresSpecial = getGenre(container)

            #AlternativeScore Main(additionalFilterFunctions.py) (Used to diverse movies from tvshows)
            movieOrSeries = getMoviesOrSeries(container)

            #Episodes main
            episodes = getEpisodes(movieOrSeries)

            #PageScore ratings(Movie score)
            pageScore = getPageScore(container)

            #Runtime Main(Blocks for EmpireTV)
            runtimes = getRuntime(container)

            #Rating Main
            ratings = getRating(container, genresSpecial)

            #Banner Main
            getBanner(container, titleXMLPic,years)

            #Get URL Main
            movieUrl = getUrlForMovie(container)

            #Save Movies for usage of Output main once we get every data
            counter += 1
            numOutputFull.append(dataArrSaver(titles, storyline, years, genres, movieOrSeries, episodes, pageScore, ratings, runtimes, titleXMLPic, counter))


            #Save Some Movie parts for Banner correction after loop
            numBannerFull.append(dataBannerSaver(movieUrl, titleXMLPic, years, counter))



            if(counter > 3):  #To make loop iterate 3 times
                 break
            ##End of Loop
    

    #Banner Alter Main -- Doesnt works at the moment, also takes some time
    #getBannerAlter(numBannerFull, headers)

    #Output Main
    dataFramer(numOutputFull)
    print(f"Loop iterated {counter} times")
