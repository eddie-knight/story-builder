from communication import Communication

# This file contains both Canine and CanineSapient communication classes

class Canine(Communication):

    def greeting(self):
        return self.randomizer([
            "Ruff!",
            "Rrrrr?",
            "bark",
        ])

    def challenge(self):
        return self.randomizer([])

    def taunt(self):
        return self.randomizer([
            "Hey, you actually came back?!",
        ])

    def announce_presense(self):
        return self.randomizer([
            "I'm back baby!",
        ])

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
        return self.randomizer([
            "You look sexy",
        ])


class CanineSapient(Communication):

    def greeting(self):
        return self.randomizer([])

    def challenge(self):
        return self.randomizer([])

    def taunt(self):
        return self.randomizer([])

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
