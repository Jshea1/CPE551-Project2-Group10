import os
from tkinter import filedialog, messagebox
from Book import Books

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
                if os.path.exist(file):
                    with open(file) as bookfile:
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
        # Implement loading shows from file
        pass

    def loadAssociations(self):
        # Implement loading associations from file
        pass

    def getMovieList(self):
        # Implement getting list of movies
        pass

    def getTVList(self):
        # Implement getting list of TV shows
        pass

    def getBookList(self):
        # Implement getting list of books
        pass

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
