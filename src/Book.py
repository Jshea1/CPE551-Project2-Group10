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

    def author(self, newAuthor):
        self.__author = newAuthor

    def isbn(self):
        return self.__isbn

    def isbn(self, newIsbn):
        self.__isbn = newIsbn

    def isbn13(self):
        return self.__isbn13

    def isbn13(self, newIsbn13):
        self.__isbn13 = newIsbn13

    def numOfRatings(self):
        return self.__numOfRatings

    def numOfRatings(self, newNumOfRatings):
        self.__numOfRatings = newNumOfRatings

    def pubDate(self):
        return self.__pubDate

    def pubDate(self, newPubDate):
        self.__pubDate = newPubDate

    def publisher(self):
        return self.__publisher
    
    def publisher(self, newPublisher):
        self.__publisher = newPublisher