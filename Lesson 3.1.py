from random import randint
print("Загадай число от 0 до 100. Я попробую его угадать.\n"
      "Если загаданное число больше введи >, если меньше <, если я угадал = ")
user_input = input("Как загадаешь нажми введи пробел")
comp_num = randint(0, 100)
max_num = 100
min_num = 0
count = 0
while user_input != "=":
    print(min_num, max_num)
    comp_num = randint(min_num, max_num)
    count += 1
    print("Это число: " + str(comp_num) + "?")
    user_input = input()
    if user_input == ">":
        min_num = comp_num+1
    elif user_input == "<":
        max_num = comp_num-1
print("Ура! я угадал число! " + str(comp_num) + " за " + str(count) + " раз")