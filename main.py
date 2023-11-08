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
