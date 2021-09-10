from story_builder.races import Wood_Sprite_Guard
from story_builder.characters import *
from story_builder.equipment import StarterWeapon, StarterArmor
from story_builder.location import Location
from story_builder.personality import *
from story_builder.game_state import GameState


class ForestEdge(Location):
    hostile_options = [Wood_Sprite_Guard] # sprite guards?
    friendly_options = [Wolf] # sprite guards?

    def enter(self):
        return "You find yourself at the edge of a forest"

class ForestInterior(Location):
    hostile_options = [Wood_Sprite_Guard, Wood_Sprite] # sprite guards?
    friendly_options = [Wolf] # sprite guards?

    def enter(self):
        return "You find yourself in a forest"

class CaveEntrance(Location):
    hostile_options = [Wolf]
    def enter(self):
        return "You're at the entrance to a cave"

@DeprecationWarning
def attackAndDefend(attacker, defender):
    if attacker.health > 0 and defender.health > 0:
        damageOutput = attacker.deal_damage(defender)
    if defender.health > 0:
        damageOutput = defender.deal_damage(attacker)
    # TODO: Return damage outputs

@DeprecationWarning
def enterForest():
    area = state.get_location(startLocationID)
    print(area.enter())
    area.spawn_hostiles(10)
    area.spawn_friendlies(5)
    count = area.count_hostiles()
    for hostile in count:
        describe = f"you see {hostile}"
        if count[hostile] > 1:
            describe += f"... {count[hostile]} of them to be precise"
        print(describe + "!")

    count = area.count_friendlies()
    for friend in count:
        describe = f"you see {friend}"
        if count[friend] > 1:
            describe += f"... {count[friend]} of them!"
        print(describe + "!")

@DeprecationWarning
def intro(player):
    print(f""" 'OPEN YOUR EYES {player.name}. You have arrived.... You begin as  
        {player.race} with {player.health} HP, and {player.strength} Str, you are wearing {player.armor}""")
    if player.weapon:
        print(f"""You have {player.weapon.describe()}!'\n """)
    hostile = NPC(race=Wood_Sprite_Guard)
    print(f"""{str(hostile).capitalize()} with {hostile.weapon} curiously approaches you!""")

##################
# Core Game Loop #
##################

state = GameState()

def main():
    for p in [Friendly(), Hostile(), Unfriendly(), Fake()]:
        print(p)
    name = input("Who are you, noob?\n> ")
    player = Character(name)
    player.equip(StarterWeapon())
    player.equip(StarterArmor())
    # intro(player)
    enterForest()

def create_forest():
    """ 
    Rough function to create a 5x5 square forest 
    I'm hoping that doing this inefficiently will help
    get ideas to make a better version later
    """

    forest_edges = []
    while len(forest_edges < 16):
        area = state.add_location_to_map(ForestEdge)
        forest_edges.append(area)

    forest_interiors = []
    while len(forest_interiors < 9):
        area = state.add_location_to_map(ForestInterior)
        forest_interiors.append(area)

    # Top left corner
    state.modify_location_connections(
        forest_edges[0], # current area
        connected_areas={
            "east": forest_edges[1],
            "south": forest_edges[5],
        }
    )
    # Top center edges
    state.modify_location_connections(
        forest_edges[1],
        connected_areas={
            "east": forest_edges[2],
            "west": forest_edges[0],
            "south": forest_edges[6],
        }
    )
    state.modify_location_connections(
        forest_edges[2],
        connected_areas={
            "east": forest_edges[3],
            "west": forest_edges[1],
            "south": forest_edges[7],
        }
    )
    state.modify_location_connections(
        forest_edges[3], # +1
        connected_areas={
            "east": forest_edges[4], # +1
            "west": forest_edges[2], # -1
            "south": forest_edges[8], # +1 from last south
        }
    )
    # Top Right Corner
    state.modify_location_connections(
        forest_edges[4], # +1
        connected_areas={
            "west": forest_edges[3], # -1
            "south": forest_edges[9], # +1 from last south
        }
    )




main()