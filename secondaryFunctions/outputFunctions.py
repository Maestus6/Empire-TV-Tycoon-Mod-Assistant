import sys #needed to write on notepad

def dataFramer(numOutputFull):  #outputResults (numOutputFull)

    orig_stdout = sys.stdout ##Original stdout
    with open('Output.txt', 'w') as sys.stdout:
        for looper in numOutputFull:
            if looper is not None:
                for titles, years, genres, movieOrSeries, episodes, pageScore, ratings, runtimes, titleXMLPic in looper:
                    titleUTCFix = str(titles.encode("utf-8"))
                    print('<Movie>')
                    print(f"<Id value=\"\">")
                    print(f"<Name value=\"{titleUTCFix}\">")
                    print("<Storyline value=\"\">")
                    print(f"<Year value=\"{years}\">")
                    print(f"<Genre value=\"{genres}\">") 
                    print(f"<Type value=\"{movieOrSeries}\">")
                    print(f"<Episodes value=\"{episodes}\">")
                    print(f"<Rating value=\"{pageScore}\">")
                    print(f"<Blocks value=\"{runtimes}\">")
                    print("<Cult value=\"0\">")
                    print(f"<Special value=\"{ratings}\">")
                    print("<Pirate value=\"0\">")  
                    print("<Speech value=\"\">")
                    print(f"<ImageTV value=\"{titleXMLPic}_{years}_tv.png\">")
                    print(f"<ImagePoster value=\"{titleXMLPic}_{years}_p.png\">")
                    print('</Movie>')

    sys.stdout.close()
    sys.stdout=orig_stdout ##Back to original stdout after writing is done


