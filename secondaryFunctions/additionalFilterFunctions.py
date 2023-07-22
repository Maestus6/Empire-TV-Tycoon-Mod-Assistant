import pandas as pd #needed for dataframe
import sys #needed to write on notepad

#Movies List Main
def dataArrSaver(titles, years, ratings, genres, runtimes, pageScore, titleXMLPic, counter, movieOrSeries):
    
    pdOutputFull = pd.DataFrame({'movie': str(titles),
                      'year': str(years),
                      'rating': str(ratings),
                      'genre': str(genres),
                      'type' : str(movieOrSeries),
                      'runtime_min': str(runtimes),
                      'imdb': str(pageScore),
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
def dataArrAnimeSaver(animeTitle, animeYears, animeGenres, animeType, animeRatings, animeRuntime, animePageScore, animeXMLTitle):

    if(animeGenres == "DELETEME" or animeRuntime == "DELETEME" or animePageScore == "DELETEME"):
        animeList = "DONTADD"
    else:
        animeList = [animeTitle, animeYears, animeGenres, animeType, animeRatings, animeRuntime, animePageScore, animeXMLTitle]

    return animeList





def animeTurnIntoList(animeList):

    purifiedAnimeList = animeList[~(animeList == "None").any(axis=1)]
    purifiedAnimeList1 = purifiedAnimeList[~(animeList == "?").any(axis=1)]
    purifiedAnimeList2 = purifiedAnimeList1[~(animeList == "Remove me from list").any(axis=1)]



    return purifiedAnimeList2


