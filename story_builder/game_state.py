import random
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

    def set_active_player(self, player) -> None:
        self.__active_player = player

    def get_active_player(self) -> Character:
        return self.__active_player

    def add_scene_to_map(self, scene_name, scene_initializer) -> None:
        scene = scene_initializer(scene_name)
        self.__scenes[scene_name] = {}
        for location in scene: # TODO
            self.__scenes[scene_name][location.id] = location

    def connect_locations(self, location1, location2) -> None:
        """
        Creates bilateral connection.
        Requires two locations as a tuple/list:
        (scene_name, location_id, exit_description)
        """
        first_scene, first_id, first_description = location1
        second_scene, second_id, second_description = location2

        first_path = self.get_location(first_scene, first_id)
        second_path = self.get_location(second_scene, second_id)
        first_path.exits[first_description] = (second_scene, second_id)
        second_path.exits[second_description] = (first_scene, first_id)

    def get_location(self, scene_name, location_ID) -> Location:
        location = self.__scenes[scene_name][location_ID]
        return location

    def get_random_location(self) -> tuple[str, int]:
        scene_name = random.choice(list(self.__scenes.keys()))
        location_id = self.get_random_id_from_scene(scene_name)
        return (scene_name, location_id)

    def get_random_id_from_scene(self, scene_name) -> int:
        return random.randint(2, self.count_locations(scene_name))

    def set_active_location(self, scene_name, location_ID) -> tuple[str, Location]:
        self.__active_location = (scene_name, location_ID)
        return self.get_active_location()

    def get_active_location(self) -> tuple[str, Location]:
        # TODO: separate this into scene and location
        scene_name, location_ID = self.__active_location
        return (scene_name, self.__scenes[scene_name][location_ID])

    def count_locations(self, scene_name) -> int:
        return len(self.__scenes[scene_name])

    def format_save(self) -> None:
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

        with open('save.json', 'w') as file:
            json.dump(data, file)
    
    def load_save(self) -> None:
        with open('save.json', 'r') as file:
            data = json.load(file) # TODO: This shouldn't be necessary...?
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
