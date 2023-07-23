import sys #needed to write on notepad

def dataFramer(numOutputFull):  #outputResults (numOutputFull)

    orig_stdout = sys.stdout ##Original stdout
    with open('Output.txt', 'w') as sys.stdout:
        for looper in numOutputFull:
            for titles, years, genres, movieOrSeries, episodes, pageScore, ratings, runtimes, titleXMLPic in looper:
                print('<Movie>')
                print(f"<Id value=\"\">")
                print(f"<Name value=\"{titles}\">")
                print(f"<Storyline value=\"\">")
                print(f"<Year value=\"{years}\">")
                print(f"<Genre value=\"{genres}\">") 
                print(f"<Type value=\"{movieOrSeries}\">")
                print(f"<Episodes value=\"{episodes}\">")
                print(f"<Rating value=\"{pageScore}\">")
                print(f"<Blocks value=\"{runtimes}\">")
                print(f"<Cult value=\"0\">")
                print(f"<Special value=\"{ratings}\">")
                print(f"<Pirate value=\"0\">")  
                print(f"<Speech value=\"\">")
                print(f"<ImageTV value=\"{titleXMLPic}_{years}_tv.png\">")
                print(f"<ImagePoster value=\"{titleXMLPic}_{years}_p.png\">")
                print('</Movie>')

    sys.stdout.close()
    sys.stdout=orig_stdout ##Back to original stdout after writing is done


