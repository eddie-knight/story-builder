class GameState:
    """
    GameState should only be created once and used for the entire runtime
    """
    __locations = {}
    __active_player = None
    __active_location = None

    def __init__(self):
        pass

    def set_active_player(self, player):
        """ Encapsulating like this may not be neccessary """
        self.__active_player = player
    
    def get_active_player(self, player):
        """ Encapsulating like this may not be neccessary """
        return self.__active_player

    def add_location_to_map(self, locationType, connected_areas=None):
        """ 
        Instantiates location with connected areas, and returns
        the identifying number for that location.
        Connected areas may be modified later using modify_map_location
        """
        locationID = len(self.__locations)+1
        
        # Instantiate Location Based on Type Provided
        self.__locations[locationID] = locationType(locationID, connected_areas)
        return locationID

    def modify_location_connections(self, locationID, connected_areas):
        """ Overwrites connected_areas for the specified location """
        location = self.get_location(locationID)
        location.connected_areas = connected_areas

    def get_location(self, locationID):
        return self.__locations[locationID]

    def set_active_location(self, locationID):
        """ Encapsulating like this may not be neccessary """
        self.__active_location = locationID
        return self.get_active_location()

    def get_active_location(self):
        return self.__locations[self.__active_location]

    def count_locations(self):
        return len(self.__locations)