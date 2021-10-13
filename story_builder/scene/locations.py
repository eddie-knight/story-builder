from story_builder.location import Location
from story_builder.scene import *
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
        return "You have set foot upon a path to the coast."
        # beach = input("""You have set foot upon a path to the coast.
        # Would you like to take a long walk on the beach? > """)
        # if beach == "yes":
        #     coast_grid()
        # else:
        #     exit()

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

class OpenPlains(Location):
     hostile_options = [Bear, Cougar, Python]
     def enter(plains_grid):
         return """ You have passed through the cliffs and onto a large open valley.  Large, steep mountains
         surround this grassy plain.  While you can see the cliffs towering above and around you, the 
         grass itself stands 8-10ft tall. This feels like pushing your way through a grassy corn maze.
         Even so, you FEEL as if there is something both terrible, and wonderful waiting for you 
         not far ahead."""

class PlainsEdge(Location):
     hostile_options = [Bear]
     def enter(self):
         return "You find yourself with unclimable, sheer cliffs and tall grasses beside you."

class PlainsInterior(Location):
     hostile_options = [Cougar]
     def enter(self):
         return "You are now completely surrounded by tall grasses, with only a few feet of room to move."

class PlainsOpenArea(Location):
     hostile_options = [Python]
     def enter(self):
         return """You have entered a large area where the grass has been flattend.  There is a small creek
         running left to right, down from one cliff, into a hole at the base of the other.  This is obviously the
         only area for the beasts of this area to find water. You stand ready for a fight. It's obvious that this 
         would be the best area for a predator to stalk."""

class Temple(Location):
    def enter(self):
        return """Though the battle was bloody and violent you stand, and look around. Just beyond the grasses
        to your South, lies an old, yet still forelornly-ellegant temple."""

class TempleEntrance(Location):
    hostile_options = [Slime, LargeSlime]
    def enter(self):
        return """As you enter the forboding temple, the large stone doors SLAM SHUT behind you! For a moment you 
        enveloped in the inky blackness, then torches magically alight, giving an eerie glow to the chamber."""

class TempleNiche(Location):
    hostile_options = [Slime] # sprite guards?

    def look_around(self):
        return f"A {self.hostile_options[1]} jumps out of the shadows and attacks!"

    def enter(self):
        self.spawn_friendlies(0)
        return "You find yourself in a deep niche with a dark hole in the wall."
        # Do you look around or exit? > """)
        # if Niche == "look around":
        #     self.look_around()
        # else:
        #     coast_grid()

class TempleHall(Location):
    def enter(self):
        return "You walk down a dark, and creepy hallway. The silence is deafening."

class TempleSanctum(Location):
    hostile_options = [LargeSlime]
    def enter(self):
        return "oh look a sack of tums"

    def look_around(self):
        self.spawn_hostiles(1)
        return """You see a large inner sactum.  There is strange artistry along the tall walls.
        It seems these ancient people used to worship the Slimes you have seen along the way.  
        But something seems odd.... The slime portrayed seems, quite ... a bit....LARGER....
        
        Suddenly, you hear stone scraping along stone. Your eyes are yanked to the top of the central
        alter, as the top of it slides off, and CRASHES to the ground!  The problem is, you didn't see
        anyone move it.  Let alone anyone that could move a stone that had to weigh at least 2 tons!
        
        Thats when you realize, it was the large gooey tenticle sliding out that moved it so easily."""

    