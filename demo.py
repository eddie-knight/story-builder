import sys
from random import randint

from story_builder.equipment import Weapon, StarterArmor
from story_builder.game_state import GameState
from story_builder.characters import Character
from story_builder.scene import forest_grid, caves_grid

def attackAndDefend(attacker, defender):
    attackOutput, defendOutput = (0,0)
    if attacker.health > 0 and defender.health > 0:
        attackOutput = attacker.deal_damage(defender)
    if defender.health > 0:
        defendOutput = defender.deal_damage(attacker)
    return (attackOutput, defendOutput)


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
    player.equip(Weapon("Crusty Gym Sock"))
    player.equip(StarterArmor())
    intro(player)

    state.add_scene_to_map(forest_grid) # ids: 1-25
    # print(state.count_locations())
    state.add_scene_to_map(caves_grid)  # ids: 26-47 (22 locations)
    # print(state.count_locations())

    forest_center = state.get_location(21)
    cave_entrance = state.get_location(26)
    forest_center.connected_areas["enter cave"] = 26
    cave_entrance.connected_areas["exit cave"] = 21

    # print(state)

    exit_location_ID = randint(2, state.count_locations())
    exit_area = state.get_location(exit_location_ID)

    # print(exit_location_ID, exit_area)

    exit_area.add_connection("Teleport Home", 1)
    exit_area.spawn_hostiles(2)

    here = state.set_active_location(1)

    while True:
        print(here.enter())

        for enemy in here.hostiles:
            print(f"A wild {enemy.race} has appeared!")
            print(f"{enemy.name}, {enemy.race} shouts: '{enemy.comms.taunt()}'")
            while player.is_alive() and enemy.is_alive():
                action = ""
                while action.lower() not in ["run", "run away", "fight"]:
                    action = input(f"You have {player.health}HP... Will you run away or fight?\n> ")
                if action == "run":
                    break
                give, take = attackAndDefend(player, enemy)
                print(f"You did {give} damage, and recieved {take} damage!")
            if not player.is_alive():
                print(f"You died, {player.name}. Try not to suck next time.")
                exit()
            elif action == "fight":
                print(f"You defeated the {enemy.race}! Congratulations, {player.name}!")

        options = here.show_exits().keys()
        directions = ", ".join(options)

        print(f"It's time to move on, {player.name}!\nYour options are: {directions}")
        direction = input("WHERE WILL YOU GO?\n> ")

        ok = False
        while not ok:
            if direction.lower() == "quit" or direction.lower() == "exit":
                print("Your vision goes blank as you collapse to the ground.")
                sys.exit()

            area = 9999
            try:
                area = int(str(direction))
            except:
                print(direction)
            if area <= state.count_locations():
                    here = state.set_active_location(area)
                    print(f"You fast travel to area {area}")
                    ok = True
                    continue

            if direction in options:
                if direction == "Teleport Home":
                    print("You found the treasure! Go feast!")
                    sys.exit()
                go = here.show_exits()[direction]
                here = state.set_active_location(go)
                print(f"You walk {direction}")
                ok = True
            else:
                print(f"YOU'RE DUMB. Seriously, {player.name}. Type Betterly.")
                print(f"Your options are: {directions}")
                direction = input("WHERE WILL YOU GO? (type a real direction!)\n> ")

main()