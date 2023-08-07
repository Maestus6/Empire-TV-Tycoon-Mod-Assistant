import sys #needed to write on notepad
import os

def dataFramer(numOutputFull, year):  #outputResults (numOutputFull)

    orig_stdout = sys.stdout ##Original stdout
    if(os.path.exists("output") == False):
        os.mkdir("output") ##creates folder as images
    with open(f'output/Movies_{year}.xml', 'w') as sys.stdout:

        # print('<!-- <xml>')
        # print('	<Movies>')
        for looper in numOutputFull:
            if looper is not None:
                for titles, storyline, years, genres, movieOrSeries, episodes, pageScore, runtimes, cult, ratings, titleXMLPic, gotTVScreen in looper:
                    print('		<Movie>')
                    print(f"			<Id value=\"\">")
                    print(f"			<Name value=\"{titles}\">")
                    print(f"			<Storyline value=\"{storyline}\">")
                    print(f"			<Year value=\"{years}\">")
                    print(f"			<Genre value=\"{genres}\">") 
                    print(f"			<Type value=\"{movieOrSeries}\">")
                    print(f"			<Episodes value=\"{episodes}\">")
                    print(f"			<Rating value=\"{pageScore}\">")
                    print(f"			<Blocks value=\"{runtimes}\">")
                    print(f"			<Cult value=\"{cult}\">")
                    print(f"			<Special value=\"{ratings}\">")
                    print("			<Pirate value=\"0\">")  
                    print("			<Speech value=\"\">")
                    if(gotTVScreen != "DELETEME"):
                        print(f"			<ImageTV value=\"{titleXMLPic}_{years}_tv.png\">")
                    else:
                        print("			<ImageTV value=\"\">")
                    print(f"			<ImagePoster value=\"{titleXMLPic}_{years}_p.png\">")
                    print('		</Movie>')

        # print('	</Movies>')
        # print('</xml> -->')

    sys.stdout.close()
    sys.stdout=orig_stdout ##Back to original stdout after writing is done

