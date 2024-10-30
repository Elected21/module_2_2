from time import sleep

print('Задача найти три одинаковых числа!')
sleep(2)
print('Приступим')

first = input('Введите первое число: ')
second = input('Введите второе число: ')
third = input('Введите третье число: ')

if first == second and first == third and second == third:
    print('Все числа совпадают!')

elif first != second and first != third and second != third:
    print('Нет совпадений!')

else: print('Два числа из трёх совпадают!')
