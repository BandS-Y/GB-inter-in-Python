plaer = {"name" : "Kola",
         "health" : 100,
         "damage" : 20}

enemy = {"name" : "Korbun",
         "health" : 100,
         "damage" : 20}

def attack(person1, person2):
    person1["health"] =  person1["health"] - person2["damage"]

print(plaer)
attack(plaer, enemy)
print(plaer)