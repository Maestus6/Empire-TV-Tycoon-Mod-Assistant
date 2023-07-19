def yearFormatter(year):
    year = year.replace('(','').replace(')','').replace('-','').replace('�','').replace(' ','') # doesn't fixes the problem for special invis characters

    purifiedYear = []
    for index in range(0, len(year), 4):
        purifiedYear.append(year[index:index+4])
    
    return purifiedYear[0]

    