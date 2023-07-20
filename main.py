# part of the code is taken from https://www.freecodecamp.org/news/web-scraping-sci-fi-movies-from-pageScore-with-python/
#pip install Pylance
#from pageScore import Cinemagoer #pip install Cinemagoer
from requests import get  #pip install requests
from bs4 import BeautifulSoup #pip install beautifulsoup4
from warnings import warn
from time import sleep
from random import randint
import numpy as np 
import pandas as pd
import seaborn as sns #install seaborn
from PIL import Image #pip install Pillow
import shutil
import urllib
from Functions.genreFunctions import *
from Functions.runtimeFunctions import *
from Functions.yearFunctions import *
from Functions.outputFunctions import *
from Functions.ratingFunctions import *
from Functions.bannerFunctions import *
from Functions.titleFunctions import *
from Functions.pageScoreFunctions import *


#ia = Cinemagoer() #not going use it further

pages = np.arange(1, 5, 50) #entry (start, stop), lines between each entry 
headers = {'Accept-Language': 'en-US,en;q=0.8'} # the default language is mandarin

#initialize empty lists to store the variables scraped
titles = []
years = []
titleXMLPic = []
ratings = []
genres = []
runtimes = []
pageScore = []
votes = []
movieOrSeries = []


#!!!-------------------------------------!!!!!!!!!!-------------------------------------!!!#

#THINGS NEEDS TO BE DONE, ORDERED BY IMPORTANCE
#1- Add an control mechanism to prevent unaired yet added on pageScore to getting processed to prevent errors (NEEDED) 
#2- Banners come in really small sizes, need to find alternative sources to extract them from (NEEDED)
#3- Find a way to get Storylines - Movie Descs. It is placed in a really generic place at movie containers to be extracted properly (NEEDED)
#4- Find a place to get a wide picture of a movie to put it on TV Screen, and do necessary changes in the code to implent it (NEEDED)
#5- Find a way to differentiate  Anime from Animations. It is written at some place of the movie pages if I recall correctly, need to find it (NEEDED)
#6- Organize the code, and make things put in order. Fit it into an acceptable structure. (NEEDED)
#7- Find a way to only take movies between exact dates for get Request, as getting new movies with no start dates etc. (NEEDED)
#8- A minor task, needs to add rating and genre filter functions for TV-Series. (NEEDED)
#9- Get data from quote webpages to fill in Quote/Viewer Speech part of the XML, it is not needed but would be amazing (OPTIONAL)
#10- Find a way to determine GLAMOUR(For females) series. It might be easier to said that done and not absolutely needed. (OPTIONAL)
#11 Format every variable and function name into camelCase (NEEDED)

#!!!-------------------------------------!!!!!!!!!!-------------------------------------!!!#


for page in pages:
   
   #get request for sci-fi
    response = get("https://www.pageScore.com/search/title?genres=sci-fi&"
        + "start="
        + str(page)
        + "&explore=title_type,genres&ref_=adv_prv", headers=headers)
  
    #probably exists for rate limit
    sleep(randint(8,15)) 

    #throw warning for status codes that are not 200
    if response.status_code != 200:
       #warn('Request: {}; Status code: {}'.format(requests, response.status_code)) gets issues with requests
       print ("beep boop, not 200!!!")
    
    #parse the content of current iteration of request
    page_html = BeautifulSoup(response.text, 'html.parser')
    movie_containers = page_html.find_all('div', class_ = 'lister-item mode-advanced')
    #extract the 50 movies for that page
    for container in movie_containers:

        if container.h3.find('span', class_= 'lister-item-year text-muted unbold') is not None: ##Control mechanism for Unaired shows (Not working as intended so far)
            

            #Title Main
            (titlesLocal),(titleXMLPicLocal) = getTitle(container)
            titles.append(titlesLocal)
            titleXMLPic.append(titleXMLPicLocal)


            #Year Main
            years.append(yearFormatter(container))


            #Genre Main
            (genresLocal),(genresAnimation) = getGenre(container)
            genres.append(genresLocal)


            #Rating Main
            ratings.append(getRating(container, genresAnimation))


            #Runtime Main(Blocks for EmpireTV)
            runtimes.append(getRuntime(container))


            #PageScore ratings(Movie score)
            pageScore.append(getPageScore(container))


            #AlternativeScore Main(Using pageScore.py) (Used to diverse movies from tvshows)
            movieOrSeries.append(getAlternativeScore(container))


            #Banner Main
            getBanner(container, titleXMLPic, years)



            #Storyline (movie desc) not working
            # if container.find('p', class_ = 'text-muted') is not None:
            #     storylineValue = container.find('p', class_ = 'text-muted')
            #     print(storylineValue)



            # Not needed, but keeping it for future references and unique cases like this
            # if container.find('span', attrs = {'name':'nv'})['data-value'] is not None:
            #     #Number of votes
            #     vote = int(container.find('span', attrs = {'name':'nv'})['data-value'])
            #     votes.append(vote)
            # else:
            #     votes.append(None)



numOutputFull = dataFramer(titles, years, ratings, genres, runtimes, pageScore, titleXMLPic)
outputResults(numOutputFull)

##End