def bannerCodeClean(bannerList):
    bannerCleaned = []

    for banner in bannerList:
        banner = banner.replace('\"', '')
        banner = banner.split("height=\"98\" loadlate=",1)[1]
        banner = banner.split("\" src=", 1)[0]
        bannerCleaned.append(banner)
        
    return bannerCleaned