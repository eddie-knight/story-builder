from random import randrange, randint

from .personality import Personality, Friendly, Hostile, Unfriendly
from .races import *
from .communication import LowCommon

class Inventory(list):
    """ Custom list object to enable adding and dropping items """
    capacity = 2
    recently_dropped_items = [] # clear this when changing areas!

    def add(self, item) -> bool:
        """ Append if below capacity. Returns True if appended """
        if self.capacity > len(self):
            self.append(item)
            return True # success
        return False # fail

    def drop(self, position) -> None:
        """ soft delete an item """
        self.drop_item(self[position])
        del self[position]

    def drop_item(self, item) -> None:
        self.recently_dropped_items.append(item)
    
    def clear_dropped(self) -> None:
        self.recently_dropped_items = []

    def save_data(self) -> dict:
        recently_dropped_data = []
        for item in self.recently_dropped_items:
            recently_dropped_data.append(item.name)

        inventory_data = []
        for item in self:
            inventory_data.append([item.name, str(item.__class__)])
        
        return {
            "capacity": self.capacity,
            "contents": inventory_data,
            "recently_dropped_items": recently_dropped_data,
        }

class Character:
    """ Used for player character, and as a base for other classes """

    race_options = [Human]
    comms_options = [LowCommon]
    name_options = [None]

    def __init__(self, name=None, race=None, personality=None) -> None:
        self.setName(name)
        self.setRace(race)
        self.setComms(personality)
        self.set_base_values()

    def __str__(self):
        return str(self.race)

    def setName(self, name) -> None:
        """ Basic bahavior, may be overridden in child classes """
        if name:
            self.name = name
        else:
            self.name = self.name_options[randrange(0, len(self.name_options))]

    def setRace(self, race) -> None:
        """ Basic bahavior, may be overridden in child classes """
        if race:
            self.race = race()
        else:
            self.race = self.race_options[randrange(0, len(self.race_options))]()

    def set_base_values(self) -> None:
        """ Basic behavior required by character classes """
        self.experience = 0
        self.inventory = Inventory()

        self.speed = self.race.speed
        self.charisma = self.race.charisma
        self.strength = self.race.strength
        self.endurance = self.race.endurance
        self.intelligence = self.race.intelligence

        self.weapon = self.race.starting_weapon()
        self.armor = self.race.starting_armor()
        self.health = self.endurance * 10
        self.max_health = self.health

    def save_data(self) -> dict:
        return {
            "name": self.name,
            "race": str(self.race),
            "experience": self.experience,
            "inventory": self.inventory.save_data(),
            "speed": self.speed,
            "charisma": self.charisma,
            "strength": self.strength,
            "endurance": self.endurance,
            "intelligence": self.intelligence,
            "weapon": str(self.weapon),
            "armor": str(self.armor),
            "health": self.health,
            "max_health": self.max_health,
        }


    #
    # Combat and HP Functions
    #
    def increase_HP(self, amount) -> int:
        """ Increase health up to its starting value """
        self.health = self.health + amount 
        return self.health

    def increase_max_HP(self, amount) -> int:
        """ Increase player's maximum health """
        self.max_health = self.max_health + amount
        return self.max_health

    def take_damage(self, amount) -> int:
        """ Take damage from a source other than a `dealDamage` attack """
        self.health = self.health - amount
        return self.health

    def deal_damage(self, target) -> int:
        """ Deal attack damage to target's health, return damage dealt """
        # TODO: get a better damage calculation for this

        if self.weapon is None: # unarmed
            damage = 5 * self.strength
        else:
            # multiply strength by a number between 1 & weapon-damage
            damage = self.strength * randint(1, self.weapon.damage)

        # do not reduce damage below zero
        if damage >= target.health:
            damage = target.health

        # subtract damage from target health
        target.health = target.health - damage
        return damage

    def is_alive(self) -> int:
        """ Return boolean based on health value """
        return self.health > 0

    #
    # Equipment and Inventory Functions
    #
    def change_capacity(self, new_capacity) -> None:
        """ Increase capacity based on strength or other modifiers """
        self.inventory.capacity = new_capacity

    def equip(self, item) -> None:
        """ Add item into armor or weapon slot """
        if item.type == "armor":
            self.armor = item
        elif item.type == "weapon":
            self.weapon = item

    def equip_from_inventory(self, placement) -> None:
        """ Equip then delete item from location in inventory """
        self.equip(self.inventory[placement])
        self.inventory.add(placement)

    def unequip(self, item_type) -> None:
        """ Remove armor or weapon, adding it to inventory """
        if item_type == "armor":
            self.inventory.add(self.armor)
            self.armor = None
        elif item_type == "weapon":
            self.inventory.add(self.weapon)
            self.weapon = None

    def discard_equipment(self, item_type) -> None:
        """ Drop equipped weapon or armor """
        if item_type == "armor":
            self.inventory.dropItem(self.armor)
            self.armor = None
        elif item_type == "weapon":
            self.inventory.dropItem(self.weapon)
            self.weapon = None

    def setComms(self, personality: Personality) -> None:
        """ Set up comms based on NPC type and disposition """
        if not personality:
            personality = Unfriendly
        self.personality = personality

        comms = self.comms_options[randrange(0, len(self.comms_options))]
        if comms:
            self.comms = comms(personality) # Initiate communication class with personality

        # TODO: make all actions accept the same parameters
        if personality == Hostile:
            self.next_action = self.comms.taunt
        if personality == Friendly:
            self.next_action = self.comms.greeting

class NPC(Character):
    """ 
    Base class for all NPCs.
    May be used directly for Low Common Humans.
    Otherwise, must be inherited to create new NPC types.
    """

    name_options = [ 
        "Aaron", "Bob", "Charlie", "David", "Eddie", "Frank", "George", 
        "Hannah","Isa", "Julie", "Kharma", "Keaton", "Kali", "Kasen", 
        "Kevin", "Koen", "Leanna", "Mildred", "Naomi", "Oliver", "Percy", 
        "Quinton", "Ralphie", "Stevie", "Tom", "Ulysses", "Victor", "Wade", 
        "Xavier", "Yolanda", "Zach"
    ]

    # next_action is a function queued for the next time
    # the NPC is prompted to act, allowing an NPC to wait
    # for an appropriate time before calling the function
    # Example: This may be used when a character flees,
    # so when the NPC is seen next it will taunt or attack
    next_action = None

    def act(self, active_player):
        if self.next_action:
            action = self.next_action
            self.last_action = action
            self.next_action = None  # Clear next action before executing
            return action(active_player)
        return None
