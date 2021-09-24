from .communication import Communication

# This file contains both Canine and CanineSapient communication classes

class Canine(Communication):

    def greeting(self):
        return self.randomizer([
            "Ruff!",
            "bark",
        ])
    def challenge(self): [
        "GRRRRRRRRRRRR...."
    ]
    def taunt(self):
        return self.challenge()
    def announce_presense(self):
        return self.greeting()

    def question_presense(self):
        return [
            "Rrrrr?",
        ]
    def haggle_lower(self):
        return self.challenge()

    def haggle_higher(self):
        return self.challenge()

    def flatter(self):
        return self.greeting()

    def admire(self):
        return self.greeting()

    def admonish(self):
        return self.challenge()

    def encourage(self):
        return self.greeting()

    

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
            "I'm about to RUFF you up!",
            "Careful, my bite is definitly worse than my Bark!",
        ])
        
    def taunt(self):
        return self.randomizer([
            "You seem a little RUFF around the edges.",
            "You seem like the type to just ROLL-OVER in a fight.",
            "Would you like your belly rubbed, or will you fight?",
        ])

    def announce_presense(self):
        return self.randomizer([
            "Who's ready to PAW-TY?",
            "Well, I'm here.  What's all this yapping?",
            "Are we ready to do this?",
        ])

    def question_presense(self):
        return self.randomizer([
            "I'm not not MUTTS about you being here.",
            "Why have you returned stickless?",
            "How can I help you?",
        ])

    def haggle_lower(self):
        return self.randomizer([
            "Seems like you threw the ball over the fence with that offer!",
            "Looks like we need to dig this hole a little deeper.",
            "I'd have no bones left if we went that high!",
        ])

    def haggle_higher(self):
        return self.randomizer([
            "You throw like a child, toss me a better ball... I mean offer!",
            "Let's see you can make a more fetching offer than that.",
            "You kind of buried that offer.  Let's see if we can dig it up.",
        ])

    def flatter(self):
        return self.randomizer([
            "Now that hits the SPOT!",
            "Aww, you look quite FETCHING!",
            "Wow, I think you are PAW-fect!",
        ])

    def admire(self):
        return self.randomizer([
            "I will love you FUR-ever!",
            "That was just Amazing!",
            "Is that truly what you are capable of? Astonishing!",
        ])

    def admonish(self):
        return self.randomizer([
            "I wish you would quit HOUNDING me!",
            "Grrrrrrr.... That was not a wise choice.",
            "I think you should try again.  And do better this time.",
        ])

    def encourage(self):
        return self.randomizer([
            "As long as you have a Dog by your side, anything is Paw-sible!"
            "You are amazing!  I'm sure you'll have no trouble with this!",
            "You can do it!"
        ])