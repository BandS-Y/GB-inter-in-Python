import random

def any_rnd(in_list):
    if len(in_list) > 0:
        return random.choice(in_list)
    else:
        return None

print(any_rnd([]))