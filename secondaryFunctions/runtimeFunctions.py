#runtime main
def getRuntime(container):

    if container.p.find('span', class_ = 'runtime') is not None:
        time = int(container.p.find('span', class_ = 'runtime').text.replace(" min", "")) # remove the minute word from the runtime and make it an integer
        fixedTime = str(runtimeFormatter(time)) #Formatting it to str, to prevent future code to treat int like float while printing
        return fixedTime
    else:
        return "DELETEME"

def runtimeFormatter(runtime):
    
    if(runtime < 100):
        return 1
    elif(runtime < 151):
        return 2
    elif(runtime > 151):
        return 3
    
#Anime Runtime Main
def animeGetRuntime(container):
   
    if container.find_all('div', class_ = 'info') is not None:
        runtimeAnimeList = container.find_all('div', class_ = 'info')
        runtimeFormatFixed = str(getAnimeRuntimeFormat(runtimeAnimeList))
        runtimeAnimeFormat = runtimeAnimeFormatter(runtimeFormatFixed)
        return runtimeAnimeFormat
    else:
        return("DELETEME")  


def getAnimeRuntimeFormat(runtimeList):
    
    a = runtimeList
    firstFixList = str(runtimeList).rsplit(" min", 1)
    runtimeFix = str(firstFixList[0])
    secondFixList = runtimeFix.rsplit("<span>", 1)
    runtimeSecondFix = str(secondFixList[1])

    return runtimeSecondFix



def runtimeAnimeFormatter(mins):

    try :
        min = int(mins)
        if(min < 15):
            return "DELETEME"
        elif(min < 36):
            return "1"
        elif(min < 80):
            return "2"
        elif(min > 80):
            return "3"
    except :
        return "DELETEME"