# Author: Saurabh Parkar

from Media import Media

class Books(Media):
    def __init__(self, id: str, title: str, rating: float, author: str, isbn: float,isbn13: float, numOfRatings: float, pubDate: str, publisher: str):
        self.__author = author
        self.__isbn = isbn
        self.__isbn13 = isbn13
        self.__numOfRatings = numOfRatings
        self.__pubDate = pubDate
        self.__publisher = publisher

        super().__init__(id,title,rating)
    
    def author(self):
        return self.__author

    def author(self, value):
        self.__author = value

    def isbn(self):
        return self.__isbn

    def isbn(self, value):
        self.__isbn = value

    def isbn13(self):
        return self.__isbn13

    def isbn13(self, value):
        self.__isbn13 = value

    def numOfRatings(self):
        return self.__numOfRatings

    def numOfRatings(self, value):
        self.__numOfRatings = value

    def pubDate(self):
        return self.__pubDate

    def pubDate(self, value):
        self.__pubDate = value

    def publisher(self):
        return self.__publisher
    
    def publisher(self, value):
        self.__publisher = value