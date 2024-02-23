import numpy as np

#Obtener los vectores X, Y
nomarch = input('Enter the name of the data file: ')
archivo = open(nomarch + '.csv', 'r')
x = []
y = []
for line in archivo:
 data = line.strip().split(',')
 x.append(float(data[0]))
 y.append(float(data[1]))
archivo.close()

#Crear la matriz A 
xvector = np.array(x).reshape(len(x),1)
yvector = np.array(y).reshape(len(y),1)
fill = np.array([0,0])
a = xvector + fill
a[:,:1] = 1

#Calcular el vector que minimiza ||y-yi||
aT = np.transpose(a)
aTa = np.dot(aT,a)
aTaINV = np.linalg.inv(aTa)
aTaINVaT = np.dot(aTaINV, aT)
u = list(np.dot(aTaINVaT, yvector).flatten())
print('Linear function: y = ', u[1], 'x + ',u[0])