
from .location import Location
from .characters import *

class CaveEntrance(Location):
    hostile_options = [Wolf]
    def enter(self):
        return "You're at the entrance to a cave"

class ForestEdge(Location):
    hostile_options = [Wood_Sprite_Guard] # sprite guards?
    friendly_options = [Wolf] # sprite guards?

    def enter(self):
        return "You find yourself at the edge of a forest"

class ForestInterior(Location):
    hostile_options = [Wood_Sprite_Guard, Wood_Sprite] # sprite guards?
    friendly_options = [Wolf]

    def enter(self):
        self.spawn_friendlies(1)
        return "You find yourself in a forest"

    def look_around(self):
        return f"You see a friendly {self.friendlies[0]}"


def create_forest(state):
    """ 
    Rough function to create a 5x5 square forest 
    I'm hoping that doing this inefficiently will help
    get ideas to make a better version later
        1  2  3  4  5
        6  17 18 19 7
        8  20 21 22 9          21 -> C1
        10 23 24 25 11               C2  C3
        12 13 14 15 16               C5  C6
    """

    count = 0
    while count < 16:
        state.add_location_to_map(ForestEdge)
        count += 1

    count = 0
    while count < 9:
        state.add_location_to_map(ForestInterior)
        count += 1


    state.modify_location_connections(
        1, # current area
        connected_areas={
            "east": 2,
            "south": 6,
            # "southeast": 17,
        }
    )
    state.modify_location_connections(
        2, # current area
        connected_areas={
            "east": 3,
            "south": 17,
            "west": 1,
        }
    )
    state.modify_location_connections(
        3, # current area
        connected_areas={
            "east": 4,
            "south": 18,
            "west": 2,
        }
    )
    state.modify_location_connections(
        4, # current area
        connected_areas={
            "east": 5,
            "south": 19,
            "west": 3,
        }
    )
    state.modify_location_connections(
        5, # current area
        connected_areas={
            "south": 7,
            "west": 4,
        }
    )
    state.modify_location_connections(
        6, # current area
        connected_areas={
            "north": 1,
            "east": 17,
            "south": 8,
        }
    )
    state.modify_location_connections(
        17, # current area
        connected_areas={
            "north": 2,
            "east": 18,
            "south": 20,
            "west": 6,
        }
    )
    state.modify_location_connections(
        18, # current area
        connected_areas={
            "north": 3,
            "east": 19,
            "south": 21,
            "west": 17,
        }
    )
    state.modify_location_connections(
        19, # current area
        connected_areas={
            "north": 4,
            "east": 7,
            "south": 22,
            "west": 18,
        }
    )
    state.modify_location_connections(
        7, # current area
        connected_areas={
            "north": 5,
            "south": 9,
            "west": 19,
        }
    )
    state.modify_location_connections(
        8, # current area
        connected_areas={
            "north": 6,
            "east": 20,
            "south": 10,
        }
    )
    state.modify_location_connections(
        20, # current area
        connected_areas={
            "north": 17,
            "east": 21,
            "south": 23,
            "west": 8,
        }
    )
    state.modify_location_connections(
        21, # current area
        connected_areas={
            "north": 18,
            "east": 22,
            "south": 24,
            "west": 20,
        }
    )
    state.modify_location_connections(
        22, # current area
        connected_areas={
            "north": 19,
            "east": 9,
            "south": 25,
            "west": 21,
        }
    )
    state.modify_location_connections(
        9, # current area
        connected_areas={
            "north": 7,
            "south": 11,
            "west": 22,
        }
    )
    state.modify_location_connections(
        10, # current area
        connected_areas={
            "north": 8,
            "east": 23,
            "south": 12,
        }
    )
    state.modify_location_connections(
        23, # current area
        connected_areas={
            "north": 20,
            "east": 24,
            "south": 13,
            "west": 10,
        }
    )
    state.modify_location_connections(
        24, # current area
        connected_areas={
            "north": 21,
            "east": 25,
            "south": 14,
            "west": 23,
        }
    )
    state.modify_location_connections(
        25, # current area
        connected_areas={
            "north": 22,
            "east": 11,
            "south": 15,
            "west": 24,
        }
    )
    state.modify_location_connections(
        11, # current area
        connected_areas={
            "north": 9,
            "south": 16,
            "west": 25,
        }
    )
    state.modify_location_connections(
        12, # current area
        connected_areas={
            "north": 10,
            "east": 13,
        }
    )
    state.modify_location_connections(
        13, # current area
        connected_areas={
            "north": 23,
            "east": 14,
            "west": 12,
        }
    )
    state.modify_location_connections(
        14, # current area
        connected_areas={
            "north": 24,
            "east": 15,
            "west": 13,
        }
    )
    state.modify_location_connections(
        15, # current area
        connected_areas={
            "north": 25,
            "east": 16,
            "west": 14,
        }
    )
    state.modify_location_connections(
        16, # current area
        connected_areas={
            "north": 11,
            "west": 15,
        }
    )

