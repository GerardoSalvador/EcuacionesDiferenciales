from matplotlib import pyplot as plt

#Se definen los valores obtenidos mediante solucion de la ec. dif
c1 = -3; c2 = 1
#se define el intervalo
x = [-2,-1,0,1,2]

#arreglo o lista donde se guardara los datos obtenidos en "y"
valores = []

#se crea encabezado de tabla
print("|\tx\t|\ty")

#se crea el iterable
for n in x:
    #sustitucion de valores en la ecuacion 
    y = -3+(n)+(1/12)*n**(4)+(1/2)*n**(2)
    g = (str(y))
    g = (g[0:10])
    g = float(g)

    #se agregan los resultados de "y" en el arreglo o lista
    valores.append(g)

    #se imprime tabla
    print("|\t",n,"\t|",y)

print(valores)

#se crea grafica
plt.plot(x,valores,'c-o')
#etiqueta de ejes
plt.xlabel("eje X")
plt.ylabel("eje Y")
#titulo
plt.title(r'$y=-3+x+\frac{1}{12}x^{4}+\frac{1}{2}x^{2}$')
plt.grid(True)
plt.axhline(0,color='r',lw=1)
plt.axvline(0,color='r',lw=1)
plt.show()