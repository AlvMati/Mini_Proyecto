import tkinter as tk
ventana = tk.Tk()
ventana.title("Login")
ventana.geometry("400x200")


etiqueta = tk.Label(ventana, text= "Usuario: ", font=("Arial", 10))
etiqueta.pack()
# usuario = str()
ingresa_usuario = tk.Entry(ventana)
ingresa_usuario.pack()


etiqueta = tk.Label(ventana, text= "Clave: ", font=("Arial", 10))
etiqueta.pack()
clave = str()
ingresa_clave = tk.Entry(ventana,textvariable=clave, show="*")
ingresa_clave.pack()


def ingresar():
    
    etiqueta_ingresando = tk.Label(ventana, text="Ingresando..", font=("Arial", 8))
    etiqueta_ingresando.pack()
    #supongamos que el usuario solo presiona una vez el boton
    ingresos = ingresa_usuario.get()
    lista_ingresos =[]
    # if ingresos:  
    #     lista_ingresos.insert(tk,end,ingresos)

def registro():
    ventana_registro = tk.Tk()
    ventana_registro.title("Nuevo Registro")
    ventana_registro.geometry("400x200")
    
    #INGRESA NUEVO NOMBRE
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

    def guardar():
        pass
    
    
    boton_guardar = tk.Button(ventana_registro, text='Guardar', command=guardar)
    boton_guardar.pack()


boton_ingresar = tk.Button(ventana, text='Ingresar', command=ingresar)
# boton_ingresar.grid(row=2, column=0)
boton_ingresar.pack()


boton_registro = tk.Button(ventana, text='Registrate', command=registro)
# boton_registro.grid(row=3, column=2)
boton_registro.pack()



ventana.mainloop()

# git add . 