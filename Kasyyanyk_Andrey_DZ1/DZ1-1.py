duration = int(input('введите количество секунд для конвертации: '))

minutes = duration//60
seconds = duration - minutes*60
hours = minutes // 60
minutes = minutes - hours * 60
days = hours // 24
hours = hours - days*24

if days == 0 and hours == 0 and minutes == 0:
    print(f'{seconds} с')
elif days == 0 and hours == 0:
    print(f'{minutes} м : {seconds} с')
elif days == 0:
    print(f'{hours} ч : {minutes} м : {seconds} с')
else:
    print(f'{days} д : {hours} ч : {minutes} м : {seconds} с')