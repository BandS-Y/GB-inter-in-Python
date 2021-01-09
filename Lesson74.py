def num_pow(num):
    try:
        if num == 13:
            raise Exception("Число = 13")
    except:
        print("Ошибка, однако. 13, однако")
    else:
        num = num ** 2
    finally:
        return num


numb = int(input("введите число: "))
print(num_pow(numb))