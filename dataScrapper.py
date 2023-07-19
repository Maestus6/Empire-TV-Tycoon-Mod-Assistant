# part of the code is taken from https://www.freecodecamp.org/news/web-scraping-sci-fi-movies-from-imdb-with-python/
#pip install Pylance
#from imdb import Cinemagoer #pip install Cinemagoer
import sys #needed to write on notepad
from requests import get  #pip install requests
from bs4 import BeautifulSoup #pip install beautifulsoup4
from warnings import warn
from time import sleep
from random import randint
import numpy as np, pandas as pd
import seaborn as sns #install seaborn
from genreFunctions import *
from runtimeFunctions import *

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
            
            genresList = container.p.find('span', class_ = 'genre').text.replace("\n", "").strip().split(",") # remove the whitespace character, strip, and split to create an array of genres  
            print(f"genresList: {genresList}")          
            genresNoWhiteSpace = genreSpaceFix(genresList)
            print(f"genreSpaceFix: {genresNoWhiteSpace}")
            genresFormated = genreValidator(genresNoWhiteSpace)
            print(f"genreValidator: {genresFormated}")
            genrePicked = genrePicker(genresFormated)
            print(f"genrePicker: {genrePicked}")
            genreCompleted = genreStrToInt(genrePicked)
            print(f"genreStrToInt: {genreCompleted}")
            genres.append(genreCompleted)
        
        else:
            genres.append("")

        if container.p.find('span', class_ = 'runtime') is not None:

            #runtime
            time = int(container.p.find('span', class_ = 'runtime').text.replace(" min", "")) # remove the minute word from the runtime and make it an integer
            fixedTime = runtimeFormatter(time)
            print(f"runtimeFormatter: {fixedTime}")
            runtimes.append(fixedTime)

        else:
            runtimes.append(None)

        if (container.strong) is not None:
            #IMDB ratings
            imdb = float(container.strong.text) # non-standardized variable
            imdb = imdb / 10
            imdb_ratings.append(imdb)

        else:
            imdb_ratings.append(None)

        if container.find('span', class_ = 'metascore') is not None:
            movieorseries.append("1")

        else:
            movieorseries.append("2")


titleandtype = {}

for title in titles:
    titleandtype[title] = movieorseries[titles.index(title)]



pdOutputFull = pd.DataFrame({'movie': titles,
                      'year': years,
                      'rating': ratings,
                      'genre': genres,
                      'runtime_min': runtimes,
                      'imdb': imdb_ratings}
                      )
numOutputFull = pdOutputFull.to_numpy()



with open('Output.txt', 'w') as sys.stdout:
    for titles, years, ratings, genres, runtimes, imdb_ratings in numOutputFull:
        print('<Movie>')
        print(f"<Id value=\"\">")
        print(f"<Name value=\"{titles}\">")
        print(f"<Storyline value=\"\">")
        print(f"<Year value=\"{years}\">")
        print(f"<Genre value=\"{genres}\">") 
        print(f"<Type value=\"1\">")
        print(f"<Episodes value=\"{runtimes}\">")
        print(f"<Rating value=\"{imdb_ratings}\">")
        print(f"<Blocks value=\"{runtimes}\">")
        print(f"<Cult value=\"0\">")
        print(f"<Special value=\"{ratings}\">")
        print(f"<Pirate value=\"0\">")  
        print(f"<Speech value=\"\">")
        print(f"<ImageTV value=\"{titles}_{years}_tv.png\">")
        print(f"<ImagePoster value=\"{titles}_{years}_p.png\">")
        print('</Movie>')


# print(titleandtype)

