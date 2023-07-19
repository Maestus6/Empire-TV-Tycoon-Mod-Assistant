

def genreSpaceFix(genreslist):
    genresnowhitespace = []
    for genre in genreslist:
        genre = genre.strip()
        genresnowhitespace.append(genre)


def genreValidator(genres):
    validgenres = ['Comedy', 'Drama', 'Sci-Fi', 'Documentary', 'Horror', 'Western', 'Sport', 'Fantasy', 'Musical', 'Romance', 'Action', 'Gameshow', 'Adult', 'Adventure', 'Mystery', 
                   'Thriller', 'War', 'Animation']
    genresetsvalid = []

    for genreset in genres:
        genresetvalid = []
        for genre in genreset:
            if genre in validgenres:
                genresetvalid.append(genre)
        genresetsvalid.append(genresetvalid)

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
    Animation = 0 #

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
            case "Animation":
                Animation+= 1


##Sorry for the big IF block, let's change this in the future if we can, it is not efficient at all --Maestus

    if(GameShow == 1):  ##Start of certainity
        return 'Gameshow'
    elif(Documentary == 1):
        return 'Documentry'
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
            return 'SciFi'
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
        return 'SciFi'
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
    
    
    


