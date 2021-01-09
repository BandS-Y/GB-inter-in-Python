list_1 = ["tomato", "apple", "carrot", "potato", "raspbery"]
list_2 = ["raspbery", "bluebarry", "carrot", "apple", "pine"]

list_3 = [fruit for fruit in list_1 if fruit in list_2]
print(list_3)