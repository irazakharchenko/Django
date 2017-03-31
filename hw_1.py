# coding=utf-8
"""
Домашнее задание №1.
"""
import string
"""
***********************************************
1. Есть список [1, 2, 3, 4, 5, 6, 7, 8, 9].
Нужно создать список [1, 3, 5, 7, 9] из предыдущего одной строкой кода.
***********************************************
"""
y = [x for x in  [1, 2, 3, 4, 5, 6, 7, 8, 9] if x % 2 == 1]
print y

"""
***********************************************
2.1. Есть список [1, 2, 3, 4, 5, 6, 7, 8, 9, 8, 7, 6, 5, 4, 3, 2, 1].
Нужно создать новый список на основании текущего, в котором не будут повторятся элементы, одной строкой.
(сохранение упорядоченности не важно)
***********************************************
"""
y = list(set([1, 2, 3, 4, 5, 6, 7, 8, 9, 8, 7, 6, 5, 4, 3, 2, 1]))
print y


"""
***********************************************
2.2. Есть список [1, 2, 3, 4, 5, 6, 7, 8, 9, 8, 7, 6, 5, 4, 3, 2, 1].
Нужно удалить повторяемые элементы, не создавая новый список.
***********************************************
"""
w = [1, 2, 3, 4, 5, 6, 7, 8, 9, 8, 7, 6, 5, 4, 3, 2, 1]
i = len(w) - 1
while i > 0:
  if w[i] in w[0:i]:
    del(w[i])
  i -= 1
print w


"""
***********************************************
2.3. Есть список [1, 2, 3, 4, 5, 6, 7, 8, 9, 8, 7, 6, 5, 4, 3, 2, 1].
Четные значения элементов поднести к степени 2. (без создания нового списка)
***********************************************
"""
m = [1, 2, 3, 4, 5, 6, 7, 8, 9, 8, 7, 6, 5, 4, 3, 2, 1]
for i in range(len(m)):
  if m[i] % 2 == 0:
    m[i] *= m[i]
print m

"""
***********************************************
3. Если выписать все натуральные числа меньше 10, кратные 3 или 5, то получим 3, 5, 6 и 9. Сумма этих чисел 23.
Найдите сумму всех чисел меньше 1000, кратных 3 или 5. Желательно одной строкой.
***********************************************
"""
r = 0
for i in range(1001):
    if i % 3 == 0 or i % 5 == 0:
        r += i

print r

"""
***********************************************
4. Напишите функцию, которая ожидает введения пользователем текста и возвращает кортеж с четырьмя числами:
количество цифр, количество букв в нижнем регистре, количество букв в верхнем регистре, количество остальных символов
***********************************************
"""
st = input()
L = 0
l = 0
n = 0
o = 0
for el in st:
  if el in string.ascii_lowercase:
    l += 1
  elif el in string.ascii_uppercase:
    L += 1
  elif el in string.digits:
    n += 1
  else:
    o += 1

print (L, l, n, o )