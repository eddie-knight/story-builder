from random import randrange, randint
from story_builder.personality import Unfriendly

from .races import *
from .communication.low_common import LowCommon

class Inventory(list):
    """ Custom list object to enable adding and dropping items """
    capacity = 2
    recently_dropped_items = [] # clear this when changing areas!

    def add(self, item):
        """ Append if below capacity """
        if self.capacity > len(self):
            self.append(item)
            return True # success
        return False # fail

    def drop(self, position):
        """ soft delete an item """
        self.drop_item(self[position])
        del self[position]

    def drop_item(self, item):
        self.recently_dropped_items.append(item)
    
    def clear_dropped(self):
        self.recently_dropped_items = []


class Character:
    """ Used for player character, and as a base for other classes """

    # NPC classes should harness these options
    race_options = [Human]
    name_options = [None]
    comms_options = [LowCommon]

    def __init__(self, name=None, race=None, personality=None):
        self.setName(name)
        self.setRace(race)
        self.setComms(personality)
        self.set_base_values()
    
    def __str__(self):
        return str(self.race)

    def setName(self, name):
        """ Basic bahavior, may be overridden in child classes """
        if name:
            self.name = name
        else:
            self.name = self.name_options[randrange(0, len(self.name_options))]

    def setRace(self, race):
        """ Basic bahavior, may be overridden in child classes """
        if race:
            self.race = race()
        else:
            self.race = self.race_options[randrange(0, len(self.race_options))]()

    def setComms(self, personality):
        if not personality:
            personality = Unfriendly
        comms = self.comms_options[randrange(0, len(self.comms_options))]
        if comms:
            self.comms = comms(personality) # Initiate communication class with personality

    def set_base_values(self):
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


    #
    # Combat and HP Functions
    #
    def increase_HP(self, amount):
        """ Increase health up to its starting value """
        self.health = self.health + amount 

    def increase_max_HP(self, amount):
        """ Increase player's maximum health """
        self.max_health = self.max_health + amount

    def take_damage(self, amount):
        """ Take damage from a source other than a `dealDamage` attack """
        self.health = self.health - amount

    def deal_damage(self, target):
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

    def is_alive(self):
        """ Return boolean based on health value """
        return self.health > 0

    #
    # Equipment and Inventory Functions
    #
    def change_capacity(self, new_capacity):
        """ Increase capacity based on strength or other modifiers """
        self.inventory.capacity = new_capacity

    def equip(self, item):
        """ Add item into armor or weapon slot """
        if item.type == "armor":
            self.armor = item
        elif item.type == "weapon":
            self.weapon = item

    def equip_from_inventory(self, placement):
        """ Equip then delete item from location in inventory """
        self.equip(self.inventory[placement])
        self.inventory.add(placement)

    def unequip(self, item_type):
        """ Remove armor or weapon, adding it to inventory """
        if item_type == "armor":
            self.inventory.add(self.armor)
            self.armor = None
        elif item_type == "weapon":
            self.inventory.add(self.weapon)
            self.weapon = None

    def discard_equipment(self, item_type):    
        """ Drop equipped weapon or armor """
        if item_type == "armor":
            self.inventory.dropItem(self.armor)
            self.armor = None
        elif item_type == "weapon":
            self.inventory.dropItem(self.weapon)
            self.weapon = None


class NPC(Character):
    """ Base class for all NPCs """

    race_options = [Human, Giant, Orc]
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

    def act(self):
        if self.next_action:
            self.last_action = self.next_action
            self.next_action = None # Clear next action before executing, 
            return self.last_action()
        return "It isn't clear whether you've been noticed"


class Monster(NPC):
    """ NPC with custom races and MonsterWeapon """

    race_options = [Wolf, Horse, Eagle, Crow, Hawk]
    name_options = ["an unnamed beast"]

