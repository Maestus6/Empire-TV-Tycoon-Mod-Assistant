#runtime main
def getRuntime(container):

    if container.p.find('span', class_ = 'runtime') is not None:
        time = int(container.p.find('span', class_ = 'runtime').text.replace(" min", "")) # remove the minute word from the runtime and make it an integer
        fixedTime = str(runtimeFormatter(time)) #Formatting it to str, to prevent future code to treat int like float while printing
        return fixedTime
    else:
        return ""

def runtimeFormatter(runtime):
    
    if(runtime < 100):
        return 1
    elif(runtime < 151):
        return 2
    elif(runtime > 151):
        return 3
    
#anime runtime main
def getAnimeRuntime(container):

    if container.find_all('div', class_ = 'info') is not None:
        testList = container.find_all('div', class_ = 'info')
        print(testList)
    else:
        print("")