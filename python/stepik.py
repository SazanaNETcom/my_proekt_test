# Решение - 1
# a, b = input().split()
# a = int(a)
# b = int(b)
# s = 0
# for i in range(a, b + 1):
#     if i % 2 == 1:
#         s += i
#     print(s)

# Решение - 2
# a, b = input().split()
# a = int(a)
# b = int(b)
# s = 0
# if a % 2 == 0:
#     a += 1
# for i in range(a, b + 1,2):
#     s += i
# print(s)

# Решение - 3
# a, b = (int(i) for i in input().split())
# s = 0
# if a % 2 == 0:a = int(input())
# b = int(input())
# s = 0
# k = 0
# if a % 3 == 1:
#     a += 2
# if a % 3 == 2:
#     a += 1
# for i in range(a, b + 1, 3):
#     s += i
#     k += 1
# print(s / k)

#     a += 1
# for i in range(a, b + 1, 2):
#     s += i
# print(s)

# a, b = (int(i) for i in input().split())


# len([i for i in range(1001) if str(3) in str(i)])

# genome = 'ATGG'
# genome[0] = A
# genome[1] = T
# genome[2] = G
# genome[3] = G
#
# genome[-1] = G
# genome[-2] = G
# genome[-3] = T
# genome[-4] = A

# i = 1
# print(genome[i])

# for i in range(4):
#     print(genome[i])

# for c in genome:
#     print(c)

# genome = input()
# cnt = 0
# for nucl in genome:
#     if nucl == 'C':
#         cnt += 1
# print(cnt)

# genome = input()
# print(genome.count('C'))

# gc = input().upper()
# c = 0
# b = len(gc)
# for proc in gc:
#     if proc == 'G'or proc == 'C':
#         c += 1
# print((c/b)*100)

# gc = input().upper()
# c = 0
# b = len(gc)
# print((genome.count('C' or 'G')/b)*100)
#
# s = input()
# i = 0
# j = len(s) - 1
# is_palindrom = True
# while i < j:
#     if s[i] != s[j]:
#         is_palindrom = False
#         break
#     i += 1
#     j -= 1
#     if is_palindrom:
#         print('YES')
#     else:
#         print('NO')

# s = input()
# r = s[::-1]
# if s == r:
#     print('YES')
# else:
#     print('NO')

# для вывода текста с кол-вом а1б4с6


# z = k
# w += 1
# p = z + str(w)
# print(p)
# for f in k:
#     if f == k:
#         w += 1
#         print(w)
#         z = k
#         x = f + str(w)
#         print(x)
#     elif z != f:
#         break
# # elif k != 'a':

# s = 'aaaabbcaa'
# a_cn = 0
# if 'a' in s:
#     a_cn +=1
#     print(a_cn)


# students = ['Iva', 'Masha', 'Sasha']
# print (len(students))
# for student in students:
#     print(('Hello, ' + student+'!'))
# teachers = ['Oleg', 'Alex']
# students + teachers
# print(students + teachers)

# students = ['Ivan', 'Masha', 'Sasha', 'Alex']
# students += ['Olga']
# students += 'Olga'
# print(students)
# print(students.index('Sasha'))
# students.remove('Nik')
# students.append('Nik')
# students.insert('Nik')
# print(students.sort())
# print(students)
# students.reverse()
# print(students)
# print(students[::-1])
#
# a = [1,'A',2]
# b = a
# a[0]=42
# print(a,b)
# Умножение чисел в списке
# a = [0]*5
# print(a)
# a = [0 for i in range(5)]
# print(a)
# a = [i * i for i in range(5)]
# print(a)
# a = [int(i) for i in input().split()]
# print (a)

# программа для суммирования введеных чисел
# a = [int(i) for i in input().split()]
# print(sum(a))д

# задача с вводом 1,3,5,6,10 и просто 10
# задан вопрос на форуме
# a = input().split()
# b = len(a) + 1
# k = 0
# s = 0
# cnt = 0
# it = []
# a.append(k)
# for i, item in enumerate(a):
#      a[i] = int(item)
# for i in a:
#     if len(a) == 1:
#         s = a[0]
#         it = s
#         break
#     if cnt != b:
#         cnt += 1
#     if cnt == b - 1:
#         s = a[cnt -2] + a[0]
#         it.append(s)
#         break
#     if i != a[0]:
#         s = a[cnt - 2] + a[cnt]
#         it.append(s)
#     elif i == a[0] and len(a)>=2:
#         s = a[1] + a[-2]
#         it.append(s)
# string = ' '.join(str(e) for e in it)
# print(string)

# 4 8 0 3 4 2 0 3
# numb_list=input().split()
# print(*(a for a in set(numb_list) if numb_list.count(a)>1))

# изучить решение данной задачи
# from itertools import cycle
# a = list(map(int, input().split()))
# c = cycle(a)
# res = [next(c) for x in range(len(a)*2+1)][len(a)-1:]
# print(a[0] if len(a) == 1 else ' '.join([str(res[x]+res[x+2]) for x in range(len(a))]))

# a = [[1, 2, 3], [4, 5, 6],[7, 8, 9]]
# print(a[1])
#
# print (a[1][1])

# n =3
# a = [[0]*n]*n
# a[0][0]=5
# print(a)
# a= [[0]*n for i in range (n)]
# a = [[0 for j in range (n)] for i in range(n)]

# a = int(input())
# b = int(input())
# c = int(input())
# if a >= b and a >= c:
#     print(a)
#     print(min(b, c))
#     print(max(b, c))
#
# elif b >= a and b >= c:
#     print(b)
#     print(min(a, c))
#     print(max(a, c))
#
# else:
#     print(c)
#     print(min(a, b))
#     print(max(a, b))

# ticket = [int(i) for i in input()]
# list(str(ticket))
# if sum(ticket[0:3])== sum(ticket[3:6]):
#     print('Ваш билет счастливый')
# else:
#     print('Ваш билет обычный')

# p = input()
# quantity_prog = []
# if 0 <= int(p) <= 1000:
#     quantity_prog = [int(qp) for qp in p]
#     programist = 1
#     list(str(quantity_prog))
#     if len(quantity_prog)>=2 and quantity_prog[-2] == 1 and 1<= quantity_prog[-1] <= 4:
#         programist = ''.join(str(e) for e in quantity_prog)
#         print('{} программистов'.format(programist))
#     elif quantity_prog[-1] == 1:
#         programist = ''.join(str(e) for e in quantity_prog)
#         print('{} программист'.format(programist))
#     elif 5 <= quantity_prog[-1] <= 9 or quantity_prog[-1] == 0:
#         programist = ''.join(str(e) for e in quantity_prog)
#         print('{} программистов'.format(programist))
#     elif 2 <= quantity_prog[-1] <= 4:
#         programist = ''.join(str(e) for e in quantity_prog)
#         print('{} программиста'.format(programist))
# else:
#     print('Введено не верное значение!')
# number = int(input())
# number_next = number + 1
# number_previous = number - 1
# print('The next number for the number {} is {}'.format(number, number_next))
# print('The previous number for the number {} is {}'.format(number, number_previous))
# n = int(input())
# print(n%60,n%60)

a = int(input())
b = int(input())
c = int(input())
N = int(input())
l = int(input())
print(a / 2 + b / 2 + c / 2)
shn = (a * (N + N) + b * (N - 1) + l)
