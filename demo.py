from os import stat
from story_builder.personality import Hostile
import story_builder
import sys

from story_builder.equipment import Weapon, StarterArmor
from story_builder.game_state import GameState
from story_builder.characters import Character
from story_builder.races import Wolf, Wood_Sprite
from story_builder.scene import (
    forest_grid,
    caves_grid,
    coast_grid,
    plains_grid,
    temple_grid,
)

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
    state.get_random_location()
    input("Press ENTER to begin the adventure\n> ")
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
    state.add_scene_to_map("Temple", temple_grid)

    state.connect_locations(
        ("North Forest", 16, "path to south forest"),
        ("South Forest", 1, "path to north forest"),
    )
    state.connect_locations(
        ("North Forest", 21, "Entrance to a dark Cave"),
        ("Caves", 1, "Exit into the Forest"),
    )
    state.connect_locations(
        ("Caves", 17, "Tunnel to the Coast"),
        ("Coast", 1, "Re-Enter the Caves"),
    )
    state.connect_locations(
        ("Coast", 16, "Exit into rolling Plains"),
        ("Plains", 1, "Return to the Coast"),
    )
    state.connect_locations(
        ("Plains", 26, "Enter a Lost Temple"),
        ("Temple", 1, "Exit the Lost Temple"),
    )
    spawn_sprite_quest(state)
    state.set_active_location("North Forest", 1)

def play():
    player = state.get_active_player()
    this_scene, this_location = state.get_active_location()

    finished = False
    while finished == False:
        print(this_location.enter())
        print("-- DEBUG --", this_scene, this_location.id)
        for character in this_location.NPCs:
            print(f"A {str(character.personality)} {character.race} has appeared!")
            print(character.act(player))

            if character.personality is Hostile:
                print(character.comms.challenge())
                print(f"You have {player.health} hit points remaining")
                while player.is_alive() and character.is_alive():
                    action = ""
                    while action.lower() not in ["run", "run away", "fight"]:
                        action = input(f"You have {player.health}HP... Will you run away or fight?\n> ")
                    if action == "run":
                        break
                    give, take = attackAndDefend(player, character)
                    print(f"You did {give} damage, and recieved {take} damage!")
                if not player.is_alive():
                    print(f"You died, {player.name}. Try not to suck next time.")
                    finished = True
                    break
                elif action == "fight":
                    print(f"You defeated the {character.race}! Congratulations, {player.name}!")

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

def random_exit(state):
    random_scene, random_id = state.get_random_location()
    print(f"Spoiler: Exit is in {random_scene} area {random_id}")

    exit_area = state.get_location(random_scene, random_id)
    exit_area.add_connection("Teleport Home", 1)
    exit_area.spawn_hostiles(2)
    exit_area.spawn_friendlies(1)
    state.set_active_location(random_scene, 1)

def spawn_sprite_quest(state):
    random_id = state.get_random_id_from_scene("North Forest")
    quest_start = state.get_location("North Forest", random_id)
    quest_start.spawn_friendlies_by_race(2, Wood_Sprite)
    quest_start.spawn_hostiles_by_race(2, Wolf)
    print(f"Attention! Wolves are attacking friendly Wood Sprites in area {random_id}")

main()