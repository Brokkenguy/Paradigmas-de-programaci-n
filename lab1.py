""" ESTE ES UN SUPERCOMENTARIO
    DE INICIO
"""

#====================
# Operaciones básicas
#====================
print (2+3)
print (2/3)
print (2**10)
print (2**0.5) #raíz cuadrada
print (10%2)
print (10%0.1) #exclusivo en python

#=========================================
#Para saber el tipo de objeto se usa type
#=========================================
t=0
print (type(t)) # entero
t=3.6
print (type(t)) # real (flotante)
t=True
print (type(t)) # boleano (bool)

#=====================
#mensajes de pantalla
#=====================
print ("Este es un comando de pyton. ", " Este es otro enunciado.", t)
print('id:',1)
print ('first Name:', 'Steve')
print ('Last Name:', 'jobs')
print("vamos a sumar esto" + "con esto otro")
#===============================================
# Continuar una instrucción en varios renglones 
#===============================================
if 100 > 99 and \
   200 <= 300 and \ 
   True != False:
        print('Hello World!')

#=======================================
# Comandos diferentes en la misma línea
#=======================================

print("Hola"); print("tu!") #Se considera mala práctica

#=================================================
# Usando paréntesis redondos, cuadrados o llaves 
# Se puede escribir en varios renglones
# ================================================
list=[1, 2, 3, 4,
      5, 6, 7, 8,
      9, 10, 11, 12]

matriz= [ [1,2,3,4],[5,6,7,8],[9,10,11,12] ]

print(list)
print(matriz)

#==================================================================
# Identación estricta para procesos dependientes de : (dos puntos)
#==================================================================
if 10>5:
   print("diez es mayor que cinco")
   print("otra identificación")
for i in list:
   print (i)
   print("ok")
if 10>5:
   print("verdadero")
   if 10<20:
      print("verdadero")
elif 5>3: #comienza segundo condicional
   print("esto no se imprimirá")
else: 
   print("aqui nunca llega")
#===========
# Funciones
#===========
def say_hello(name):
    print("Hello",name)
    print("Welcome to python Tutorials")

say_hello("Julián")
