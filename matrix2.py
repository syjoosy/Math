import numpy as np
import numpy.linalg as la
import random

#некоторая случайная матрица
mat = np.array([random.randint(-2,3) for x in range(16)]).reshape((4,4))
#получение самосопряжённого оператора, гарантирующего действительность и положительность собственных чисел
matConj = mat @ mat.transpose()

eVals, eVecs = la.eig(matConj) #вычисление собственных чисел каким-либо способом

#фукнция, вычисляющая собственные векторы
def getEigenVectors(m, values): #2 входных аргумента - матрица линейного отображения и собственные числа
    size = m.shape[0] #размер матрицы
    vectors = [] #контейнер, в который будут добавляться собственные вектора по мере вычисления
    for v in values: #векторов столько же, сколько и чисел - нужен цикл
        hMat = m - v * np.identity(size) #вычисление характеристической матрицы
        #последняя координата вектора принимается равной 1
        #выполняется переход от однородной системы уравнений с матрицей nxn
        #к системе уравнений с матрицей (n-1)xn и вектором свободных членов, составленному из крайнего правого столбца коэффициентов
        lesMat = hMat[0:size - 1, 0:size - 1] #матрицу новой системы получаем с помощью среза
        lesVec = np.negative(hMat[0:size - 1,size-1:size]) #вектор свободных членов также получется с помощью среза
        #необходимо изменить знак компонент вектора, потому что он переносится через знак равенства
        #независимо от того, какое собственное число рассматривается, вектор свободных членов не меняется
        #поэтому его можно было бы получить до входа в цикл
        vecArr = la.solve(lesMat, lesVec) #решение полученной системы линейных уравнений с вычислением оставшихся координат
        vecArr = np.append(vecArr, 1) #дописывается значение последней координаты
        vectors.append(vecArr / la.norm(vecArr)) #вектор нормируется (опционально) и добавляется к коллекции собственных веткоров

    return vectors

#проверка
eVecsTwo =  getEigenVectors(matConj, eVals) #вычисление собственных векторов предложенным способом
#собственные векторы должны удовлетворять следующему условию: A * vec = lambda * vec
#где А - матрица линейного преобразовнаия, lambda - собственное число, vec - соответствующий ему собственный вектор
for i in range(len(eVals)):
    print(matConj @ eVecsTwo[i] - eVals[i] * eVecsTwo[i])

#использование векторов, возвращаемых функцией np.eig(...)
#векторы возвращаются функцией в виде матрицы, которая хранится в памяти построчно
#поэтому обращение к ней вида eigVecs[i] возвращает не i-й собственный вектор,
#а i-ю строку матрицы собственных векторов
#поэтому на паре получались противоречащие друг другу результаты
#
#извлечь столбцы из такой матрицы можно либо транспонированием, либо извлечением среза
print('Векторы, возвращаемые функцией np.eig(...). Доступ с помощью транспонирования')
for i in range(len(eVals)):
    print(matConj @ eVecs.transpose()[i] - eVals[i] * eVecs.transpose()[i])
#или
print('альтернативный способ с использованием среза')
for i in range(len(eVals)):
    print(matConj @ eVecs[0:, i:i+1] - eVals[i] * eVecs[0:, i:i+1])


#приведение матрицы к диагональному виду - на паре этого не было, но учитывая полученный результат, это легко выполнить
#матрица, составленная из собственных вектор-столбцов, может выполнять роль матрицы перехода к новому базису (или матрицы подобного преобразования),
#в котором матрица линейного преобразования имеет диагональный вид
#причём на главной диагонали располагаются собственные числа исходной матрицы
#то есть справедливо
print(np.array(eVecsTwo).transpose() @ np.diag(eVals) @ np.array(eVecsTwo) - matConj)#нулевая матрица
#или
print(np.array(eVecsTwo) @ matConj @ np.array(eVecsTwo).transpose() - np.diag(eVals))#также нулевая матрица