# some_value = 4
#
# bool_value_1 = (2 == some_value)
# bool_value_2 = ("z" not in "q.werty")
# print(bool_value_2)

# bool_value = bool_value_1 or bool_value_2
# print(bool_value_1, bool_value_2, bool_value)
# print(bool_value, type(bool_value))

# value = "-11.4"
# new_value = float(value)
# new_value_2 = int(new_value)
# print(new_value_2, type(new_value_2))


# value_1 = "25"
# value_2 = "4"
# value = value_1 / value_2  # обычное деление
# value = value_1 // value_2  # целочисленное деление (без округления)
# value = value_1 % value_2  # остаток от деления
# value = value_1 ** value_2  # возведение в степень. корень для ** 0.5
# value = value_1 + value_2
# print(value)  # , type(value))

# first = "qwe"
# second = 1
# value = first
# first = second
# second = value
# first, second = second, first
# print(first, second)


# print("Hello, World")
# # comment
# print("Hello, World")
# print('Hello!')
#
# print(123 * 2, "456", '789', "qwe")
# print(12 - 3)
# print(23 + 5 * 10)

# value = 0
# value_bool = bool(value)  # true кроме знач 0 --> false
# print(value_bool)

# temp = 0.1
# if temp > 0:
#     print("Можно не надевать шапку")
#     print("temp:", temp)
# else:
#     print("Надень шапку")

# case = input("throw a cube: ")
# # case = int(case)
# if case == "6":
#     print("win Vasya:", case)
# elif case == "1":
#     print("win Petya:", case)
# else:
#     print("all lose:", case)

# from random import randint
#
# case = randint(1,6)
# print("ur number:", case)
# if case == 6:
#     print("win Vasya:", case)
# elif case == 1:
#     print("win Petya:", case)
# else:
#     print("all lose:", case)

# тернарный оператор
# if case > 3:
#     result = case ** 2
# else:
#     result = - case

# from random import randint
#
# case = randint(1,6)
# print("ur number:", case)
# result = case ** 2 if case > 3 else - case
#
# print("ur number:", case, "result", result)

# case = 1
# result = 2
# print(f"ur number:{case} with ur result: {result}")

# dir_name = "home"
# filename = "test.py"
# path = f"{dir_name}/{filename}"
# print(path)

# str1 = "I'm Qwerty"
# str2 = '"apple" inc.'
#
# # index = -5
# # symbol = str1[index]
# # print(symbol)
# str1_len = len(str1)
# print(str1_len, str1[str1_len - 1])
# index = 5
# str1 = "I'm Qwerty"
# new_str = str1[:index] + "K" + str1[index + 1:]
# print(new_str)

# str1 = "I'm Qwerty"
# if str1[-1] == "a":
#     print(f"'a' on the last position in {str1}")
# else:
#     print(f"'a' not on the last position in {str1}")

# str1 = "I'm Qwerty"
# for symbol in str1:
#     if (symbol not in "EYUIOAeyuioa") and symbol.isalpha():
#         print(symbol)

# str1 = "I'm Qwerty"
# for symbol in str1:
#     if (symbol.lower() not in "eyuioa") and symbol.isalpha() and symbol.isupper():
#         print(symbol)

str1 = "I'm Qwerty"
# for symbol in str1:
#     print(f"symbol '{symbol}' --> {ord(symbol)}")

for index in range(ord("A"), ord('z')+ 1, 2):
    print(f"index: {index} --> '{chr(index)}'")

