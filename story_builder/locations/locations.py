from story_builder.location import Location
from story_builder.races import *

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


class Coast(Location):
    def enter(self):
        beach = input("""You have set foot upon a path to the coast.
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
        return "You find yourself in a large open area."
        # Would you like to look around or exit? > """)
        # if enter == "look around":
        #     self.look_around()
        # else:
        #     coast_grid()
    
class CliffNiche(Location):
    hostile_options = [Wood_Sprite_Guard, Wood_Sprite] # sprite guards?
    friendly_options = [Wolf]

    def look_around(self):
        return f"A {self.hostile_options[1]} jumps out of the shadows and attacks!"

    def enter(self):
        self.spawn_friendlies(0)
        return "You find yourself in a deep niche in the cliffs."
        # Do you look around or exit? > """)
        # if Niche == "look around":
        #     self.look_around()
        # else:
        #     coast_grid()
    

class CliffPath(Location):
    def enter(self):
        return "You squeeze between through a pass in the tall cliffs."


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