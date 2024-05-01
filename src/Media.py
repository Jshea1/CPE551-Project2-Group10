# Author: Saurabh Parkar

class Media:
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
        
    # Accessor Functions
    
    def getID(self):
        return self.__id
    
    
    def getTitle(self):
        return self.__title
    
    def getRating(self):
        return self.__rating
    
    # set functions might not be needed since constructor 
    # uses parameters to set member variables
    def setID(self,ID):
        self.__id=ID
    
        
    def setTitle(self,title):
        self.__title=title
    
    def setRating(self, rating):
        self.__rating=rating
        

