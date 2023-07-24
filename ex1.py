# ✔ Напишите функцию, которая принимает на вход строку — абсолютный путь до файла.
# Функция возвращает кортеж из трёх элементов: путь, имя файла, расширение файла.

import re

def partition(my_str):
    my_list = re.split("\.|\/", my_str)
    print(my_list)
    *a, b, c = my_list
    parts = (a, b, c)
    return parts

print(partition(input("Введите абсолютный путь до файла: ")))
# C:\Thecode\Media\статья.txt
