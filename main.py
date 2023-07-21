#Libraries
from requests import get  #pip install requests
from bs4 import BeautifulSoup #pip install beautifulsoup4
from warnings import warn
from time import sleep
from random import randint
import numpy as np


#Functions
from Functions.genreFunctions import *
from Functions.runtimeFunctions import *
from Functions.yearFunctions import *
from Functions.outputFunctions import *
from Functions.ratingFunctions import *
from Functions.bannerFunctions import *
from Functions.titleFunctions import *
from Functions.pageScoreFunctions import *


#Possible Future Use
# import pandas as pd
# import shutil
# import urllib
# import seaborn as sns #install seaborn
# from PIL import Image #pip install Pillow


#!!!-------------------------------------!!!!!!!!!!-------------------------------------!!!#

#THINGS NEEDS TO BE DONE, ORDERED BY IMPORTANCE
#0- Find a way to make Functions.pageScoreFunctions.getBannerAlter work (OPTIONAL, RELATED TO #2)!!!!!!!
#1- Add an control mechanism to prevent unaired yet added on pageScore to getting processed to prevent errors (NEEDED) 
#2- Banners come in really small sizes, need to find alternative sources to extract them from (NEEDED)
#3- Find a way to get Storylines - Movie Descs. It is placed in a really generic place at movie containers to be extracted properly (NEEDED)
#4- Find a place to get a wide picture of a movie to put it on TV Screen, and do necessary changes in the code to implent it (NEEDED)
#5- Find a way to differentiate  Anime from Animations. It is written at some place of the movie pages if I recall correctly, need to find it (NEEDED)
#6- Find a way to only take movies between exact dates for get Request, as getting new movies with no start dates etc. (NEEDED)
#7- A minor task, needs to add rating and genre filter functions for TV-Series. (NEEDED)
#8- Get data from quote webpages to fill in Quote/Viewer Speech part of the XML, it is not needed but would be amazing (OPTIONAL)

#!!!-------------------------------------!!!!!!!!!!-------------------------------------!!!#


pages = np.arange(1, 2, 100) #entry (start, stop), lines between each entry 
headers = {'Accept-Language': 'en-US,en;q=0.8'} # the default language is mandarin
counter = 0 #to Count loop iterations
numOutputFull = []


for page in pages:
   
   #get request for sci-fi
    response = get("https://www.imdb.com/search/title?genres=sci-fi&"
        + "start="
        + str(page)
        + "&explore=title_type,genres&ref_=adv_prv", headers=headers)
      

    sleep(randint(8,15)) #anti rate limit

    #throw warning for status codes that are not 200
    if response.status_code != 200:
       #warn('Request: {}; Status code: {}'.format(requests, response.status_code)) gets issues with requests
       print ("beep boop, not 200!!!")
    

    page_html = BeautifulSoup(response.text, 'html.parser')
    movie_containers = page_html.find_all('div', class_ = 'lister-item mode-advanced')


    for container in movie_containers:
        print(container)
        #Title Main
        (titles),(titleXMLPic) = getTitle(container)

        #Year Main
        years = getYear(container)

        #Genre Main
        genres,genresSpecial = getGenre(container)

        #Rating Main
        ratings = getRating(container, genresSpecial)

        #Runtime Main(Blocks for EmpireTV)
        runtimes = getRuntime(container)

        #PageScore ratings(Movie score)
        pageScore = getPageScore(container)

        #AlternativeScore Main(Using pageScore.py) (Used to diverse movies from tvshows)
        movieOrSeries = getAlternativeScore(container)

        #Banner Main
        #getBanner(container, titleXMLPic, years)
        getBanner(container, titleXMLPic, years)

        #Storyline (movie desc) not working
        # if container.find('p', class_ = 'text-muted') is not None:
        #     storylineValue = container.find('p', class_ = 'text-muted')
        #     

        #Save Movies for usage of Output main once we get every data
        counter += 1
        numOutputFull.append(dataArrSaver(titles, years, ratings, genres, runtimes, pageScore, titleXMLPic, counter))

        ##End of Loop
        

#Output Main
dataFramer(numOutputFull)

print(f"Loop iterated {counter} times")