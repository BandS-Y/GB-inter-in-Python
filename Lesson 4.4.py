plaer = {"name": "Kola",
         "health": 100,
         "damage": 20,
         "armor": 1.2}

enemy = {"name": "Korbun",
         "health": 100,
         "damage": 20,
         "armor": 1.2}

def armor_down(armor, damage):
    return armor / damage

def attack(person1, person2):
    new_damage = armor_down(person1["armor"], person2["damage"])
    person1["health"] =  person1["health"] - new_damage

print(plaer)
attack(plaer, enemy)
print(plaer)