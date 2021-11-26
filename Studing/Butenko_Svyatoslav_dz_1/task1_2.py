list_a = []
list_b = []
def devision(a):
    b = a % 10
    c = a // 10
    return ( b, c )

for i in range(1, 1000, 2):
    list_a.append(i**3)
def check_seven(list_a):
    last_sum = 0
    for i,a in enumerate(list_a):
        sum_a = 0
        while a != 0:
            b, a = devision(a)
            sum_a = sum_a + b
        if sum_a % 7 == 0:
            last_sum = list_a[i] + last_sum
    print(last_sum)
check_seven(list_a)
for i, a in enumerate(list_a):
    list_a[i] = a + 17
check_seven(list_a)
