


### funciones de  ejercicio3##########################################################################
def circulo(n1):
    n1=float(input('ingrese el valor del radio :  '))
    area =(n1*n1)*3.141592
    return print('el area del circulo es  :  ',area)

def cuadrado(n2):
    n2=float(input('ingrese el valor del lado:  '))
    area=(n2*n2)
    return print('el area del cuadrado es de : ',area)
def tringulo(val1,val2):
    val1=float(input(' porfavor ingrese el valor  de la base :  '))
    val2= float(input('porfavor ingrese  el valor de la altura:  '))
    area =(val1*val2)/2
    return print('el area del trainagulo es de  : ',area)

##########################################################################
   ## FUNCIONES DEL EJERCICIO 4




class Calculadora:
    def __init__(self,dato1,dato2):
        self.suma =dato1+dato2
        self.resta =dato1-dato2
        self.multiplicacion =dato1*dato2
        self.division = dato1/dato2
        


    
        
def SelecOperacion():
    print(''' porfavor ingrese el tipo de operacion que quiere hacer:
                  para sumar ingrese : +
                  para restar ingrese : -
                  para multiplicar ingrese : *
                  para dividir ingrese   : /         
                 ''')
    opreracion=str(input())
    while opreracion !='+'and opreracion!='-'and opreracion!='*'and opreracion!='/' :
        print(''' porfavor ingrese bien  el tipo de operacion que quiere hacer:
                  para sumar ingrese : +
                  para restar ingrese : -
                  para multiplicar ingrese : *
                  para dividir ingrese   : /         
                 ''')
        opreracion=str(input())
        
    
        
    return opreracion

def Aritmetica(dato1,dato2):
    operacion = Calculadora(dato1,dato2)
    signo =SelecOperacion()
    if signo =='+':
        resultado = operacion.suma
        print('EL RESULTADO DE LA SUMA  DE  ',dato1,' Y DE  ',dato2,'ES  = ',operacion.suma)
    elif signo=='-':
        print('EL RESULTADO DE LA RESTA  DE  ',dato1,' Y DE  ',dato2,'ES  = ',operacion.resta)
    elif signo=='*':
        print('EL RESULTADO DE LA MULTIPLICACION  DE  ',dato1,' Y DE  ',dato2,'ES  = ',operacion.multiplicacion)
    elif signo=='/':
        
        print('EL RESULTADO DE LA DIVISION   DE  ',dato1,' Y DE  ',dato2,'ES  = ',operacion.division)
        
    

###########################################################################
