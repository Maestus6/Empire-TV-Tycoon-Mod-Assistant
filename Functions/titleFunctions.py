# Remove following characters for Windows Naming rescrictions:  \ / : * ? " < > | and blank space
def titleXMLPicFixer (titles):
    fixTitle = []
    for title in titles:
        title.replace(":", "").replace(" ","").replace("*","").replace("?","").replace("/","").replace("<","").replace(">","").replace("|","")
        title.replace("/","").replace("\\","").replace(">","").replace("|","").replace("/","").replace("\"","")
        fixTitle.append(title)

    return fixTitle
    