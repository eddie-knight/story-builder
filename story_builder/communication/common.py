from random import randrange

from .communication import Communication


class Common(Communication):

    def greeting(self):
        return self.randomizer([])

    def challenge(self):
        return self.randomizer([])

    def taunt(self):
        return self.randomizer([])

    def taunt_character_previously_fled(self, name=None):
        if name:
            options = [
                f"You ran away last time I saw you, {name}!",
                f"{name}, you're a weak little chicken.",
                f"Gonna run away again, {name}?"
            ]
        else:
            options = [
                f"You ran away last time I saw you!",
                f"You're a weak little chicken.",
                f"Gonna run away again?"
            ]
        return self.randomizer(options)


    def announce_presense(self):
        return self.randomizer([])

    def question_presense(self):
        return self.randomizer([])

    def haggle_lower(self):
        return self.randomizer([])

    def haggle_higher(self):
        return self.randomizer([])

    def flatter(self):
        return self.randomizer([])

    def admire(self):
        return self.randomizer([])

    def admonish(self):
        return self.randomizer([])

    def encourage(self):
        return self.randomizer([])

    def flatter(self):
        return self.randomizer([])
