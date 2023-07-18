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

pages = np.arange(1, 2, 50) #entry (start, stop), lines between each entry 
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

for page in pages:
   
   #get request for sci-fi
    response = get("https://www.imdb.com/search/title?genres=sci-fi&"
        + "start="
        + str(page)
        + "&explore=title_type,genres&ref_=adv_prv", headers=headers)
  
    sleep(randint(8,15)) #probably exists for rate limit

      #throw warning for status codes that are not 200
    if response.status_code != 200:
       warn('Request: {}; Status code: {}'.format(requests, response.status_code))
