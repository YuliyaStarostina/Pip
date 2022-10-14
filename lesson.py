some_dict = {'name': 'Ivan',
             'last_name': 'Ivanov',
             'age': 32}
print(some_dict['age'])
print(some_dict.get('рорсм', 'Ключ не найден'))# если ключ не найден, то не выдает ошибку, а пишет None
print(some_dict.setdefault('adress', 'Nekrasova 63')) # если не находит ключ и имеет 2 аргумента, то добавляет новый ключ и значение
print(some_dict)