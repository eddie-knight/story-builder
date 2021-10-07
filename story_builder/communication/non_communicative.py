from .communication import Communication


class NonCommunicative(Communication):
    """ This class should return self.randomizer([]) for all methods """

    def greeting(self):
        return self.randomizer([
            "(Their eyes widen and brighten with pleasant greeting!)",
        ])
        
    def challenge(self):
        return self.randomizer([
            "(Their brow furrows, and eyes narrow.  Ready for a fight.)",
        ])

    def taunt(self):
        return self.randomizer([
            "(A mischivious glint appears in their eye as their weapon appears)",
        ])

    def announce_presense(self):
        return self.randomizer([
            "(They stomp up and BELLOW loudly into the sky!)",
        ])

    def question_presense(self):
        return self.randomizer([
            "(A questioning look appears on their face as you approach)",
        ])

    def haggle_lower(self):
        return self.randomizer([
            "(Their brow furrows at your offer. You just know you aimed too high.)",
        ])

    def haggle_higher(self):
        return self.randomizer([
            "(Their brow raises with amusement at your offer. Your bid must be too low.)",
        ])

    def flatter(self):
        return self.randomizer([
            "(A look of gratitude shines on their face.)",
        ])

    def admire(self):
        return self.randomizer([
            "(A look of astonished wonder reflects in their gaze!)",
        ])

    def admonish(self):
        return self.randomizer([
            "(As their brow furrows in disappointment, you just know: You Fucked up.)",
        ])

    def encourage(self):
        return self.randomizer([
            "(The look of trust and support they give you is all the encouragement you need!)",
        ])

