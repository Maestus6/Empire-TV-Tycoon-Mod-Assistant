#Libraries
from requests import get  #pip install requests
from bs4 import BeautifulSoup #pip install beautifulsoup4
from time import sleep
from random import randint
import numpy as np #pip install numpy


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
     
    # yearValList = [1980, 1981, 1982, 1983, 1984, 1985, 1985 , 1986, 1987, 12010, 2011, 2012, 2013, 2014, 2015, 2016, 2017, 2018, 2019, 2020]
    yearValList = np.arange(2000, 2015).tolist()
    # yearValList = [1992]

    existingMovieList = checkExistingMovies()

    #heeeeeeeeeey
    #heeeeeee

    for yearVal in yearValList:

        pages = np.arange(1, 2, 1)
        endYearVal = yearVal + 1
        numOutputFull = []
        counter = 0 #to Count loop iterations
        # years = str(yearVal)
        preexistingTitleList = checkExistingMoviesForYear(existingMovieList, yearVal)
        preexistingCultList = getCultList()
        
        for page in pages:

        #get request for sci-fi
            response = get(f"https://www.imdb.com/search/title/?release_date={str(yearVal)}-01-01,{str(endYearVal)}-01-01&languages=en&start={str(page)}&ref_=adv_nxt", timeout = 10, headers=headers)
            
            sleep(randint(8,15)) #anti rate limit

            if response.status_code != 200:
            #warn('Request: {}; Status code: {}'.format(requests, response.status_code)) gets issues with requests
                print ("beep boop, not 200!!!")
            

            page_html = BeautifulSoup(response.text, 'html.parser')
            movie_containers = page_html.find_all('div', class_ = 'lister-item mode-advanced')
            
            for container in movie_containers:

                #Title Main
                (titles),(titleXMLPic) = getTitle(container)

                #Check if this movie exists at base game
                checkExistingCondition = checkIfMovieNeeded(titles, preexistingTitleList)

                if(checkExistingCondition != "DONTCONTINUE"):

                    if(titles == "X-Men: The Animated Series"):
                        print("hey")
                        
                    #Storyline Main
                    storyline = getStoryline(container)

                    #Year Main
                    years = str(yearVal)

                    #Cult Main // Using ratingFunctions.py
                    cult = getCult(preexistingCultList, titles, years)

                    #Genre Main
                    genres,genresSpecial = getGenre(container)

                    #PageScore ratings(Movie score)
                    pageScore = getPageScore(container)

                    #Runtime Main(Blocks for EmpireTV)
                    runtimes = getRuntime(container)

                    #Rating Main
                    ratings, movieOrSeries = getRating(container, genresSpecial)

                    #Episodes main
                    episodes = getEpisodes(movieOrSeries)

                    #Quote Main (Hard to make use of it)
                    #quotes = getQuote(urlSecondPart)


                    #Save Movies for usage of Output main once we get every data
                    counter += 1

                    if (titles != "DELETEME" and storyline != "DELETEME" and years != "DELETEME" and genres != "DELETEME" and movieOrSeries != "DELETEME" and 
                    episodes != "DELETEME" and pageScore != "DELETEME" and runtimes != "DELETEME" and cult != "DELETEME" and ratings != "DELETEME" and titleXMLPic != "DELETEME" and counter != "DELETEME"):
                        #Banner Main
                        getBanner(container, titleXMLPic,years)

                        #TV Screen Main
                        gotTVScreen = getTVScreenAlter(container, titleXMLPic, years)

                    numOutputFull.append(dataArrSaver(titles, storyline, years, genres, movieOrSeries, episodes, pageScore, runtimes, cult, ratings, titleXMLPic, counter, gotTVScreen))

                    # if(counter > 5):  #To make loop iterate 20 times
                    #     break
                    #End of Loop
        


        #Output Main
        dataFramer(numOutputFull, int(yearVal))
        print(f"Loop iterated {counter} times")
