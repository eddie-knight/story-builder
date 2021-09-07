from abc import ABC, abstractmethod


class Personality(ABC):
    # next_action is a function queued for the next time
    # the NPC is prompted to act, allowing an NPC to wait
    # for an appropriate time before calling the function
    # Example: This may be used when a character flees,
    # so when the NPC is seen next it will taunt or attack
    next_action = None

    def __str__(self):
        return self.__class__.__name__

    def act(self):
        if self.next_action:
            self.last_action = self.next_action
            self.next_action = None # Clear next action before executing, 
            return self.last_action()
        return "It isn't clear whether you've been noticed"

    def prepare(self, function):
        self.next_action = function

class Unfriendly(Personality):
    pass


class Friendly(Personality):
    pass


class Hostile(Personality):
    pass


class Fake(Personality):
    pass
