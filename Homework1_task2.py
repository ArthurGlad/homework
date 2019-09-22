n = int(input('Введите натуральное число от 1 до 9999:'))
if 1 <= n < 10:
    print('True') #Палиндром ли? Если да, то ответ True; если нет - False
elif 10 <= n < 100:
    if n // 10 == n % 10:
        print('True')
    else:
        print('False')
elif 100 <= n < 1000:
    if n // 100 == n % 100 // 10:
        print('True')
    else:
        print('False')
elif 1000 <= n <= 9999:
    if n // 100 == n % 100: #то есть числа вида 110, 220, 330 будут считаться палиндромами (если добавить слева ноль)
        print('True')
    elif n // 100 == int(str(n % 100)[-1]+str(n % 100)[0]):
        print('True')
    elif n // 1000 == n % 1000 and n // 100 % 10 == n % 100 // 10:
        print('True')
    else:
        print('False')
if n < 1 or n > 9999:
    print('Введенное число не попадает в диапазон от 1 до 9999!')
