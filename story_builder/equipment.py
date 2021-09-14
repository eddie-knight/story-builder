import random
from abc import ABC, abstractmethod


class Equipment(ABC):
    traits = []

    def __str__(self):
        if self.name[-1] == "s":
            return self.name.lower()
        return f"a {self.name.lower()}"

    def __init__(self, name=None, how_many_traits=None):
        if name:
            self.name = name
        else:
            self.name = random.choice(list(self.options))

        if how_many_traits:
            self.setTraits(how_many_traits)

        self.durability = self.options[self.name][1]
        self.set_base_values()

    def setTraits(self, how_many_traits):
        """ Add random traits from this class until the
            equipment has the specified number of traits """
        if self.trait_options:
            while len(self.traits) < how_many_traits:
                trait = random.choice(list(self.trait_options))
                if trait not in self.traits:
                    self.traits.append(trait)

    @abstractmethod
    def set_base_values(self):
        """ Execute class-specific initialization """
        pass

    @abstractmethod
    def describe(self):
        """ Return a string describing the equipment """
        pass


######################
#   Weapon Classes   #
######################

class Weapon(Equipment):
    # weapon name: durability, damage
    options = {
        "Mace": (110, 11),
        "Pole-Axe": (91, 16),
        "Battle-Axe": (1, 18),
        "Sword": (201, 21),
        "Rubber Chicken": (10001, 101),
        "Frying Pan": (51, 11),
        "Crusty Gym Sock": (100000, 1001),
        "Fart Gun": (16, 81),
        "Rocket Launcher": (81, 101),
        "Butter Knife": (190, 5),
        "Wooden Spoon": (501, 1),
        "2x4": (61, 31),
        "small twig": (1, 1),
    }
    # trait name: damage, length of effect in seconds
    trait_options = {
        "freezing": (1, 11),
        "flame": (1, 21),
        "vomiting": (1, 10),
        "stun": (1, 5),
        "confusion": (1, 5),
        "hallucinations": (1, 5),
    }

    def set_base_values(self):
        self.type = "weapon"
        self.damage = self.options[self.name][1]

    def describe(self):
        description = f"{self} that inflicts {self.damage} damage"
        if self.traits:
            if len(self.traits) > 1:
                description = f"{description}, {', '.join(self.traits[:-1])} and {self.traits[-1]}"
            else:
                description = f"{description} and {self.traits[0]}"
        return description


class StarterWeapon(Weapon):
    # Name: durability, damage
    options = {
        "Small Dagger": (10, 10),
        "Weak Bow with 5 Arrows": (10, 15),
        "Strong Sling-Shot with 20 Lead pellets": (10, 5),
        "Hunting Knife": (15, 15),
    }
    trait_options = None


class MonsterWeapon(Weapon):
    # weapon name: durability, damage
    options = {
        "Fangs": (10, 10),
        "Claws": (10, 10),
        "Talons": (10, 10),
    }
    # trait name: damage, length of effect in seconds
    trait_options = {
        "poison": (1,10),
    }


######################
#   Armor Classes    #
######################

class Armor(Equipment):
    # armor name: durability, resistance
    options = {
        "a": (10, 7),
        "b": (10, 8),
        "c": (10, 9),
        "d": (10, 10),
        "e": (10, 11),
        "f": (10, 12),
        "g": (10, 13),
        "h": (10, 14),
        "i": (10, 15),
        "j": (10, 16),
        "k": (10, 17),
        "l": (10, 18),
        "m": (10, 19),
    }
    # trait name: damage, length of effect in seconds
    trait_options = { 
        "freezing": (1, 2),
        "flame": (1, 3),
        "vomiting": (1, 1),
        "stun": (1, 1),
        "confusion": (1, 1),
        "hallucinations": (1, 1),
    }

    def set_base_values(self):
        self.type = "armor"
        self.resistance = self.options[self.name][1]

    def describe(self):
        description = f"{self} with {self.resistance} resistance and {self.durability} durability"
        if self.traits:
            description = f"{description}- causes {', '.join(self.traits)} to anyone who strikes it"
        return description

class StarterArmor(Armor):
    # Name: durability, resistance
    options = {
        "T-shirt and Jeans": (5, 2),
        "Bath robe": (3, 1),
        "Long Johns": (1, 1),
        "Coveralls": (6, 3),
        "Fast Food Uniform": (3, 6),
        "Dress Clothes with Inconvenient Footwear": (5, 2),
    }
    trait_options = None
