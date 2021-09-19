import importlib

def get_class(class_unformatted):
    # TODO: DRY- this is being used in game_state also
    preformat = class_unformatted.split("'")[1].split(".")
    module_name = ".".join(preformat[0:-1])
    class_name = preformat[-1]
    module = importlib.import_module(module_name)
    return getattr(module, class_name)

def load_character(type, data):
    character = type()
    character.name = data["name"]
    character.race = data["race"]
    # character.personality = data["personality"] # TODO
    character.experience = data["experience"]
    character.speed = data["speed"]
    character.charisma = data["charisma"]
    character.strength = data["strength"]
    character.endurance = data["endurance"]
    character.intelligence = data["intelligence"]
    character.weapon = data["weapon"]
    character.armor = data["armor"]
    character.health = data["health"]
    character.max_health = data["max_health"]
    character.inventory.capacity = data["inventory"]["capacity"]
    for item in data["inventory"]["contents"]:
        # item[0] is name, item[1] is class
        item_class = get_class(item[1])
        character.inventory.add(item_class(item[0]))
    return character