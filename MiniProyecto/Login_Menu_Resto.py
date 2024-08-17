import tkinter as tk
ventana = tk.Tk()
ventana.title("Login")
ventana.geometry("400x200")


etiqueta = tk.Label(ventana, text= "Usuario: ", font=("Arial", 10))
etiqueta.pack()

ingresa_usuario = tk.Entry(ventana)
ingresa_usuario.pack()

etiqueta = tk.Label(ventana, text= "Clave: ", font=("Arial", 10))
etiqueta.pack()

clave = str()
ingresa_clave = tk.Entry(ventana, textvariable=clave, show="*")
ingresa_clave.pack()


def ingresar():
    etiqueta_ingresando = tk.Label(ventana, text="Ingresando..", font=("Arial", 8))
    etiqueta_ingresando.pack()
    #supongamos que el usuario solo presiona una vez el boton

def registro():
    #link para registro
    pass

boton_ingresar = tk.Button(ventana, text='Ingresar', command=ingresar)
# boton_ingresar.grid(row=2, column=0)
boton_ingresar.pack()

boton_registro = tk.Button(ventana, text='Registrate', command=registro)
# boton_registro.grid(row=3, column=2)
boton_registro.pack()



ventana.mainloop()