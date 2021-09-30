from story_builder.locations.locations import TempleSactum
from story_builder.locations import TempleHall, TempleNiche
from story_builder.races import Slime, LargeSlime
"""
        1
        2
    3 4 5 6 7
        8
        9
  10 11 12 13 14
  15    16    17
  18          19
  20 21    22 23
  24          25
  26 27 28 29 30
        31
        32
        """

def LostTemple_grid(scene_name):
    return([
        TempleHall(
            scene_name=scene_name,
            id=1,
            exits= {
            "south": 2,
        }),    
        TempleHall(
            scene_name=scene_name,
            id=2,
            exits= {
            "south": 5,
        }),    
        TempleNiche(
            scene_name=scene_name,
            id=3,
            exits= {
            "west": 4,
            #"Look Around":
        }),
        TempleHall(
            scene_name=scene_name,
            id=4,
            exits= {
            "east": 5,
            "west": 3,
        }),
        TempleHall(
            scene_name=scene_name,
            id=5,
            exits= {
            "north": 2,
            "west": 4,
            "east": 6,
            "south": 8,
        }),
        TempleHall(
            scene_name=scene_name,
            id=6,
            exits= {
            "east": 7,
            "west": 5,
        }),
        TempleNiche(
            scene_name=scene_name,
            id=7,
            exits= {
            "west": 6,
             #"Look Around": Hostile_options,
        }),
        TempleHall(
            scene_name=scene_name,
            id=8,
            exits= {
            "north": 5,
            "south": 9,
        }),
        TempleHall(
            scene_name=scene_name,
            id=9,
            exits= {
            "north": 8,
            "south": 12,
        }),
        TempleHall(
            scene_name=scene_name,
            id=10,
            exits= {
            "east": 11,
            "south": 15,
        }),
        TempleHall(
            scene_name=scene_name,
            id=11,
            exits= {
            "east": 12,
            "west": 10
        }),
        TempleHall(
            scene_name=scene_name,
            id=12,
            exits= {
            "north": 9,
            "south": 16,
            "west": 11,
            "east": 13,
        }),
        TempleHall(
            scene_name=scene_name,
            id=13,
            exits= {
            "east": 14,
            "west": 12,
        }),
        TempleHall(
            scene_name=scene_name,
            id=14,
            exits= {
            "west": 13,
            "south": 17,
        }),
        TempleHall(
            scene_name=scene_name,
            id=15,
            exits= {
            "south": 18,
        }),
        TempleNiche(
            scene_name=scene_name,
            id=16,
            exits= {
            "north": 12,
        }),
        TempleHall(
            scene_name=scene_name,
            id=17,
            exits= {
            "north": 14,
            "south": 19,
        }),
        TempleHall(
            scene_name=scene_name,
            id=18,
            exits= {
            "north": 15,
            "south": 20,
        }),
        TempleHall(
            scene_name=scene_name,
            id=19,
            exits= {
            "north": 17,
            "south": 23,
        }),
        TempleHall(
            scene_name=scene_name,
            id=20,
            exits= {
            "east": 21,
            "south": 24,
        }),
        TempleNiche(
            scene_name=scene_name,
            id=21,
            exits= {
            "west": 20,
             #"Look Around": Hostile_options,
        }),
        TempleNiche(
            scene_name=scene_name,
            id=22,
            exits= {
            "east": 23,
             #"Look Around": Hostile_options,
        }),
        TempleHall(
            scene_name=scene_name,
            id=23,
            exits= {
            "south": 25,
            "north": 19,
            "west": 22,
        }),
        TempleHall(
            scene_name=scene_name,
            id=24,
            exits= {
            "north": 20,
            "south": 26,
        }),
        TempleHall(
            scene_name=scene_name,
            id=25,
            exits= {
            "north": 23,
            "south": 30,
        }),
        TempleHall(
            scene_name=scene_name,
            id=26,
            exits= {
            "east": 27,
            "north": 24,
        }),
        
        TempleHall(
            scene_name=scene_name,
            id=27,
            exits= {
            "east": 28,
            "west": 26,
        }),
        TempleHall(
            scene_name=scene_name,
            id=28,
            exits= {
            "south": 31,
            "west": 27,
            "east": 29,
        }),
        TempleHall(
            scene_name=scene_name,
            id=29,
            exits= {
            "east": 30,
            "west": 28,
        }),
        TempleHall(
            scene_name=scene_name,
            id=30,
            exits= {
            "north": 25,
            "west": 29,
        }),
        TempleHall(
            scene_name=scene_name,
            id=31,
            exits= {
            "north": 28,
            "south": 32,
        }),
        TempleSactum(
            scene_name=scene_name,
            id=32,
            exits= {
            "north": 31,
             #"Look Around": Hostile_options,
        }),
    ])
