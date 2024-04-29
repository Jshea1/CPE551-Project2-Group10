import os
class Recommender:
    def __init__(self):
        self.books = {}
        self.shows = {}
        self.associations = {}

    def loadBooks():
        fileName = input("what is your files neme?")
        while not os.path.exists(fileName):
            fileName = input("File does not exist. Please enter a correct file name: ")
        
        for entry in fileName:
            pass
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