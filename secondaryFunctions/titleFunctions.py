# Remove following characters for Windows Naming rescrictions:  \ / : * ? " < > | and blank space
import re

##Movie
def getTitle(container):
    
    title = container.h3.a.text
    titleXMLPic = titleXMLPicFixer(title) #Needed for naming during file creation and calling them via xml
    return title, titleXMLPic

def titleXMLPicFixer (titles):
    
    titleChange =  re.sub('[^\w_.)( -]', '', titles)
    titleChange = titleChange.replace(' ', '_')
    return titleChange



##Anime
def getAnimeTitle(animeContainer):

    if animeContainer.find('span', class_ = 'js-title') is not None:

        title = animeContainer.find('span', class_ = 'js-title')
        titleXMLPic = fixAnimeContainer(str(title))
        print(titleXMLPic)
        return title, titleXMLPic

    else:
        return "", ""

def fixAnimeContainer (titles):

    firstFixList = titles.split(";\">", 1)
    titleFix = firstFixList[1]
    secondFixList = titleFix.split("</span>", 1)
    titleFix = secondFixList[0]
    titleFix = titleXMLPicFixer(titleFix)
    return titleFix
    




