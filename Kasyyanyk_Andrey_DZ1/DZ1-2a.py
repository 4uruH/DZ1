a = [] # Создали пустой список
summa_last = 0
for i in range (1000): # Зполняем список кубами нечетных чисел

    if i % 2 != 0:
        a.append(i**3)

for i in range(len(a)): # Ищем сумму цифр каждого элемената списка
    n = a[i]
    summa = 0
    while n > 0:
        digit = n % 10
        summa = summa + digit
        n = n//10
    if summa % 7 == 0: # Проверка кратности суммы цифр элемента списка семи
        summa_last = summa_last + a[i] # сумма элементов удовлетворяющих условию
print(summa_last)
