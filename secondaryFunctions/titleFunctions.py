# Remove following characters for Windows Naming rescrictions:  \ / : * ? " < > | and blank space
import re

##Movie
def getTitle(container):
    
    title = container.h3.a.text
    titleStr = titleUTCFixer(title)
    titleXMLPic = titleXMLPicFixer(titleStr) #Needed for naming during file creation and calling them via xml
    return titleStr, titleXMLPic

def titleXMLPicFixer (titles):
    
    titleChange =  re.sub('[^\w_.)( -]', '', str(titles))
    titleChange = titleChange.replace(' ', '_')
    return titleChange

def titleUTCFixer (title):

    titleUTCFix = str(title.encode("utf-8"))
    if titleUTCFix[0] == "b":
        titleUTCFix = titleUTCFix[2:]
        titleUTCFix = titleUTCFix[:-1]
        return str(titleUTCFix)
    else:
        return str(titleUTCFix)



##Anime
def getAnimeTitle(animeContainer):

    if animeContainer.find('span', class_ = 'js-title') is not None:

        title = animeContainer.find('span', class_ = 'js-title')
        title = fixAnimeContainer(str(title))
        titleStr = titleUTCFixer(title)
        titleXMLPic = titleXMLPicFixer(titleStr)
        return titleStr, titleXMLPic

    else:
        return "DELETEME", "DELETEME"

def fixAnimeContainer (titles):

    firstFixList = titles.split(";\">", 1)
    titleFix = firstFixList[1]
    secondFixList = titleFix.split("</span>", 1)
    titleFix = secondFixList[0]
    return titleFix







