#Still need to fix caves_grid def to look like this.
#then put the right turns into plains and temple grids



from story_builder.scene.caves_grid import caves_grid
from story_builder.scene import plains_grid
from story_builder.locations import OpenPlains
from story_builder.locations import Coast, CliffNiche, CliffPath, OpenArea

""" 

    9  8  7  6  1  2  3  4  5       #13, 14, 17, 19: Are all niches with a bad guy in them.  18 is the final room
    10       11    12       13       this is a beach along a cliff with niches. At 4 parts of the cliffs you can 
    14    15          17    18       enter, but only the last on each side (9 , 5) will lead to the back side.
    19 20 21 22 23 24 25 26 27       only 25 will lead to 18 which is the final spot.
                16
"""  
def coast_grid(scene_name):
    return([
        Coast(
            scene_name=scene_name,
            id=1,
            exits= {
            "east": 2,
            "west": 6,
            "Caves": caves_grid(),
            }
        ),    
        Coast(
            scene_name=scene_name,
            id=2,
            exits= {
            "east": 3,
            "south": 12,
            "west": 1,
            }
        ),    
        Coast(
            scene_name=scene_name,
            id=3,
            exits= {
            "east": 4,
            "west": 2,
            }
        ),
        Coast(
            scene_name=scene_name,
            id=4,
            exits= {
            "east": 5,
            "west": 3,
            }
        ),
        Coast(
            scene_name=scene_name,
            id=5,
            exits= {
            "south": 13,
            "west": 4,
            }
        ),
        Coast(
            scene_name=scene_name,
            id=6,
            exits= {
            "east": 1,
            "west": 7,
            "south": 11,
            }
        ),
        Coast(
            scene_name=scene_name,
            id=7,
            exits= {
            "east": 6,
            "west": 8,
            }
        ),
        Coast(
            scene_name=scene_name,
            id=8,
            exits= {
            "east": 7,
            "west": 9,
            }
        ),
        Coast(
            scene_name=scene_name,
            id=9,
            exits= {
            "east": 8,
            "south": 10,
            }
        ),
        CliffPath(
            scene_name=scene_name,
            id=10,
            exits= {
            "north": 9,
            "south": 14,
            }
        ),
        CliffNiche(
            scene_name=scene_name,
            id=11,
            exits= {
            "north": 6,
            }
        ),
        CliffNiche(
            scene_name=scene_name,
            id=12,
            exits= {
            "north": 2,
            }
        ),
        CliffPath(
            scene_name=scene_name,
            id=13,
            exits= {
            "north": 5,
            "south": 18,
            }
        ),
        CliffPath(
            scene_name=scene_name,
            id=14,
            exits= {
            "north": 10,
            "south": 19,
            }
        ),
        CliffNiche(
            scene_name=scene_name,
            id=15,
            exits= {
            "south": 21,
            }
        ),
        OpenArea(
            scene_name=scene_name,
            id=16,
            exits= {
            "north": 23,
            "south": plains_grid()
            }
        ),
        CliffNiche(
            scene_name=scene_name,
            id=17,
            exits= {
            "south": 25,
            }
        ),
        CliffPath(
            scene_name=scene_name,
            id=18,
            exits= {
            "north": 13,
            "south": 27,
            }
        ),
        CliffPath(
            scene_name=scene_name,
            id=19,
            exits= {
            "north": 14,
            "east": 20,
            }
        ),
        CliffPath(
            scene_name=scene_name,
            id=20,
            exits= {
            "east": 21,
            "west": 19,
            }
        ),
        CliffPath(
            scene_name=scene_name,
            id=21,
            exits= {
            "north": 15,
            "east": 22,
            "west": 20,
            }
        ),
        CliffPath(
            scene_name=scene_name,
            id=22,
            exits= {
            "east": 23,
            "west": 21,
            }
        ),
        CliffPath(
            scene_name=scene_name,
            id=23,
            exits= {
            "south": 16,
            "east": 24,
            "west": 22,
            }
        ),
        CliffPath(
            scene_name=scene_name,
            id=24,
            exits= {
            "east": 25,
            "west": 23,
            }
        ),
        CliffPath(
            scene_name=scene_name,
            id=25,
            exits= {
            "north": 17,
            "east": 26,
            "west": 24,
            }
        ),
        CliffPath(
            scene_name=scene_name,
            id=26,
            exits= {
            "east": 27,
            "west": 25,
            }
        ),
        CliffPath(
            scene_name=scene_name,
            id=27,
            exits= {
            "north": 18,
            "west": 26,
            }
        ),
    ])
