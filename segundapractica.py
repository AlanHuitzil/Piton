#Libreria para generar datos aleatorios
import random

#Libreria para generar gráficas
#Para instalar esto necesitas ejecutar:
#python -m pip install -U pip
#python -m pip install -U matplotlib
import matplotlib.pyplot as plt


#número aleatorio y lo imprime
print(random.randint(1,20))
print(random.randrange(10,100,2))

#Reacomodar una lista al azar
lista = [1,2,3,4,5,6,7,8,9,10]
print('Lista original',lista)

#Mezcla los elementos de la lista al azar
random.shuffle(lista)
#Imprime la lista mezclada
print('Lista mixeada',lista)

#Genera una gráfica de campana de GAUSS
#Genera lo datos de la gráfica
campanaDeGauss = [random.gauss(1,0.5)for i in range(1000)]
#Arma la gráfica
plt.hist(campanaDeGauss, bins=15)
#Muestra la gráfica
plt.show()
