def multi(digit):
    mult_sum = 0
    for mult in range(1, digit):
        if digit % mult == 0:
            mult_sum += mult
    return mult_sum


for digit in range(100000):
    if digit % 1000 == 0:
        print(digit)
    a = multi(digit)
    b = multi(a)
    if digit == b and a <= b:
        print(a, b)

print("finish")