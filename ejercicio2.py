# Ejercicio 2: Modelar una computadora
# 
# En este archivo debés crear la clase Computadora siguiendo las consignas del README.
# Recordá:
# - Definir atributos relevantes en el constructor (__init__), con valores por defecto.
# - Implementar el método __str__ para mostrar la información esencial.
# - Instanciar al menos 3 computadoras con distintos valores.
# - Llevar la cuenta de computadoras creadas (usar variable de clase).
# - Implementar al menos 2 métodos de los sugeridos (updateOS, PM, addRAM, getCapacity).
# - Crear otra clase para un componente (ej: Disco, RAM, etc.) con su propio __init__, __str__ y al menos un método.
# 
# ¡No olvides probar todos los métodos y comentar tu criterio para los valores


class Computadora:

    contador=1

    def __init__(self,marca,modelo,memoria,sistoperativo):
        self.id=Computadora.contador
        self.marca=marca
        self.modelo=modelo
        self.memoria=memoria
        self.sistoperativo=sistoperativo
        Computadora.contador+=1
        
    def __str__(self):
        return "La computadora es de la marca {}, modelo {}, tiene {}GB de memoria y {} es el sistema operativo".format(self.marca,self.modelo,self.memoria,self.sistoperativo)

    def updateOS(self,nuevoOS):
        print(f"Actualizando sistema operativo de {self.sistoperativo} a {nuevoOS}...")
        self.sistoperativo=nuevoOS

    def getCapacity(self,componente):
        if componente.lower()=="memoria":
            print(f"La capacidad de la memoria es de {self.memoria}GB")
        else:
            print("No se encontro informacion del componente")


class Memoria:

    def __init__(self,marca,capacidad):
        self.marca=marca
        self.capacidad=capacidad

    
    def __str__(self):
        return f"La memoria tiene capacidad de {self.capacidad}GB"

    


if __name__=="__main__":
    compu=Computadora("Samsung","vision",250,"ryzen")

    compu.updateOS("Windows")
    print(compu)

    compu.getCapacity("memoria")


