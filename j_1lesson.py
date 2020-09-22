import matplotlib.pyplot as plt
import numpy as np
import random
x = np.arange(0,20,0.1)
y = np.sin(x * np.pi /5) * 2
lst = []
#x = exp(-x)
def transFunc(x):
    return np.exp(np.negative(x)) - x

def roots_binary(left, right, f, eps):
    if f(left)*f(right) > 0:
        print('Корней нет или их четное количество')
        return None
    
    middle = (left + right) / 2
    lst.append(middle)
    while abs(left-right) > eps:
        if f(middle)*f(right) < 0:
            left = middle
        else:
            right = middle
        middle = (left + right) / 2
        lst.append(middle)
    return middle

def roota_newton_inner(start,f,eps):
    def getDerivative(x,f,delta):
        return (f(x + delta)-f(x)) / delta
    #def getSecondDerivative()

root = roots_binary(0.4,0.8, transFunc, 1e-4)
fg = plt.figure(figsize=(5,5))
#plt.subplot(121)
plt.plot(x,transFunc(x),'b-') #color - blue, style - sploshnoy
plt.plot(x,x,'r-')
plt.plot(x, np.exp(np.negative(x)),'g-')
plt.scatter(root,transFunc(root),s = 10)

plt.grid()
'''
plt.subplot(122)
xy = np.random.random((200,200))
plt.contour(xy)
'''
#plt.subplot(122)
for x in lst:
    plt.scatter(x,transFunc(x), s= 10, c= 'black')
'''
Задача сохранить приблеженные, промежуточные Х и визуализировать 
'''

plt.show()