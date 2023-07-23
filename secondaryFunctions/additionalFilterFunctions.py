import pandas as pd #needed for dataframe
import sys #needed to write on notepad
#Movies List Main
def dataArrSaver(titles, years, genres, movieOrSeries, episodes, pageScore, ratings, runtimes, titleXMLPic, counter):
    
    pdOutputFull = pd.DataFrame({'name': str(titles),
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
def dataArrAnimeSaver(animeTitle, animeYears, animeGenres, animeType, animeEpisodes, animePageScore, animeRatings, animeRuntime, animeXMLTitle):

    if(animeTitle == "DELETEME" or animeYears == "DELETEME" or animeGenres == "DELETEME" or animeType == "DELETEME" or animeEpisodes == "DELETEME" or animePageScore == "DELETEME" or animeRatings == "DELETEME" or animeRuntime == "DELETEME" or animeXMLTitle == "DELETEME"):
        animeList = "DONTADD"
    else:
        animeList = [animeTitle, animeYears, animeGenres, animeType, animeEpisodes, animePageScore, animeRatings, animeRuntime, animeXMLTitle]

    return animeList





def animeTurnIntoList(animeList):

    purifiedAnimeList = animeList[~(animeList == "None").any(axis=1)]
    purifiedAnimeList1 = purifiedAnimeList[~(animeList == "?").any(axis=1)]
    purifiedAnimeList2 = purifiedAnimeList1[~(animeList == "Remove me from list").any(axis=1)]



    return purifiedAnimeList2


