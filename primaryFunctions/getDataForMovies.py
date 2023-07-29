#Libraries
from requests import get  #pip install requests
from bs4 import BeautifulSoup #pip install beautifulsoup4
from time import sleep
from random import randint
import numpy as np


#Functions
from secondaryFunctions.genreFunctions import *
from secondaryFunctions.runtimeFunctions import *
from secondaryFunctions.outputFunctions import *
from secondaryFunctions.ratingFunctions import *
from secondaryFunctions.bannerFunctions import *
from secondaryFunctions.titleFunctions import *
from secondaryFunctions.pageScoreFunctions import *
from secondaryFunctions.additionalFilterFunctions import *
from secondaryFunctions.episodesFunctions import *
from secondaryFunctions.storylineFunctions import *
from secondaryFunctions.tvScreenFunctions import *
from secondaryFunctions.quoteFunctions import *


def movieLoops():

     #entry (start, stop), lines between each entry 
    headers = {'Accept-Language': 'en-US,en;q=0.8'} # the default language is mandarin
     
    yearValList = [1990, 1991, 1992, 1993, 1994, 1995, 1996, 1997, 1998, 1999, 2000]
    

    for yearVal in yearValList:

        pages = np.arange(1, 2, 1)
        endYearVal = yearVal + 1
        numOutputFull = []
        counter = 0 #to Count loop iterations
        # years = str(yearVal)
        
        for page in pages:

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

                # #Year Main
                years = str(yearVal)

                #Genre Main
                genres,genresSpecial = getGenre(container)

                #AlternativeScore Main(additionalFilterFunctions.py) (Used to diverse movies from tvshows)
                #movieOrSeries = getMoviesOrSeries(container)

                #PageScore ratings(Movie score)
                pageScore = getPageScore(container)

                #Runtime Main(Blocks for EmpireTV)
                runtimes = getRuntime(container)

                #Rating Main
                ratings, movieOrSeries = getRating(container, genresSpecial)

                #Episodes main
                episodes = getEpisodes(movieOrSeries)

                #Banner Main
                urlSecondPart = getBanner(container, titleXMLPic,years)

                #Quote Main (Hard to make use of it)
                #quotes = getQuote(urlSecondPart)

                #TV Screen Main
                getTVScreenAlter(urlSecondPart, titleXMLPic, years)

                #Save Movies for usage of Output main once we get every data
                counter += 1
                numOutputFull.append(dataArrSaver(titles, storyline, years, genres, movieOrSeries, episodes, pageScore, runtimes, ratings,  titleXMLPic, counter))

                # if(counter > 5):  #To make loop iterate 20 times
                #     break
                #End of Loop
        


        #Output Main
        dataFramer(numOutputFull, int(yearVal))
        print(f"Loop iterated {counter} times")
