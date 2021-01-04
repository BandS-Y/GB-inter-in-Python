import os


def create_dir():
    name = "dir_"
    dir_exist = os.listdir(path=".")
    for count in range(1, 10):
        name_full = name+str(count)
        new_path = os.path.join(os.getcwd(), name_full)
        if name_full not in dir_exist:
            os.mkdir(new_path)
        else:
            print("directory already exists")


def dell_dir():
    name = "dir_"
    dir_exist = os.listdir(path=".")
    for count in range(1, 10):
        name_full = name+str(count)
        new_path = os.path.join(os.getcwd(), name_full)
        if name_full in dir_exist:
            os.rmdir(new_path)
        else:
            print("directory is not exists")


def check_dir():
    name = "dir_"
    dir_exist = os.listdir(path=".")
    for count in range(1, 10):
        name_full = name+str(count)
        if name_full in dir_exist:
            print("directory exists")
        else:
            print("directory is not exists")