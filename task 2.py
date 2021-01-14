time_s = int(input('введите время в секундах: '))
if time_s // 60 < 1:
    seconds = time_s
    print(f'время: 00:00:{seconds:02}')
elif time_s // 60 >= 1 and time_s // 60 < 60:
    minutes = time_s // 60
    seconds = time_s % 60
    print(f'время: 00:{minutes:02}:{seconds:02}')
elif time_s // 60 >= 60:
    maxi_minutes = time_s // 60
    seconds = time_s % 60
    hours = maxi_minutes // 60
    minutes = maxi_minutes % 60
    print(f'время: {hours:02}:{minutes:02}:{seconds:02}')
