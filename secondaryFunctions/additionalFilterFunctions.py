import pandas as pd #needed for dataframe
import sys #needed to write on notepad
#Movies List Main
def dataArrSaver(titles, storyline, years, genres, movieOrSeries, episodes, pageScore, runtimes, ratings, titleXMLPic, counter):
    
    pdOutputFull = pd.DataFrame({'name': str(titles),
                      'storyline': str(storyline),
                      'year': str(years),
                      'genre': str(genres),
                      'type' : str(movieOrSeries),
                      'episodes' :str(episodes),
                      'rating': str(pageScore),
                      'block': str(runtimes),
                      'special': str(ratings),
                      'titleXMLPic': str(titleXMLPic)} , index = [counter]
                      )
    numOutputFull = pdOutputFull.to_numpy()

    return numOutputFull



#Movies Or Series main
def getMoviesOrSeries(container):
    if container.find('span', class_ = 'metascore') is not None:
        return 1
    else:
        return 2
    

#Anime List Main
def dataArrAnimeSaver(animeTitle, animeStoryline, animeYears, animeGenres, animeType, animeEpisodes, animePageScore, animeRatings, animeRuntime, animeXMLTitle, animeCounter):

    if(animeTitle != "DELETEME" and animeYears != "DELETEME" and animeGenres != "DELETEME" and animeType != "DELETEME" and animeEpisodes != "DELETEME" 
       and animePageScore != "DELETEME" and animeRatings != "DELETEME" and animeRuntime != "DELETEME" and animeXMLTitle != "DELETEME"):
        #animeList = [animeTitle, animeYears, animeGenres, animeType, animeEpisodes, animePageScore, animeRatings, animeRuntime, animeXMLTitle]
        animePandaFull = pd.DataFrame({'name': str(animeTitle),
                        'storyline': str(animeStoryline),
                        'year': str(animeYears),
                        'genre': str(animeGenres),
                        'type' : str(animeType),
                        'episodes' :str(animeEpisodes),
                        'rating': str(animePageScore),
                        'block': str(animeRatings),
                        'special': str(animeRuntime),
                        'titleXMLPic': str(animeXMLTitle)} , index = [animeCounter]
                        )
        animeNumFull = animePandaFull.to_numpy()
        return animeNumFull
    


def animeTurnIntoList(animeList):

    purifiedAnimeList = animeList[~(animeList == "None").any(axis=1)]
    purifiedAnimeList1 = purifiedAnimeList[~(animeList == "?").any(axis=1)]
    purifiedAnimeList2 = purifiedAnimeList1[~(animeList == "Remove me from list").any(axis=1)]



    return purifiedAnimeList2








def checkExistingMovies():

    returnList = []
    f = open("DefaultMovies.xml", "r")
    lines = f.read()
    f.close()
    counter = 0

    movieList = lines.split("<Movie>\n\t\t\t<Id")
    movieList.pop(0)

    for eachMovie in movieList:
        nameList = eachMovie.split("<Name value=\"", 1)
        nameList = nameList[1].split("\"", 1)
        yearList = eachMovie.split("<Year value=\"", 1)
        yearList = yearList[1].split("\"", 1)
        
        returnList.append(checkExistingMovieListMaker(nameList[0], yearList[0], counter))
        counter += 1

    return returnList


def checkExistingMovieListMaker(name, year, counter):
    pdMovie = pd.DataFrame({'name': str(name),
                      'year': str(year)} , index = [counter]
                      )
    
    numMovie = pdMovie.to_numpy()
    return numMovie



def checkExistingMoviesForYear(existingMovieList, currentYear):

    returnList = []

    for eachMovie in existingMovieList:
        for title, year in eachMovie:
            if year == str(currentYear):
                returnList.append(title)
    
    return returnList


def checkIfMovieNeeded(title, preexistingTitleList):
    for existingTitle in preexistingTitleList:
        if title == existingTitle:
            return "DONTCONTINUE"
    return "CONTINUE"
    
