
for i in range(1, 101):
    if 11 <= i <= 19:
        b = 'ов'
    elif i % 10 == 1:
        b = ''
    elif 2 <= i % 10 <= 4:
        b = 'a'
    elif i % 10 == 0 or 5 <= i % 10 <= 9:
        b = 'ов'
    print(f'{i} процент{b}')