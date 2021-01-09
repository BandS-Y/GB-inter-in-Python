import json
import pickle

my_favourite_group = {
'name': 'Г.М.О.',
'tracks': ['Последний месяц осени', 'Шапито'],
'Albums': [{'name': 'Делать панк-рок', 'year': 2016}, {'name': 'Шапито', 'year': 2014}]}

with open("favourit_group.picle", "wb") as f:
    pickle.dump(my_favourite_group, f)

with open("favourit_group.json", "w", encoding="utf-8") as f:
    json.dump(my_favourite_group, f)

print("done write")

with open("favourit_group.json", "r", encoding="utf-8") as f:
    my_f_gr = json.load(f)
    print(my_f_gr)

with open("favourit_group.picle", "rb") as f:
    my_f_gr = pickle.load(f)
    print(my_f_gr)

print("loading done")