duration = int(input('Введите продолжительность в секундах '))
if duration < 60:
    second = duration
    print(second, ' сек')
elif 60 <= duration < 3600:
    minute = duration//60
    second = duration - minute * 60
    print(minute, ' минут', second, 'сек')
elif 3600 <= duration < 86400:
    hour = duration//3600
    minute = (duration - hour * 3600)//60
    second = (duration - hour * 3600 - minute * 60)
    print(hour, ' час', minute, ' минут', second, 'сек')
elif 86000 <= duration:
    day = duration // 86000
    hour = (duration - day * 86000) // 3600
    minute = (duration - day * 86000 - hour * 3600) // 60
    second = (duration - day * 86000 - hour * 3600 - minute * 60)
    print(day, ' дн', hour, ' час', minute, ' минут', second, 'сек')