"""
EJERCICIO 3
Crea un algoritmo que calcule el área de un círculo, cuadrado o triángulo,
para ello el sistema debe pedir la figura de la que se quiere calcular su
área y según lo introducido pedirá los valores necesarios para calcular el
área. Se debe crear un método por cada figura para calcular cada área,
este devolverá un número real mostrándolo en pantall"""
#ALGORITMO DESARROLLADO POR CARLOS CUELLAR

from ast import Import
import Funciones



print(' este algorimo  puede calcular el area de un circulo, de cuadrado y de  trangulo')
figura = str(input(' por favor ingrese un valor  del 1 al 3  ciendo 1 circulo, 2 cuadrado, 3 triangulo  :  '))


while figura!='3' and figura!='2' and figura!='1' :# ponemos un ciclo whilie para garantizar el usuario ingrese bien la selecion
    figura = str(input(' por favor ingrese BIEN el valor  recuerde que del 1 al 3  ciendo 1 circulo, 2 cuadrado, 3 triangulo  :  '))
    
    
if figura =='1':
    res = Funciones.circulo(figura)
    
else:
    if figura =='2':
        res=Funciones.cuadrado(figura)
    else:
        res= Funciones.tringulo(figura,float)
        
        
    
    