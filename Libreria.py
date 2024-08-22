class Libro():
    def __init__(self, titulo, autor, ISBN, numeropaginas, genero):
        self.titulo = titulo
        self.autor = autor
        self.ISBN = ISBN
        self.numeropaginas = numeropaginas
        self.genero = genero
        self.disponible = False

    def prestar(self):
        if self.disponible:
            print(f"El libro '{self.titulo}' ha sido prestado.")
        else:
            print(f"El libro '{self.titulo}' está disponible para prestar.")

    def devolver(self):
        if self.disponible:
            print(f"El libro '{self.titulo}' no ha sido devuelto.")
        else:
            print(f"El libro '{self.titulo}' ha sido devuelto.")

    def buscarPorTítulo(self, libro):
        if libro in Libro:
           print(libro)
        if self.prestar == False:
           print('Libro disponible')

L_1 = Libro('Info', 'Matias, Alv', 'xxxxxx', '350', 'Drama')

print(L_1.devolver())
print(L_1.prestar())


class Libreria(Libro):
    def __init__(self, libros, autores, lectores):
        self.libros = []
        self.autores = []
        self.lectores = []



class Autor():
    def __init__(self, nombre, nacionadidad, fecha_nacimiento):
        self.nombre = nombre
        self.nacionad = nacionadidad
        self.fecha_nacimiento = fecha_nacimiento




class Lector():
    def __init__(self, nombre, edad, direccion, numsocio):
        self.nombre = nombre
        self.edad = edad
        self.direccion = direccion
        self.numsocio = numsocio


    def solicitarPrestamo (self):
        pass

    def devolverLibro (self):
        pass



