my_tuple = (1, 2, 3)
print(len(my_tuple + (1, 3, 'aaa',))) # len не изменяет?
print(my_tuple)


a = {'a', (1, 2), 3}
b = {3, (1, 2), 'unique'}
a.intersection(b)
{(1, 2), 3}

a.union(b)
{(1, 2), 3, 'a', 'unique'}


a.symmetric_difference(b)

a - b

b - a


# В словарь легко добавлять элементы через оператор присваивания
#name_to_number['Владимир'] = '+1 111 111-11-11'
#print(name_to_number['Владимир'])
# через оператор in можно узнать, есть ли ключ в словаре
#'Владимир' in name_to_number