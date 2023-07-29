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





##HEADER LIST
# HEADERS = []
# HEADERS[0] = {
#         "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:98.0) Gecko/20100101 Firefox/98.0",
#         "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8",
#         "Accept-Language": "en-US,en;q=0.5",
#         "Accept-Encoding": "gzip, deflate",
#         "Connection": "keep-alive",
#         "Upgrade-Insecure-Requests": "1",
#         "Sec-Fetch-Dest": "document",
#         "Sec-Fetch-Mode": "navigate",
#         "Sec-Fetch-Site": "none",
#         "Sec-Fetch-User": "?1",
#         "Cache-Control": "max-age=0",
#     }
# HEADERS[1] = {
#     {
#         "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:106.0) Gecko/20100101 Firefox/106.0",
#         "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8",
#         "Accept-Language": "en-US,en;q=0.5",
#         "Accept-Encoding": "gzip, deflate",
#         "Connection": "keep-alive",
#         "Upgrade-Insecure-Requests": "1",
#         "Sec-Fetch-Dest": "document",
#         "Sec-Fetch-Mode": "navigate",
#         "Sec-Fetch-Site": "none",
#         "Sec-Fetch-User": "?1",
#         "Cache-Control": "max-age=0",
#     }
# }

# HEADERS[2] = {

# }