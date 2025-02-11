from xmlrpc.client import boolean

i = 3

name = 'Roma'
age = 37
is_student = False
print(name, age, is_student) # можно было бы сделать через запятую, но похуй

# бабки, бабки, сука, бабки!
total_money = 1000
price = 100
jar_count = total_money / price
print(int(jar_count))

a = 3
b = 7
c = -10
x1 = (2*a)-b+((b*b)-(4*a*c))
x2 =(2*a)-b-((b*b)-(4*a*c))
print(x1, x2)
print(-9**0.5)

tasks_my = ('Полить цветы, Покормить кота, Забрать посылку ')
tasks_friend = ('Почитать книгу по программированию, Ответить на письмо двоюродной тети')
tasks_all = tasks_my + tasks_friend
print(tasks_all)


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


task = {
    1:'Полить цветы',
    0:'Покормить кота',
    1:'Забрать посылку',
    2:'Почитать книгу по программированию',
    3:'Ответить на письмо двоюродной тети'
}
print(task)