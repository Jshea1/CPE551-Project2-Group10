# Author: Yash Patel

from Media import Media

class Show(Media):
    def __init__(self, id, showType, title,directors,cast, averageRating, countryCode, dateAdded, releaseYear, rating, duration, genres, description):
        super().__init__(id, title, averageRating)
        self.__showType = showType
        self.__directors = directors
        self.__cast = cast
        self.__countryCode = countryCode
        self.__dateAdded = dateAdded
        self.__releaseYear = releaseYear
        self.__rating = rating
        self.__duration = duration
        self.__genres = genres
        self.__description = description
    
    def __str__(self):
        return f'''Title: {self.getTitle()}
Show Type: {self.getShowType()}
Directors: {self.getDirectors()}
Cast: {self.getCast()}
Country Code: {self.getCountryCode()}
Date Added: {self.getDateAdded()}
Release Year: {self.getReleaseYear()}
Average Rating: {self.getRating()}
Duration: {self.getDuration()}
Genres: {self.getGenres()}
Description: {self.getDescription()}

***********************************************************************

'''

    def getShowType(self):
        return self.__showType

    def setShowType(self, newShowType):
        self.__showType = newShowType

    def getDirectors(self):
        return self.__directors

    def setDirectors(self, newDirectors):
        self.__directors = newDirectors

    def getCast(self):
        return self.__cast

    def setCast(self, newCast):
        self.__cast = newCast

    def getCountryCode(self):
        return self.__countryCode

    def setCountryCode(self, newCountryCode):
        self.__countryCode = newCountryCode

    def getDateAdded(self):
        return self.__dateAdded

    def setDateAdded(self, newDateAdded):
        self.__dateAdded = newDateAdded

    def getReleaseYear(self):
        return self.__releaseYear

    def setReleaseYear(self, newReleaseYear):
        self.__releaseYear = newReleaseYear

    def getRating(self):
        return self.__rating

    def setRating(self, newRating):
        self.__rating = newRating

    def getDuration(self):
        return self.__duration

    def setDuration(self, newDuration):
        self.__duration = newDuration

    def getGenres(self):
        return self.__genres

    def setGenres(self, newGenres):
        self.__genres = newGenres

    def getDescription(self):
        return self.__description

    def setDescription(self, newDescription):
        self.__description = newDescription
