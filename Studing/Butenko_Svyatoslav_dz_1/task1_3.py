number = int(input('Введите число от 1 до 100 '))
if number == 1 or number == 21 or number == 31 or number == 41 or number == 51 or number == 61 or number == 71 or number == 81 or number == 91:
    print( number, ' процент' )
elif 1 < number < 5 or  21 < number < 25 or 31 < number < 35 or 41 < number < 45 or 51 < number < 55 or 51 < number < 55 or 61 < number < 65 or 71 < number < 75 or 81 < number < 85  or 91 < number < 95 :
    print( number, ' процента' )
elif 5 < number < 21 or  24 < number < 31 or 34 < number < 41 or 44 < number < 51 or 54 < number < 61 or 64 < number < 71 or 74 < number < 81 or 84 < number < 91  or 94 < number < 100:
    print( number, ' процентов' )
else:
    print('АШЫБКА! Нужно было ввести  число от 1 до 100')
