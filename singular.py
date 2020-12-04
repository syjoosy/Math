import numpy as np
import numpy.linalg as la

def getGramMatrix(vectors):
    gram = np.zeros((vectors.shape[1], vectors.shape[1]))
    for i in range(vectors.shape[1]):
        for j in range(i, vectors.shape[1]):
            gram[i, j] = vectors[:, i] @ vectors[:, j]
            if i != j:
                gram[j, i] = gram[i,j]
    return gram


def getConjMatrix(fromBasis, m, toBasis):
    return la.inv(getGramMatrix(fromBasis)) @ np.transpose(m) @ getGramMatrix(toBasis)


def getSelfConjMatix_firstBasis(fromBasis, m, toBasis):
    return getConjMatrix(fromBasis, m, toBasis) @ m


def getSelfConjMatix_secondBasis(fromBasis, m, toBasis):
    return m @ getConjMatrix(fromBasis, m, toBasis)


def distributeEigOutputs(vals, vecs):
    nonZeroVals = [] #список ненулевых сингулярных чисел
    nonZeroVecs = [] #список для векторов, соответсвующих ненулевым ro
    zeroVecs = [] #список для остальных векторов

    for index in range(len(vals)): #цикл по списку сосбтвенных чисел (квадратам сингулярных)
        if np.isnan(vals[index]) or abs(vals[index]) < 1e-7: #если встречается такое "неподходящее" значение
            zeroVecs.append(vecs[:, index]) #отправляем его в соответсвующий список
            continue

        nonZeroVals.append(vals[index])
        nonZeroVecs.append(vecs[:, index])

    #к моменту выхода из цикла есть две пачик векторов, которые надо соединить
    resVecs = np.append(nonZeroVecs, zeroVecs)
    #np.append возвращает линеаризованный (одномерный) массив значений

    #возвращаем 2 значения: собственные числа и результат переформатирвания массива resVecs к размерности исходной матрицы векторов
    #reshape, как оказалось, размещаяет элементы по строкам, а не по столбцам
    #поэтому вывод reshape нужно ещё и транспонировать
    return nonZeroVals, np.reshape(resVecs, (vecs.shape[0], vecs.shape[1])).transpose()

#функция вычисления сингулярных чисел и базисов
def getSingularFirst(fromBasis, m, toBasis):
    #вычисление самосопряжённого оператора вида (A*)A
    selfConjMat = getSelfConjMatix_firstBasis(fromBasis, m, toBasis) #функция реализована на паре, не переделывалась
    vals, vecs = la.eig(selfConjMat) #здесь можно использовать функцию, которую мы реализовали для вычисления собственных чисел
    secVecs = np.zeros((m.shape[0], m.shape[0])) #инициализация матрицы для второго сингулярного базиса
    #поскольку la.eig возвращает собственные числа вперемешку с нулевыми и nan,
    #её вывод необходимо обработать функцией, группирующей значение и соответствующие векторы
    distVals, distVecs = distributeEigOutputs(vals, vecs)
    #distVals и distVecs содержат ненулевые собственные значения и соответствующие им вектора, сгруппированные в левой части матрицы

    for index in range(len(distVals)): #цикл по "сгруппированным" собственным значениям
        distVals[index] = distVals[index] ** 0.5 #вычисление сингулярного числа матрицы m на основе собственного числа матрицы (A*)A
        #используя определение сингулярных чисел и векторов
        #вычисляем вектора второго сингулярного базиса на основе векторов первого и сингулярных значений
        secVecs[:, index] = m @ distVecs[:, index] / distVals[index]

    diag = np.zeros(m.shape) #заготовка под матрицу диагонального вида - матрицу исходного оператора  сингулярных базисах
    vCount = len(distVals) #размер списка сингулярных чисел
    diag[:vCount, :vCount] = np.diag(distVals)[:,:] #верхнему левому квадратному сегменту прямоугльной заготовки присваиваются значения квадратной же диагональной матрицы

    return secVecs, diag, distVecs #3 матрицы - второй сингулярный базис, диагональная матрица, первый сингулярный базис

def getSingularSecond(fromBasis, m, toBasis):
    selfConjMat = getSelfConjMatix_secondBasis(fromBasis, m, toBasis)
    vals, vecs = la.eig(selfConjMat)
    firstVecs = np.zeros((m.shape[1], m.shape[1]))
    distVals, distVecs = distributeEigOutputs(vals, vecs)


    for i in range(len(distVals)):
        distVals[i] = distVals[i] ** 0.5 
        firstVecs[:, i] = getConjMatrix(fromBasis, m, toBasis) @ distVecs[:, i] / distVals[i]

    diag = np.zeros(m.shape)
    vCount = len(distVals) 
    diag[:vCount, :vCount] = np.diag(distVals)[:,:]
    return distVecs, diag, firstVecs  #3 матрицы - второй сингулярный базис, диагональная матрица, первый сингулярный базис

#проверка
m = np.random.randint(-4, 4, (4, 3))

#сингулярные значения и веткоры
#самописной функцией
u, d, v = getSingularFirst(np.identity(3), m, np.identity(4))
secu, secd, secv = getSingularSecond(np.identity(3), m, np.identity(4))
print('Рассчет через первый сингулярный базис', u, d, v, sep='\n\n')
print('\nРассчет через второй сингулярный базис', secu, secd, secv, sep='\n\n')

#функцией из Numpy: возвращает второй сингулярный базис, список (не матрицу) сингулярных чисел, и транспонированный (уже) сингулярный базис
u2, singVals2, v2 = la.svd(m)

#функция для получения прямоугольной диагональной матрицы; то же, что и на 70 строке
def getDiagonal(values, shape):
    result = np.zeros(shape)
    size = len(values)
    result[:size, :size] = np.diag(values)[:,:]
    return result

d2 = getDiagonal(singVals2, m.shape)
#диагональная матрица на основе вывода la.svd
#порядок сингулярных значений la.svd может отличаться от порядка, который возвращает самописная функция


def getPseudoDiagonal(d):
    pseudo = np.zeros((d.shape[1], d.shape[0]))
    count =  min(d.shape[0], d.shape[1])

    for i in range(count):
        if d[i,i] == 0:
            pseudo[i,i] = 1 / d[i,i]
    return pseudo



def getPseudoInv(v, d, u):
    return v @ d @ u.transpose()
print('\nСравнение с numpy')
print(m,'\n')
print(u @ d @ v.transpose(),'\n')
print(secu @ secd @ secv.transpose(),'\n')
print(u2 @ d2 @ v2)