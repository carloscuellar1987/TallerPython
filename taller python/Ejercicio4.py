# algoritmo desarrollado por carlos cuellar
"""
Cree un algoritmo que dados dos números con decimales y un símbolo (+,
-, * y /), el cálculo correspondiente de acuerdo con el símbolo ingresado y
muestre en pantalla el resultado de la operación. Se debe crear un
método por cada uno de los símbolos u operaciones.
"""

from ast import Import
import Funciones
print('''buen dia señor usuario este algoritmo nos permite realizar
      operaciones  matematicas basicas  como suma, resta, division y multiplicacion
      porfavor siga las instrucciones  atentamente..
      ''')

val1=float(input('porfavor ingrese el primer numero   :  '))
val2=float(input('porfavor ingrese el segundo numero  :   '))

resultado = Funciones.Aritmetica(val1,val2)



        
    
    