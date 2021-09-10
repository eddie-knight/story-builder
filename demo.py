from story_builder.races import Wood_Sprite_Guard
from story_builder.characters import *
from story_builder.equipment import StarterWeapon, StarterArmor
from story_builder.location import Location
from story_builder.personality import *
from story_builder.game_state import GameState

state = GameState()

class ForestEdge(Location):
    hostile_options = [Wood_Sprite_Guard] # sprite guards?
    friendly_options = [Wolf] # sprite guards?

    def enter(self):
        return "You find yourself at the edge of a forest"

class CaveEntrance(Location):
    hostile_options = [Wolf]
    def enter(self):
        return "You're at the entrance to a cave"

# def getMonsters(amount):
#     monsters = []
#     while len(monsters) <= amount:
#         monsters.append(Monster(None))
#     return monsters

# def attackAndDefend(attacker, defender):
#     if attacker.health > 0 and defender.health > 0:
#         damageOutput = attacker.deal_damage(defender)
#     if defender.health > 0:
#         damageOutput = defender.deal_damage(attacker)
#     # TODO: Return damage outputs

##################
# Core Game Loop #
##################

def main():
    for p in [Friendly(), Hostile(), Unfriendly(), Fake()]:
        print(p)
    name = input("Who are you, noob?\n> ")
    player = Character(name)
    player.equip(StarterWeapon())
    player.equip(StarterArmor())
    # intro(player)
    enterForest()

def intro(player):
    print(f""" 'OPEN YOUR EYES {player.name}. You have arrived.... You begin as  
        {player.race} with {player.health} HP, and {player.strength} Str, you are wearing {player.armor}""")
    if player.weapon:
        print(f"""You have {player.weapon.describe()}!'\n """)
    hostile = NPC(race=Wood_Sprite_Guard)
    print(f"""{str(hostile).capitalize()} with {hostile.weapon} curiously approaches you!""")


def enterForest():
    startLocationID = state.add_location_to_map(ForestEdge, None)
    northID = state.add_location_to_map(ForestEdge, {"south": 1})
    # TODO: the return values here are making extra work; revise

    area = state.get_location(locationID)
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


main()