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


task = {
    1:'Полить цветы',
    0:'Покормить кота',
    1:'Забрать посылку',
    2:'Почитать книгу по программированию',
    3:'Ответить на письмо двоюродной тети'
}
print(task)

