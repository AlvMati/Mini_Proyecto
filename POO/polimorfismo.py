#Polimorfismo
# metodos igual de class diferentes pueden obtener diferentes resultados
# usando el mismo metodo, podemos llamar varias veces y tener diferentes resultados.
# llamar al mismo metodo (hablar- idiomas-) cada vez que lo llamar lo podes sobreescribir
# para ver diferentes resultado.


class Animal:
    def hablar():
        return ''
    
class Perro(Animal):
    def hablar(self):
        return 'Guau!'

class Gato(Animal):
    def hablar(self):
        return 'Miauu!'
    
class Vaca(Animal):
    def hablar(self):
        return 'Muuuu!'
    
perro = Perro()
gato = Gato()
vaca = Vaca()

print(perro.hablar())
print(gato.hablar())
print(vaca.hablar())