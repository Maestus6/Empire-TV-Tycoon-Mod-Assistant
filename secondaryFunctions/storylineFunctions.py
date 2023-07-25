#Storyline Main
def getStoryline(container):

    if container.find('div', class_ = 'lister-item-content') is not None:
        storyline = container.find('div', class_ = 'lister-item-content')
        storyline = storylineFix(str(storyline))
        return storyline


def storylineFix (storyline):
    strExists = storyline.find('Metascore\n            </div>\n</div>\n<p class="text-muted">\n')
    
    if strExists > 0:
        storylineFixList = storyline.split('Metascore\n            </div>\n</div>\n<p class="text-muted">\n', 1)
        storylineFix = storylineFixList[1]
    else:
        storylineFixList = storyline.split("\n</div>\n</div>\n<p class=\"text-muted\">\n", 1)
        storylineFix = storylineFixList[1]
    
    storylineFixList = storylineFix.split("\n", 1) #Needed for series with long descs
    storylineFix = storylineFixList[0]
    storylineFixList = storylineFix.split("</p>", 1)
    storylineFix = storylineFixList[0]
    return storylineFix




#Anime Storyline Main
def getAnimeStoryline (container):

    if container.find('div', class_ = 'synopsis js-synopsis') is not None:
        animeStoryline = container.find('div', class_ = 'synopsis js-synopsis')
        animeStoryline = animeStorylineFix(str(animeStoryline))
        return animeStoryline
    else:
        return ""


def animeStorylineFix (animeStoryline):

    strExists = 0
    animeStorylineFix = animeStoryline.split("<p class=\"preline\">", 1)
    animeStorylineFix1 = animeStorylineFix[1]
    strExists = animeStorylineFix1.find('<button class=\"js-toggle-text')

    if strExists < 0:
        return ""
    
    elif strExists > 1:
        strExists = animeStorylineFix1.find('[Written by MAL Rewrite]')
        if(strExists < 1):
            animeStorylineFix2 = animeStorylineFix1.split("<button class=\"js-toggle-text", 1)
            animeStorylineFix3 = animeStorylineFix2[0].split("\n", 1)
            return animeStorylineFix3[0]      
        else:
            animeStorylineFix2 = animeStorylineFix1.split("[Written by MAL Rewrite]", 1)
            animeStorylineFix3 = animeStorylineFix2[0].split("\n", 1)
            return animeStorylineFix3[0]

        
    
    # else:
    #     return ""