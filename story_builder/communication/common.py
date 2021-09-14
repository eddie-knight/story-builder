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
                f"{name}, you're a weak little chicken shit.",
                f"Gonna run away again, {name}?"
            ]
        else:
            options = [
                f"You ran away last time I saw you!",
                f"You're a weak little chicken shit.",
                f"Gonna run away again, bitch?"
            ]
        return self.randomizer(options)


    def announce_presense(self):
        return self.randomizer([
            "Hidee-Hoe y'all!",
            "Well, I'm here, what all the hubbub,bub?",
            "Ok, let's get this thing started",
        ])

    def question_presense(self):
        return self.randomizer([
            "What brings you here?",
            "Why on earth did you come here?",
            "Seriously, why are you here?",
        ])

    def haggle_lower(self):
        return self.randomizer([
            "Yaaa..... I hear what your saying.... but I believe we can make this more reasonable.",
            "Indeed that is an item of value, but not when it's above my available budget. Is there wiggle-room on that price?",
            "Yeah... No.  Let's bring that down into a resonable bargaining range."
        ])

    def haggle_higher(self):
        return self.randomizer([
            "I understand you might not have the dough, but this is worth more than that.",
            "Let's see if we can't get that offer a little higher?",
            "Whadaya say? Let's talk some rational offers?",
        ])

    def flatter(self):
        return self.randomizer([
            "I do believe you are the best I have ever seen!",
            "Wow, you are just astonashing!",
            "I couldn't have done it better myself.  Well done!",
        ])

    def admire(self):
        return self.randomizer([
            "I am astounded by your abilities!",
            "I truly wish I could do what you can!",
            "You are just amazing!",
        ])

    def admonish(self):
        return self.randomizer([
            "I can't believe you just did that!",
            "What are on EARTH were you thinking?!",
            "Please tell me that you're not serious?",
        ])

    def encourage(self):
        return self.randomizer([
            "You've got this!",
            "Don't worry, we are in this together! Still, I'm gonna let you go first.",
            "Good luck! We are all behind you on this!..... Way behind you.",
        ])

    
