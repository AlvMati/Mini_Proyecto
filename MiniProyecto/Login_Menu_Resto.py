import tkinter as tk
from tkinter import messagebox

def ingresar():
    usuario = ingresa_usuario.get()
    clave = ingresa_clave.get()
    if usuario and clave:
        ventana_menu = tk.Tk()
        ventana_menu.title("Bienvenidos al MENU")
        ventana_menu.geometry("400x400")
        etiqueta = tk.Label(ventana_menu, text= "🤘💥BIENVENIDOS AL MENU💥🤘 ", font=("Arial", 15))
        etiqueta.pack()
    else:
        # messagebox.showerror (ventana emergente- error)
        messagebox.showerror("Error", "Ingrese usuario y clave")
  
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
            
            # messagebox.showinfo("Gracias!", "Los datos fueron guardados correctamente")
            ventana_registro.destroy()
       else:
            messagebox.showerror("Error", "Ingrese todos los campos")
        


    boton_guardar = tk.Button(ventana_registro, text='Guardar', command=guardar)
    boton_guardar.pack()

# Crea ventana login
ventana = tk.Tk()
ventana.title("Login")
ventana.geometry("400x200")

#crea input y nombre de usuario
nombre = tk.Label(ventana, text= "Usuario: ", font=("Arial", 10))
nombre.pack()
ingresa_usuario = tk.Entry(ventana)
ingresa_usuario.pack()

#crea input y clave 
clave = tk.Label(ventana, text= "Clave: ", font=("Arial", 10))
clave.pack()
ingresa_clave = tk.Entry(ventana, show="*")
ingresa_clave.pack()


boton_ingresar = tk.Button(ventana, text='Ingresar', command=ingresar)
boton_ingresar.pack()

boton_registro = tk.Button(ventana, text='Registrate', command=registro)
boton_registro.pack()



ventana.mainloop()