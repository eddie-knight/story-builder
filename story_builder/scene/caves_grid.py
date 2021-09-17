from story_builder.location import Location
from story_builder.races import *


class CaveTunnel(Location):
    hostile_options = [Wolf] # sprite guards?
    friendly_options = [Wood_Sprite_Guard] # sprite guards?

    def enter(self):
        print("You're in a narrow, dark, underground corridor. Fortunately your compass still works.")
        # splunk = input("Do you dare enter? > ")
        # if splunk == "yes":
        #     caves_grid()#I need help implementing this
        # elif "no":
        #     exit()
        # else:
        #     print("Come on! Really? This is a simple Yes or No question!")

class LargeCavern(Location):
    hostile_options = [Slime, LargeSlime] # sprite guards?
    friendly_options = [Wood_Sprite_Guard]

    def enter(self):
        self.spawn_hostiles(5)
        return """You are in a huge cavern, with one large hole in the roof far above.
        Sunlight blazes through, spotlighting enemies, hunched and ready to pounce.
        It looks like you have come upon them right before a kill, and dinner time!"""

    def look_around(self):
        return self.hostiles if self.hostiles else ""


"""
    1  2  3  4  5
    6  17 18    7
    8  20 21    9
    10       22 11
    12 13 14 15 16
"""
caves_grid = {
        1: [CaveTunnel, {
            "east": 2,
            "south": 6,
        }],
        2: [CaveTunnel, {
            "east": 3,
            "west": 1,
        }],
        3: [CaveTunnel, {
            "east": 4,
            "south": 18,
            "west": 2,
        }],
        4: [CaveTunnel, {
            "east": 5,
            "west": 3,
        }],
        5: [CaveTunnel, {
            "south": 7,
            "west": 4,
        }],
        6: [CaveTunnel, {
            "north": 1,
            "south": 8,
        }],
        7: [CaveTunnel, {
            "north": 5,
            "south": 9,
        }],
        8: [CaveTunnel, {
            "north": 6,
            "south": 10,
        }],
        9: [CaveTunnel, {
            "north": 7,
            "south": 11,
        }],
        10: [CaveTunnel, {
            "north": 8,
            "south": 12,
        }],
        11: [CaveTunnel, {
            "north": 9,
            "south": 16,
            "west": 22,
        }],
        12: [CaveTunnel, {
            "north": 10,
            "east": 13,
        }],
        13: [CaveTunnel, {
            "east": 14,
            "west": 12,
        }],
        14: [CaveTunnel, {
            "east": 15,
            "west": 13,
        }],
        15: [CaveTunnel, {
            "north": 22,
            "east": 16,
            "west": 14,
        }],
        16: [CaveTunnel, {
            "north": 11,
            "west": 15,
            "northwest": 22,
        }],
        17: [LargeCavern, {
            "southeast": 21,
        }],
        18: [LargeCavern, {
            "north": 3,
            "south": 21,
        }],
        20: [LargeCavern, {
            "east": 21,
            "west": 8,
        }],
        21: [LargeCavern, {
            "north": 18,
            "northwest": 17,
            "west": 20,
        }],
        22: [LargeCavern, {
            "northwest": 21,
            "southeast": 16,
        }],
    }
