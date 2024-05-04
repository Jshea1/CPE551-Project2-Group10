# Authors: Saurabh Raman Parkar, Yash Patel, John Shea
# Date: 5-4-2024
# Description: Logic for getting information from files
# I pledge my honor that I have abided by the Stevens Honor System

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
        '''Loads Books into member variable in Dictionary format from csv file'''

        while True:
            # opens file dialog to select file
            # all load functions follow this structure
            file = filedialog.askopenfilename(initialdir=os.getcwd() + r'/inpur_files',
                                              title='Load Books information file', filetypes=[("CSV files", "*.csv")])
            if file:
                # checks if file exists
                if os.path.exists(file):
                    with open(file) as bookfile:
                        # skips the header
                        next(bookfile)
                        # reads each line and splits it by comma and stores it as
                        # a params list to pass to book class
                        for line in bookfile:
                            _line = line.strip().split(',')

                            # Explode the line value as parameters to book class
                            self.__books[f'{_line[0]}'] = Books(*_line)
                    break
            else:
                messagebox.showerror('Error', 'No File Selected')

    def loadShows(self):
        '''Loads Shows into Dictionary from csv file'''

        while True:
            file = filedialog.askopenfilename(initialdir=os.getcwd() + r'/input_files',
                                              title='Load Shows information file', filetypes=[("CSV files", "*.csv")])
            if file:
                if os.path.exists(file):
                    with open(file) as showfile:
                        next(showfile)
                        for line in showfile:
                            _line = line.strip().split(',')
                            self.__shows[f'{_line[0]}'] = Show(*_line)
                    break

            else:
                messagebox.showerror('Error', 'No File Selected')

    def loadAssociations(self):
        '''Loads Associations from file into associations member variable in Dictionary format from csv file'''

        while True:
            # Opens associated file and stores association in a dict in {id:[list]} format
            # with id(key) being showid or bookid as per the requirement and
            # list(values) being associated books/shows
            file = filedialog.askopenfilename(initialdir=os.getcwd() + r'/input_files', title='Loads Associations File',
                                              filetypes=[("CSV files", "*.csv")])
            if file:
                if os.path.exists(file):
                    with open(file) as associationfile:
                        # iterate over each line and split it by comma
                        # and store it in the associations dictionary
                        # with outer key being showid or bookid and inner key being associated showid or bookid
                        # and value being the count of association
                        for line in associationfile:
                            _line = line.strip().split(',')

                            # Show -> Books association
                            if _line[0] not in self.__associations:
                                self.__associations[_line[0]] = {_line[1]: 1}
                            else:
                                if _line[1] not in self.__associations[_line[0]]:
                                    self.__associations[_line[0]][_line[1]] = 1
                                else:
                                    self.__associations[_line[0]][_line[1]] += 1

                            # Book -> Shows association
                            if _line[1] not in self.__associations:
                                self.__associations[_line[1]] = {_line[0]: 1}
                            else:
                                if _line[0] not in self.__associations[_line[1]]:
                                    self.__associations[_line[1]][_line[0]] = 1
                                else:
                                    self.__associations[_line[1]][_line[0]] += 1

                    break
            else:
                messagebox.showerror('Error', 'No File Selected')

    def getMovieList(self):
        '''Filters only movies from the dictionary and returns a formatted string of all movies in the dictionary
        Returns : str
            Formatted string of all movies Title and Duration in the dictionary'''
        self.__movies = {}
        # All getList functions follow the same structure

        # filtering only movies
        for id, info in self.__shows.items():
            if info.getShowType() == 'Movie':
                self.__movies[id] = info

        # max len for formatting output
        maxTitleLength = 0
        for movie in self.__movies.values():
            if len(movie.getTitle()) > maxTitleLength:
                maxTitleLength = len(movie.getTitle())

        # Build the output as a list of strings
        output = []
        header = f"{'Title':<{maxTitleLength}}   Duration"
        output.append(header)

        # Adding each movie's information formatted
        for movie in self.__movies.values():
            title = movie.getTitle()
            duration = movie.getDuration()
            line = f"{title:<{maxTitleLength}}   {duration}"
            output.append(line)

        return "\n".join(output)

    def getTVList(self):
        '''filters only TV shows from the dictionary and returns a formatted string of all TV shows in the dictionary
        Returns : str
            Formatted string of all TV shows Title and Duration in the dictionary'''

        # filtering only shows
        self.__TVShows = {}
        for id, info in self.__shows.items():
            if info.getShowType() == 'TV Show':
                self.__TVShows[id] = info

        # max len for formatt
        maxTitleLength = 0
        for show in self.__TVShows.values():
            titlelength = len(show.getTitle())
            if titlelength > maxTitleLength:
                maxTitleLength = titlelength

            # Build the output as a list of strings
        output = []
        header = f"{'Title':<{maxTitleLength}}   Duration"
        output.append(header)

        # Adding each TV show's information formatted
        for show in self.__TVShows.values():
            title = show.getTitle()
            seasons = show.getDuration()
            line = f"{title:<{maxTitleLength}}   {seasons}"
            output.append(line)

        return "\n".join(output)

    def getBookList(self):
        '''Returns a formatted string of all books in the books dictionary'''

        # max len for formatting
        maxTitleLength = 0
        for book in self.__books.values():
            titleLength = len(book.getTitle())
            if titleLength > maxTitleLength:
                maxTitleLength = titleLength

        output = []
        header = f"{'Title':<{maxTitleLength}}   Author"
        output.append(header)

        # Format each book's information
        for book in self.__books.values():
            title = book.getTitle()
            author = book.getAuthor()
            line = f"{title:<{maxTitleLength}}  {author}"
            output.append(line)

        return "\n".join(output)

    def getMovieStats(self):
        '''Gets movie stats from the movies dictionary and returns a formatted string of the stats'''

        # initializing variables for stats
        ratings = {}
        totalDuration = 0
        directors = {}
        actors = {}
        genres = {}

        for movie in self.__movies.values():
            # counting ratings
            rating = movie.getRating()
            ratings[rating] = ratings.get(rating, 0) + 1

            # duration total
            duration = int(movie.getDuration().split(' ')[0])
            totalDuration += duration

            # director total
            director = movie.getDirectors()
            if director:
                directors[director] = directors.get(director, 0) + 1

            # cast total
            for actor in movie.getCast().split(', '):
                if actor:
                    actors[actor] = actors.get(actor, 0) + 1

            # genre total
            for genre in movie.getGenres().split(', '):
                genres[genre] = genres.get(genre, 0) + 1

        totalMovies = len(self.__movies)
        ratingPercentages = {r: f"{(count / totalMovies * 100):.2f}%" for r, count in ratings.items()}
        ratingOutput = "\n".join(f"{rating}: {percentage}" for rating, percentage in ratingPercentages.items())
        averageDuration = f"{totalDuration / totalMovies:.2f}"
        mostCommonDirector = max(directors, key=directors.get)
        mostCommonActor = max(actors, key=actors.get)
        mostCommonGenre = max(genres, key=genres.get)

        return (f"Rating Percentages:\n"
                f"{ratingOutput}\n"
                f"Average Movie Duration: {averageDuration} minutes\n"
                f"Most Common Director: {mostCommonDirector}\n"
                f"Most Common Actor: {mostCommonActor}\n"
                f"Most Common Genre: {mostCommonGenre}")

    def getTVStats(self):
        '''Gets TV show stats from the TV shows dictionary and returns a formatted string of the stats'''

        # initializing variables for stats
        ratings = {}
        totalSeasons = 0
        cast = {}
        genres = {}

        for show in self.__TVShows.values():
            # total ratings
            rating = show.getRating()
            if rating not in ratings:
                ratings[rating] = 1
            else:
                ratings[rating] += 1

            # total seasons
            seasons = int(show.getDuration().split(' ')[0])
            totalSeasons += seasons

            for actor in show.getCast().split(", "):
                if actor and "1" not in actor:
                    cast[actor] = cast.get(actor, 0) + 1

            # Genre total
            for genre in show.getGenres().split(','):
                if genre not in genres:
                    genres[genre] = 1
                else:
                    genres[genre] += 1
        # stat calcs
        totalTVShows = len(self.__TVShows)
        ratingPercentages = {r: f"{(count / totalTVShows * 100):.2f}%" for r, count in ratings.items()}
        ratingOutput = "\n".join(f"{rating}: {percentage}" for rating, percentage in ratingPercentages.items())
        averageSeasons = f"{totalSeasons / totalTVShows:.2f}"
        mostCommonActor = max(cast, key=cast.get)
        mostCommonGenre = max(genres, key=genres.get)

        # returning
        return (f"Rating Percentages:\n"
                f"{ratingOutput}\n"
                f"Average Number of Seasons: {averageSeasons}\n"
                f"Most Common Actor: {mostCommonActor}\n"
                f"Most Common Genre: {mostCommonGenre}")

    def getBookStats(self):
        '''Gets book stats from the books dictionary and returns a formatted string of the stats'''

        # initializing variables for stats
        totalPageCount = 0
        authors = {}
        publishers = {}

        for book in self.__books.values():
            pageCount = float(book.getNumPages())
            totalPageCount += pageCount

            author = book.getAuthor()
            if author in authors:
                authors[author] += 1
            else:
                authors[author] = 1

            publisher = book.getPublisher()
            if publisher in publishers:
                publishers[publisher] += 1
            else:
                publishers[publisher] = 1

        # stat calc
        totalBooks = len(self.__books)
        averagePageCount = f"{totalPageCount / totalBooks:.2f}"
        mostCommonAuthor = max(authors, key=authors.get)
        mostCommonPublisher = max(publishers, key=publishers.get)

        # returning
        return (f"Average Page Count: {averagePageCount}\n"
                f"Author with Most Books: {mostCommonAuthor}\n"
                f"Publisher with Most Books: {mostCommonPublisher}")

    # Search Functions and Recommedation function are flexible in the sense that they can search based on substring findings
    # since we use "term" in "object_term" approach rather "term"=="object_term",
    # to search for the term in the object attributes
    # but could be less efficient in terms of results, and search is case sensitive.

    def searchTVMovies(self, title, director, cast, genre):
        '''Searches for TV shows and movies based on the search terms provided'''

        # query list stores the search results from the search terms
        self.__query = []

        # exit function if files are not loaded
        if not self.__shows:
            messagebox.showerror('Error', 'Please Make sure you have loaded Shows file')
            return

        # exit function if no search term is entered
        if title == '' and director == '' and cast == '' and genre == '':
            messagebox.showerror('Error', 'Please enter a search term')
            return

        # Conditional search based on the search terms
        # and appends the search results to the query list
        # individual if statements are used to allow for multiple search terms
        # and combinations of search terms
        if title:
            for show in self.__shows.values():
                if title in show.getTitle():
                    self.__query.append(show)
        if director:
            for show in self.__shows.values():
                if director in show.getDirectors():
                    self.__query.append(show)
        if cast:
            for show in self.__shows.values():
                if cast in show.getCast():
                    self.__query.append(show)
        if genre:
            for show in self.__shows.values():
                if genre in show.getGenres():
                    self.__query.append(show)

        if len(self.__query) == 0:
            messagebox.showerror('No Results', 'No Results Found')
        return self.__query

    def searchBooks(self, title, author, publisher):
        '''Searches for books based on the search terms provided'''

        # query list stores the search results from the search terms
        self.__query = []

        # exit function if files are not loaded
        if not self.__books:
            messagebox.showerror('Error', 'Please Make sure you have loaded Books file')
            return

        # exit function if no search term is entered
        if not title and not author and not publisher:
            messagebox.showerror('Error', 'Please enter a search term')
            return

        # Conditional search based on the search terms
        # and appends the search results to the query list
        # individual if statements are used to allow for multiple search terms
        # and combinations of search terms' results.
        if title:
            for book in self.__books.values():
                if title in book.getTitle():
                    self.__query.append(book)
        if author:
            for book in self.__books.values():
                if author in book.getAuthor():
                    self.__query.append(book)
        if publisher:
            for book in self.__books.values():
                if publisher in book.getPublisher():
                    self.__query.append(book)
        if len(self.__query) == 0:
            messagebox.showerror('No Results', 'No Results Found')
        return self.__query

    def getRecommendations(self, type, title):
        '''Gets recommendations based on the type and title provided from the associations dictionary'''

        # recommendations list stores the recommendations based on the type and title
        # and association dictionary
        self.__recommendations = []

        # Checks if files are loaded
        if len(self.__books) == 0 or len(self.__shows) == 0:
            messagebox.showerror('Error', 'Please Make sure you have loaded Books and shows file')
            return

        # Checks if Associations file is loaded
        if len(self.__associations) == 0:
            messagebox.showerror('Error', 'Please Make sure you have loaded Associations file')
            return

        # Checks if title is entered and throws error if not
        if title != '':

            # Searches depending on the type and title
            if type == 'Book':
                for book in self.__books.values():
                    if title in book.getTitle():
                        for show in self.__associations[book.getID()]:
                            self.__recommendations.append(self.__shows[show])

            elif type == 'TV Show':
                for show in self.__TVShows.values():
                    if title in show.getTitle():
                        for book in self.__associations[show.getID()]:
                            self.__recommendations.append(self.__books[book])

            elif type == 'Movie':
                for show in self.__movies.values():
                    if title in show.getTitle():
                        for book in self.__associations[show.getID()]:
                            self.__recommendations.append(self.__books[book])
        elif title == '':
            messagebox.showerror('Error', 'Please enter a title')
            return
        if len(self.__recommendations) == 0:
            messagebox.showerror('No Recommendations', 'No Recommendations Found')
            return
        return self.__recommendations

    # Functions for bonus ratings tab
    def getBooks(self):
        return self.__books

    def getMovies(self):
        return self.__movies

    def getTVShows(self):
        return self.__TVShows