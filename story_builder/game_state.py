import json
import importlib

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
        scene_name, location_ID = self.__active_location
        return (scene_name, self.__scenes[scene_name][location_ID])

    def count_locations(self, scene_name):
        return len(self.__scenes[scene_name])

    def format_save(self):
        save = {}
        for scene, locations in self.__scenes.items():
            save[scene] = []
            for _, location in locations.items():
                save[scene].append(location.save_data())
        data = json.dumps(save) 
        print(data)

        with open('save.json', 'w') as file:
            json.dump(data, file)
    
    def load_save(self):
        with open('save.json', 'r') as file:
            data = json.load(file) # TODO: This shouldn't be necessary
            data = json.loads(data)
            for scene in data:
                self.__scenes[scene] = {}
                for location_data in data[scene]:
                    location_class = self.get_class(location_data["class"])
                    location = location_class(
                        scene_name=scene,
                        save_data=location_data)
                    self.__scenes[scene][location.id] = location

    def get_class(self, class_unformatted):
        preformat = class_unformatted.split("'")[1].split(".")
        module_name = ".".join(preformat[0:-1])
        class_name = preformat[3]
        module = importlib.import_module(module_name)
        return getattr(module, class_name)

