#9 проверьте файл пуст или нет
# Напишите программу, чтобы проверить, пуст ли данный файл или нет

import os

# file_size = os.stat("python-train/pynative_files/empty_file_9.txt").st_size()

file_name = input("Please enter file name here: " + "\n")

# path = "python-train/pynative_files/test_6.txt"
user_path = "python-train/pynative_files/{}.txt"

path = user_path.format(file_name)

file_size = os.stat(path).st_size

if file_size == 0 :
    print("File is empty")
else :
    print("File size is: ", file_size)

# or short example

size = os.stat(path).st_size
if size == 0:
    print('file is empty')