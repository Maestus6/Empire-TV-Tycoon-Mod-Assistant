# Remove following characters for Windows Naming rescrictions:  \ / : * ? " < > | and blank space
import re

def getTitle(container):
    
    title = container.h3.a.text
    titleXMLPic = titleXMLPicFixer(title) #Needed for naming during file creation and calling them via xml
    return title, titleXMLPic

def titleXMLPicFixer (titles):
    
    titleChange =  re.sub('[^\w_.)( -]', '', titles)
    titleChange = titleChange.replace(' ', '_')
    return titleChange
    