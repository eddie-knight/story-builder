from abc import ABC, abstractmethod
from random import randrange

from .equipment import *

class Race(ABC):
    # Required Values for Child Classes
    speed = None # average = 30
    charisma = None # average = 10
    strength = None # average = 10
    intelligence = None # average = 10
    endurance = None # average = 10
    arms = None
    legs = None
    racial_weapons = None
    racial_armor = None

    def __init__(self):
        # ensure ABC was implemented properly
        for value, value_name in (
            (self.speed, "speed"),
            (self.arms, "arms"),
            (self.legs, "legs"),
            (self.charisma, "charisma"),
            (self.intelligence, "intelligence"),
            (self.strength, "strength"),
            (self.racial_weapons, "racial_weapons"),
            (self.racial_armor, "racial_armor")):
            if value is None:
                raise ValueError(
                    f"Race may not be used without setting {value_name}"
                )
    
    def __str__(self):
        name = self.__class__.__name__.lower()
        name = " ".join(name.split("_"))
        if name[0] in ["a", "e", "i", "o", "u"]:
            return f"an {name}"
        return f"a {name}"

    def starting_weapon(self):
        weapon = self.racial_weapons[randrange(0, len(self.racial_weapons))]
        if weapon:
            return weapon()

    def starting_armor(self):
        armor = self.racial_armor[randrange(0, len(self.racial_armor))]
        if armor:
            return armor()

    @abstractmethod
    def describe(self):
        pass


#########################
#   Humanoid Classes    #
#########################

class Humanoid(Race):
    """ Still an ABC """
    arms = 2
    legs = 2
    speed = 30
    endurance = 10
    racial_weapons = [Weapon]
    racial_armor = [None]

class Human(Humanoid):
    charisma = 12
    strength = 10
    intelligence = 10

    def describe(self):
        return """ Usually sporting only a tuft of hair on their head,
                   these creatures are the only species pretentious enough
                   to name an entire racial category after themselves """

class Giant(Humanoid):
    charisma = 4
    strength = 30
    endurance = 20
    intelligence = 4

    def describe(self):
        return """ Giants are big and- in this world at least- quite dumb and ugly """

class Orc(Humanoid):
    charisma = 6
    strength = 14
    endurance = 14
    intelligence = 6

    def describe(self):
        return """ Orcs are like giants- but less big, and sometimes they can speak """

class Wood_Sprite(Humanoid):
    charisma = 16
    strength = 2
    intelligence = 14

    def describe(self):
        return """ Wood sprites are short, thin humanoids who can easily think- or talk- themselves into and out of trouble """

class Wood_Sprite_Guard(Wood_Sprite):
    charisma = 12
    strength = 5
    endurance = 12
    intelligence = 14


#########################
#   Quadraped Classes   #
#########################

class Quadraped(Race):
    arms = 0
    legs = 4
    speed = 50
    charisma = 2
    endurance = 14
    racial_weapons = [MonsterWeapon]
    racial_armor = [None]

    def describe(self):
        return """ Quadrapeds can move quickly, but they aren't very convincing in an argument """


class Wolf(Quadraped):
    strength = 10
    intelligence = 5

class Horse(Quadraped):
    strength = 20
    intelligence = 2

#########################
#     Flying Classes    #
#########################

class Flying(Race):
    arms = 2
    legs = 2
    speed = 50
    charisma = 2
    intelligence = 2
    endurance = 4
    racial_weapons = [MonsterWeapon]
    racial_armor = [None]

    def describe(self):
        return """ Flyers are the fastest creatures, but they get fooled very easily """

class Eagle(Flying):
    strength = 15
    endurance = 8

class Crow(Flying):
    strength = 5

class Hawk(Flying):
    speed = 60
    strength = 10
