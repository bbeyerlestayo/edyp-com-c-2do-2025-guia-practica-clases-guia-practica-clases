# Este archivo corresponde al Ejercicio 1 de la guía práctica sobre Clases.
# Aquí deberás implementar la clase Camion y resolver los puntos a, b, c, d y f según las consignas


class Camion:

    patentes_existentes=[]
    lista_camiones=[]

    def __init__(self,patente, marca, carga, anio):
        if patente.lower() in Camion.patentes_existentes:
            raise ValueError (f"La patente {patente} ya existe")
        self.patente = patente
        self.marca = marca
        self.setter_carga(carga)
        self.anio = anio
        Camion.patentes_existentes.append(patente.lower())
        Camion.lista_camiones.append(self)

    def __str__(self):
        return f"Camión: #{self.patente} \nCarga: {self.carga} \nMarca: {self.marca} \nAño: {self.anio}"
    
    def __eq__(self,otro):
        if isinstance(otro,Camion):
            return (self.patente==otro.patente and
                    self.marca==otro.marca and 
                    self.carga==otro.carga and
                    self.anio==otro.anio)
        return False
        
    #def __eq__(self,otro):
        #if isinstance(otro,Camion):
            #return (self.patente==otro.patente)
        #return False

    def setter_carga(self,carga):
        self.carga=carga
    

furgon1 = Camion("ABC123", "Mercedes", 1000, 2020)
furgon2 = furgon1
furgon3 = Camion("DEF456", "Volvo", 2000, 2021)
furgon4 = Camion("ABC223", "Mercedes", 1000, 2020)



#print(furgon1 == furgon2)
#print(furgon1 is furgon2)
#print(furgon3 == furgon4)
#print(furgon3 is furgon4)
#print(furgon1 == furgon4)  


def registrar_camion():
    patente=input("Patente: ")
    marca=input("Marca: ")

    while True:
        try:
            carga=int(input("carga: "))
            break
        except ValueError:
            print("La carga es un numero")

    while True:
        try:
            anio=int(input("Año: "))
            break
        except ValueError:
            print("El año es un numero")

    Camion(patente,marca,carga,anio)


def modificar_carga():
    patente= input("Patente de camion para modificar carga: ")
    for i in Camion.lista_camiones:
        if i.patente==patente:
            nueva_carga=input("Nueva carga: ")
            Camion.setter_carga(nueva_carga)
            print("Carga modificada")
            return 
        else:
            print(f"No se encontro camion con patente {patente}")

def mostrar_camiones():
    lista_ordenada= sorted(Camion.lista_camiones, key=lambda c:c.anio)
    for camion in lista_ordenada:
        print(camion)

def marca_mas_registrada():
    conteo={}
    for i in Camion.lista_camiones:
        if i.marca in conteo:
            conteo[i.marca]+=1
        else:
            conteo[i.marca]=1
    
    top=max(conteo,key=conteo.get)
    print(f"La marca mas registrada es {top}")




def menu():
    while True: 
        print("1. Registrar Camion \n2. Modificar Carga \n3. Mostrar Camiones \n5.Salir")
        a=int(input("Selecciona una opcion: "))
        if a==1:
            registrar_camion()
        elif a==2:
            modificar_carga()
        elif a==3:
            mostrar_camiones()
        elif a==4:
            marca_mas_registrada()
        elif a==5:
            break
        else:
            print("Opcion Invalida")


menu()

