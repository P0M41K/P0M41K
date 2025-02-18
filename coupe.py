ticket = int(input())
coupe_1 = (1, 4)
coupe_2 = (5, 8)
coupe_3 = (9, 12)
coupe_4 = (13, 16)
coupe_5 = (17, 20)
coupe_6 = (21, 24)
coupe_7 = (25, 28)
coupe_8 = (29, 32)
coupe_9 = (33, 36)
if ticket in range(1,4):
    print('Number_of_carriage is: Coupe_1')
elif ticket in range(5,8):
    print('Number_of_carriage is: Coupe_2')
elif ticket in range(9,12):
    print('Number_of_carriage is: Coupe_3')
elif ticket in range(13, 16):
    print('Number_of_carriage is: Coupe_4')
elif ticket in range(17, 20):
    print('Number_of_carriage is: Coupe_5')
elif ticket in range(21, 24):
    print('Number_of_carriage is: Coupe_6')
elif ticket in range(25, 28):
    print('Number_of_carriage is: Coupe_7')
elif ticket in range(29, 32):
    print('Number_of_carriage is: Coupe_8')
else:
    print('Number_of_carriage is: Coupe_9')