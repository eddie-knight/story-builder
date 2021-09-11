import sys
from random import randint

from story_builder.equipment import StarterWeapon, StarterArmor
from story_builder.personality import *
from story_builder.game_state import GameState
from story_builder.characters import Character
from story_builder.demo_forest import create_forest

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

def intro(player):
    print(f""" 'OPEN YOUR EYES {player.name}. You have arrived.... You begin as  
        {player.race} with {player.health} HP, and {player.strength} Str, you are wearing {player.armor}""")
    if player.weapon:
        print(f"""You have {player.weapon.describe()}!'\n """)

##################
# Core Game Loop #
##################

state = GameState()

def main():
    player = Character(input("Who are you, noob?\n> "))
    player.equip(StarterWeapon())
    player.equip(StarterArmor())
    intro(player)

    create_forest(state)
    here = state.set_active_location(1)

    exit = randint(2, state.count_locations())
    exit_area = state.get_location(exit)
    exit_area.add_connection("Teleport Home", 1)

    while True:
        here.spawn_friendlies(2)
        print(here.enter())

        options = here.show_exits().keys()
        directions = ", ".join(options)

        print(f"{player.name}, your options are: {directions}")
        travel = input("WHERE WILL YOU GO?\n> ")

        ok = False
        while not ok:
            if travel in options:
                if travel == "Teleport Home":
                    print("You found the treasure! Go feast!")
                    sys.exit()
                go = here.show_exits()[travel]
                here = state.set_active_location(go)
                ok = True
            else:
                print(f"YOU'RE DUMB. Seriously, {player.name}. Type Betterly.")
                print(f"Your options are: {directions}")
                travel = input("WHERE WILL YOU GO? (type a real direction!)\n> ")

main()