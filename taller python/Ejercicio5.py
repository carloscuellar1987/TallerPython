#ejercicio desarrollado por carlos  cuellar
'''Cree un algoritmo que calcule el factorial de un valor numérico introducido
como parámetro o argumento en la línea de comandos'''
from math import factorial
print('''buen dia señor usuario este algoritmo nos  permite
      calcular el factorial  de  un numero  ingresado...
      ''')

dato =int(input('ingrese el numero para sacar el factorias:   '))

fact = 1
for i in range(1,dato+1):
    fact =fact*i
    print(fact)
    
    
print('el factorial del numero, ',dato,'  es   ',fact)