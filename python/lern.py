# x = int(input())
# if x < 0:
#     x = -x
# print(x)

# x = int(input())
# y = int(input())
# if x > 0:
#     if y > 0:               # x > 0, y > 0
#         print("Первая четверть")
#     else:                   # x > 0, y < 0
#         print("Четвертая четверть")
# else:
#     if y > 0:               # x < 0, y > 0
#         print("Вторая четверть")
#     else:                   # x < 0, y < 0
#         print("Третья четверть")

# a = int(input())
# b = int(input())
# c = int(input())
# d = int(input())
# if a % 2 == 1 and b % 2 == 1:
#     if c % 2 == 1 and d % 2 == 1:
#         print('YES')
#     elif c % 2 == 0 and d % 2 == 0:
#         print('YES')
#
# elif a % 2 == 0 and b % 2 == 1:
#     if c % 2 == 1 and d % 2 == 0:
#         print('YES')
#     elif c % 2 == 0 and d % 2 == 1:
#         print('YES')
#     elif c % 2 == 0 and d % 2 == 0:
#         print('NO')
#     elif c % 2 == 1 and d % 2 == 1:
#         print('YES')
#
# elif a % 2 == 0 and b % 2 == 0:
#     if c % 2 == 1 and d % 2 == 1:
#         print('YES')
#     elif c % 2 == 0 and d % 2 == 1:
#         print('NO')
#     elif c % 2 == 0 and d % 2 == 0:
#         print('YES')
#
# elif a % 2 == 1 and b % 2 == 0:
#     if c % 2 == 1 and d % 2 == 0:
#         print('YES')
#     elif c % 2 == 0 and d % 2 == 1:
#         print('YES')
#
# # равельное решение задачи с шахматной доской
# x1 = int(input())
# y1 = int(input())
# x2 = int(input())
# y2 = int(input())
# if (x1 + y1 + x2 + y2) % 2 == 0:
#     print('YES')
# else:
#     print('NO')

# высокосный год
# god = int(input())
# if god % 4 == 0 and god % 100 != 0 or god % 400 == 0:
#     print('YES')
# else:
#     print('NO')

# # Задача «Минимум из трех чисел»
# a = int(input())
# b = int(input())
# c = int(input())
# if a > b and a>c:
#     if b>c:
#         print(c)
# elif a<b and a<c:
#     print(a)
# elif b>c:
#     print(c)
# else:
#     print(b)
#
# # лучшее
# a = int(input())
# b = int(input())
# c = int(input())
# if b >= a <= c:
#     print(a)
# elif a >= b <= c:
#     print(b)
# else:
#     print(c)

# Задача «Сколько совпадает чисел»
# a = int(input())
# b = int(input())
# c = int(input())
# if a == b and a == c or b == a and b == c or c == b and c == a:
#     print(3)
# elif a == b or a == c or b == a or b == c or c == b or c == a:
#      print(2)
# else:
#     print(0)
#
# # лучшее решение
# a = int(input())
# b = int(input())
# c = int(input())
# if a == b == c:
#     print(3)
# elif a == b or b == c or a == c:
#     print(2)
# else:
#     print(0)

# Задача «Ход ладьи»
# a = int(input())
# b = int(input())
# c = int(input())
# d = int(input())
# if a == d and b ==c:
#     print('NO')
# elif a ==1 and b ==2 and c == 1 and d ==3:
#     print('YES')
# elif a+b==3 and c+d==4:
#     print('NO')
# elif a == d or b ==c:
#         print('YES')
# elif (a + b + c + d) % 2 == 0:
#     print('NO')
# elif a+b ==8 and c+d==9:
#     print('NO')
# elif a == d or b ==c:
#     print('YES')
# else:
#      print('YES')

# # Лучший вариант
# x1 = int(input())
# y1 = int(input())
# x2 = int(input())
# y2 = int(input())
# if x1 == x2 or y1 == y2:
#     print('YES')
# else:
#     print('NO')

x1 = int(input())
y1 = int(input())
x2 = int(input())
y2 = int(input())
if x1+y1==x2+y2 or x1+y1==x2+y2+1 or x1+y1+2==x2+y2:
    print('YES')
else:
    print('NO')