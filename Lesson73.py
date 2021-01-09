import random
import math

numbers = [random.randint(-50, 99) for num in range(1, 30)]
print(numbers)

def num_proc (numbers):
    result = []
    for num in numbers:
        result.append(round(math.sqrt(num), 2) if num > 0 else num)
    return result

print(num_proc(numbers))
