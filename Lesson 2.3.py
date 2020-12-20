my_list = [2, 2, 5, 12, 8, 2, 12, 3, 7, 3]
my_set = set(my_list)
fin_list = []
for element in my_set:
    if my_list.count(element) == 1:
        fin_list.append(element)
print(fin_list)
