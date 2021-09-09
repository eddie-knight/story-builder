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
        return self.randomizer([
            "Season's TWEETINGS to you!",
            "Its TWEET to meet you!",

        ])

    def challenge(self):
        return self.randomizer([
            "Are these BIRD PUNS flying right over your head?",
            "TOUCAN play at that game!",
            "You are driving me QUACKERS!",
            "What the FLOCK do you think you are doing?!",
        ])

    def taunt(self):
        return self.randomizer([
            "I love it when you talk BIRDY to me!",
            "BIRD on the street, is you hit like a fairy!",
            "Let's do this mother PUFFER!",
            "Flock off, pretty bird!",
            "BEAK-a-Boo! You missed me!",
            "Looks like you've been through the WINGER!",
        ])

    def announce_presense(self):
        return self.randomizer([
            "HOOOO's here?  I'm Here!!",
        ])

    def question_presense(self):
        return self.randomizer([
            "Well, this is HAWKWARD... Why are you here?",
            "Why the FLOCK did you come back?",
        ])

    def haggle_lower(self):
        return self.randomizer([
            "You PELICAN'T be serious, let's try that again!",
            "You PELICAN do better than that!",
            "TOUCAN play at this game.",
        ])

    def haggle_higher(self):
        return self.randomizer([
            "You PELICAN'T be serious, let's try that again!",
            "You PELICAN do better than that!",
            "TOUCAN play at this game.",
        ])

    def flatter(self):
        return self.randomizer([
            "I think you are DOVELY.",
            "Aww, you're so tweet! Thank you!",
        ])

    def admire(self):
        return self.randomizer([
            "Here's a TOUCAN of my appreciation.",
            "You are really OWLSOME!",
        ])

    def admonish(self):
        return self.randomizer([
            "I BIRD you the first time!",
            "What the DUCK were you thinking?!",
            "I suspect FOWL play!",
            "Just CROW away and leave me alone already.",
            "Owl always love you!",
        ])

    def encourage(self):
        return self.randomizer([
            "TOUCAN do it! All night long!",
            "Wow! You are DUCKING awesome!",
            "Good luck! I'm HOOTING for you!",
        ])

    
