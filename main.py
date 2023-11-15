Модуль 2
задание 1

print('Введите n')
n = int(input())
print('Введите k')
k = int(input())
if n>k:
  print('no')
else:
  print('yes')

задание 2

a = int(input())
b = int(input())
c = int(input())
if a == b == c:
    print('Треугольник равносторонний')
if a == b != c or b == c != a or a == c != b:
    print('Треугольник равнобедренный')
if a != b != c:
    print('Треугольник разносторонний')
 Задание 3

a = int(input())
b = int(input())
c = int(input())
if a < b < c or a > b > c:
    print(b)
elif b < c < a or b > c > a:
    print(c)
else:
    print(a)

задание 4

a = int(input())
if a == 2:
    print ('28')
elif a <= 7:
    print(30 + a%2)
else:
    print(31 - a%2)

задание 5

a = int(input())
if a < 60:
    print('Легкий вес')
elif a < 64:
    print('Первый полусредний вес')
elif a < 69:
    print('Полусредний вес')

задание 6

a = input()
b = input()
if (a == 'красный' and b == 'синий') or (a == 'синий' and b == 'красный'):
    print('фиолетовый')
elif a == 'красный' and b == 'красный':
    print('красный')
elif (a == 'красный' and b == 'желтый') or (a == 'желтый' and b == 'красный'):
    print('оранжевый')
elif a == 'желтый' and b == 'желтый':
    print('желтый')
elif (a == 'синий' and b == 'желтый') or (a == 'желтый' and b == 'синий'):
    print('зеленый')
elif a == 'синий' and b == 'синий':
    print('синий')
else:
    print('ошибка цвета')

задание 7 

b = int(input())
if b < 00 or b > 3636:
    print('ошибка ввода')
elif b == 0:
    print('зеленый')
elif 1111 <= b <= 1010 or 1919 <= b <= 2828:
    if b % 2 == 0:
        print('черный')
    else:
        print('красный')
elif 11 <= b <= 1818 or 2929 <= b <= 3636:
    if b % 2 == 0:
        print ('красный')
    else:
        print ('черный')
