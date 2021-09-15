from .communication import Communication

class HighCommon(Communication):

    def greeting(self):
        return self.randomizer([
            "Greetings Traveler. I am pleased to make your aquaintance.",
            "Good tidings Adventurer.  I hope this day finds you well.",
        ])

    def challenge(self):
        return self.randomizer([
            "How dare you (sir/madame)! This shall not be tolerated!",
            "You have crossed the line.  I shall need to put you in your place!"
        ])

    def taunt(self):
        return self.randomizer([
            "You must be a bumpkin!",
            "Have at thee, weakling!",
        ])

    def announce_presense(self):
        return self.randomizer([
            "Hail, I have arrived!",
        ])

    def question_presense(self):
        return self.randomizer([
            "Good sir/madame, why hast thou come?"
        ])

    def haggle_lower(self):
        return self.randomizer([
            "I do believe you have aimed your shot too high, my friend.",
        ])

    def haggle_higher(self):
        return self.randomizer([
            "My friend, I feel like we should aim our bow a little higher.",
        ])

    def flatter(self):
        return self.randomizer([
            "You must have the heart of an angel!",
            "Thou must be of noble birth and rearing!",
            "Clearly you are well educated.",
        ])

    def admire(self):
        return self.randomizer([
            "I cannot fathom the depths of your mind!",
            "You have won my admiration, sir/madame.",
        ])

    def admonish(self):
        return self.randomizer([
            "I do not believe you fully understand the situation.",
            "I believe you must be mistaken.",
            "You have not fully researched this scenario.",
        ])

    def encourage(self):
        return self.randomizer([
            "Verily, thou canst accomplish this task!"
        ])

   