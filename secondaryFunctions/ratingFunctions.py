#(0) REGULAR MOVIE (1) +16 (2) XXX (3) GLAMOUR (4) CARTOON (5) ANIME

#Rating Main
def getRating(container, genresSpecial):

    if container.p.find('span', class_ = 'certificate') is not None:
        rating = container.p.find('span', class_= 'certificate').text
        ratingFound, movieOrSeries = ratingFinder(genresSpecial, rating)
        return ratingFound, movieOrSeries

    else:
        return "DELETEME", "DELETEME"
    
def ratingFinder(specialGenre, rating):

    movieOrSeries = rating.find('TV')

    if specialGenre == 1 and movieOrSeries > 0 :
        return "4", "2"
    elif specialGenre == 1 and movieOrSeries < 1 :
        return "4", "1"
    elif specialGenre == 2 and movieOrSeries > 0 :
        return "3", "2"
    elif specialGenre == 2 and movieOrSeries < 1 :
        return "3", "1"
    elif rating == "TV-MA" :
        return "1", "2"
    elif movieOrSeries > 0  :
        return "0", "2"
    elif(rating == "R" or rating == "NC-16" or rating == "NC-17" or rating == "NC_18" or rating == "PG-16" or rating == "PG-17" or rating == "PG-18"):
        return "1", "1"
    else:
        return "0", "1"
    


def isItCult(title, year):

    returnList = []
    f = open("CultMoviesList.xml", "r")
    cultsList = f.readline()
    f.close()
    counter = 0






