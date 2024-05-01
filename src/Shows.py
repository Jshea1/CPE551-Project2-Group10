# Author: Yash Patel

from Media import Media

class Show(Media):
    def __init__(self, id, title, averageRating, showType, directors, actors, countryCode, dateAdded, releaseYear, rating, duration, genres, description):
        super().__init__(id, title, averageRating)
        self.showType = showType
        self.directors = directors
        self.actors = actors
        self.countryCode = countryCode
        self.dateAdded = dateAdded
        self.releaseYear = releaseYear
        self.rating = rating
        self.duration = duration
        self.genres = genres
        self.description = description

    def showType(self):
        return self.__showType

    def showType(self, newShowType):
        self.__showType = newShowType

    def directors(self):
        return self.__directors

    def directors(self, newDirectors):
        self.__directors = newDirectors

    def actors(self):
        return self.__actors

    def actors(self, newActors):
        self.__actors = newActors

    def countryCode(self):
        return self.__countryCode

    def countryCode(self, newCountryCode):
        self.__countryCode = newCountryCode

    def dateAdded(self):
        return self.__dateAdded

    def dateAdded(self, newDateAdded):
        self.__dateAdded = newDateAdded

    def releaseYear(self):
        return self.__releaseYear

    def releaseYear(self, newReleaseYear):
        self.__releaseYear = newReleaseYear

    def rating(self):
        return self.__rating

    def rating(self, newRating):
        self.__rating = newRating

    def duration(self):
        return self.__duration

    def duration(self, newDuration):
        self.__duration = newDuration

    def genres(self):
        return self.__genres

    def genres(self, newGenres):
        self.__genres = newGenres

    def description(self):
        return self.__description

    def description(self, newDescription):
        self.__description = newDescription