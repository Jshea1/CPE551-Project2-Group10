from Media import Media

class Books(Media):
    def __init__(self, id: str, title: str,author: str, rating: float, isbn: float, isbn13: float,languageCode: str, numPages: float, numOfRatings: float, pubDate: str, publisher: str):
        self.__author = author
        self.__isbn = isbn
        self.__isbn13 = isbn13
        self.__numOfRatings = numOfRatings
        self.__pubDate = pubDate
        self.__publisher = publisher
        self.__languageCode = languageCode
        self.__numPages = numPages

        super().__init__(id, title, rating)
        
    def __str__(self):
        return f'''Title: {self.getTitle()}
Author: 
{self.getAuthor()}
Average Rating: 
{self.getRating()}
ISBN: 
{self.getIsbn()}
ISBN13: 
{self.getIsbn13()}
Language Code: 
{self.getLanguageCode()}
Pages: 
{self.getNumPages()}
Number of Ratings: 
{self.getNumOfRatings()}
Publication Date: 
{self.getPubDate()}
Publisher: 
{self.getPublisher()}

***********************************************************************

'''


    def getAuthor(self):
        return self.__author

    def setAuthor(self, newAuthor):
        self.__author = newAuthor

    def getIsbn(self):
        return self.__isbn

    def setIsbn(self, newIsbn):
        self.__isbn = newIsbn

    def getIsbn13(self):
        return self.__isbn13

    def setIsbn13(self, newIsbn13):
        self.__isbn13 = newIsbn13

    def getNumOfRatings(self):
        return self.__numOfRatings

    def setNumOfRatings(self, newNumOfRatings):
        self.__numOfRatings = newNumOfRatings

    def getPubDate(self):
        return self.__pubDate

    def setPubDate(self, newPubDate):
        self.__pubDate = newPubDate

    def getPublisher(self):
        return self.__publisher

    def setPublisher(self, newPublisher):
        self.__publisher = newPublisher

    def getLanguageCode(self):
        return self.__languageCode

    def setLanguageCode(self, newLanguageCode):
        self.__languageCode = newLanguageCode

    def getNumPages(self):
        return self.__numPages

    def setNumPages(self, newNumPages):
        self.__numPages = newNumPages
