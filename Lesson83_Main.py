import sys

from Lesson82_Core import create_file, create_folder, list_dir, delete_file, copy_file, save_info

save_info ("Старт")
command = sys.argv[1]

if command == "list":
    list_dir()
elif command == 'create_file':
    try:
        name = sys.argv[2]
    except IndexError:
        print("необходимо задать имя файла")
    else:
        create_file(name)
elif command == 'create_folder':
    try:
        name = sys.argv[2]
    except IndexError:
        print("необходимо задать имя файла")
    else:
        create_folder(name)
elif command == 'delete':
    try:
        name = sys.argv[2]
    except IndexError:
        print("необходимо задать имя файла")
    else:
        delete_file(name)
elif command == 'copy':
    try:
        name = sys.argv[2]
        new_name = sys.argv[3]
    except IndexError:
        print("необходимо задать имя файла который копируют и имя файла куда копируют")
    else:
        copy_file(name, new_name)
elif command == "help":
    print("           Помощь ")
    print("         list - список файлов")
    print('  create_file - создать файл')
    print('create_folder - создать папку')
    print('       delete - удалить папку или файл')
    print('         copy - скопировать папку или файл')


save_info ("Конец")