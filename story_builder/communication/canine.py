from .communication import Communication

# This file contains both Canine and CanineSapient communication classes

class Canine(Communication):

    def greeting(self):
        return self.randomizer([
            "Ruff!",
            "bark",
        ])
    def challenge(self):
        return None

    def taunt(self):
        return None
    def announce_presense(self):
        return None

    def question_presense(self):
        return [
            "Rrrrr?",
        ]
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

    def flatter(self):
        return None

class CanineSapient(Communication):

    def greeting(self):
        return self.randomizer([
            "It's Grrrrrrrrreat to MEAT you",
            "PLAY? I mean, did you need something?",
            "You look like you've had a RUFF day.",
            "What? You think a talking Dog is a little far-FETCHED?",
        ])
    def challenge(self):
        return self.randomizer([
            "I'm about to make you my BITCH!",
        ])
        
    def taunt(self):
        return self.randomizer([
            "You seem a little RUFF around the edges.",
            "You seem like the type to just ROLL-OVER in a fight.",
        ])

    def announce_presense(self):
        return self.randomizer([
            "Who's ready to PAW-TY?",
        ])

    def question_presense(self):
        return self.randomizer([
            "I'm not not MUTTS about you being here.",
        ])

    def haggle_lower(self):
        return self.randomizer([
            "Seems like you threw the ball over the fence with that offer!",
        ])

    def haggle_higher(self):
        return self.randomizer([
            "You throw like a child, toss me a better ball... I mean offer!",
        ])

    def flatter(self):
        return self.randomizer([
            "Now that hits the SPOT!",
            "Aww, you look quite FETCHING!",
        ])

    def admire(self):
        return self.randomizer([
            "I will love you FUR-ever!",
        ])

    def admonish(self):
        return self.randomizer([
            "I wish you would quit HOUNDING me!",
        ])

    def encourage(self):
        return self.randomizer([
            "As long as you have a Dog by your side, anything is Paw-sible!"
        ])

    def flatter(self):
        return self.randomizer([
            "Wow, I think you are PAW-fect!"
        ])
