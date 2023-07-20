#PageScore main
def getPageScore(container):

    if (container.strong) is not None:

        pageScore = float(container.strong.text) # non-standardized variable
        pageScore = round((pageScore / 10), 2) #From 1/100 Point System to 0.00/1.00, formatting to max two decimals
        return pageScore

    else:
        return ""
    
    
#AlternativeScore main
def getAlternativeScore(container):

    if container.find('span', class_ = 'metascore') is not None:
        return 1

    else:
        return 2