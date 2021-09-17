
from story_builder.location import Location
from story_builder.characters import *
#Teleport home (exit) Teleport Next, next location in the list, (Caves)
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



""" 
Rough dict to create a 5x5 square forest 
I'm hoping that doing this inefficiently will help
get ideas to make a better version later
    1  2  3  4  5
    6  17 18 19 7
    8  20 21 22 9          21 -> C1
    10 23 24 25 11               C2  C3
    12 13 14 15 16               C5  C6
"""
forest_grid = {
        1: [ForestEdge, {
            "east": 2,
            "south": 6,
            "southeast": 17,
        }],
        2: [ForestEdge, {
            "east": 3,
            "south": 17,
            "west": 1,
        }],
        3: [ForestEdge, {
            "east": 4,
            "south": 18,
            "west": 2,
        }],
        4: [ForestEdge, {
            "east": 5,
            "south": 19,
            "west": 3,
        }],
        5: [ForestEdge, {
            "south": 7,
            "west": 4,
        }],
        6: [ForestEdge, {
            "north": 1,
            "east": 17,
            "south": 8,
        }],
        7: [ForestEdge, {
            "north": 5,
            "south": 9,
            "west": 19,
        }],
        8: [ForestEdge, {
            "north": 6,
            "east": 20,
            "south": 10,
        }],
        9: [ForestEdge, {
            "north": 7,
            "south": 11,
            "west": 22,
        }],
        10: [ForestEdge, {
            "north": 8,
            "east": 23,
            "south": 12,
        }],
        11: [ForestEdge, {
            "north": 9,
            "south": 16,
            "west": 25,
        }],
        12: [ForestEdge, {
            "north": 10,
            "east": 13,
        }],
        13: [ForestEdge, {
            "north": 23,
            "east": 14,
            "west": 12,
        }],
        14: [ForestEdge, {
            "north": 24,
            "east": 15,
            "west": 13,
        }],
        15: [ForestEdge, {
            "north": 25,
            "east": 16,
            "west": 14,
        }],
        16: [ForestEdge, {
            "north": 11,
            "west": 15,
        }],
        17: [ForestInterior, {
            "north": 2,
            "east": 18,
            "south": 20,
            "west": 6,
        }],
        18: [ForestInterior, {
            "north": 3,
            "east": 19,
            "south": 21,
            "west": 17,
        }],
        19: [ForestInterior, {
            "north": 4,
            "east": 7,
            "south": 22,
            "west": 18,
        }],
        20: [ForestInterior, {
            "north": 17,
            "east": 21,
            "south": 23,
            "west": 8,
        }],
        21: [ForestInterior, {
            "north": 18,
            "east": 22,
            "south": 24,
            "west": 20,
        }],
        22: [ForestInterior, {
            "north": 19,
            "east": 9,
            "south": 25,
            "west": 21,
        }],
        23: [ForestInterior, {
            "north": 20,
            "east": 24,
            "south": 13,
            "west": 10,
        }],
        24: [ForestInterior, {
            "north": 21,
            "east": 25,
            "south": 14,
            "west": 23,
        }],
        25: [ForestInterior, {
            "north": 22,
            "east": 11,
            "south": 15,
            "west": 24,
        }],
    }
