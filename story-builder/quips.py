from random import randrange

def taunt_character_fled(name=None):
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
