from abc import ABC, abstractmethod
from random import randrange

from .characters import *


class Location(ABC):

    # Options should be a list of uninstantiated NPC classes.
    # These will be drawn from to populate the area.
    # To adjust the frequency of a NPC type, classes may be
    # added to the options list multiple times.
    # Example: for a 3/1 chance to spawn wolves above orcs, 
    # use [Wolf, Wolf, Wolf, Orc]
    hostile_options = []
    friendly_options = []

    # Hostiles and Friendlies may be spawned at random
    # using the options list, or manually by pre-filling
    # during initialization. These should be lists of
    # instantiated NPC class objects.
    hostiles = [] 
    friendlies = []

    def __init__(self, id, connected_areas=None):
        if connected_areas:
            for areaID in connected_areas.values():
                if type(areaID) is not int:
                    raise TypeError(
                        "Expected connected area value type to be int, but " \
                        f"connected areas for location {id} contained value {type(areaID)}")
        self.id = id
        self.connected_areas = connected_areas

    @abstractmethod
    def enter(self):
        """ Message for when the player enters an area """
        pass

    def spawn_hostiles(self, count):
        while len(self.hostiles) < count:
            self.hostiles.append(
                NPC(race=self.hostile_options[
                        randrange(0, len(self.hostile_options))
                    ])
            )
        return self.hostiles

    def spawn_friendlies(self, count):
        while len(self.friendlies) < count:
            self.friendlies.append(
                NPC(race=self.friendly_options[
                        randrange(0, len(self.friendly_options))
                    ])
            )
        return self.friendlies

    def count_hostiles(self):
        counter = {}
        for hostile in self.hostiles:
            if str(hostile) not in counter.keys():
                counter[str(hostile)] = 1
            else:
                counter[str(hostile)] += 1
        return counter

    def count_friendlies(self):
        counter = {}
        for friendly in self.friendlies:
            if str(friendly) not in counter.keys():
                counter[str(friendly)] = 1
            else:
                counter[str(friendly)] += 1
        return counter

    def show_exits(self):
        # TODO: Make this return a descriptive text
        return self.connected_areas

    def take_exit(self, exitName):
        # TODO: Check exit exists?
        return self.connected_areas[exitName]

    def add_connection(self, name, location):
        self.connected_areas[name] = location
