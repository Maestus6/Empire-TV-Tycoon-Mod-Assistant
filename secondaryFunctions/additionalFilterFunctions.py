import pandas as pd #needed for dataframe
import sys #needed to write on notepad

#Movies List Main
def dataArrSaver(titles, years, ratings, genres, runtimes, pageScore, titleXMLPic, counter):
    
    pdOutputFull = pd.DataFrame({'movie': str(titles),
                      'year': str(years),
                      'rating': str(ratings),
                      'genre': str(genres),
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
    




def dataArrAnimeSaver(animeTitle, animeYears, animeGenres, animeRatings, animeRuntime, animePageScore, animeXMLTitle, animeCounter):

    pdOutputFull = pd.DataFrame({'animeTitle': animeTitle,
                      'animeYears': str(animeYears),
                      'animeRatings': str(animeRatings),
                      'animeGenres': str(animeGenres),
                      'animeRuntime': str(animeRuntime),
                      'animePageScore': str(animePageScore),
                      'animeXMLTitle': str(animeXMLTitle)} , index = [animeCounter]
                      )
    
    animeList = pdOutputFull.values.tolist()
    animeFilteredList = animeTurnIntoList(animeList)

    print(animeFilteredList)

    return animeFilteredList





def animeTurnIntoList(animeList):

    for animeTitle, animeYears, animeGenres, animeRatings, animeRuntime, animePageScore, animeXMLTitle in animeList.copy():
        if animeTitle == "" or animeYears == "" or animeGenres == "" or animeRuntime == "" or animePageScore == "" or animePageScore == "0":
            animeList.remove(animeList)
    
    return animeList
