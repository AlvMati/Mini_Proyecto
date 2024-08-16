# HERENCIA SIMPLEEE */*/*/**/***/*//**//**//**/*/
# # Clase padre/superclase
# class Animal:
#     def __init__(self, nombre):
#         self.nombre = nombre

#     def hablar(self):
#         pass

# # Clase hijo/subclase
# class Perro(Animal):
#     def hablar(self):
#         return f"{self.nombre} dice: Guauu!!!"

# perro = Perro("Filulaiss")

# print(perro.hablar())

# Herencia multiple ***/*/*/**//**/*/*/**/*/*/*/*/*/**/

# class volador:
#     def volar(self):
#         return "puedo volar"

# class nadador:
#     def nadar(self):
#         return "puedo volar"

# class Pato(volador, nadador):
#     pass

# pato = Pato()
# print(pato.volar())
# print(pato.nadar())


# Herencia Jerarquita /* /* /* /*/* *//**/ */* //* */ */
# clase abuelo / padre / hijo 

# class Animal:
#     def __init__(self, nombre):
#         self.nombre = nombre
    
#     def hablar(self):
#         pass

# class Perro(Animal):
#     def hablar(self):
#         return f'{self.nombre} dice Guau!'
    
# class Gato(Animal):
#     def hablar(self):
#         return f'{self.nombre} dice Miauu!'
    
# perro = Perro('Firu')
# gato = Gato('Michi')

# print(perro.hablar())
# print(gato.hablar())

# multinivel */ */*/* /* /*/ / */ */ */ */ */ */ * /*
# abuelo  / padre   / hijoo  

class Animal:
    def __init__(self, nombre):
        self.nombre = nombre
    
    def caminar(self):
        return 'Estoy caminando'

class Mamifero(Animal):
    def pelaje(self):
        return 'Tengo pelaje'

class Perro(Mamifero):
    def hablar(self):
        return f'{self.nombre} dice Guaui!'
    
perro = Perro('Firu')

print(perro.hablar())
print(perro.caminar())
print(perro.pelaje())