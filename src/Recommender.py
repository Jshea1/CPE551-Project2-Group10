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
            file = filedialog.askopenfilename(initialdir=os.getcwd(), title='Load Books information file', filetypes=[("CSV files", "*.csv")])
            if file:
                if os.path.exists(file):
                    with open(file) as bookfile:  
                        next(bookfile)                  
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
            file = filedialog.askopenfilename(initialdir=os.getcwd(), title='Load Shows information file', filetypes=[("CSV files", "*.csv")])
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
        #pass

    def loadAssociations(self):
        # Implement loading associations from file
        # creating new member variable dicts to store associations
        while True:
            # Opens associated file and stores association in a dict in {id:[list]} format
            # with id(key) being showid or bookid as per the requirement and 
            # list(values) being associated books/shows
            file = filedialog.askopenfilename(initialdir=os.getcwd(), title='Loads Associations File',filetypes=[("CSV files", "*.csv")])
            if file:
                if os.path.exists(file):
                    with open(file) as associationfile:
                        for line in associationfile:
                            _line = line.strip().split(',')
                            # Show -> Books association
                            if _line[0] not in self.__associations:
                                self.__associations[_line[0]] = {_line[1]:1}
                            else:
                                if _line[1] not in self.__associations[_line[0]]:
                                    self.__associations[_line[0]][_line[1]] = 1
                                else:
                                    self.__associations[_line[0]][_line[1]] += 1
                            
                            # Book -> Shows association
                            if _line[1] not in self.__associations:
                                self.__associations[_line[1]] = {_line[0]:1}
                            else:
                                if _line[0] not in self.__associations[_line[1]]:
                                    self.__associations[_line[1]][_line[0]] = 1
                                else:
                                    self.__associations[_line[1]][_line[0]] += 1

                    break
            else:
                messagebox.showerror('Error','No File Selected')
                            
                                

    def getMovieList(self):
        self.movies = {}
        #filtering only movies
        for id, info in self.__shows.items():
            if info.getShowType() == 'Movie':  
                self.movies[id] = info


        # max len for formatting
        maxTitleLength = 0
        for movie in self.movies.values():
            if len(movie.getTitle()) > maxTitleLength:
                maxTitleLength = len(movie.getTitle())

            # Build the output as a list of strings
        output = []
        header = f"{'Title':<{maxTitleLength}} | Duration"
        output.append(header)

        # Adding each movie's information formatted
        for movie in self.movies.values():
            title = movie.getTitle()
            duration = movie.getDuration()
            line = f"{title:<{maxTitleLength}} | {duration}"
            output.append(line)

        return "\n".join(output)

    def getTVList(self):
        # filtering only shows
        self.TVShows = {}
        for id, info in self.__shows.items():
            if info.getShowType() == 'TV Show':
                self.TVShows[id] = info

        # max len for formatt
        maxTitleLength = 0
        for show in self.TVShows.values():
            titlelength = len(show.getTitle())
            if titlelength > maxTitleLength:
                maxTitleLength = titlelength

            # Build the output as a list of strings
        output = []
        header = f"{'Title':<{maxTitleLength}} | Duration"
        output.append(header)

        # Adding each TV show's information formatted
        for show in self.TVShows.values():
            title = show.getTitle()
            seasons = show.getDuration()
            line = f"{title:<{maxTitleLength}} | {seasons}"
            output.append(line)

        return "\n".join(output)


    def getBookList(self):
        # max len for formatting
        maxTitleLength = 0
        for book in self.__books.values():
            titleLength = len(book.getTitle())
            if titleLength > maxTitleLength:
                maxTitleLength = titleLength

        output = []
        header = f"{'Title':<{maxTitleLength}} | Author"
        output.append(header)

        # Format each book's information
        for book in self.__books.values():
            title = book.getTitle()
            author = book.getAuthor()
            line = f"{title:<{maxTitleLength}} | {author}"
            output.append(line)

        return "\n".join(output)


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

        totalMovies = len(movies)
        ratingPercentages = {r: f"{(count / totalMovies * 100):.2f}%" for r, count in ratings.items()}
        ratingOutput = "\n".join(f"{rating}: {percentage}" for rating, percentage in ratingPercentages.items())
        averageDuration = f"{totalDuration / totalMovies:.2f}"
        mostCommonDirector = max(directors, key=directors.get)
        mostCommonActor = max(actors, key=actors.get)
        mostCommonGenre = max(genres, key=genres.get)

        # return
        return (f"Rating Percentages:\n"
                f"{ratingOutput}\n"
                f"Average Movie Duration: {averageDuration} minutes\n"
                f"Most Common Director: {mostCommonDirector}\n"
                f"Most Common Actor: {mostCommonActor}\n"
                f"Most Common Genre: {mostCommonGenre}")




    def getTVStats(self):
        # Filter TV shows from the list
        tv_shows = {}
        for id, info in self.__shows.items():
            if info.getShowType() == 'TV Show':
                tv_shows[id] = info

        ratings = {}
        totalSeasons = 0
        cast = {}
        genres = {}

        for show in tv_shows.values():
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
        totalTVShows = len(tv_shows)
        ratingPercentages = {r: f"{(count / totalTVShows * 100):.2f}%" for r, count in ratings.items()}
        ratingOutput = "\n".join(f"{rating}: {percentage}" for rating, percentage in ratingPercentages.items())
        averageSeasons = f"{totalSeasons / totalTVShows:.2f}"
        mostCommonActor = max(cast, key=cast.get)
        mostCommonGenre = max(genres, key=genres.get)


        #returning
        return (f"Rating Percentages:\n"
                f"{ratingOutput}\n"
                f"Average Number of Seasons: {averageSeasons}\n"
                f"Most Common Actor: {mostCommonActor}\n"
                f"Most Common Genre: {mostCommonGenre}")





    def getBookStats(self):

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
                        publishers[publisher] +=1
                    else:
                        publishers[publisher]=1

        # stat calc
        totalBooks = len(self.__books)
        averagePageCount = f"{totalPageCount / totalBooks:.2f}" 
        mostCommonAuthor = max(authors, key=authors.get)
        mostCommonPublisher = max(publishers, key=publishers.get)

        # returning
        return (f"Average Page Count: {averagePageCount}\n"
                f"Author with Most Books: {mostCommonAuthor}\n"
                f"Publisher with Most Books: {mostCommonPublisher}")


    def searchTVMovies(self, title, director, cast, genre):
        # Implement searching for TV shows and movies
        self.__query= []
        if title=='' and director=='' and cast=='' and genre=='':
            messagebox.showerror('Error', 'Please enter a search term')
            return
        elif title:
            for show in self.__shows.values():
                if title in show.getTitle():
                    self.__query.append(show)
        elif director:
            for show in self.__shows.values():
                if director in show.getDirectors():
                    self.__query.append(show)
        elif cast:
            for show in self.__shows.values():
                if cast in show.getCast():
                    self.__query.append(show)
        elif genre:
            for show in self.__shows.values():
                if genre in show.getGenres():
                    self.__query.append(show)
        
        if len(self.__query) == 0:
            messagebox.showerror('No Results', 'No Results Found')
        print(self.__query)
        return self.__query
        
        

    def searchBooks(self, title, author, publisher):
        # Implement searching for books

        self.__query = []
        if not title and not author and not publisher:
            messagebox.showerror('Error', 'Please enter a search term')
            return
        elif title:
            for book in self.__books.values():
                if title in book.getTitle():
                    self.__query.append(book)
        elif author:
            for book in self.__books.values():
                if author in book.getAuthor():
                    self.__query.append(book)
        elif publisher:
            for book in self.__books.values():
                if publisher in book.getPublisher():
                    self.__query.append(book)
        if len(self.__query) == 0:
            messagebox.showerror('No Results', 'No Results Found')
        return self.__query

    def getRecommendations(self, type, title):
        # Implement getting recommendations
        self.__recommendations = []
        if type == 'Book':
            for book in self.__books.values():
                if title in book.getTitle():
                    for show in self.__associations[book.getID()]:
                        self.__recommendations.append(self.__shows[show])
        elif type == 'TV Show' or type == 'Movie':
            for show in self.__shows.values():
                if title in show.getTitle():
                    for book in self.__associations[show.getID()]:
                        self.__recommendations.append(self.__books[book])
        if len(self.__recommendations) == 0:
            messagebox.showerror('No Recommendations', 'No Recommendations Found')
            return
        return self.__recommendations
