# # Создать 2 списка с одинаковым количеством элементов
# # На выходе получить словарь, гду ключами станут элементы 1 списка, а значаниями - эл-ты второго списка

# # count = int(input('Введите количество элементов в списках: '))
# first_list = [1, 2, 3, 4, 5]
# second_list = ['a', 'b', 'c', 'd', 'e']
# some_dict = {}
# for i in range(0, len(first_list)):
#     some_dict[first_list[i]] = second_list[i]
# print(some_dict)

# # Решение при помощи функции zip
# some_dict = dict(zip(first_list, second_list))
# print(some_dict)

# ////////////////////////////////////////////////////////
# Написать функцию num_translate, переводящую числительные от 0 до 10
# с англ на русс язык
# list_1 = ['zero', 'one', 'two', 'three', 'four', 'five']
# list_2 = ['ноль', 'один', 'два', 'три', 'четыре', 'пять']
# some_dict = dict(zip(list_1, list_2))
# print(some_dict)
# print(some_dict.get(input('Введите числительное на англ языке: '), 'None'))


from fnmatch import translate
from typing import Mapping


# def num_translate(number):
#     translate_dict = {'zero': 'ноль', 'one': 'один', 'two': 'два', 'three': 'три', 'four': 'четыре', 'five': 'пять'}
#     if number[0].isupper():
#         print(translate_dict.get(number.lower()).capitalize()) # меняет строчные буквы на заглавные
#     else:
#         print(translate_dict.get(number))
# num_translate('one')
# num_translate('Two')
        
#//////////////////////////////////////////////////////////////////////////////



# import itertools

# list_1 = ['Иван', 'Мария', 'Илья', 'Петр', 'Земфира']
# dic = {}
# for item in range(len(list_1)):
#     if list_1[item][0] in dic:
#         dic[list_1[item][0]].append(list_1[item])
#     else:
#         dic[list_1[item][0]] = [list_1[item]]
        
# print(dic)

# вариант с функцией:
# lst = ['Иван', 'Мария', 'Илья', 'Петр', 'Земфира']
# def thesaurus(lst):
#     lst = ['Иван', 'Мария', 'Илья', 'Петр', 'Земфира']
#     dic = {}
#     for i in lst:
#         if i[0] in dic.keys():
#             dic[i[0]].append(i)
#         else:
#             dic[i[0]] = [i]
#     print(dic)

# lst = ['Иван Сергеев', 'Инна Перова', 'Юлия Иванова']
# dic = {}
# for i in range(len(lst)):
#     if lst


# print(len(lst))

    
