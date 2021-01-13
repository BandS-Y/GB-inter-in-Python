import os
import shutil
import datetime


def create_file(name, text=None):
    with open(name, "w", encoding="utf-8") as f:
        if text:
            f.write(text)


def create_folder(name):
    try:
        os.mkdir(name)
    except FileExistsError:
        print("Такая папка уже существует")


def list_dir(folder_only=False):
    result = os.listdir()
    if folder_only:
        result = [f for f in result if os.path.isdir(f)]
    print(result)


def delete_file(name):
    if os.path.isdir(name):
        os.rmdir(name)
    else:
        os.remove(name)


def copy_file(name, new_name):
    if os.path.isdir(name):
        try:
            shutil.copytree(name, new_name)
        except FileExistsError:
            print("Такая папка уже существует")
    else:
        try:
            shutil.copy(name, new_name)
        except FileExistsError:
            print("Такой файл уже существует")


def save_info(messadge):
    current_time = datetime.datetime.now()
    result = f'{current_time} - {messadge}'
    print(result)
    with open("log.txt", "a", encoding="utf-8") as f:
        f.write(result + '\n')
