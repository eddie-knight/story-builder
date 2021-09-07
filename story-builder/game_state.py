class GameState:
    """
    GameState should only be created once and used for the entire runtime
    """
    __locations__ = {}

    def __init__(self):
        pass
    
    def add_location_to_map(self, locationType, connected_areas):
        """ 
        Instantiates location with connected areas, and returns
        the identifying number for that location.
        Connected areas may be modified later using modify_map_location
        """
        locationID = str(len(self.__locations__)+1)
        print((locationID, connected_areas))
        self.__locations__[locationID] = locationType(locationID, connected_areas)
        return locationID

    def modify_map_location(self, locationID, connected_areas):
        """ Overwrites connected_areas for the specified location """
        self.__locations__[locationID].connected_areas = connected_areas


    def get_location(self, locationID):
        return self.__locations__[str(locationID)]