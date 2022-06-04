# algoritmo desarrollado por carlos cuellar

""" Escribir un algoritmo que permita ingresar y recibir información de una
persona por consola, la información que debe recibir es:
o Tipo de documento (a escoger).
o N.° de documento (entero).
o Nombre (string).
o Edad (entero).
o Sexo (char).
o Peso (double).
o Altura (a escoger).

"""


from ast import Str, While
print('''
      buen dia señor usuario este algoritmo recoge sus datos personales
      y calcula  si usted se encuentra en sobre peso porfavor siga
      atentamente las  instrucciones ......
      ''')

datos={'tipo de docuemneto':'','numero de documento': int,'nombre':str,'edad':int,'sexo':str,'peso':int,'altura': float, }
#funsion para capturar datos

def captura(val):
    print(' se requiere su ',val,'  por favor  ingrese el dato  :')
    per=input()
    return datos.update({val:per})
###########################################################################################

# FUSION PARA SELECIONAR DOCUMENTO
def selecDocumento(val):
    print('''PORFAVOR SELECIONE SU TIPO DE DOCUMENTO CON EL NUMERO
          1 CEDULA CIUDADANIA
          2 CEDULA DE EXTRANJERIA
          3 TARJETA IDENTIDAD
          4 PASAPORTE''')
    tipo=str(input())
    while tipo!='4'and tipo!='3'and tipo!='2'and tipo!='1':
        print('''INGRESO MAL SU SELECION PORFAVOR SELECIONE SU TIPO DE DOCUMENTO CON EL NUMERO
          1 CEDULA CIUDADANIA
          2 CEDULA DE EXTRANJERIA
          3 TARJETA IDENTIDAD
          4 PASAPORTE''')
        tipo=str(input())
    if tipo== '1':
        documento= 'CEDULA CIUDADANIA'
    elif tipo =='2':
        documento ='CEDULA DE EXTRANJERIA'
    elif tipo == '3':
        documento = 'TARJETA IDENTIDAD'
    else:
        documento = 'PASAPORTE'
    
    
    return datos.update({val:documento})

#selecion de  sexo
def Sexo(val):
    print(''' porfavor ingrese su  genero
          INGRESE 1 PARA MASCULINO
          INGRESE 2 PARA FEMENINO
          INGRESE 3 PARA  OTRO
          ''')
    genero =str(input())
    while genero!='1' and genero!='2' and genero!='3':
         print(''' SUS DATOS SON ERRONEOS PORFAVOR VUELVA A INGRESARLOS
          INGRESE 1 PARA MASCULINO
          INGRESE 2 PARA FEMENINO
          INGRESE 3 PARA  OTRO
          ''')
         genero =str(input())
    if genero=='1':
        dato='MASCULINO'
    if genero=='2':
        dato='FEMENINO'
    if genero=='3':
        dato=input('PORFAVOR INGRESE SU GENERO...  ')

    return datos.update({val:dato})
        
        
    
#### realizamos un for para recorrer el dicionario HE INGRESAR DATOS
for cont1 in datos:
    #print(cont1)
    if cont1 == 'tipo de docuemneto':
         
        dato=selecDocumento(cont1)
    elif cont1=='numero de documento':
        dato=captura(cont1)
        
    elif cont1=='nombre':
        dato=captura(cont1)
        
    elif cont1 =='edad':
        dato=captura(cont1)
        
    elif cont1 =='sexo':
        
        dato=Sexo(cont1)
          
    elif cont1 =='peso':
        print('RECUERDE QUE EL PESO DEBE SER INGRESADO EN  kg')
        dato=captura(cont1)
           
    elif cont1 =='altura':
        print('RECUERDE QUE LA ALTURA DEBE SER INGRESADA EN CM')
        #alturas = float(input('ingrese su altura  :  '))
       # altura =datos.update({datos:altura})

        dato=captura(cont1)
        
        
    ####  codigo  de salida al usuario 

for cont2 in datos:
    print('sus datos son ',cont2,' su informacion es : ',datos[cont2])
    
    if cont2=='edad':
        if datos['edad']>= '18':
            print('eres mayor de edad')
        else:
            print('eres menor de edad')
    
    if cont2=='altura':
        dato1= float(datos['altura'])/100
        
        dato2 =float(datos['peso'])
        
        icm =float(dato2/(dato1*dato1))
        print('tu indice de masa  coorporal es  de  :  ',icm)
        if icm < 18.5:
            print(' estas bajo de  peso')
        elif (icm>18.5 and icm <24.9):
            print('estas en un peso normal')
        elif (icm >24.9 and icm<29.9):
            print('estas en sobrepeso')
        elif (icm>30.0):
            print('estas obeso')
            
            
            
            
            
            
        
        


        

    
