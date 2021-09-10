from communication import Communication

# This file contains both Fowl and FowlSapient communication classes

class Fowl(Communication):

    def greeting(self):
        return self.randomizer([
            "Quack",
            "Chirp",
            "Screech",
            "Squack",
        ])

    def challenge(self):
        return None

    def taunt(self):
        return None

    def announce_presense(self):
        return None

    def question_presense(self):
        return None

    def haggle_lower(self):
        return None

    def haggle_higher(self):
        return None

    def flatter(self):
        return None

    def admire(self):
        return None

    def admonish(self):
        return None

    def encourage(self):
        return None

   


class FowlSapient(Communication):

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
