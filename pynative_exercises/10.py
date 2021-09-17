# прочтите строку номер 4 из следующего файла
# Создайте файл test.txt и добавьте в него приведенный ниже контент
# строка 1 line2 line3 line4 line5 line6 line7

path = "python-train/pynative_files/test_10.txt"

with open(path, "r") as file:
    lines = file.readlines()
    print(lines[3])