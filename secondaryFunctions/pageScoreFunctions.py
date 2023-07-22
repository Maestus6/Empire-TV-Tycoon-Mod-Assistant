#PageScore main
def getPageScore(container):

    if (container.strong) is not None:
        pageScore = float(container.strong.text) # non-standardized variable
        pageScore = round((pageScore / 10), 1) #From 1/100 Point System to 0.0/1.0, formatting to max two decimals
        return pageScore
    else:
        return ""
    

#AlternativeScore main
def getAlternativeScore(container):
    if container.find('span', class_ = 'metascore') is not None:
        return 1
    else:
        return 2
    

#Anime score main
def getAnimeScore(container):

    scoreAnimeList = container.find_all('div', class_ = 'scormem-container')
    scoreAnimeFormatted = animeScoreFormater(scoreAnimeList)
    return scoreAnimeFormatted


    # if (container.strong) is not None:
    #     pageScore = float(container.strong.text) # non-standardized variable
    #     pageScore = round((pageScore / 10), 2) #From 1/100 Point System to 0.00/1.00, formatting to max two decimals
    #     return pageScore
    # else:
    #     return ""
    

def animeScoreFormater(scoreAnime):

    scoreAnime = str(scoreAnime)
    scoreAnimeListFixed = scoreAnime.rsplit("star mr4\"></i>", 1)
    scoreAnimeFix = scoreAnimeListFixed[1]
    scoreAnimListFixed2 = scoreAnimeFix.split("        </div>", 1)
    scoreAnimeFix = (scoreAnimListFixed2[0]).strip()

    if (scoreAnimeFix != "N/A"):
        scoreAnime = round(float(scoreAnimeFix) , 1)
        return scoreAnime
    else:
        return ""
    