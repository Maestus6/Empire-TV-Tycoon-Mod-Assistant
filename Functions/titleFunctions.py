# Remove following characters for Windows Naming rescrictions:  \ / : * ? " < > | and blank space
import re

def getTitle(container):
    titles = []
    #titleXMLPic = []
    title = container.h3.a.text
    titles.append(title)
    titleXMLPic = titleXMLPicFixer(title) #Needed for naming during file creation and calling them via xml
    #titleXMLPic.append(titleXMLPicFixer(titles))
    return titles, titleXMLPic

def titleXMLPicFixer (titles):
    # fixTitle = []
    # for title in titles:
    titleChange =  re.sub('[^\w_.)( -]', '', titles) 
    # fixTitle.append(titleChange)

    return titleChange
    