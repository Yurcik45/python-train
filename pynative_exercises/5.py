#5 Примите список из 5 чисел с плавающей запятой как ввод от пользователя

# Ожидаемый результат : [78.6, 78.6, 85.3, 1.2, 3.5]

float_input_1 = float(input("float 1 "))
float_input_2 = float(input("float 2 "))
float_input_3 = float(input("float 3 "))
float_input_4 = float(input("float 4 "))
float_input_5 = float(input("float 5 "))

my_list = []

my_list.append(float_input_1)
my_list.append(float_input_2)
my_list.append(float_input_3)
my_list.append(float_input_4)
my_list.append(float_input_5)

print(my_list)

# or correctly

numbers = []

# 5 is the list size
# run loop 5 times
for i in range(0, 5):
    print("Enter number at location", i, ":")
    # accept float number from user
    item = float(input())
    # add it to the list
    numbers.append(item)

print("User List:", numbers)