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

            ventana1.pack()
        
        # VENTANAS DE LOS MENUS--- COLORES DISEÑO
        def entrada():
            ventanita = tk.Tk()
            ventanita.title("Entradas")
            ventanita.geometry("600x400")
            ventanita.config(bg="orange")
            tk.Label(ventanita,text= "Si se complica mucho con listas, se agrega imagen de la carta",bg="white", font=("Arial", 20)).grid(padx=100 , pady= 150)
            ventanita.pack()
        

        def plato():
            ventanita = tk.Tk()
            ventanita.title("PlatoPrincipal")
            ventanita.geometry("600x400")
            ventanita.config(bg="red")
            tk.Label(ventanita,text= "Si se complica mucho con listas, se agrega imagen de la carta",bg="white", font=("Arial", 20)).grid(padx=100 , pady= 150)
            ventanita.pack()


        def bebidas():
            ventanita = tk.Tk()
            ventanita.title("Bebidas")
            ventanita.geometry("600x400")
            ventanita.config(bg="olive")
            tk.Label(ventanita,text= "Si se complica mucho con listas, se agrega imagen de la carta",bg="white", font=("Arial", 20)).grid(padx=100 , pady= 150)
            ventanita.pack()
        
        def postre():
            ventanita = tk.Tk()
            ventanita.title("Postre")
            ventanita.geometry("600x400")
            ventanita.config(bg="LightGreen")
            tk.Label(ventanita,text= "Si se complica mucho con listas, se agrega imagen de la carta",bg="white", font=("Arial", 20)).grid(padx=100 , pady= 150)
            ventanita.pack()
        
        def reservas():
            pass
        
        menu = tk.Menu(ventana)
        ventana.config(menu=menu)

        
        
        menu_entrada = tk.Menu(menu)
        menu_plato = tk.Menu(menu)
        menu_bebidas = tk.Menu(menu)
        menu_postre = tk.Menu(menu)
        reserva = tk.Menu(menu)
        
        #CASCADA BEBIDA / ENTRADA / PLATO PRINCIPAL / POSTRE
       
        menu.add_cascade(label ='Entradas', font=("Arial", 8), menu=menu_entrada)
        menu.add_cascade(label ='Plato Principal', font=("Arial", 8), menu=menu_plato)
        menu.add_cascade(label ='Bebidas', font=("Arial", 8), menu=menu_bebidas)
        menu.add_cascade(label ='Postre', font=("Arial", 8), menu=menu_postre)
        # menu.add_cascade(label ='Reservas', font=("Arial", 8), menu=reserva)

        menu_bebidas.add_command(label = "Con Alcohol", font=("Times", 8), command=bebidas)
        menu_bebidas.add_command(label = "Sin Alcohol", font=("Times", 8), command=bebidas)
        
        menu_entrada.add_command(label = "Menu Niños", font=("Arial", 8), command=entrada)
        menu_entrada.add_command(label = "Todo", font=("Arial", 8), command=entrada)

        menu_plato.add_command(label = "Platos Tradicionales", font=("Arial", 8), command=plato)
        menu_plato.add_command(label = "Platos Gourmet", font=("Arial", 8), command=plato)
        menu_plato.add_command(label = "Platos Veganos", font=("Arial", 8), command=plato)
        
        menu_postre.add_command(label = "Postres Frios", font=("Arial", 8), command=postre)
        menu_postre.add_command(label = "Postres Calientes", font=("Arial", 8), command=postre)    
    
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