from .communication import Communication

class Celestial(Communication):

    def greeting(self):
        return self.randomizer([
            "Welcome! I am pleased to make your aqcuaintance!",
        ])

    def challenge(self):
        return self.randomizer([
            "Dosth thou truly wish that we come to blows?",
        ])

    def taunt(self):
        return self.randomizer([
            "Thou art a Silly-Ninny!",
        ])

    def announce_presense(self):
        return self.randomizer([
            "Harken and Rejoice mine fellows! I have arrived! "
        ])

    def question_presense(self):
        return self.randomizer([
            "Why hast thou darkened my door-step once again?",
        ])

    def haggle_lower(self):
        return self.randomizer([
            "Dosth mine ears decieve me? I believe thou may aim for the stars. Might that we bring this discussion back to earth.",
        ])

    def haggle_higher(self):
        return self.randomizer([
            "Mine good fellow, I do hope that we can bring this up into a more cordial numerical area."
        ])

    def flatter(self):
        return self.randomizer([
            "I am astonished by thine brilliance!",
        ])

    def admire(self):
        return self.randomizer([
            "Thou art the light of my day!"
        ])

    def admonish(self):
        return self.randomizer([
            "Mine fine fellow, thou hast made quite the blunder",
        ])

    def encourage(self):
        return self.randomizer([
            "I doth belive that thou shalt be capable of accomplishing this task!",
        ])

    