# part of the code is taken from https://www.freecodecamp.org/news/web-scraping-sci-fi-movies-from-imdb-with-python/
#pip install Pylance
#from imdb import Cinemagoer #pip install Cinemagoer
from requests import get  #pip install requests
from bs4 import BeautifulSoup #pip install beautifulsoup4
from warnings import warn
from time import sleep
from random import randint
import numpy as np, pandas as pd
import seaborn as sns #install seaborn

#ia = Cinemagoer() #not going use it further

pages = np.arange(1, 5, 50) #entry (start, stop), lines between each entry 
headers = {'Accept-Language': 'en-US,en;q=0.8'} # the default language is mandarin

#initialize empty lists to store the variables scraped
titles = []
years = []
ratings = []
genres = []
runtimes = []
imdb_ratings = []
imdb_ratings_standardized = []
metascores = []
votes = []
movieorseries = []

for page in pages:
   
   #get request for sci-fi
    response = get("https://www.imdb.com/search/title?genres=sci-fi&"
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

        #title
        title = container.h3.a.text
        titles.append(title)

        if container.h3.find('span', class_= 'lister-item-year text-muted unbold') is not None:
        
            #year released
            year = container.h3.find('span', class_= 'lister-item-year text-muted unbold').text # remove the parentheses around the year and make it an integer
            years.append(year)

        else:
            years.append(None) # each of the additional if clauses are to handle type None data, replacing it with an empty string so the arrays are of the same length at the end of the scraping

        if container.p.find('span', class_ = 'certificate') is not None:
            #rating
            rating = container.p.find('span', class_= 'certificate').text
            ratings.append(rating)

        else:
            ratings.append("")

        if container.p.find('span', class_ = 'genre') is not None:
            #genre Temp solution by Anxious
            genreslist = container.p.find('span', class_ = 'genre').text.replace("\n", "").strip().split(",") # remove the whitespace character, strip, and split to create an array of genres
            genresnowhitespace = []
            for genre in genreslist:
                genre = genre.strip()
                genresnowhitespace.append(genre)
            

            genres.append(genresnowhitespace)
        
        else:
            genres.append("")

        if container.p.find('span', class_ = 'runtime') is not None:

            #runtime
            time = int(container.p.find('span', class_ = 'runtime').text.replace(" min", "")) # remove the minute word from the runtime and make it an integer
            runtimes.append(time)

        else:
            runtimes.append(None)

        if (container.strong) is not None:
            #IMDB ratings
            imdb = float(container.strong.text) # non-standardized variable
            imdb_ratings.append(imdb)

        else:
            imdb_ratings.append(None)

        if container.find('span', class_ = 'metascore') is not None:
            movieorseries.append("I am a movie")

        else:
            movieorseries.append("I am a series")

        if container.find('span', attrs = {'name':'nv'}) is not None:
            if container.find('span', attrs = {'name':'nv'})['data-value'] is not None:
                #Number of votes
                vote = int(container.find('span', attrs = {'name':'nv'})['data-value'])
                votes.append(vote)

            else:
                votes.append(None)

titleandtype = {}

for title in titles:
    titleandtype[title] = movieorseries[titles.index(title)]

print(titleandtype)

# print(titleandtype)

def genreCounter(arr):
    Short = 0
    Drama = 0
    Comedy = 0
    Documentary = 0
    Adult = 0
    Action = 0
    Romance = 0
    Thriller = 0
    Animation = 0
    Family = 0
    Crime = 0
    Horror = 0
    Music = 0
    Adventure = 0
    Fantasy = 0
    SciFi = 0
    Mystery = 0
    Biography = 0
    Sport = 0
    History = 0
    Musical = 0
    Western = 0
    War = 0
    RealityTV = 0
    News = 0
    TalkShow = 0
    GameShow = 0
    FilmNoir = 0
    Lifestyle = 0
    Experimental = 0
    Commercial = 0

    for oneGenre in genre:
        match oneGenre:
            case "Short":
                Short+= 1
            case "Drama":
                Drama+= 1
            case "Comedy":
                Comedy+= 1
            case "Documentary":
                Documentary+= 1
            case "Adult":
                Adult+= 1
            case "Action":
                Action+= 1
            case "Romance":
                Romance+= 1
            case "Thriller":
                Thriller+= 1
            case "Animation":
                Animation+= 1
            case "Family":
                Family+= 1
            case "Crime":
                Crime+= 1
            case "Horror":
                Horror+= 1
            case "Music":
                Music+= 1
            case "Adventure":
                Adventure+= 1
            case "Fantasy":
                Fantasy+= 1
            case "Sci-Fi":
                SciFi+= 1
            case "Mystery":
                Mystery+= 1
            case "Biography":
                Biography+= 1
            case "Sport":
                Sport+= 1
            case "History":
                History+= 1
            case "Musical":
                Musical+= 1
            case "Western":
                Western+= 1
            case "War":
                War+= 1
            case "Reality-TV":
                RealityTV+= 1
            case "News":
                News+= 1
            case "Talk-Show":
                TalkShow+= 1
            case "Game-Show":
                GameShow+= 1
            case "Film-Noir":
                FilmNoir+= 1
            case "Lifestyle":
                Lifestyle+= 1
            case "Experimental":
                Experimental+= 1
            case "Commercial":
                Commercial+= 1