# Authors: Saurabh Raman Parkar, Yash Patel, John Shea
# Date: 5-4-2024
# Description: Containing media information and attributes
# I pledge my honor that I have abided by the Stevens Honor System

class Media:
    '''Super Class for Books, Shows class stores common attributes of both Books and Shows'''

    def __init__(self, id: str, title: str, rating: float):
        '''
        Paramters
        ---------

        id: str
            stores id of movie/show
        type: str
            type of media Movie/ TV Show
        title: str
            title of media
        rating: float
        '''
        self.__id = id
        self.__title = title
        self.__rating = rating

    # Getters and Setters for Media class
    def getID(self):
        return self.__id

    def getTitle(self):
        return self.__title

    def getRating(self):
        return self.__rating

    def setID(self, ID):
        self.__id = ID

    def setTitle(self, title):
        self.__title = title

    def setRating(self, rating):
        self.__rating = rating

