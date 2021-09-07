from random import randrange

from communication import Communication


class Common(Communication):

    def greeting(self):
        return None

    def challenge(self):
        return None

    def taunt(self):
        return None

    def taunt_character_previously_fled(self, name=None):
        if name:
            options = [
                f"You ran away last time I saw you, {name}!",
                f"{name}, you're a weak little chicken.",
                f"Gonna run away again, {name}?"
            ]
        else:
            options = [
                f"You ran away last time I saw you!",
                f"You're a weak little chicken.",
                f"Gonna run away again?"
            ]
        return options[randrange(0, len[options])]


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

    def flatter(self):
        return None
