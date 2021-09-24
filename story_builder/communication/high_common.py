from .communication import Communication

class HighCommon(Communication):

    def greeting(self):
        return self.randomizer([
            "Greetings Traveler. I am pleased to make your aquaintance.",
            "Good tidings Adventurer.  I hope this day finds you well.",
            "Hello there! How might I be of service?",
        ])

    def challenge(self):
        return self.randomizer([
            "How dare you (sir/madame)! This shall not be tolerated!",
            "You have crossed the line.  I shall need to put you in your place!",
            "Art thou ready for an ASS-WHOOPING?",
        ])

    def taunt(self):
        return self.randomizer([
            "You must be a bumpkin!",
            "Have at thee, weakling!",
            "Let me speak, so thou might comprehend.  You're weak.  I'll whip your behind!",
        ])

    def announce_presense(self):
        return self.randomizer([
            "Hail, I have arrived!",
            "Sound the trumpets! I.... am here!",
            "Yep.  I'm here.  What about it?",
        ])

    def question_presense(self):
        return self.randomizer([
            "Good sir/madame, why hast thou come?",
            "Is there a valid reason for your return?",
            "Hast thou accomplished thine task so soon?",
        ])

    def haggle_lower(self):
        return self.randomizer([
            "I do believe you have aimed your shot too high, my friend.",
            "I would of course love to give you too much for this item, but I feel it would burden you greatly.",
            "Kindest Sir/Madame, thou..hmph... forget that.  Dude, your asking too much!",
        ])

    def haggle_higher(self):
        return self.randomizer([
            "My friend, I feel like we should aim our bow a little higher.",
            "I'm not aware of this ever selling for such a low value.",
            "Even thou my heart tells me to take your offer, my wallet is screaming that I should not.",
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
            "I am astounded by your skills!",
        ])

    def admonish(self):
        return self.randomizer([
            "I do not believe you fully understand the situation.",
            "I believe you must be mistaken.",
            "You have not fully researched this scenario.",
        ])

    def encourage(self):
        return self.randomizer([
            "Verily, thou canst accomplish this task!",
            "Thou art worthy!",
            "Thine attributes... Sheesh, I'm tired of talking like that.  You've got this!",
        ])

   