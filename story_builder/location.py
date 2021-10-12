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
    hostile_options = []
    friendly_options = []

    def __init__(self, scene_name=str, id=int, exits={}, save_data=None):
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
        self.NPCs = []
        self._scene_name = scene_name
        self.id = id
        self.exits = self._revise_exits(exits)

        if save_data:
            self.load_data(save_data)

    @abstractmethod
    def enter(self):
        """ Message for when the player enters an area """
        pass

    def save_data(self):
        return {
            "id": self.id,
            "class": str(self.__class__),
            "exits": self.exits,
            "NPCs": self.get_character_saves(self.NPCs),
        }

    def load_data(self, save_data):
        self.id = save_data["id"]
        for exit, data in save_data["exits"].items():
            if type(data) is list:
                self.exits[exit] = tuple(data)
            if type(data) is int:
                self.exits[exit] = (self._scene_name, data)
        for data in save_data["hostiles"]:
            character = load_character(NPC, data)
            self.hostiles.append(character)


    def get_character_saves(self, characters):
        data = []
        for character in characters:
            data.append(character.save_data())
        return data

    def _revise_exits(self, exits):
        revised_exits = {}
        for exit_name, exit_target in exits.items():
            if type(exit_target) is tuple:
                revised_exits[exit_name] = exit_target
            elif type(exit_target) is int:
                revised_exits[exit_name] = (self._scene_name, exit_target)
            else:
                raise TypeError("Location parameter 'exits' must contain either tuples or integers")
        return revised_exits

    def spawn_hostiles(self, count):
        if len(self.hostile_options) == 0:
            return []

        for _ in range(0, count):
            newNPC = NPC(
                personality=Hostile,
                race=self.hostile_options[randrange(0, len(self.hostile_options), 1)],
            )
            self.NPCs.append(newNPC)
        return self.NPCs

    def spawn_friendlies(self, count):
        if len(self.friendly_options) == 0:
            return []

        for _ in range(0, count):
            newNPC = NPC(
                personality=Friendly,
                race=self.friendly_options[randrange(0, len(self.friendly_options), 1)],
            )
            self.NPCs.append(newNPC)
        return self.NPCs

    def get_hostiles(self):
        """ Returns a list of hostile NPCs in this location """
        hostiles = []
        for character in self.NPCs:
            if character.personality is Hostile:
                hostiles.append(character)
        return hostiles

    def get_friendlies(self):
        """ Returns a list of friendly NPCs in this location """
        friendlies = []
        for character in self.NPCs:
            if character.personality is Hostile:
                friendlies.append(character)
        return friendlies

    def count_hostile_types(self):
        counter = {}
        for character in self.NPCs:
            if character.personality is Hostile:
                if str(character) not in counter.keys():
                    counter[str(character)] = 1
                else:
                    counter[str(character)] += 1
        return counter

    def count_friendly_types(self):
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

    def take_exit(self, exitName):
        # TODO: Check exit exists?
        return self.exits[exitName]

    def add_connection(self, name, location):
        self.exits[name] = location
