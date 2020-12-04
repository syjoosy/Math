import numpy as np
import numpy.linalg as linalg
import itertools as it
import matplotlib.pyplot as plt

class LinAlg:

  def ValuesSet(self):
    self.size = int(input("Введите размерность квадратной матрицы (линейного оператора):"))
    self.min = float(input("Минимальное значение элемента матрицы:"))
    self.max = float(input("Максимальное значение элемента матрицы:"))
    self.lev = float(input("Левая граница поиска корней:"))
    self.prav = float(input("Правая граница поиска корней:"))
    self.shag = float(input("Искать с шагом:"))

  def LinearOperator(self):

    m = np.random.uniform(self.min, self.max, (self.size, self.size))
    mSelfConj = m @ m.transpose()

    def getMiddle(left, right):
      return (left + right) / 2

    def GetCoefficients(m):
      if m.shape[0] == m.shape[1]:
        diagonal = list(range(0, m.shape[0]))
        coeffs = [(-1) ** m.shape[0], np.trace(m) * ((-1) ** (m.shape[0] - 1))]
        for i in range(2, m.shape[0]):
          comb = list(it.combinations(diagonal, i))
          coords = [list(it.product(j, j)) for j in comb]
          det = 0
          for coord in coords:
            minor = np.reshape([m[c[0], c[1]] for c in coord], (i, i))
            det += linalg.det(minor)
          coeffs.append(det * ((-1) ** (m.shape[0] - i)))
        coeffs.append(linalg.det(m))
        return coeffs
      else:
        raise Exception('Матрица должна быть квадратной')

    coeffs = GetCoefficients(mSelfConj)

    def PolynominalFactory(coeffs):
      return lambda x: np.polyval(coeffs, x)

    polynominal = PolynominalFactory(coeffs)

    def FindRootRanges(initial, final, lenght, rootscount, f):
      ranges = []
      left_x = initial
      left_y = f(left_x)
      right_x = left_x + lenght
      right_y = f(right_x)
      while right_x < final and len(ranges) < rootscount:
        if left_y * right_y < 0:
          ranges.append([left_x, right_x])
        left_y = right_y
        left_x = right_x
        right_x += lenght
        right_y = f(right_x)
      return ranges

    def roots_binary(left, right, f, eps):
      if f(left) * f(right) > 0:
        print('Корней нет или их четное количество')
        return None
      middle = getMiddle(left, right)
      mids = [middle]
      while abs(left - right) > eps:
        if f(middle) * f(left) < 0:
          right = middle
        else:
          left = middle
        middle = getMiddle(left, right)
        mids.append(middle)
      return middle, mids

    ranges = FindRootRanges(self.lev, self.prav, self.shag, self.size, polynominal)
    roots = []
    for interval in ranges:
      roots.append(roots_binary(interval[0], interval[1], polynominal, 1e-10)[0])

    return m, ranges, roots, coeffs, self.size




sol = LinAlg()      #создаём объект класса для нахождения решения
sol.ValuesSet()    #вызываем метод, который проделывает вычисления

matrix, ranges, roots, coeffs, size = sol.LinearOperator()

print('Линейный оператор:', matrix, sep='\n')
print('Диапазоны нахождения корней характеристического уравнения в пределах поиска:', ranges, sep='\n')
print('Корни характеристического уравнения в пределах поиска:', roots, sep='\n',)
print('Коэффициенты характеристического уравнения:', coeffs, sep='\n')

def charakterx(x,coeffs,size,n): #рекурсивная функция вычисления характеристического уравнения
   fx = 0
   if size - 1 > -2:
     fx = (x ** size)*coeffs[n] + charakterx(x,coeffs,size - 1, n + 1)
   return fx

if len(roots) > 0:
  for i in range(0,len(roots),1):
    x = np.linspace(roots[i]-5, roots[i]+5, 10000)
    y = charakterx(x,coeffs,size, 0)
    plt.title('  на этом графике отображён корень х' + str(i) + ' = ' + str(roots[i]))
    plt.plot(x, y)
    plt.plot(x, np.zeros(10000))
    mask = np.abs(y) < 1e-1
    plt.scatter(x[mask], y[mask], color='black', s=40, marker='o')
    plt.show()




