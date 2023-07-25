from primaryFunctions.getDataForMovies import *
from primaryFunctions.getDataForAnime import *


#!!!-------------------------------------!!!!!!!!!!-------------------------------------!!!#

#THINGS NEEDS TO BE DONE, NOT ORDERED BY IMPORTANCE
#0- Normal TV screen for Anime (NEEDED)
#1- Get Banners from a different webpage(Check bannerFunctions.py / getBannerAlter for further explaination), Movie Tv screen(Other source) for Movies/TV Series(NEEDED)
#2- Find a way to only take movies between exact dates for get Request, as getting new movies with no start dates etc. (NEEDED) //We can filter this too but would be handy
#3  Overhaul Episodes for TV Series(Movies) (NEEDED)
#4- Make naming more consistent for variables, right now they are rather confusing (NEEDED)
#5- Get data from quote webpages to fill in Quote/Viewer Speech part of the XML, it is not needed but would be amazing (OPTIONAL)
#6- Add an control mechanism to prevent unaired yet added on pageScore to getting processed to prevent errors (OPTIONAL)   //Can filter the input or list for them 
#7- Allow user input to be taken for getting needed stuff (NEEDED)
#8- Create a proper, non-text based UI(GUI) (NEEDED)

#!!!-------------------------------------!!!!!!!!!!-------------------------------------!!!#

##TEST IS DONE VIA COMMENTING THE UNNEEDED ONE FOR NOW!!!

movieLoops()
#animeLoops()


