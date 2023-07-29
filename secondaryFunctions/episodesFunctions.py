#Episode Main
def getEpisodes(movieOrSeries):
    if movieOrSeries == '1':
        episodes = "0"
    elif movieOrSeries == '2':
        episodes = "10"
    else:
        episodes = "DELETEME"

    return episodes




#anime episode main
def getAnimeEpisode(container):

    if container.find_all('div', class_ = 'info') is not None:
        
        episodeList = container.find_all('div', class_ = 'info')
        episodeFormatFixed = str(getAnimeTextFormat(episodeList))
        episodeAnimeFormat = episodeAnimeFormatter(episodeFormatFixed)
        return episodeAnimeFormat
    else:
        return("DELETEME")


def getAnimeTextFormat(episodeList):
    
    a = episodeList
    firstFixList = str(episodeList).rsplit(" ep", 1)
    titleFix = str(firstFixList[0])
    secondFixList = titleFix.rsplit("<span>", 1)
    titleSecondFix = str(secondFixList[1])

    return titleSecondFix



def episodeAnimeFormatter(eps):

    try :
        ep = int(eps)
        if(ep < 7):
            return "DELETEME"
        elif(ep < 9):
            return "1"
        elif(ep < 15):
            return "2"
        elif(ep > 15):
            return "3"
    except :
        return "DELETEME"