def getYear(container):

    if container.h3.find('span', class_= 'lister-item-year text-muted unbold') is not None:
        year = container.h3.find('span', class_= 'lister-item-year text-muted unbold').text # remove the parentheses around the year and make it an integer
        yearFixed = yearFormatter(year)
        return yearFixed
    else:
        return ""

def yearFormatter(year):

    year = year.replace('(','').replace(')','').replace('-','').replace('�','').replace(' ','') # doesn't fixes the problem for special invis characters
    purifiedYear = []
    for index in range(0, len(year), 4):
        purifiedYear.append(year[index:index+4])
    return purifiedYear[0]

    