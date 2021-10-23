from abc import ABC, abstractmethod
from random import randrange

from story_builder import load_character

from .characters import *


class Location(ABC):

    # Options should be a list of uninstantiated NPC classes.
    # These will be drawn from to populate the area.
    # To adjust the frequency of a NPC type, classes may be
    # added to the options list multiple times.
    # Example: for a 3/1 chance to spawn wolves above orcs, 
    # use [Wolf, Wolf, Wolf, Orc]
    # Note: Overwriting this at runtime will overwrite it for
    # all instances of the same class.
    hostile_options = list[NPC]
    friendly_options = list[NPC]

    def __init__(self, scene_name, id=None, exits={}, save_data=None) -> None:
        """
        Exits specified during initialization may optionally
        use an int, omitting the tuple (scene_name, location_id)
        if the location is part of this scene
        That value will be automatically filled in using scene_name

        Hostiles and Friendlies may be spawned at random
        using the options list, or manually by filling
        after initialization. These should be lists of
        instantiated NPC class objects
        """
        self.NPCs = list[NPC]()
        self._scene_name = str(scene_name)
        self.id = None if id is None else int(id)

        self.exits = self._revise_exits(exits)

        if save_data:
            self.load_data(save_data)

    @abstractmethod
    def enter(self) -> str:
        """ Message for when the player enters an area """
        pass

    def save_data(self) -> None:
        return {
            "id": self.id,
            "class": str(self.__class__),
            "exits": self.exits,
            "NPCs": self.get_character_saves(self.NPCs),
        }

    def load_data(self, save_data) -> None:
        self.id = save_data["id"]
        for exit, data in save_data["exits"].items():
            if type(data) is list:
                self.exits[exit] = tuple(data)
            if type(data) is int:
                self.exits[exit] = (self._scene_name, data)
        for data in save_data["NPCs"]:
            character = load_character(NPC, data)
            self.NPCs.append(character)


    def get_character_saves(self, characters) -> list[NPC]:
        data = []
        for character in characters:
            data.append(character.save_data())
        return data

    def _revise_exits(self, exits) -> dict[str, tuple[str, int]]:
        revised_exits = {}
        for exit_name, exit_target in exits.items():
            if type(exit_target) is tuple:
                revised_exits[exit_name] = exit_target
            elif type(exit_target) is int:
                revised_exits[exit_name] = (self._scene_name, exit_target)
            else:
                raise TypeError("Location parameter 'exits' must contain either tuples or integers")
        return revised_exits

    def spawn_hostiles(self, count) -> list[NPC]:
        """ Spawn a specified number of random hostiles """
        if len(self.hostile_options) == 0:
            return []
        race = randrange(0, len(self.hostile_options), 1)
        return self.spawn_hostiles_by_race(count, race)

    def spawn_hostiles_by_race(self, count, race) -> list[NPC]:
        """ Spawn a set number of hostiles of a specific race """
        for _ in range(0, count):
            self.spawn_hostile_by_race(race)
        return self.NPCs

    def spawn_hostile_by_race(self, race) -> NPC:
        """ Spawn one hostile of a specific race """
        newNPC = NPC(
            personality=Hostile,
            race=race,
        )
        self.NPCs.append(newNPC)

    def spawn_friendlies(self, count) -> list[NPC]:
        """ Spawn a specified number of random friendlies """
        if len(self.friendly_options) == 0:
            return []
        race = randrange(0, len(self.friendly_options), 1)
        return self.spawn_friendlies_by_race(count, race)

    def spawn_friendlies_by_race(self, count, race) -> list[NPC]:
        """ Spawn a set number of friendlies of a specific race """
        for _ in range(0, count):
            self.spawn_friendly_by_race(race)
        return self.NPCs

    def spawn_friendly_by_race(self, race) -> None:
        """ Spawn one friendly of a specific race """
        newNPC = NPC(
            personality=Friendly,
            race=race,
        )
        self.NPCs.append(newNPC)

    def get_hostiles(self) -> list[NPC]:
        """ Returns a list of hostile NPCs in this location """
        hostiles = []
        for character in self.NPCs:
            if character.personality is Hostile:
                hostiles.append(character)
        return hostiles

    def get_friendlies(self) -> list[NPC]:
        """ Returns a list of friendly NPCs in this location """
        friendlies = []
        for character in self.NPCs:
            if character.personality is Hostile:
                friendlies.append(character)
        return friendlies

    def count_hostile_types(self) -> int:
        counter = {}
        for character in self.NPCs:
            if character.personality is Hostile:
                if str(character) not in counter.keys():
                    counter[str(character)] = 1
                else:
                    counter[str(character)] += 1
        return counter

    def count_friendly_types(self) -> int:
        counter = {}
        for character in self.NPCs:
            if str(character) not in counter.keys():
                counter[str(character)] = 1
            else:
                counter[str(character)] += 1
        return counter

    def show_exits(self):
        # TODO: Make this return a descriptive text
        return self.exits

    def take_exit(self, exitName) -> tuple[str, int]:
        """ Returns the scene name and location id for the specified exit """
        # TODO: Check exit exists?
        return self.exits[exitName]

    def add_connection(self, name, location) -> None:
        self.exits[name] = location
