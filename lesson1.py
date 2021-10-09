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

# str1 = "I'm Qwerty"
# for symbol in str1:
#     print(f"symbol '{symbol}' --> {ord(symbol)}")

# for index in range(ord("A"), ord('z')+ 1, 2):
#     print(f"index: {index} --> '{chr(index)}'")

# count = 0
# while count < 10:
#     print("while loop", count)
#     count += 1

# count = 0
# do_loop = True
# while do_loop:
#     print("while loop", count)
#     count += 1
#     if count >= 10:
#         do_loop = False

# count = 0
# while True:
#     print("while loop", count)
#     count += 1
#     if count >= 10:
#         break

# from random import randint
# min_limit = 1
# max_limit = 100
# comp_value = randint(min_limit, max_limit)
# cur_value = int(input(f"Угадай число от {min_limit} до {max_limit}: "))
# go_game = True
# while go_game:
#     if cur_value > comp_value:
#         cur_value = int(input("Попробуй число меньше: "))
#     elif cur_value < comp_value:
#         cur_value = int(input("Попробуй число больше: "))
#     else:
#         go_game = False
#         print("Ты победил")

# from random import randint
# min_limit = 1
# max_limit = 100
# comp_value = randint(min_limit, max_limit)
# cur_value = int(input(f"Угадай число от {min_limit} до {max_limit}: "))
# while cur_value != comp_value:
#     case_word = "меньше" if cur_value > comp_value else "больше"
#     cur_value= int(input(f"Попробуй число {case_word}"))
#     # if cur_value > comp_value:
#     #     cur_value = int(input("Попробуй число меньше: "))
#     # else:
#     #     cur_value = int(input("Попробуй число больше: "))
# print("Ты победил")

# value = input("Введи целое число: ")
# try:
#     value_int = int(value)
#     result = 1 / value_int
#     print(result)
# except ValueError:
#     print("Это не число")
# except ZeroDivisionError:
#     print("Делить на 0 нельзя")

# my_str = "qwerty 123 %(^ SGS"
# for symbol in my_str:
#     if not symbol.isalnum() and symbol != " ":
#         print(symbol)

# my_str = "qwerty 123 %(^ AGS"
# for symbol in my_str:
#     if symbol.lower() in "eyuioa":
#         print(symbol)

# my_tuple = (1, -10, "qwe", True, 3.14, (-2, 0), ["a", "z"])
# my_list = [1, -10, "qwe", True, 3.14, (-2, 0), ["a", "z"]]

# print(my_tuple, type(my_tuple))
# print(my_list, type(my_list))
# index = -1
# print(my_tuple[index], my_list[index])
# print(len(my_tuple), len(my_list))

# new_list = my_list[1:-1]
# print(new_list)
#
# new_tuple = my_tuple[::-1]
# print(new_tuple)

# for value in my_list:
#     if type(value) == int:
#         print(value)

# my_tuple = (1, -10, "qwe", True, 3.14, (-2, 0), ["a", "z"])
# my_list = [1, -10, "qwe", True, 3.14, (-2, 0), ["a", "z"]]
# my_list[0] = 100
# print(my_list)

# my_tuple = (1, -10, "qwe", True, 3.14, (-2, 0), ["a", "z"])
# val1, *val = my_tuple
# print(val1, val)

# my_list = [1, (-2, 0), ["a", "z"]]
# my_list[-1][0] = 100
# print(my_list)

# my_tuple = (1, (-2, 0), ["a", "z"])
# my_tuple[-1][0] = 100
# print(my_tuple)

# my_table = [[1, 2], [3, 4]]
# my_table[1][1] = 24
# print(my_table)

# my_tuple = (1, 2, 3)
# print(id(my_tuple), id(1))
# my_tuple = (100, *my_tuple[1:])
# print(id(my_tuple))

# list_1 = [1, 2]
# list_2 = [3, 4]
# new_list = [list_1.copy(), list_2]
# print(new_list)
# list_1[0] = 100
# list_2[0] = 300
# print(new_list, list_1)

# value = [10, 20]
# new_list = [value] * 5
# value[0] = 100
# print(new_list)

# new_list = []
# for symbol in "qwerty":
#     new_list.append(symbol)
# new_list.append(1000)
# print(new_list)
# result = new_list.pop(5)
# print(result)

# new_list = list("qwerty")
# print(new_list)

# new_list = list("new_tuple")
# print(new_list)
# new_str = "$".join(new_list)
# print(new_str)

# filename = "lesson1.py.txt"

##  filename = filename.replace(".txt", "")

# filename_parts = filename.split(".")
# filename = ".".join(filename_parts[:-1])

# filename = filename.rsplit(".", 1)[0]  # задать вопрос
# print(filename)

#### практика

# my_str = "blablacar"
# my_symbol = "bla"

# result = my_str.count(my_symbol)
# # new_str = my_str.replace(my_symbol, '')
# # result = (len(my_str) - len(new_str)) // len(my_symbol)
# print(result)
###############################################################
# my_symbol_count = my_str.count(my_symbol)
# # result =  f"{my_symbol}\n" * my_symbol_count
# # result = result.strip()
# # print(result)
#
# for my_count in range(my_symbol_count):
#     print(my_symbol)
#################################################################
# my_str = "bla BLA car"
# lower_str = my_str.lower()
# unique_symbols = []
# for symbol in lower_str:
#     if symbol not in unique_symbols:
#         unique_symbols.append(symbol)
# unique_symbols_count = len(unique_symbols)
# print(unique_symbols_count)

