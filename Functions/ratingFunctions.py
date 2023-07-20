#(0) REGULAR MOVIE (1) +16 (2) XXX (3) GLAMOUR (4) CARTOON (5) ANIME

#Rating Main
def getRating(container, genresAnimation):

    ratings = []
    rating = container.p.find('span', class_= 'certificate').text
    ratingFound = ratingFinder(genresAnimation, rating)
    ratings.append(ratingFound)
    return ratings

    
def ratingFinder(animation, rating):
    if(animation == 1):
        return "4"
    elif(rating == "R" or rating == "NC-16" or rating == "NC-17" or rating == "NC_18" or rating == "TV-MA" or rating == "PG-16" or rating == "PG-17" or rating == "PG-18"):
        return "1"
    else:
        return "0"
    








