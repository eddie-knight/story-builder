from os import stat
import story_builder
import sys
from random import randint

from story_builder.equipment import Weapon, StarterArmor
from story_builder.game_state import GameState
from story_builder.characters import Character
from story_builder.scene import forest_grid
from story_builder.scene.caves_grid import caves_grid
from story_builder.scene.coast_grid import coast_grid
from story_builder.scene.plains_grid import plains_grid
from story_builder.scene.LostTemple_grid import LostTemple_grid

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
    if len(sys.argv) > 1 and sys.argv[1] == "load":
        state.load_save()
    else:
        setup()
    input("Press any button to begin the adventure\n> ")
    play()

    state.format_save()

def setup():
    player_name = input("Who are you, noob?\n> ")
    state.set_active_player(Character(player_name))

    player = state.get_active_player()
    player.equip(Weapon("Crusty Gym Sock"))
    player.equip(StarterArmor())
    intro(player)

    state.add_scene_to_map("North Forest", forest_grid)
    state.add_scene_to_map("South Forest", forest_grid)
    state.add_scene_to_map("Caves", caves_grid)
    state.add_scene_to_map("Coast", coast_grid)
    state.add_scene_to_map("Plains", plains_grid)
    state.add_scene_to_map("Temple", LostTemple_grid)

    # OLD CONNECTION LOGIC
    # first_path = state.get_location("North Forest", 16)
    # second_path = state.get_location("South Forest", 1)
    # first_path.exits["path to south forest"] = ("South Forest", 1)
    # second_path.exits["path to north forest"] = ("North Forest", 16)

    # NEW CONNECTION LOGIC
    state.connect_locations(
        ("North Forest", 16, "path to north forest"),
        ("South Forest", 1, "path to south forest"),
    )

    cave_entrance = state.get_location("North Forest", 21)
    cave_forest_exit = state.get_location("Caves", 1)
    cave_coast_exit = state.get_location("Caves", 17)
    coast_cave_entrance = state.get_location("Coast", 1)
    plains_coast_entrance = state.get_location("Coast", 16)
    coast_plains_exit = state.get_location("Plains", 1)
    temple_plains_entrance = state.get_location("Plains", 26)
    plains_temple_exit = state.get_location("Temple", 1)
    #game_exit = state.get_location("Temple", 32)

    cave_forest_exit.exits["Exit into the Forest"] = ("North Forest", 21)
    cave_entrance.exits["Entrance to a dark Cave"] = ("Caves", 1)
    coast_cave_entrance.exits["Re-Enter the Caves"] = ("Caves", 17)
    cave_coast_exit.exits["Exit onto the Coast"] = ("Coast", 1)
    plains_coast_entrance.exits["Return to the Coast"] = ("Coast", 16)
    temple_plains_entrance.exits["Exit the Lost Temple"] = ("Plains", 26)
    coast_plains_exit.exits["Exit into rolling Plains"] = ("Plains", 1)
    plains_temple_exit.exits["Enter a Lost Temple"] = ("Temple", 1)
#    game_exit["You have completed this story arc"] = (exit)

    exit_location_ID = randint(2, state.count_locations("South Forest"))
    exit_area = state.get_location("South Forest", exit_location_ID)
    print(f"Spoiler: Exit is in South Forest area {exit_location_ID}")

    exit_area.add_connection("Teleport Home", 1)
    exit_area.spawn_hostiles(2)
    state.set_active_location("North Forest", 1)

def play():
    player = state.get_active_player()
    this_scene, this_location = state.get_active_location()
    
    finished = False
    while finished == False:
        print("-- DEBUG --", this_scene, this_location.id)

        for enemy in this_location.hostiles:
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
                finished = True
                break
            elif action == "fight":
                print(f"You defeated the {enemy.race}! Congratulations, {player.name}!")

        options = this_location.show_exits().keys()
        directions = ", ".join(options)

        print(f"It's time to move on, {player.name}!\nYour options are: {directions}")
        direction = input("WHERE WILL YOU GO?\n> ")

        ok = False
        while not ok:
            if direction.lower() == "quit" or direction.lower() == "exit":
                print("Your vision goes blank as you collapse to the ground.")
                finished = True
                break

            area = 9999
            try:
                area = int(str(direction))
            except:
                print(direction)
            if area < 9999: # TODO: use number of locations in target scene
                this_scene, this_location = state.set_active_location(state.get_active_location()[0], area)
                print(f"You fast travel to area {area}")
                ok = True
                continue
            if direction in options:
                if direction == "Teleport Home":
                    print("You found the treasure! Go feast!")
                    finished = True
                    break
                target_scene, target_location = this_location.show_exits()[direction]
                this_scene, this_location = state.set_active_location(target_scene, target_location)
                print(f"You walk {direction}")
                ok = True
            else:
                print(f"YOU'RE DUMB. Seriously, {player.name}. Type Betterly.")
                print(f"Your options are: {directions}")
                direction = input("WHERE WILL YOU GO? (type a real direction!)\n> ")

main()