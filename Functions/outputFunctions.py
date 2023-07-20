import pandas as pd #needed for dataframe
import sys #needed to write on notepad

def dataFramer(titles, years, ratings, genres, runtimes, imdb_ratings, titleXMLPic):

    pdOutputFull = pd.DataFrame({'movie': titles,
                      'year': years,
                      'rating': ratings,
                      'genre': genres,
                      'runtime_min': runtimes,
                      'imdb': imdb_ratings,
                      'titleXMLPic': titleXMLPic}
                      )
    numOutputFull = pdOutputFull.to_numpy()
    
    return numOutputFull

def outputResults(numOutputFull):
    with open('Output.txt', 'w') as sys.stdout:
        for titles, years, ratings, genres, runtimes, imdb_ratings, titleXMLPic in numOutputFull:
            print('<Movie>')
            print(f"<Id value=\"\">")
            print(f"<Name value=\"{titles}\">")
            print(f"<Storyline value=\"\">")
            print(f"<Year value=\"{years}\">")
            print(f"<Genre value=\"{genres}\">") 
            print(f"<Type value=\"1\">")
            print(f"<Episodes value=\"{runtimes}\">")
            print(f"<Rating value=\"{imdb_ratings}\">")
            print(f"<Blocks value=\"{runtimes}\">")
            print(f"<Cult value=\"0\">")
            print(f"<Special value=\"{ratings}\">")
            print(f"<Pirate value=\"0\">")  
            print(f"<Speech value=\"\">")
            print(f"<ImageTV value=\"{titleXMLPic}_{years}_tv.png\">")
            print(f"<ImagePoster value=\"{titleXMLPic}_{years}_p.png\">")
            print('</Movie>')