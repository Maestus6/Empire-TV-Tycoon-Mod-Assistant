# synopsis js-synopsis

def getAnimeStoryline (container):

    if container.find('div', class_ = 'synopsis js-synopsis') is not None:
        animeStoryline = container.find('div', class_ = 'synopsis js-synopsis')
        animeStoryline = animeStorylineFix(str(animeStoryline))
        print(animeStoryline)
    else:
        return ""


def animeStorylineFix (animeStoryline):

    animeStorylineFix = animeStoryline.split("<p class=\"preline\">", 1)
    try:
        animeStorylineFix1 = []
        animeStorylineFix1 = animeStorylineFix[1].split("[Written by MAL Rewrite]</p>", 1)
        return animeStorylineFix1[0]
    except:
        animeStorylineFix1 = []
        animeStorylineFix1 = animeStorylineFix[1].split("<button class=\"js-toggle-text", 1)
        return animeStorylineFix1[0]