# my_str = "bla BLA car"
# lower_str = my_str.lower()
# unique_symbols = set(lower_str)
# print(unique_symbols)
# unique_symbols_count = len(unique_symbols)
# print(unique_symbols_count)

# my_str = "bla BLA car"
# unique_symbols_count = len(set(my_str.lower()))
# print(unique_symbols_count)
#################################################################
# my_list = []
# my_str = "ksjbndvlgsbvd"
# print(id(my_list), my_list)
# new_str = my_str[::2]
# # for symbol in new_str:
# #     my_list.append(symbol)
# my_list += list(new_str)
# print(id(my_list), my_list)
################################################################
# val_1 = 123
# val_2 = 100
# val_1 += val_2
# print(val_1)
################################################################
# from string import ascii_lowercase as alphabet
# my_str = alphabet
# str_index = [7, 8, 11, 11, 4, 11]
# my_list = []
# for index in str_index:
#     symbol = my_str[index]
#     my_list.append(symbol)
# print(my_list)
################################################################
# number = 123456789123456789
# digit_count = len(str(number))
# print(digit_count)
################################################################
# number = 3276276173811313
# max_symbol = max(str(number))
# print(max_symbol)
################################################################
# number = 27368761846874123
# # numb_str = str(number)
# result_number = int(str(number)[::-1])
# # result_number = int(numb_str[::-1])
# print(result_number)
#################################################################
# number = 73242472770241
# numb_str = str(number)
# sort_numb_list = sorted(numb_str)
# new_number = "".join(sort_numb_list)
# result = int(new_number)
# print(result)
#################################################################
# number = 46264822770241
# numb_str = str(number)
# sort_numb_list = sorted(numb_str)
# new_number = "".join(sort_numb_list[::-1])
# result = int(new_number)
# print(result)

# number = 46264822770241
# numb_str = str(number)
# sort_numb_list = sorted(numb_str, reverse=True)
# new_number = "".join(sort_numb_list)
# result = int(new_number)
# print(result)
#
# my_list = [3, 6, 1, 8]
# # my_list_sorted = sorted(my_list, reverse=True) # новый id
# my_list.sort(reverse=True) # старый id
# print(my_list)
#################################################################
# my_list_1 = [1, 2, 3]
# my_list_2 = [10, 20, 30]
# my_result = []
#
# for index in range(len(my_list_1)):
#     my_result.extend([my_list_1[index], my_list_2[index]])
#     # my_result.append(my_list_1[index])
#     # my_result.append(my_list_2[index])
# print(my_result)
################################################################
# my_list_1 = [1, 2, 3, 4, 5, 6, 7, 8]
# my_list_2 = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
# my_result = []
# min_len_lists = min(len(my_list_1), len(my_list_2))
# tail = my_list_1[min_len_lists:] + my_list_2[min_len_lists:]
# print(tail)
# for index in range(min_len_lists):
#     my_result.append(my_list_1[index])
#     my_result.append(my_list_2[index])
# my_result.extend(tail)
# print(my_result)
###############################################################
# ord(), chr()
# print(ord("A"))
# print(chr(110))

# генераторы списков (list comprehension)
# alphabet_list = []
# for index_ascii in range(ord('a'), ord('z') + 1):
#     alphabet_list.append(chr(index_ascii))
# alphabet = " ".join(alphabet_list)


# alphabet_list = [chr(index_ascii) for index_ascii in range(ord('a'), ord('z') + 1)]
# alphabet = " ".join(alphabet_list)
# print(alphabet)

# result = [x ** 2 for x in range(25)]
# print(result)

# my_list = [12, -45, 23, 5, 0, 21, 900]
# res = [str(value) * 20 for value in my_list if value > 10]
# # res = []
# # for value in my_list:
# #     if value > 10:
# #         res.append(value)
# [print(line) for line in res]
# # for line in res:
# #     print(line)
# # print(res)

# # множества (set) - изменяемый тип данных, только один представитель для каждого объекта, порядок не сохраняется
# my_list = [1, "2", 3, 4, 5, 5, "1", "5"]
# my_list_unique = list(set(my_list)) # убрать дубли в списке
# my_set = set(my_list)
# my_set.add(100)
# print(my_set, type(my_set))

# пересечение множеств
# my_str_1 = "bbfivhbgvlibbhfbjdfhdjf"
# my_str_2 = "dhfjdocmxnuhfihvidbpsbgwqtyeiosp"
# my_str_1_set = set(my_str_1)
# my_str_2_set = set(my_str_2)
# same_symbols = my_str_1_set.intersection(my_str_2_set)
# print(same_symbols)

# объединение множеств
# my_str_1 = "bbfivhbgvlibbhfbjdfhdjf"
# my_str_2 = "dhfjdocmxnuhfihvidbpsbgwqtyeiosp"
# my_str_1_set = set(my_str_1)
# my_str_2_set = set(my_str_2)
# all_symbols = my_str_1_set.union(my_str_2_set)
# print(all_symbols)

# разность множеств
# my_str_1 = "bbfivhbgvlibbhfbjdfhdjf"
# my_str_2 = "dhfjdocmxnuhfihvidbpsbgwqtyeiosp"
# my_str_1_set = set(my_str_1)
# my_str_2_set = set(my_str_2)
# first_str_unique = my_str_1_set.difference(my_str_2_set)
# print(first_str_unique)
#
# my_str_1 = "bbfivhbgvlibbhfbjdfhdjf"
# my_str_2 = "dhfjdocmxnuhfihvidbpsbgwqtyeiosp"
# my_str_1_set = set(my_str_1)
# my_str_2_set = set(my_str_2)
# second_str_unique = my_str_2_set.difference(my_str_1_set)
# print(second_str_unique)





