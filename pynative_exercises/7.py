#7 примите любые три строки из одного вызова input ()

print("Anter three words:" + "\n")
word_1 = input("First: ")
word_2 = input("Second: ")
word_3 = input("Treeth: ")

print("First word: " + word_1 + "\n" + "Second word: " + word_2 + "\n" + "Treeth word: " + word_3 + "\n")

# or correctly

str1, str2, str3 = input("Enter three string").split()
print('Name1:', str1)
print('Name2:', str2)
print('Name3:', str3)