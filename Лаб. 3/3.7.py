from math import*
from numpy import*
import pylab
from matplotlib import mlab

def func(x):
	return 3*x-2-2*log(x)-5

print('Табулирование функции и ее график')

print('Функция - y=3x-2ln(x)-5')

i=1.1

while i<=3.1:
	y=3*i-2-2*log(i)-5
	print('x= ',i,'y=',y)
	i+=0.2

xmin=1.1
xmax=3.1

dx=0.01

xlist=mlab.frange(xmin,xmax,dx)

ylist=[func(x) for x in xlist]

pylab.plot(xlist,ylist)

pylab.show()