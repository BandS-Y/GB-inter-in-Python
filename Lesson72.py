import random

numbers = [random.randint(-99,99) for num in range(1, 30)]
print(numbers)

numbers_1 = [num for num in numbers if num > 0 and num % 3 == 0 and num % 4 != 0]
print(numbers_1)
