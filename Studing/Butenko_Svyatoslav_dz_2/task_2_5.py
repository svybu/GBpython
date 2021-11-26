seq = [35.4, 55, 98.5, 74.35, 68.32, 47.34, 98, 42, 65.35, 87.08]
price = []
for i in seq:
    if type(i) != float:
        price.append(str(i) + " руб 00 коп")
    else:
        rub, kop = str(i).split('.')
        if len(kop) == 1:
            kop = kop + "0"
        price.append(str(rub) + ' руб ' + kop + ' коп')
print(', '.join(price))
print(id(seq))  # id до сортировки
seq.sort()
print(seq)
print(id(seq))  # id после сортировки
sort_price = sorted(seq, reverse=True)
print(sort_price)
print(sorted(sort_price[:5]))
