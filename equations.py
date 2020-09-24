import numpy as np
import matplotlib.pyplot as plt
import numpy.linalg as alg


x = np.arange(0, 20, 0.1)
y = np.sin(x * np.pi / 5) * 2

# x = exp(-x)
def transFunc(x):
    return np.exp(np.negative(x)) - x


def roots_binary(left, right, f, eps):
    if f(left) * f(right) > 0:
        print('Корней нет или их четное количество')
        return None
    middle = (left + right) / 2
    mids = [middle]
    while abs(left - right) > eps:
        if f(middle) * f(left) < 0:
            right = middle
        else:
            left = middle
        middle = (left +right) / 2
        mids.append(middle)
    return middle, mids

def roots_newton_inner(start, f, eps):
    def getDerivative(x, f, delta):
        return (f(x + delta) - f(x)) / delta
    def getSecondDerivative(x, f, delta):
        return (getDerivative(x + delta) - getDerivative(x)) / delta
    return None


root, riter = roots_binary(0.4, 0.8, transFunc, 1e-6)
color = range(len(riter))
fg = plt.figure()
#plt.subplot(121)
#print(roots)
plt.scatter(riter, transFunc(riter),s = 30,c=color, cmap='viridis')
plt.plot(x, transFunc(x), 'b-')
plt.plot(x, x, 'r-')
#plt.plot(args, roots, '-m')


plt.plot(x, np.exp(np.negative(x)), 'g-')
plt.scatter(root, transFunc(root),s = 10)


plt.axis()
plt.grid()

'''
plt.subplot(122)
xy = np.random.random((200, 200))
plt.contour(xy)
'''

#plt.show()

#23.09.20

m = np.random.randint(-2, 2, (3, 3))
mSelfConj = m @ m.transpose()


eVals = alg.eigvals(mSelfConj)
hCoeffs = np.poly(eVals)


def PolynominalFactory(hCoeffs):
    return lambda x: np.polyval(hCoeffs,x)


polynominal = PolynominalFactory(hCoeffs)


xH = np.arange(0, 50, 0.1)
yH = polynominal(xH)


fg = plt.figure()
plt.plot(xH, yH, 'r')


def getCoefficients(a):
    tr = np.trace(a)
    if a.shape == (3,3):
        return (1, -tr, -(np.trace(alg.matrix_power(a, 2)- tr ** 2)) / 2, 
        -alg.det(m))
    else:
        raise Exception('Матрица должна быть 3x3')

polynominal_2 = PolynominalFactory(getCoefficients(mSelfConj))
yU = polynominal_2(xH)
plt.plot(xH, yU, 'b')
diff = yH - yU
print(np.max(diff), np.average(diff), np.std(diff - np.average(diff)))
plt.plot(xH, diff, 'g')
plt.axvline(x=0, c = 'k')
plt.axhline(y=0, c = 'k')
'''
rootOne, iterOne  = roots_binary(0, 0.1, polynominal, 1e-10)
rootTwo, iterTwo = roots_binary(3, 3.5, polynominal, 1e-10)
rootThree, iterThree = roots_binary(5, 10, polynominal, 1e-10)
print(rootOne, rootTwo, rootThree)
'''
plt.show()