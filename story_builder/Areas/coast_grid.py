from story_builder.location import Location
from story_builder.characters import *
from scene import *


class Coast(Location):
    def enter(self):
        beach = input(""" You have set foot upon a path to the coast.
        Would you like to take a long walk on the beach? > """)
        if beach == "yes":
            coast_grid()
        else:
            exit()
class OpenArea(Location):
    hostile_options = [Giant, Hawk] # sprite guards?
    friendly_options = [Wolf] # sprite guards?
    def look_around(self):
        return f"You see :{self.hostile_options[2]} about to attack a {self.friendly_options[1]}!"
        # help = input("Do you help, or retreat? > ")
        # if help == "help":
        #     #battle
        #     #if battle == victorious:
        #         #Teleport to next scene
        # elif help == "retreat":
        #     coast_grid()
            
    def enter(self):
        enter = input("""You find yourself in a large open area.
        Would you like to look around or exit? > """)
        if enter == "look around":
            self.look_around()
        else:
            coast_grid()
    
class CliffNiche(Location):
    hostile_options = [Wood_Sprite_Guard, Wood_Sprite] # sprite guards?
    friendly_options = [Wolf]
    def look_around(self):
        return f"A {self.hostile_options[1]} jumps out of the shadows and attacks!"
    def enter(self):
        self.spawn_friendlies(0)
        Niche = input("""You find yourself in deep niche in the cliffs.
        Do you look around or exit? > """)
        if Niche == "look around":
            self.look_around()
        else:
            coast_grid()


    

class CliffPath(Location):
    def enter(self):
        return "You squeeze between through a pass in the tall cliffs."

""" 

    9  8  7  6  1  2  3  4  5       #13, 14, 17, 19: Are all niches with a bad guy in them.  18 is the final room
    10       11    12       13       this is a beach along a cliff with niches. At 4 parts of the cliffs you can 
    14    15    16    17    18       enter, but only the last on each side (9 , 5) will lead to the back side.
    19 20 21 22 23 24 25 26 27       only 25 will lead to 18 which is the final spot.

"""    
coast_grid = {
        1: [Coast, {
            "east": 2,
            "west": 6,
            #"Area.enter" from caves_grid
        }],
        2: [Coast, {
            "east": 3,
            "south": 12,
            "west": 1,
        }],
        3: [Coast, {
            "east": 4,
            "west": 2,
        }],
        4: [Coast, {
            "east": 5,
            "west": 3,
        }],
        5: [Coast, {
            "south": 13,
            "west": 4,
        }],
        6: [Coast, {
            "east": 1,
            "west": 7,
            "south": 11,
        }],
        7: [Coast, {
            "east": 6,
            "west": 8,
        }],
        8: [Coast, {
            "east": 7,
            "west": 9,
        }],
        9: [Coast, {
            "east": 8,
            "south": 10,
        }],
        10: [CliffPath, {
            "north": 9,
            "south": 14,
        }],
        11: [CliffNiche, {
            "north": 6,
        }],
        12: [CliffNiche, {
            "north": 2,
        }],
        13: [CliffPath, {
            "north": 5,
            "south": 18,
        }],
        14: [CliffPath, {
            "north": 10,
            "south": 19,
        }],
        15: [CliffNiche, {
            "south": 21,
        }],
        16: [OpenArea, {
            "south": 23,
            #"Teleport": plains_grid()
        }],
        17: [CliffNiche, {
            "south": 25,
        }],
        18: [CliffPath, {
            "north": 13,
            "south": 27,
        }],
        19: [CliffPath, {
            "north": 14,
            "east": 20,
        }],
        20: [CliffPath, {
            "east": 21,
            "west": 19,
        }],
        21: [CliffPath, {
            "north": 15,
            "east": 22,
            "west": 20,
        }],
        22: [CliffPath, {
            "east": 23,
            "west": 21,
        }],
        23: [CliffPath, {
            "north": 16,
            "east": 24,
            "west": 22,
        }],
        24: [CliffPath, {
            "east": 25,
            "west": 23,
        }],
        25: [CliffPath, {
            "north": 17,
            "east": 26,
            "west": 24,
        }],
        26: [CliffPath, {
            "east": 27,
            "west": 25,
        }],
        27: [CliffPath, {
            "north": 18,
            "west": 26,
        }],
    }
