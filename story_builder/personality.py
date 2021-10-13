from abc import ABC, abstractmethod


class Personality(ABC):
    # TODO: change this to disposition
    # TODO: if we don't have any other functionality here, we might not need this
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
