
#Genre Main
def getGenre(container):

    if container.p.find('span', class_ = 'genre') is not None:

        genresList = container.p.find('span', class_ = 'genre').text.replace("\n", "").strip().split(",") # remove the whitespace character, strip, and split to create an array of genres  
        genresNoWhiteSpace = genreSpaceFix(genresList)
        genresSpecial = str(specialGenreCheck(genresNoWhiteSpace)) #to check if it is an animation
        genresFormated = genreValidator(genresNoWhiteSpace)
        genrePicked = genrePicker(genresFormated)
        genreCompleted = str(genreStrToInt(genrePicked)) #Formatting it to str, to prevent future code to treat int like float while printing
        return genreCompleted, genresSpecial
    
    else:
        return (""), "0"
                

def genreSpaceFix(genreslist):
    genresnowhitespace = []
    for genre in genreslist:
        genre = genre.strip()
        genresnowhitespace.append(genre)
    return genresnowhitespace


def specialGenreCheck (genreList):
    if any("Animation" in s for s in genreList):
        return 1
    elif any("Romance" in s for s in genreList):
        return 2
    else:
        return 0

def genreValidator(genres):
    validGenres = ['Comedy', 'Drama', 'Sci-Fi', 'Documentary', 'Horror', 'Western', 'Sport', 'Fantasy', 'Musical', 'Romance', 'Action', 'Gameshow', 'Adult', 'Adventure', 'Mystery', 
                   'Thriller', 'War']
    genreSetsValid = []
    for genreSet in genres:
        if genreSet in validGenres:
            genreSetsValid.append(genreSet)
    return genreSetsValid

def genrePicker(genre):
    
    Drama = 0
    Comedy = 0
    Documentary = 0 #
    Adult = 0 #
    Action = 0 #
    Romance = 0 #
    Thriller = 0 #
    Horror = 0 #
    Music = 0 #
    Adventure = 0 #
    Fantasy = 0 #
    SciFi = 0 #
    Mystery = 0 #
    Sport = 0 #
    Musical = 0 #
    Western = 0 #
    GameShow = 0 #
    War = 0 #

    for oneGenre in genre:
        match oneGenre:
            case "Drama":
                Drama+= 1
            case "Comedy":
                Comedy+= 1
            case "Documentary": 
                Documentary+= 1
            case "Adult": 
                Adult+= 1
            case "Action":
                Action+= 1
            case "Romance":
                Romance+= 1
            case "Thriller":
                Thriller+= 1
            case "Horror":
                Horror+= 1
            case "Music":
                Music+= 1
            case "Adventure":
                Adventure+= 1
            case "Fantasy":
                Fantasy+= 1
            case "Sci-Fi":
                SciFi+= 1
            case "Mystery":
                Mystery+= 1
            case "Sport":
                Sport+= 1
            case "Musical":
                Musical+= 1
            case "Western":
                Western+= 1
            case "War":
                War+= 1
            case "Game-Show":
                GameShow+= 1


##Sorry for the big IF block, let's change this in the future if we can, it is not efficient at all
    if(GameShow == 1):  ##Start of certainity
        return 'Gameshow'
    elif(Documentary == 1):
        return 'Documentary'
    elif(Music == 1):
        return 'Music' ##End of certainity
    
    elif(War == 1):    ##Phase of Subgenres
        if(Action == 1):
            return 'Action'
        elif(Drama == 1):
            return 'Drama'
    elif(Adult == 1):
        if(Drama == 1):
            return 'Drama'
        elif(Romance == 1):
            return 'Romance'
    elif(Adventure == 1):
        if(Fantasy == 1):
            return 'Fantasy'
        elif(SciFi == 1):
            return 'Sci-Fi'
        elif(Western == 1):
            return 'Western'
        elif(Action == 1):
            return 'Action'
    elif(Mystery == 1):
        if(SciFi == 1):
            return 'Sci-Fi'
        elif(Horror == 1):
            return 'Horror'
        elif(Drama == 1):
            return 'Drama'
    elif(Thriller == 1):
        if(Horror == 1):
            return 'Horror'
        elif(Western == 1):
            return 'Western'
        elif(SciFi == 1):
            return 'Sci-Fi'
        elif(Action == 1):
            return 'Action'
        elif(Sport == 1):
            return 'Sport'
        elif(Drama ==  1):
            return 'Drama'
        elif(Romance == 1):
            return 'Romance' ##End of the Subgenres
        
    elif(Sport == 1): ##Rest of the main Genres
        return 'Sport'
    elif(SciFi == 1):
        return 'Sci-Fi'
    elif(Western == 1): 
        if(Horror == 1):
            return 'Horror'
        else:
            return 'Western'
    elif(Fantasy == 1):
        return 'Fantasy'
    elif(Horror == 1):
        return 'Horror'
    elif(Romance == 1):
        return 'Romance'
    elif(Action == 1):
        return 'Action'
    elif(Drama == 1):
        return 'Drama'
    elif(Comedy == 1):
        return 'Comedy' ##End of sad IF Block and function
    else:
        return 'Something went wrong!'
    
def genreStrToInt(genreStr):
    match genreStr:
        case "Comedy":
            return 0
        case "Drama":
            return 1
        case "Sci-Fi":
            return 2
        case "Documentary":
            return 3
        case "Horror":
            return 4
        case "Western":
            return 5
        case "Sport":
            return 6
        case "Fantasy":
            return 7
        case "Musical":
            return 8
        case "Romance":
            return 9
        case "Action":
            return 10
        case "Gameshow":
            return 11
        case "Something went wrong!":
            return "Something went wrong!"
    
    


