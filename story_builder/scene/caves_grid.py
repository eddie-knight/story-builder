from story_builder.races import Wolf
from story_builder.scene import forest_grid
from .locations import CaveTunnel, LargeCavern
from story_builder.scene import coast_grid



"""
    1  2  3  4  5
    6  17 18    7
    8  20 21    9
    10       22 11
    12 13 14 15 16
"""
def caves_grid(scene_name):
    return([
        CaveTunnel(
         scene_name=scene_name,
            id=1,
            exits= {
            "east": 2,
            "south": 6,
            #"North Forest": forest_grid()
        }),
        CaveTunnel(
         scene_name=scene_name,
            id=2,
            exits= {
            "east": 3,
            "west": 1,
        }),
        CaveTunnel(
         scene_name=scene_name,
            id=3,
            exits= {
            "east": 4,
            "south": 18,
            "west": 2,
        }),
        CaveTunnel(
         scene_name=scene_name,
            id=4,
            exits= {
            "east": 5,
            "west": 3,
        }),
        CaveTunnel(
         scene_name=scene_name,
            id=5,
            exits= {
            "south": 7,
            "west": 4,
            #"Look Around": Hostile_options,
        }),
        CaveTunnel(
         scene_name=scene_name,
            id=6,
            exits= {
            "north": 1,
            "south": 8,
        }),
        CaveTunnel(
         scene_name=scene_name,
            id=7,
            exits= {
            "north": 5,
            "south": 9,
        }),
        CaveTunnel(
         scene_name=scene_name,
            id=8,
            exits= {
            "north": 6,
            "south": 10,
        }),
        CaveTunnel(
         scene_name=scene_name,
            id=9,
            exits= {
            "north": 7,
            "south": 11,
        }),
        CaveTunnel(
         scene_name=scene_name,
            id=10,
            exits= {
            "north": 8,
            "south": 12,
        }),
        CaveTunnel(
         scene_name=scene_name,
            id=11,
            exits= {
            "north": 9,
            "south": 16,
            "west": 22,
        }),
        CaveTunnel(
         scene_name=scene_name,
            id=12,
            exits= {
            "north": 10,
            "east": 13,
             #"Look Around": Hostile_options,
        }),
        CaveTunnel(
         scene_name=scene_name,
            id=13,
            exits= {
            "east": 14,
            "west": 12,
        }),
        CaveTunnel(
         scene_name=scene_name,
            id=14,
            exits= {
            "east": 15,
            "west": 13,
        }),
        CaveTunnel(
         scene_name=scene_name,
            id=15,
            exits= {
            "north": 22,
            "east": 16,
            "west": 14,
        }),
        CaveTunnel(
         scene_name=scene_name,
            id=16,
            exits= {  #spawn hostile
            "north": 11,
            "west": 15,
            "northwest": 22,
             #"Look Around": Hostile_options,
        }),
        LargeCavern(
         scene_name=scene_name,
         #hostile_options = (Wolf(3))
            id=17,
            exits= { #Spawn 2 Hostiles and if Victiorious Teleport to next location (Coast)
            "southeast": 21,
            #"Coast": coast_grid(),
        }),
        CaveTunnel(
         scene_name=scene_name,
            id=18,
            exits= {  #spawn hostile
            "north": 3,
            "south": 21,
             #"Look Around": Hostile_options,
        }),
        CaveTunnel(
         scene_name=scene_name,
            id=20,
            exits= {
            "east": 21,
            "west": 8,
             #"Look Around": Hostile_options,
        }),
        CaveTunnel(
         scene_name=scene_name,
            id=21,
            exits= {
            "north": 18,
            "northwest": 17,
            "west": 20,
        }),
        CaveTunnel(
         scene_name=scene_name,
            id=22,
            exits= {
            "northwest": 21,
            "southeast": 16,
        }),
    ])
