# Remove following characters for Windows Naming rescrictions:  \ / : * ? " < > | and blank space
import re

def titleXMLPicFixer (titles):
    fixTitle = []
    for title in titles:
        titleChange =  re.sub('[^\w_.)( -]', '', title) 
        fixTitle.append(titleChange)

    return fixTitle
    