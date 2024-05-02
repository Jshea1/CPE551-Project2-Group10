import os
from tkinter import filedialog, messagebox
from Book import Books
from Shows import Show

class Recommender:
    def __init__(self):
        self.__books = {}
        self.__shows = {}
        self.__associations = {}

    def loadBooks(self):
        '''Loads Books into Dictionary from csv file'''

        while True:
            file = filedialog.askopenfile(initialdir=os.getcwd(), title='Load Books information file', filetypes=[("CSV files", "*.csv")])
            if file:
                if os.path.exists(file):
                    with open(file) as bookfile:                    # !!!! IDK IF IT HAS TO REPEATEDLY ASK THE USER FOR A FILE IF THEY INPUT IT WRONG!!! 
                        for line in bookfile:
                            _line = line.strip().split(',')
                            
                            # Explode the line value as parameters to book class
                            #  for this i've made sure that each element in the line will be taken in as paramater
                            self.__books[f'{_line[0]}'] = Books(*_line)
                    break
            else:
                messagebox.showerror('Error', 'No File Selected')


    def loadShows(self):
        '''Loads Shows into Dictionary from csv file'''
        while True:
            file = filedialog.askopenfile(initialdir=os.getcwd(), title='Load Shows information file', filetypes=[("CSV files", "*.csv")])
            if file:
                if os.path.exists(file):                # !!!! IDK IF IT HAS TO REPEATEDLY ASK THE USER FOR A FILE IF THEY INPUT IT WRONG!!! 
                    with open(file) as showfile:
                        for line in showfile:
                            _line = line.strip().split(',')
                            self.__shows[f'{_line[0]}'] = Show(*_line)
                    break

            else:
                messagebox.showerror('Error', 'No File Selected')
        #pass

    def loadAssociations(self):
        # Implement loading associations from file
        pass

    def getMovieList(self):
        movies = {}
        #filtering only movies
        for id, info in self.__shows.items():
            if info.getType() == 'Movie':  
                movies[id] = info


        # max len for formatting
        maxTitleLength = 0
        maxDurationLength = 0
        for movie in movies.values():
            if len(movie['title']) > maxTitleLength:
                maxTitleLength = len(movie['title'])
            if len(movie['duration']) > maxDurationLength:
                maxDurationLength = len(movie['duration'])

        # printing header
        print(f"{'Title':<{maxTitleLength}} | {'Duration':>{maxDurationLength}}")

        # printing vals in format
        for movie in movies.values():
            print(f"{movie['title']:<{maxTitleLength}} | {movie['duration']:>{maxDurationLength}}")

    def getTVList(self):
        # filtering only shows
        TVShows = {}
        for id, info in self.__shows.items():
            if info.getType() == 'TV Show':
                TVShows[id] = info

        # max len for formatt
        maxTitleLength = 0
        maxSeasonsLength = 0
        for TVShows in TVShows.values():
            if len(TVShows['title']) > maxTitleLength:
                maxTitleLength = len(TVShows['title'])
            seasonsLength = len(TVShows['duration'])  
            if seasonsLength > maxSeasonsLength:
                maxSeasonsLength = seasonsLength

        # printing headers
        print(f"{'Title':<{maxTitleLength}} | {'Seasons':>{maxSeasonsLength}}")

        # prtinin vals in format
        for TVShows in TVShows.values():
            print(f"{TVShows['title']:<{maxTitleLength}} | {TVShows['duration']:>{maxSeasonsLength}}")


    def getBookList(self):
        # max len for formatting
        maxTitleLength = 0
        maxAuthorsLength = 0
        for book in self.__books.values():
            if len(book.title) > maxTitleLength:
                maxTitleLength = len(book.title)
            if len(book.authors) > maxAuthorsLength:
                maxAuthorsLength = len(book.authors)

        # printing headers
        print(f"{'Title':<{maxTitleLength}} | {'Authors':<{maxAuthorsLength}}")

        # printing values in format
        for book in self.__books.values():
            print(f"{book.title:<{maxTitleLength}} | {book.authors:<{maxAuthorsLength}}")


    def getMovieStats(self):
        movies = {}
        for id, info in self.__shows.items():
            if info.getShowType() == 'Movie':
                movies[id] = info

        ratings = {}
        totalDuration = 0
        directors = {}
        actors = {}
        genres = {}

        for movie in movies.values():
            # counting ratings
            rating = movie.getRating()
            ratings[rating] = ratings.get(rating, 0) + 1
            
            # duration total
            duration = int(movie.getDuration())
            totalDuration += duration
            
            # director total
            director = movie.getDirectors()
            directors[director] = directors.get(director, 0) + 1
            
            # cast total
            for actor in movie.getCast().split(', '):
                actors[actor] = actors.get(actor, 0) + 1

            # genre total
            for genre in movie.getGenres().split(', '):
                genres[genre] = genres.get(genre, 0) + 1

        # stat calcs
        totalMovies = len(movies)
        ratingPercentages = {r: f"{(count / totalMovies * 100):.2f}%" for r, count in ratings.items()}
        averageDuration = f"{totalDuration / totalMovies:.2f}"
        mostCommonDirector = max(directors, key=directors.get)
        mostCommonActor = max(actors, key=actors.get)
        mostCommonGenre = max(genres, key=genres.get)

        # printing stats -----------------------------------------------!!! ARE WE PRINTING OR MAKING A BIG RETURN STATEMENT? !!!
        print(f"Rating Percentages: {ratingPercentages}")
        print(f"Average Movie Duration: {averageDuration} minutes")
        print(f"Most Common Director: {mostCommonDirector}")
        print(f"Most Common Actor: {mostCommonActor}")
        print(f"Most Common Genre: {mostCommonGenre}")



    def getTVStats(self):
        # Filter TV shows from the list
        tv_shows = {id: info for id, info in self.__shows.items() if info.getShowType() == 'TV Show'}

        ratings = {}
        totalSeasons = 0
        cast = {}
        genres = {}

        for show in tv_shows.values():
            # total ratings
            rating = show.getRating()
            ratings[rating] = ratings.get(rating, 0) + 1
            
            # total seasons
            seasons = int(show.getDuration())  
            totalSeasons += seasons
            
            # Cast total
            for actor in show.getCast().split(', '):
                cast[actor] = cast.get(actor, 0) + 1

            # Genre total
            for genre in show.getGenres().split(', '):
                genres[genre] = genres.get(genre, 0) + 1

        # stat calcs
        totalTVShows = len(tv_shows)
        ratingPercentages = {r: f"{(count / totalTVShows * 100):.2f}%" for r, count in ratings.items()}
        averageSeasons = f"{totalSeasons / totalTVShows:.2f}"
        mostCommonActor = max(cast, key=cast.get)
        mostCommonGenre = max(genres, key=genres.get)


        #printing -----------------------------------------------!!! ARE WE PRINTING OR MAKING A BIG RETURN STATEMENT? !!!
        print(f"Rating Percentages: {ratingPercentages}")
        print(f"Average Number of Seasons: {averageSeasons}")
        print(f"Most Common Actor: {mostCommonActor}")
        print(f"Most Common Genre: {mostCommonGenre}")


    def getBookStats(self):

        totalPageCount = 0
        authors = {}
        publishers = {}

        for book in self.__books.values():
            # pg count
            pageCount = int(book.getPageCount())
            totalPageCount += pageCount
            
            # book count by author
            author = book.getAuthor()
            authors[author] = authors.get(author, 0) + 1

            # book count by pub
            publisher = book.getPublisher()
            publishers[publisher] = publishers.get(publisher, 0) + 1

        # stat calc
        totalBooks = len(self.__books)
        averagePageCount = f"{totalPageCount / totalBooks:.2f}" 
        mostCommonAuthor = max(authors, key=authors.get)
        mostCommonPublisher = max(publishers, key=publishers.get)

        # printing  -----------------------------------------------!!! ARE WE PRINTING OR MAKING A BIG RETURN STATEMENT? !!!
        print(f"Average Page Count: {averagePageCount}")
        print(f"Author with Most Books: {mostCommonAuthor}")
        print(f"Publisher with Most Books: {mostCommonPublisher}")

    def searchTVMovies(self, title, director, cast, genre):
        # Implement searching for TV shows and movies
        pass

    def searchBooks(self, title, author, publisher):
        # Implement searching for books
        pass

    def getRecommendations(self, type_, title):
        # Implement getting recommendations
        pass
