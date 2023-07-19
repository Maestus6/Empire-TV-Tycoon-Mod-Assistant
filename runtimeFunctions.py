def runtimeFormatter(runtimeList):
    runtimeList = []
    for runtime in runtimeList:
        if(runtime < 100):
            runtimeList.append(1)
        elif(runtime < 150):
            runtimeList.append(2)
        elif(runtime > 179):
            runtimeList.append(3)
    return runtimeList