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
        "Mace": (1, 1),
        "Pole-Axe": (1, 1),
        "Battle-Axe": (1, 1),
        "Sword": (1, 1),
        "Rubber Chicken": (1, 1),
        "Frying Pan": (1, 1),
        "Crusty Gym Sock": (1, 1),
        "Fart Gun": (1, 1),
        "Rocket Launcher": (1, 1),
        "Butter Knife": (1, 1),
        "Wooden Spoon": (1, 1),
        "2x4": (1, 1),
        "small twig": (1, 1),
    }
    # trait name: damage, length of effect in seconds
    trait_options = {
        "freezing": (1, 1),
        "flame": (1, 1),
        "vomiting": (1, 1),
        "stun": (1, 1),
        "confusion": (1, 1),
        "hallucinations": (1, 1),
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
        "Small Dagger": (1, 1),
        "Weak Bow with 5 Arrows": (1, 1),
        "Strong Sling-Shot with 5 Lead pellets": (1, 1),
        "50ft Rope": (1, 1),
        "Hunting Knife": (1, 1),
    }
    trait_options = None


class MonsterWeapon(Weapon):
    # weapon name: durability, damage
    options = {
        "Fangs": (1, 1),
        "Claws": (1, 1),
        "Talons": (1, 1),
    }
    # trait name: damage, length of effect in seconds
    trait_options = {
        "poison": (1,1),
    }


######################
#   Armor Classes    #
######################

class Armor(Equipment):
    # armor name: durability, resistance
    options = {
        "a": (1, 1),
        "b": (1, 1),
        "c": (1, 1),
        "d": (1, 1),
        "e": (1, 1),
        "f": (1, 1),
        "g": (1, 1),
        "h": (1, 1),
        "i": (1, 1),
        "j": (1, 1),
        "k": (1, 1),
        "l": (1, 1),
        "m": (1, 1),
    }
    # trait name: damage, length of effect in seconds
    trait_options = { 
        "freezing": (1, 1),
        "flame": (1, 1),
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
        "T-shirt and Jeans": (1, 1),
        "Bath robe": (1, 1),
        "Long Johns": (1, 1),
        "Coveralls": (1, 1),
        "Fast Food Uniform": (1, 1),
        "Dress Clothes with Inconvenient Footwear": (1, 1),
    }
    trait_options = None
