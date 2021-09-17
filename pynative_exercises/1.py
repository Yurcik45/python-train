#1 Напишите программу, которая принимает от пользователя два числа и вычисляет умножение

num_one_1 = input("first num")
num_two_1 = input("second num")

# num_one_1 = int(num_one_1)
# num_two_1 = int(num_two_1)

# print(num_one_1 * num_two_1)

def multiplaying(num_1, num_2):
    if type(num_1) is str or type(num_2) is str:
        num_1 = int(num_1)
        num_2 = int(num_2)
        print("to num")
    else :
        print("its numbers")
    result = num_1 * num_2
    return result

print(multiplaying(num_one_1, num_two_1))