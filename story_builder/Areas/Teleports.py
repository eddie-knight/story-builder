#I am working to understand the method of Teleporting or tranistioning from one location to another.
#I only truly understand the Direct Transport idea.  You type Teleport, and you are moved to the next grid.
#I think this can be done back and forth if needed and done correctly.  And in my mind this seems simple (with your help).
#What I am doing here is to set a location for the teleport to the next area.  In the forest that doesn't HAVE to be 
    #the same area as the boss fight.  However in the Caves and Coast, it is.  I know that there is a way to get to the
    #end boss of each level without fighting your way there, but I love games where if you don't complete each fight, you
    #don't get all the loot/xp you would have otherwise.  So I think that the player should do all the battles, if they are smart,
    #but they can skip through if they choose that path.  
    #Spawn in the Forest, find the Cave.  Exit onto a beach surrounded by Cliffs. Battle your way to and through the plains.
    #Enter the final location.  For now that's a City, but I think I might change that to a lost temple or such.
    #Like I said, I beleive a simple Teleport = ..._grid(1) command should suffice.  This should enter you at #1 spot
    #on said grid (unless you know how to enter where the character left).
    #Does this make sense, and better is it too simplistic in thinking?  I have done my best to build it here in this file for you to see.



from story_builder.characters import Character
from Areas import forest_grid, coast_grid, caves_grid



class Location:
    
    def __init__(self):
        places = [ 
            "deep in a Forest", "surrounded by Desert", "in a series of Caves", " by the Coast of a large Ocean",
             "in a deplapidated building within a City", "surrounded by Plains of hills and grass"
        ]
        self.enter = "deep in a Forest"

Area = Location()


player_name = input("""\n\n\n( A Strong, Deep Voice echos:) Hello New Player! Who will you be?
    (This simple question resonates with power, and... import!  Who will you be?  
    Will you become a NAME to be sung or cursed?  Will you shape events or allow them to shape you?
    Will you make an IMPACT or simply live?  What is your NAME: WHO WILL YOU BE?):\n\n >> """)
player = Character(player_name)
# player.equip(Weapon())
##player.equip(StarterArmor())
# player.unequip(Weapon())
# player.unequip(Armour())

def Main():
    # player.printInventory()
    # placement = input("Which item would you like to equip?\n> ")
    # player.equipFromInventory(int(placement))
    # player.printInventory()
    # exit()

    print(f"""\n\nWELCOME {player.name}, here your journey begins!  You have started what you 'THINK' is a game,
    but you will soon find, there are more to your 'CHOICES' than mere changes in your character.  Your 'CHOICES'
    will guide your growth, or end it.  As in life, there is no garuntee that you will survive.  No garuntee that 
    you will thrive.  And no garuntee you will make past even your first challenge.... Good luck {player.name}.""")

    print(f"""\nLET US BEGIN! (Darkness immediately obscures your vision, yet you hear, and feel, 
    the loudest RUMBLE of thunder, possibly EVER!  It Goes on for long minutes... then silence... \n\n\n""")
    print("\n\n ----------------------------------------------------------------\n\n")
    print(f"OPEN YOUR EYES {player.name}. You have arrived {Area.enter}...")# You begin as a 
        # {player.race} with {player.health} HP, and {player.strength} Str,  {Area.enter}, you are wearing {Scrubs.type} 
        # You have a {player.weapon.type} with {player.weapon.durability} durability and, if used properly,
        # it can do {player.weapon.damage} damage.'\n """)

    exit()

def Begining():

    if Area.enter == "deep in a Forest":
        print(f" {player.name} you are fortuitus to have started here in this lush Forest!  Like only a few others you have begun your Journey in an environment rich with resources.\n")
        forest_grid(1)
    #elif Area.enter == "surrounded by Desert":
        # print(f" {player.name} you have begun your journey in one of the most desolate desert reaches of The Land.  Will you whither and die, or search for the 'Diamond in this Rough'\n?")
        # Caves()
    elif Area.enter == "in a series of Caves":
        print(f" {player.name} you might be in some Caves, but your Luck must be high! These Caves have a luminescent moss lining the walls. \n")
        caves_grid(1)
    elif Area.enter == " by the Coast of a large Ocean":
        print(f" {player.name} you are fortuitus to have started here on the Coast of 'The Everlasting Blue'!  Like only a few others you have begun your Journey in an environment rich with resources.\n")
        coast_grid(1)
    # elif Area.enter ==  "in a deplapidated building within a City":
    #     print(f" {player.name} even though you are in a City, do not expect this journey to be an easy one.\n")
    #     Caves()
    elif Area.enter == "surrounded by Plains of hills and grass":
        print(f" {player.name} though the Plains offer little for protection from the elements, you feel it may just be the rich environment you are hoping for.\n")
        plains_grid(1)




