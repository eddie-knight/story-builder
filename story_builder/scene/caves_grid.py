from story_builder.location import Location
from story_builder.characters import *
from scene import *

class CaveTunnel(Location):
    hostile_options = [Wolf] # sprite guards?
    friendly_options = [Wood_Sprite_Guard] # sprite guards?

    def enter(self):
        print("You're at the entrance to a cave.")
        splunk = input("Do you dare enter? > ")
        if splunk == "yes":
            caves_grid()#I need help implementing this
        elif "no":
            exit()
        else:
            print("Come on! Really? This is a simple Yes or No question!")
class LargeCavern(Location):
    hostile_options = [Wolf, Crow] # sprite guards?
    friendly_options = [Wood_Sprite_Guard]

    def enter(self):
        self.spawn_friendlies(1)
        return """You find yourself in a huge cavern, with one large hole in the roof.
        Sunlight blazes through, spotlighting enemies, hunched and ready to pounce.
        It looks like you have come upon them right before a kill, and dinner time!"""

    def look_around(self):
        return f"You see a friendly {self.friendlies[0]}"


"""
    
Rough dict to create a 5x5 square forest 
I'm hoping that doing this inefficiently will help
get ideas to make a better version later
    1  2  3  4  5
    6  17 18    7
    8  20 21    9          21 -> C1
    10       25 11               C2  C3
    12 13 14 15 16               C5  C6
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
            "west": 25,
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
            "north": 25,
            "east": 16,
            "west": 14,
        }],
        16: [CaveTunnel, {  #spawn hostile
            "north": 11,
            "west": 15,
            "northwest": 25,
        }],
        17: [LargeCavern, { #Spawn 2 Hostiles and if Victiorious Teleport to next location (Coast)
            "southeast": 21,
        }],
        18: [CaveTunnel, {  #spawn hostile
            "north": 3,
            "south": 21,
        }],
        20: [CaveTunnel, {
            "east": 21,
            "west": 8,
        }],
        21: [CaveTunnel, {
            "north": 18,
            "northwest": 17,
            "west": 20,
        }],
        25: [CaveTunnel, { #spawn hostile
            "northwest": 21,
            "southeast": 16,
        }],
    }
