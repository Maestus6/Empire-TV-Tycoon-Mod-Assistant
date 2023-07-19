# Empire-TV-Tycoon-Mod-Assistant

Here are some useful notes for future development:

#Format for XML files are:

<!-- XML MOVIES #1.5.0#
----- [IMAGES] -----

TV IMAGES (374x254): CREATE A 'imagesMovieTV' FOLDER UNDER YOUR ADDON FOLDER
PLACE ALL THE IMAGES THERE AND TYPE THE NAME (WITHOUT EXTENSION) IN THE 'IMAGETV' FIELD FOR ANY MOVIE
POSTER IMAGES (112x168): CREATE A 'imagesMoviePoster' FOLDER UNDER YOUR ADDON FOLDER
PLACE ALL THE IMAGES THERE AND TYPE THE NAME (WITHOUT EXTENSION) IN THE 'IMAGEPOSTER' FIELD FOR ANY MOVIE
ALL IMAGES MUST BE PNG

----- [VALUE GUIDE] -----

ID -> THE ID OF THE MOVIE. USE THE SAME ID TO 'EDIT' THE MOVIE OR LEAVE IT BLANK TO PRODUCE A 'NEW' ONE
NAME -> THE NAME OF THE MOVIE
STORYLINE -> THE STORYLINE OF THE MOVIE
YEAR -> THE YEAR THAT THE MOVIE WAS PRODUCED (THIS IS USED IN DAILY QUESTS)
GENRE -> THE GENRE OF THE MOVIE (0) COMEDY (1) DRAMA (2) SCI-FI (3) DOCUMENTARY (4) HORROR (5) WESTERN (6) SPORT (7) FANTASY (8) MUSICAL (9) ROMANCE (10) ACTION (11) GAMESHOW
TYPE -> (1) MOVIES (2) TV SHOWS
EPISODES -> # OF EPISODES IN CASE THAT IT IS A TV SHOW. ACCEPTED VALUES ARE (5), (10) AND (15) IF IT IS A MOVIE THEN (0).
RATING -> THE MOVIE RATING, GOES FROM (0.0) TO (10.0)
BLOCKS -> THE NUMBER OF BLOCKS FOR THIS MOVIE, GOES FROM (1) TO (3)
CULT -> (0) REGULAR MOVIE (1) CULT MOVIE
SPECIAL -> (0) REGULAR MOVIE (1) +16 (2) XXX (3) GLAMOUR (4) CARTOON (5) ANIME
PIRATE -> (0) REGULAR MOVIE (1) PIRATE MOVIE
SPEECH -> TEXT THAT WILL BE SAID BY THE AUDIENCE RANDOMLY WHEN THE MOVIE IS BEING BROADCASTED
IMAGETV -> THE IMAGE NAME (WITHOUT EXTENSION) THAT WILL BE USED FOR THIS MOVIE IN THE TV PICTURE
IMAGEPOSTER -> THE IMAGE NAME (WITHOUT EXTENSION) THAT WILL BE USED FOR THIS MOVIE IN THE LISTS


EXAMPLE OF MODIFYING THE FIRST MOVIE OF THE GAME ID=500 (CHANGED THE STORYLINE AND SCORE), TRANSLATING THE SECOND MOVIE, AND THEN ADDINGA NEW MOVIE AND A NEW TV-SHOW INTO THE GAME

- THE ID FIELD IS ALWAYS REQUIRED, EVEN WITH NEW MOVIES YOU MUST INCLUDE THE ID FIELD AND LEAVE IT BLANK.
- FOR MODIFYING OR TRANSLATING A MOVIE YOU ONLY NEED THE ID AND THE FIELDS THAT YOU WANT TO MODIFY
- WHEN ADDING A NEW MOVIE, YOU NEED TO INCLUDE ALL THE FIELDS EVEN IF SOME OF THEM(STORYLINE,SPEECH AND IMAGES) ARE LEFT BLANK.
--> 
 
<xml>
	<Movies>
		<Movie>
			<Id value="500">
			<Storyline value="The cross-country adventures of two good-hearted but incredibly stupid friends.">
			<Rating value="6.2">
		</Movie>
		<Movie>
			<Id value="501">
			<Name value="Title in my language">
			<Storyline value="Translated Storyline">
			<Speech value="Translated speech">
		</Movie>
		<Movie>
			<Id value="">
			<Name value="My robot movie">
			<Storyline value="Robots and lasers!">
			<Year value="2016">
			<Genre value="2">
			<Type value="1">
			<Episodes value="0">
			<Rating value="9.3">
			<Blocks value="2">
			<Cult value="0">
			<Special value="0">
			<Pirate value="0">
			<Speech value="Whoooaaahhhh!!!">
			<ImageTV value="">
			<ImagePoster value="">
		</Movie>
		<Movie>
			<Id value="">
			<Name value="My robot show">
			<Storyline value="Robots and lasers! now every week!">
			<Year value="2016">
			<Genre value="2">
			<Type value="2">
			<Episodes value="10">
			<Rating value="9.2">
			<Blocks value="1">
			<Cult value="0">
			<Special value="0">
			<Pirate value="0">
			<Speech value="They are back!!!">
			<ImageTV value="">
			<ImagePoster value="">
		</Movie>
		
	</Movies>
</xml>


# Every genre available for movies:
Short
Drama
Comedy
Documentary
Adult
Action
Romance
Thriller
Animation
Family
Crime
Horror
Music
Adventure
Fantasy
Sci-Fi
Mystery
Biography
Sport
History
Musical
Western
War
Reality-TV
News
Talk-Show
Game-Show
Film-Noir
Lifestyle
Experimental
Commercial
