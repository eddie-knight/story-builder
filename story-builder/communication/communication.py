from abc import ABC, abstractmethod

class Communication(ABC):

    def __init__(self, personality):
        self.personality = personality

    def friendly(self):
        return self.personality.lower() == "friendly"

    def unfriendly(self):
        return self.personality.lower() == "unfriendly"

    def hostile(self):
        return self.personality.lower() == "hostile"

    def fake(self):
        return self.personality.lower() == "fake"

    @abstractmethod
    def greeting(self):
        pass

    @abstractmethod
    def challenge(self):
        pass

    @abstractmethod
    def taunt(self):
        pass

    @abstractmethod
    def announce_presense(self):
        pass

    @abstractmethod
    def question_presense(self):
        pass

    @abstractmethod
    def haggle_lower(self):
        pass

    @abstractmethod
    def haggle_higher(self):
        pass

    @abstractmethod
    def flatter(self):
        pass

    @abstractmethod
    def admire(self):
        pass

    @abstractmethod
    def admonish(self):
        pass

    @abstractmethod
    def encourage(self):
        pass

    @abstractmethod
    def flatter(self):
        pass
