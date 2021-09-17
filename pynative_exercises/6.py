# Запишите все содержимое данного файла (test_6.txt) в новый файл (test_6_result.txt), пропустив строку номер 5

# file = open(r"update/users/yurcik45/Desktop/python_learn/pynative_exercises/1.py", "r")
file = open("python-train/pynative_files/test_6.txt", "r")
new_file = open("python-train/pynative_files/test_6_result.txt", "w")

file_content = []
new_file_content = []

for i in range (7):
    file_content.append(file.readline().strip())
    # file.close()

for i in file_content:
    if i != "line5":
        new_file_content.append(i)

for i in new_file_content:
    print(i)
    new_file.write(i + "\n")

file.close()
new_file.close()


print("initial content", file_content)
print("result content", new_file_content)

# or correctly

# read test.txt
with open("python-train/pynative_files/test_6.txt", "r") as fp:
    # read all lines from a file
    lines = fp.readlines()

# open new file in write mode
with open("python-train/pynative_files/test_6_result.txt", "w") as fp:
    count = 0
    # iterate each lines from a test.txt
    for line in lines:
        # skip 5th lines
        if count == 4:
            count += 1
            continue
        else:
            # write current line
            fp.write(line)
        # in each iteration reduce the count
        count += 1