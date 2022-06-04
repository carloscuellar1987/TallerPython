# algorimo desarrollado por carlos cuellar
"""De manera libre el estudiante debe crear un algoritmo que haga uso de los
diferentes operadores existentes. Se espera que cree un método en el que
se haga uso de los diferentes tipos de operadores:
o Operadores unitarios: -, +, --, ++.
o Operador de asignación: = (en este método se espera que el
estudiante haga uso de declaraciones compuestas del tipo +=, -=,
*=, /=, %=).
o Operadores relacionales: ==, !=, <, <=, >=.
o Operadores lógicos: &&, ||.
o Operador ternario: condición ? if true : if false.
"""

import FuncionesYClases

print('''
      buen dia señor ususario   este algoritmo nos permite  realizar  operaciones  de comparacion  
      entre dos numeros  enteros y tambien nos permite realiazar  operaciones 
      como multiplicacion, suma resta,division   y modulo de  dos numeros ingresados....
      
      
      ''')
        
s= FuncionesYClases.Ejercicio1()
s.dato()
#print(s.n1+s.n2)
print(' vamos a determinar  que numero es mayor')
if s.n1>s.n2:
    
    print('el numero ingresado ',s.n1,'es mayor que el numero  :  ',s.n2)
    
elif s.n1<s.n2:
    print('el numero ingresado ',s.n2,'es mayor que el numero :   ',s.n1)
elif s.n1==s.n2:
    print('el numero ingresado ',s.n2,'es igual que el numero  :   ',s.n1)
    
    
    
valor1=int(input('ingrese el numero uno : '))
valor2=int(input('ingrese el numero dos : '))
nombre=['','.suma','.resta','.multiplicacion','division','.modentero','.modentero2'] # creamos una lista  para poder visualizar autamtico el resulatdo de la operacion 

  

resultado = FuncionesYClases.Operaciones(valor1,valor2)
print('la suma de  los numeros ',valor1,'  y el numero ',valor2, ' es:  ',resultado.suma)
print('la resta de  los numeros ',valor1,'  y el numero ',valor2, ' es:  ',resultado.resta)
print('la division de  los numeros ',valor1,'  y el numero ',valor2, ' es:  ',resultado.division)
print('la multiplicacion de  los numeros ',valor1,'  y el numero ',valor2, ' es:  ',resultado.multiplicacion)
print('el modulo  de  los numeros ',valor1,  ' es:  ',resultado.modentero)
print('el modulo  de  los numeros ',valor2,  ' es:  ',resultado.modentero2)

