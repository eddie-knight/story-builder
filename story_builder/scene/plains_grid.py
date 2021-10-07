from story_builder.scene import coast_grid
from story_builder.locations.locations import LostTemple_grid
from story_builder.locations import PlainsOpenArea, PlainsEdge, PlainsInterior, LostTemple
from story_builder.races import Bear, Cougar, Python 


"""
    1  2  3  4  5
    6  17 18 19 7
    8  20 21 22 9          21 -> C1
    10 23 24 25 11
    12 13 14 15 16
          26
"""
def plains_grid(scene_name):
    return ([
        PlainsEdge(
            scene_name=scene_name,
            id=1,
            exits={
                "east": 2,
                "south": 6,
                "southeast": 17,
                "Coast": coast_grid(),
            }
        ),
        PlainsEdge(
            scene_name=scene_name,
            id=2,
            exits={
                "east": 3,
                "south": 17,
                "west": 1,
            }
        ),
        PlainsEdge(
            scene_name=scene_name,
            id=3,
            exits={
                "east": 4,
                "south": 18,
                "west": 2,
            }
        ),
        PlainsEdge(
            scene_name=scene_name,
            id=4,
            exits={
                "east": 5,
                "south": 19,
                "west": 3,
            }
        ),
        PlainsEdge(
            scene_name=scene_name,
            id=5,
            exits={
                "south": 7,
                "west": 4,
            }
        ),
        PlainsEdge(
            scene_name=scene_name,
            id=6,
            exits={
                "north": 1,
                "east": 17,
                "south": 8,
            }
        ),
        PlainsEdge(
            scene_name=scene_name,
            id=7,
            exits={
                "north": 5,
                "south": 9,
                "west": 19,
            }
        ),
        PlainsEdge(
            scene_name=scene_name,
            id=8,
            exits={
                "north": 6,
                "east": 20,
                "south": 10,
                 #"Look Around": Hostile_options,
            }
        ),
        PlainsEdge(
            scene_name=scene_name,
            id=9,
            exits={
                "north": 7,
                "south": 11,
                "west": 22,
                 #"Look Around": Hostile_options,
            }
        ),
        PlainsEdge(
            scene_name=scene_name,
            id=10,
            exits={
                "north": 8,
                "east": 23,
                "south": 12,
            }
        ),
        PlainsEdge(
            scene_name=scene_name,
            id=11,
            exits={
                "north": 9,
                "south": 16,
                "west": 25,
            }
        ),
        PlainsEdge(
            scene_name=scene_name,
            id=12,
            exits={
                "north": 10,
                "east": 13,
            }
        ),
        PlainsEdge(
            scene_name=scene_name,
            id=13,
            exits={
                "north": 23,
                "east": 14,
                "west": 12,
            }
        ),
        PlainsOpenArea(
            scene_name=scene_name,
            id=14,
            exits={
                "north": 24,
                "east": 15,
                "west": 13,
                "south": 26,
                 #"Look Around": Hostile_options,
            }
        ),
        PlainsEdge(
            scene_name=scene_name,
            id=15,
            exits={
                "north": 25,
                "east": 16,
                "west": 14,
            }
        ),
        PlainsEdge(
            scene_name=scene_name,
            id=16,
            exits={
                "north": 11,
                "west": 15,
            }
        ),
        PlainsInterior(
            scene_name=scene_name,
            id=17,
            exits={
                "north": 2,
                "east": 18,
                "south": 20,
                "west": 6,
            }
        ),
        PlainsInterior(
            scene_name=scene_name,
            id=18,
            exits={
                "north": 3,
                "east": 19,
                "south": 21,
                "west": 17,
            }
        ),
        PlainsInterior(
            scene_name=scene_name,
            id=19,
            exits={
                "north": 4,
                "east": 7,
                "south": 22,
                "west": 18,
            }
        ),
        PlainsInterior(
            scene_name=scene_name,
            id=20,
            exits={
                "north": 17,
                "east": 21,
                "south": 23,
                "west": 8,
            }
        ),
        PlainsInterior(
            scene_name=scene_name,
            id=21,
            exits={
                "north": 18,
                "east": 22,
                "south": 24,
                "west": 20,
                 #"Look Around": Hostile_options,
            }
        ),
        PlainsInterior(
            scene_name=scene_name,
            id=22,
            exits={
                "north": 19,
                "east": 9,
                "south": 25,
                "west": 21,
            }
        ),
        PlainsInterior(
            scene_name=scene_name,
            id=23,
            exits={
                "north": 20,
                "east": 24,
                "south": 13,
                "west": 10,
            }
        ),
        PlainsInterior(
            scene_name=scene_name,
            id=24,
            exits={
                "north": 21,
                "east": 25,
                "south": 14,
                "west": 23,
            }
        ),
        PlainsInterior(
            scene_name=scene_name,
            id=25,
            exits={
                "north": 22,
                "east": 11,
                "south": 15,
                "west": 24,
            }
        ),
        LostTemple(
            scene_name=scene_name,
            id=26,
            exits={
                "north": 14,
                "south": LostTemple_grid(1),
            }
        )
    ])
