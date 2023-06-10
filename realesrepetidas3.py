#Se importan librerias necesarias
from math import e
from matplotlib import pyplot as plt

#Se definen los valores obtenidos mediante solucion de la ec. dif
c1 = 3; c2 = 18
#se define intervalo
x = [0,1,2,3,4]

#arreglo o lista donde se guardara los datos obtenidos en "y"
valores = []

#se crea encabezado de tabla
print("|\tx\t|\ty")

#se crea el iterable
for n in x:
    #sustitucion de valores en la ecuacion 
    y = (c1 + c2*(n))*e**(-7 * n)

    #se agregan los resultados de "y" en el arreglo o lista
    valores.append(y)

    #se imprime tabla
    print("|\t",n,"\t|",y)

#print(valores)
valoresy=[3.0,0.0191495212,3.2429620045,4.3220594439,5.1858000802]

#se crea grafica
plt.plot(x,valoresy,'r-o')
#etiqueta de ejes
plt.xlabel("eje X")
plt.ylabel("eje Y")
#titulo
plt.title(r'$f(y)=(c_{1}+c_{2}x)e^{-7x}$')
plt.grid(True)
plt.axhline(0,color='r',lw=1)
plt.axvline(0,color='r',lw=1)
plt.show()