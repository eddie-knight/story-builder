from story_builder import scene
from .location import Location

class GameState:
    """
    GameState should only be created once and used for the entire runtime
    """
    __scenes = {}
    __active_player = None
    __active_location = None

    def __init__(self):
        pass

    def set_active_player(self, player):
        self.__active_player = player

    def get_active_player(self):
        return self.__active_player

    def add_scene_to_map(self, scene_name, scene):
        self.__scenes[scene_name] = {}
        for id, location in scene.items():
            initialized_location = location["class"](
                scene_name, id, location["connections"])
            self.__scenes[scene_name][id] = initialized_location

    def get_location(self, scene_name, location_ID):
        location = self.__scenes[scene_name][location_ID]
        assert isinstance(location, Location)
        return location

    def set_active_location(self, scene_name, location_ID):
        self.__active_location = (scene_name, location_ID)
        return self.get_active_location()

    def get_active_location(self):
        scene_name, location_ID = self.__active_location
        return self.__scenes[scene_name][location_ID]

    def count_locations(self, scene_name):
        return len(self.__scenes[scene_name])
