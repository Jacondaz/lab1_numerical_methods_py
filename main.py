import numpy as np


def unknown(matrix_b, matrix_c):
    sum_mult = 0  # сумма произведений элементов B на C
    sum_pov = 0  # сумма квадратов элементов B
    for j in range(len(matrix_b)):
        sum_mult += matrix_b[j] * matrix_c[j]
    for j in range(len(matrix_b)):
        sum_pov += matrix_b[j][0] ** 2
    lyambda = sum_mult / sum_pov
    lyambda = round(lyambda[0], 3)

    return lyambda


dimension = int(input("Введите размерность матрицы: "))
e = 0.001
flag = 0
A = np.ones((dimension, dimension))  # Матрица A
print("Введите элементы матрицы A: ", end='\n')
for i in range(dimension):
    k = list(map(int, input().split()))
    A[i] = k
if np.linalg.det(A) != 0:
    flag = 1
print('')
print("Введите элементы вектора B: ", end='\n')
B = np.ones((dimension, 1))  # Вектор B
k = list(map(int, input().split()))
for i in range(len(k)):
    B[i] = k[i]

C = A.dot(B)  # C - вектор при умножении A на B
b1 = B.copy()  # копия матрицы B
c1 = C.copy()  # копия вектора полученного при умножении
e_max = unknown(b1, c1)  # следующий лямбда#
e_curr = 0  # предыдущий лямбда#
count = 1

while (abs(e_max - e_curr)) >= e:  # прямой цикл
    b1 = c1
    c1 = A.dot(b1)
    e_curr = e_max
    e_max = unknown(b1, c1)
    count += 1
    #print("Итарация № ", count)
    #print("Лямбда: ", e_max)
print('max = ', e_max)
print("Количество итераций: ", count)


if flag == 1:
    a1 = np.linalg.inv(A)
    C = a1.dot(B)
    b2 = B.copy()
    c2 = C.copy()
    e_max2 = unknown(b2, c2)  # следующий лямбда#
    e_curr2 = 0  # предыдущий лямбда#
    count2 = 1

    while (abs(e_max2 - e_curr2)) >= e:  # обратный счёт#
        b2 = c2
        c2 = a1.dot(b2)
        e_curr2 = e_max2
        e_max2 = unknown(b2, c2)
        count2 += 1
    e_max2 = round(1 / e_max2, 3)

    print('min = ', e_max2)
    print('Количество итераций: ', count2)
else:
    print("Матрица вырожденная, не удалось найти минимальное собственное значение")

