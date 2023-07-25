import pandas as pd #needed for dataframe
import sys #needed to write on notepad
#Movies List Main
def dataArrSaver(titles, storyline, years, genres, movieOrSeries, episodes, pageScore, ratings, runtimes, titleXMLPic, counter):
    
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
    

#Banner saver for after loop
def dataBannerSaver(titles, titleXMLPic, years, counter):

    pdOutputFull = pd.DataFrame({'title': str(titles),
                      'titleXMLPic': str(titleXMLPic),
                      'year': str(years)} , index = [counter]
                      )
    numOutputFull = pdOutputFull.to_numpy()

    return numOutputFull




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


