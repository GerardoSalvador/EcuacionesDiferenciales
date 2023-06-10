from matplotlib import pyplot as plt

# se definen los valores obtenidos mediante solucion de la ec. dif
c1=-3; c2=1
# se define el intervalo
#x= [-1 <=, <=1] con incrementos de 0.25+
x= [-1,-0.75,0-.50,-0.25,0,0.25,0.50,0.75,1]
#arreglo de valores donde se guardaran los datos obtenidos en "y"
valores =[]
#se crea encabezado de la tabla
print("|\tx\t|\ty")

#se crea el valor iterable
for n in x:
    #sustitucion de valores en la ecuacion
    y= c1+c2*(n)+(1/12)*n**(4)+(1/2)*n**(2)
    g= (str(y))
    g=(g[0:10])
    g= float(g)
    valores.append(g)
    print ("|\t",n,"\|",y)

print (valores)

plt.plot(x,valores,'c-o')

plt.xlabel("eje x")
plt.ylabel("eje y")

plt.title(r'$y=1+-2x+\frac{1}{12}x^[4]+\frac{1}{2}x^2{2}$')
plt.grid(True)
plt.axhline(0,color='r',lw=1)
plt.axvline(0,color='r',lw=1)
plt.show()