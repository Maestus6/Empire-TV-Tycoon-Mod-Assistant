#Episode Main
def getEpisodes(movieOrSeries):
    if movieOrSeries == 1:
        episodes = "0"
    elif movieOrSeries == 2:
        episodes = "10"
    else:
        episodes = "DELETEME"

    return episodes