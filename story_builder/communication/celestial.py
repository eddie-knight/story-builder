from .communication import Communication

class Celestial(Communication):

    def greeting(self):
        return self.randomizer([
            "Welcome! I am pleased to make your aqcuaintance!",
            "Thine presence is a blessing.",
            "Nature rejoices at thine arrival.",

        ])

    def challenge(self):
        return self.randomizer([
            "Dosth thou truly wish that we come to blows?",
            "Thine weapon seems ill-equipped for a battle against mine self.",
            "Thine intellect stat must be wanting, if thou believes a victory is possible.",
        ])

    def taunt(self):
        return self.randomizer([
            "Thou art a Silly-Ninny!",
            "Dosth thine bovine knowesth that thou art trying to poke other people?",
            "Thine Mother lays with swine!",

        ])

    def announce_presense(self):
        return self.randomizer([
            "Harken and Rejoice mine fellows! I have arrived!",
            "It is I! Let us begin!",
            "With mine presence, surely the tides have changed!"
        ])

    def question_presense(self):
        return self.randomizer([
            "Why hast thou darkened my door-step once again?",
            "Have thine lost thine way?",
            "Where fore art thou heading?",

        ])

    def haggle_lower(self):
        return self.randomizer([
            "Doesth mine ears decieve me? I believe thou may aim for the stars. Even so, might that we bring this discussion back to earth.",
            "I do believe that we can find a more reasonable middle-ground.",
            "Would thou consider a more reasonable offer?",

        ])

    def haggle_higher(self):
        return self.randomizer([
            "Mine good fellow, I do hope that we can bring this up into a more cordial numerical area."
            "I do believe thou hast a false understanding of the value this item represents.",
            "Let us review and recalculate. This item appears to have a more substantial value.",
        ])

    def flatter(self):
        return self.randomizer([
            "I am astonished by thine brilliance!",
            "Never have I seen such exceptional skill!",
            "Thou art truly gifted!",
        ])

    def admire(self):
        return self.randomizer([
            "Thou art the light of my day!",
            "I am honored by your presence.",
            "Is there anyone greater than thou?",
        ])

    def admonish(self):
        return self.randomizer([
            "Mine fine fellow, thou hast made quite the blunder",
            "Doesth mine ears decieve me?  Hast thou truly failed so miserably?",
            "Why hast thou returned empty handed?",
        ])

    def encourage(self):
        return self.randomizer([
            "I doth belive that thou shalt be capable of accomplishing this task!",
            "Thou art sturdy and extremly capable.  I am positive thou shall succeed!",
            "Thine prowess confounds the weak!  Go forth and conquere!",
        ])

    