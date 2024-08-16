#encapsulacion *** nadie deberia modificar atributos de un objeto mas que el mismo (desde afuera)**

#Publico

# class Persona:
#     def __init__(self, nombre, DNI):
#         self.nombre = nombre
#         self.DNI = DNI


# p_1 = Persona( 'Matias', '12345678')
# print(p_1.DNI)
# print(p_1.nombre)

#/*/*/*/*/*/*/*/*/*/*/*/*/*
# noo tan publicos

# class Persona:
#     def __init__(self, nombre, DNI):
#         self.nombre = nombre
#         self.__DNI = DNI
#     # getter  para obtenet el nro dni
    
#     def get_DNI(self):
#         return f'DNI: {self.__DNI}'


# p_1 = Persona( 'Matias', '12345678')
# print(p_1.get_DNI())

#   PRIVADOS/*/*/*/*/*/ 

class Persona:
    def __init__(self, nombre, DNI):
        self.nombre = nombre
        self.__DNI = DNI
    # getter  para obtenet el nro dni
    
    def get_DNI(self):
        return f'DNI: {self.__DNI}'
    
    # SETTER MODIFICA EL ATRIBUTO DNI
    def set_DNI(self, nuevo_dni):
        self.__DNI = nuevo_dni  
        

p_1 = Persona( 'Matias', '12345678')
print(p_1.get_DNI())

p_1.set_DNI('65468789')
print(p_1.get_DNI())



# /*//////////
# class Persona:
#     def __init__(self, nombre, DNI):
#         self.nombre = nombre
#         self.__DNI = DNI

#     # getter para obtener el nro dni
#     def get_DNI(self):
#         return f"DNI: {self.__DNI}"

#     # setter modifica el atributo dni
#     def set_DNI(self, nuevo_dni):
#         self.__DNI = nuevo_dni


# p_1 = Persona("Dany", "12345567")
# # print("dni", p_1.__DNI)
# print("dni", p_1.get_DNI())
# # p_1.__DNI = "Hola"
# # print("dni", p_1.DNI)
# p_1.set_DNI("nuevo dni")
# print("dni", p_1.get_DNI())
# print("nombre", p_1.nombre)


# Definir tareas- y codear
# diseñao
# vistas 
# funcionaliades