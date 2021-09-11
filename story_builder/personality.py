from abc import ABC, abstractmethod


class Personality(ABC):
    def __str__(self):
        return self.__class__.__name__

class Unfriendly(Personality):
    pass


class Friendly(Personality):
    pass


class Hostile(Personality):
    pass


class Fake(Personality):
    pass
