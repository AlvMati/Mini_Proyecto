import tkinter as tk
from tkinter import messagebox
from lista_comidas import *

# Crea ventana login
ventana_login = tk.Tk()
ventana_login.title("Login")
ventana_login.geometry("400x200")

#crea input y nombre de usuario
nombre = tk.Label(ventana_login, text= "Usuario: ", font=("Arial", 10))
nombre.pack()
ingresa_usuario = tk.Entry(ventana_login)
ingresa_usuario.pack()

#crea input y clave
clave = tk.Label(ventana_login, text= "Clave: ", font=("Arial", 10))
clave.pack()
ingresa_clave = tk.Entry(ventana_login, show="*")
ingresa_clave.pack()


def ingresar():
    usuario_input = ingresa_usuario.get()
    clave_input = ingresa_clave.get()

    acceso = False

    for usuario in lista_usuarios:
        
        if usuario["nombre"] == usuario_input and usuario["clave"]== clave_input:
            acceso = True
    
    if acceso:
        ventana = tk.Tk()
        ventana.title("COMILANDIA")
        # ventana.iconbitmap("comil.ico")
        ventana.geometry("600x400")
        ventana.config(bg="white")
        tk.Label(ventana,text= "BIENVENIDOS MENU RESTO🍕🍔",bg="violet", font=("Arial", 20)).grid(padx=100 , pady= 150)
        # deberiamos agregar una imagen de fonde- Los botones de bebidas, entrada, etc. Ya contiene la lista. 
        # Se puede ir desplegando ejemple "bebidas" ----> con alcohol ---> sin alcohol
        
        def solo_menu():
            ventana1 = tk.Tk()
            ventana1.geometry("600x400")
            ventana1.config(bg="green")
            row=2
            for menu in menus: #recorre no por indice sino por elemento
                nombre = menu.get("nombre") #toma el valor de la key
                tipo = menu.get("tipo")
                precio = menu.get("precio")
                tk.Entry(ventana1,width=4,bg="grey").grid(row=row, column=2, padx=20)
                tk.Label(ventana1,text= nombre,bg="yellow", font=("Arial", 8)).grid(row=row, column=1, pady=10)
                

                row+=1

            ventana1.pack(expand=1)
        
        barra_menu = tk.Menu(ventana)
        ventana.config(menu=barra_menu)

        menu_comidas = tk.Menu(barra_menu)
        barra_menu.add_cascade(label ='Bebidas', font=("Arial", 8), menu=menu_comidas)
        barra_menu.add_cascade(label ='Entradas', font=("Arial", 8), menu=menu_comidas)
        barra_menu.add_cascade(label ='Plato Principal', font=("Arial", 8), menu=menu_comidas)
        barra_menu.add_cascade(label ='Postre', font=("Arial", 8), menu=menu_comidas)

        menu_comidas.add_command(label= "Seleccionar Menues", font=("Arial", 8),command=solo_menu)
        menu_comidas.add_command(label= "Otros", font=("Arial", 8),command=solo_menu)
        ventana.pack()
    else:
        messagebox.showerror("Error", "Tenes que registrarte!")
        
    ventana.mainloop()


lista_usuarios = [{"nombre": "a", "clave": "a"}]

def registro():
    ventana_registro = tk.Tk()
    ventana_registro.title("Nuevo Registro")
    ventana_registro.geometry("400x300")

    #INGRESA NOMBRE
    nombre = tk.Label(ventana_registro, text= "Nombre: ", font=("Arial", 10))
    nombre.pack()
    ingresa_nombre = tk.Entry(ventana_registro)
    ingresa_nombre.pack()

    # INGRESA TELEFONO
    telefono = tk.Label(ventana_registro, text= "Telefono: ", font=("Arial", 10))
    telefono.pack()
    ingresa_telefono = tk.Entry(ventana_registro)
    ingresa_telefono.pack()

    # INGRESA DIRECCION
    direccion = tk.Label(ventana_registro, text= "Dirección: ", font=("Arial", 10))
    direccion.pack()
    ingresa_direccion = tk.Entry(ventana_registro)
    ingresa_direccion.pack()

    # INGRESA CLAVE
    clave = tk.Label(ventana_registro, text= "Clave Nueva: ", font=("Arial", 10))
    clave.pack()
    #clave = str()
    ingresa_clave = tk.Entry(ventana_registro, show="*")
    ingresa_clave.pack()

    # REPETIR CLAVE
    rep_clave = tk.Label(ventana_registro, text= "Repetir Clave: ", font=("Arial", 10))
    rep_clave.pack()
    repetir_clave = tk.Entry(ventana_registro, show="*")
    repetir_clave.pack()


    def guardar():
       nombre = ingresa_nombre.get()
       telefono = ingresa_telefono.get()
       direccion = ingresa_direccion.get()
       clave = ingresa_clave.get()
       rep_clave =  repetir_clave.get()

       if nombre and telefono and direccion and clave and rep_clave:
            datos_registro = {"nombre": nombre,
                     "telefono": telefono,
                     "direccion": direccion,
                     "clave": clave,
                     "repetir_clave": rep_clave}

            print(datos_registro)

            lista_usuarios.append(datos_registro)

            # messagebox.showinfo("Gracias!", "Los datos fueron guardados correctamente")
            ventana_registro.destroy()
       else:
            messagebox.showerror("Error", "Ingrese todos los campos")



    boton_guardar = tk.Button(ventana_registro, text='Guardar', command=guardar)
    boton_guardar.pack()



boton_ingresar = tk.Button(ventana_login, text='Ingresar', command=ingresar)
boton_ingresar.pack()

boton_registro = tk.Button(ventana_login, text='Registrate', command=registro)
boton_registro.pack()



ventana_login.mainloop()
