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

        # for entry in fileName:
        #     pass

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
            if info['type'] == 'Movie':
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
            if info['type'] == 'TV Show':
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
        # Implement getting statistics for movies
        pass

    def getTVStats(self):
        # Implement getting statistics for TV shows
        pass

    def getBookStats(self):
        # Implement getting statistics for books
        pass

    def searchTVMovies(self, title, director, actor, genre):
        # Implement searching for TV shows and movies
        pass

    def searchBooks(self, title, author, publisher):
        # Implement searching for books
        pass

    def getRecommendations(self, type_, title):
        # Implement getting recommendations
        pass
