# import tkinter as tk
# # from SeleccionEntrega import *
# ventana = tk.Tk()
# ventana.title('Menú desplegable')
# ventana.geometry('400x200')
# barra_menu = tk.Menu(ventana)
# ventana.config(menu=barra_menu)

# def abrir_ventana2():
#     global ventana2
#     ventana2 = tk.Tk()
#     ventana2.title("Tipo de envio")
#     ventana2.geometry('600x200')

# #se crean los botones principales de la barra de menu

# menu_principal = tk.Menu(barra_menu)
# menu_principal2 = tk.Menu(barra_menu)

# #Se le asigna la etiqueta a cada boton principal

# barra_menu.add_cascade(label ='Principal', menu=menu_principal)
# barra_menu.add_cascade(label ='Principal2', menu=menu_principal2)

# #Se crean los submenu del menu principal

# submenu = tk.Menu(menu_principal)
# submenu2 = tk.Menu(menu_principal2)

# #Se le asigna la etiqueta al submenu

# menu_principal.add_cascade(label ='Opciones', menu=submenu)
# submenu.add_command(label = 'Opción 1')
# submenu.add_command(label = 'Opción 2')

# #Se le asigna la etiqueta al submenu2

# menu_principal2.add_cascade(label ='Ver', menu=submenu2)
# submenu2.add_command(label = 'Claro')
# submenu2.add_command(label = 'Oscuro', command=abrir_ventana2)

# ventana.mainloop()