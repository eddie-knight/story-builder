import json
from story_builder.load import load_character

from story_builder import get_class, Character
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

    def add_scene_to_map(self, scene_name, scene_initializer):
        scene = scene_initializer(scene_name)
        self.__scenes[scene_name] = {}
        for location in scene: # TODO
            self.__scenes[scene_name][location.id] = location

    def get_location(self, scene_name, location_ID):
        location = self.__scenes[scene_name][location_ID]
        assert isinstance(location, Location)
        return location

    def set_active_location(self, scene_name, location_ID):
        self.__active_location = (scene_name, location_ID)
        return self.get_active_location()

    def get_active_location(self):
        # TODO: separate this into scene and location
        scene_name, location_ID = self.__active_location
        return (scene_name, self.__scenes[scene_name][location_ID])

    def count_locations(self, scene_name):
        return len(self.__scenes[scene_name])

    def format_save(self):
        save = {
            "scenes": {},
            "player": self.get_active_player().save_data(),
            "active_scene": self.__active_location[0],
            "active_location_id": self.__active_location[1],
        }

        for scene, locations in self.__scenes.items():
            save["scenes"][scene] = []
            for _, location in locations.items():
                save["scenes"][scene].append(location.save_data())
        data = json.dumps(save, indent=2)
        print(data)

        with open('save.json', 'w') as file:
            json.dump(data, file)
    
    def load_save(self):
        with open('save.json', 'r') as file:
            data = json.load(file) # TODO: This shouldn't be necessary
            data = json.loads(data)
            player = load_character(Character, data["player"])
            self.set_active_player(player)
            self.__active_location = (data["active_scene"], data["active_location_id"])
            for scene in data["scenes"]:
                self.__scenes[scene] = {}
                for location_data in data["scenes"][scene]:
                    location_class = get_class(location_data["class"])
                    location = location_class(
                        scene_name=scene,
                        save_data=location_data)
                    self.__scenes[scene][location.id] = location
