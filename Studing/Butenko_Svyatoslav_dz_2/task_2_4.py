seq = ['инженер-конструктор Игорь', 'главный бухгалтер МАРИНА', 'токарь высшего разряда нИКОЛАй', 'директор аэлита']
for i, item in enumerate(seq):
    item = item.split(' ')
    name = (item[-1].title())
    print(f'Привет, {name}')
