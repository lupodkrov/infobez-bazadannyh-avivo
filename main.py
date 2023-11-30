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

задание 8

a1 = int(input())
b1 = int(input())
a2 = int(input())
b2 = int(input())
if a2 > b1 or a1 > b2:
    print('Пустое множество')
elif a1 == b1:
    print(a1)
elif a2 == b1:
    print(a2)
else:
    if a1 > a2:
        a2 = a1
    if b1 < b2:
        b2 = b1
    print(a2, b2)

Контрольная работа
№1 
print()
№2
print('Поэма "Мертвые души" одна из самых интересных')
print("I'm a math teacher and a programmer!")
print("3.1415")
print()
№3
print("Python",,"is the best")
print('Python','is the best','!!')
№4
print("The world's a little blurry","Or maybe it's my eyes",end='!!!',sep=':)')
print("Honey, what's your hurry",end=="")
print("Told you not to worry","But maybe that's a lie",sep=':)')
№5
input()
№6
n=int(input())
№7
Имя переменной может начинаться с подчеркивания (_)
Имя переменной не может начинаться с цифры
Имя переменной не может совпадать с ключевым (зарезервированным) словом
№8
s = 13
k = -5
d = s + 2
s = d
k = 2 * s 
print(s + k + d)
Ответ: 60
№9
a = 17 // (23 % 7)
b = 34 % a * 5 - 29 % 4 * 3
print(a * b)
Ответ:56
№10
print('*****************')
print('*               *')
print('*               *')
print('*****************')
№11
a = int(input())
b = int(input())
print(f'Квадрат суммы {a} и {b} равен {(a + b) ** 2}')
print(f'Сумма квадратов {a} и {b} равна {a ** 2 + b ** 2}')
№12
a = int(input()) 
b = int(input())
c = int(input())
d = int(input()) 
print(a ** b + c ** d)
№13
n = int(input())
print(n + n * 10 + n + n * 100 + n *10 + n)

Модуль 1
Задание 1
s = 0
k = 15
d = k - 10
k = 4 * d
s = k - 50
print('ответ 1:', s)
Задание 2
x = 3
y = 4
z = x + y
z = z + 1
x = y
y = 5
x = z + y + 7
print('ответ 2:', x)
Задание 3
n = int(input())
print(n)
print(n + 1)
print(n + 2)
Задание 4
a = int(input())
b = int(input())
c = int(input())
d = a + b + c
print(d)
Задание 5
a = int(input())
b = 6 * (a * a)
print(b)
Задание 6
a = int(input()) 
b = int(input()) 
print(3*((a+b)**3)+275*(b**2)-127*a-41)
Задание 7
a = int(input())
b = a + 1
c = a - 1
print("следующее число после", a, ":', b)
print("предыдущее число после", a, ":', b)
Задание 8
a = int(input())
b = int(input())
c = int(input())
d = int(input())
e = a + b + c + d
n = e * 3
print(n)
Задание 9
a = int(input()) 
b = int(input()) 
c = a + b
d = a - b
e = a * b 
print("сумма", c)
print("разность", d)
print("произведение", e)
Задание 10
a1 = int(input())
d = int(input())
n = int(input())
print(a1+d*(n-1))
Задание 11
a = int(input())
print(a, a*2, a*3, a*4, a*5, sep='-'*3)
Задание 12
b1 = int(input())
q = int(input())
n = int(input())
print(b1 * q ** (n-1))
Задание 13
a = int(input())
b = a // 100
print(b)
Задание 14
a = int(input())
b = int(input())
print(b // a)
print(b % a)
Задание 15
n = int(input())
print(n//2 + n%2)
Задание 16
a = int(input())
print((a + 3) // 4)
Задание 17
a = int(input())
b = a // 60
c = a % 60
print(a, "мин - это", b, "час", c, "минут.")
Задание 18
n = int(input())
a = n % 10 
b = (n % 100) // 10
c = n // 100
print("Сумма цифр =", c + b + a)
print("Произведение цифр =", c * b * a)
Задание 19
abc = int(input())
c = abc % 10
b = (abc % 100) // 10
a = abc // 100
print(a, b, c, sep='')
print(a, c, b, sep='')
print(b, a, c, sep='')
print(b, c, a, sep='')
print(c, a, b, sep='')
print(c, b, a, sep='')
Задание 20
a = int(input())
a1 = a // 1000
a2 = (a // 100) % 10 
a3 = (a // 10) % 10
a4 = a % 10
print("Цифра в позиции тысяч равна", a1)
print("Цифра в позиции сотен равна", a2)
print("Цифра в позиции десятков равна", a3)
print("Цифра в позиции единиц равна", a4)
Задание 21
a = (input())
b = (input())
print('Пароль принят') if a == b else print('Пароль не принят')
Задание 22
a = int(input())
print('Нечетное') if a % 2 else print('Четное')
Задание 23
a = int(input()) 
b = int(input())
c = int(input())
d = int(input()) 
print('да' if int(a) + int(d) == int(b) - int(c) else 'нет')
Задание 24
a = int(input())
print('Доступ разрешен') if a >= 18 else print('Доступ запрещен')
Задание 25
a1 = int(input())
a2 = int(input())
a3 = int(input())
if a3 - a2 == a2 - a1:
    print('yes')
else:
    print('no')
Задание 26
a = int(input()) 
b = int(input())
if a > b:
    a = b
print(a)
Задание 27
a = int(input()) 
b = int(input())
c = int(input())
d = int(input()) 
if a > b:
    a = b
if c > d:
    c = d
if a > c:
    a = c
print(a)
Задание 28
a = int(input())
if a <= 13:
    print('Детство')
elif a <= 24:
    print('Молодость')
elif a <= 59:
    print('Зрелость')
elif a >= 60:
    print('Старость')
Задание 29
a = int(input()) 
b = int(input())
c = int(input())
n = 0
if a > 0:
    n += a
if b > 0:
    n += b
if c > 0:
    n += c
print('сумма положительных чисел равна:', n)
Задание 30
a = int(input())
if (a % 7 == 0 or a % 17 == 0):
    print('yes')
else:
    print('no')
Задание 31
a, b, c = int(input()), int(input()), int(input())
if a + b > c and b + c > a and c + a > b:
print('yes2')
else:
print('no')
Задание 32
a = int(input())
print('yes') if ((a % 4 == 0) and not (a % 100 == 0)) or (a % 400 == 0) 
else print('no')
Задание 33
a = int(input())
b = int(input())
c = int(input())
d = int(input())
print('yes') if (a == c) or (b == d) else print('no')
