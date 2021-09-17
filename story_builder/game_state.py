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

    def add_location_to_map(self, location_type, connected_areas=None):
        """
        Instantiates location with connected areas, and returns
        the identifying number for that location.
        Connected areas may be modified later using modify_map_location
        """
        location_ID = len(self.__locations)+1
        
        # Instantiate Location Based on Type Provided
        self.__locations[location_ID] = location_type(location_ID, connected_areas)
        return location_ID

    def add_scene_to_map(self, scene):
        self.offset_location_IDs(scene)
        for _, location in scene.items():
            self.add_location_to_map(location[0], location[1])

    def offset_location_IDs(self, scene):
        offset = len(self.__locations) -1
        print("OFFSET:", offset)
        if offset <= 0:
            return
        for id, location in scene.items():
            for connected_area in location[1]:
                scene[id][1][connected_area] = offset + scene[id][1][connected_area]

    def modify_location_connections(self, location_ID, connected_areas):
        """ Overwrites connected_areas for the specified location """
        location = self.get_location(location_ID)
        location.connected_areas = connected_areas

    def get_location(self, location_ID):
        return self.__locations[location_ID]

    def set_active_location(self, location_ID):
        """ Encapsulating like this may not be neccessary """
        self.__active_location = location_ID
        return self.get_active_location()

    def get_active_location(self):
        return self.__locations[self.__active_location]

    def count_locations(self):
        return len(self.__locations)
