from primaryFunctions.getDataForMovies import *
from primaryFunctions.getDataForAnime import *


#!!!-------------------------------------!!!!!!!!!!-------------------------------------!!!#

#THINGS NEEDS TO BE DONE, ORDERED BY IMPORTANCE
#0- Add Anime desc and normal TV screen for Anime (NEEDED)
#1- Get Descs(Probably other source), Get Banners from a different webpage(Other source), Movie Tv screen(Other source) for Movies/TV Series(NEEDED)
#2- Find a way to only take movies between exact dates for get Request, as getting new movies with no start dates etc. (NEEDED) //We can filter this too but would be handy
#3 Overhaul Episodes for TV Series(Movies) (NEEDED)   //Currently incomplete
#4 Overhaul Runtime for Anime based on ep mins (NEEDED)
#5- Make naming more consistent for variables, right now they are rather confusing (NEEDED)
#6- Get data from quote webpages to fill in Quote/Viewer Speech part of the XML, it is not needed but would be amazing (OPTIONAL)
#7- Add an control mechanism to prevent unaired yet added on pageScore to getting processed to prevent errors (OPTIONAL)   //Can filter the input or list for them 
#8- Allow user input to be taken for getting needed stuff (NEEDED)
#9- Create a proper, non-text based UI(GUI) (NEEDED)

#!!!-------------------------------------!!!!!!!!!!-------------------------------------!!!#

##TEST IS DONE VIA COMMENTING THE UNNEEDED ONE FOR NOW!!!

#movieLoops()
animeLoops()


