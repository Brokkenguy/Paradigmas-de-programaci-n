#=====================================
#  PROGRAMACIÓN ORIENTADA A OBJETOS
#=====================================

#=================================
# Una clase para un objeto vacío
# No está tan vacío, necesita 
# la palabra pass = pasar
#=================================
class ObjetoVacio:
    pass

#===========================
#  nada es un ObjetoVacio
#===========================
nada = ObjetoVacio()
print(type(nada))

#===================
#  La clase llanta
#===================
class Llanta:
    #======================================
    # Variable cuenta es de toda la clase
    #======================================
    cuenta = 0
    #====================================
    #  Función constructora de identidad 
    #  __init__ es una función reservada 
    #  comienza con uno mismo: self
    #  pero puede ser otro nombre (mi)
    #  parámetros de entrada = default
    #====================================
    def __init__(mi,radio=50,ancho=30,presión=1.5):
        # variable de la estructura completa Llanta
        Llanta.cuenta += 1
        # variables exclusivas de cada objeto
        mi.radio = radio
        mi.ancho = ancho
        mi.presión = presión

#===========================
# Objetos (instanciados)
#===========================
llanta1 = Llanta(50,30,1.5)
llanta2 = Llanta(presión=1.2)
llanta3 = Llanta()
llanta4 = Llanta(40,30,1.6)

#=================










