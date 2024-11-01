
#Importar modulo tkkinter para crear la interfaz
# import tkinter as tk
# #Ventana principal
# root=tk.Tk()
# #root.title('Titulo de la ventana')
# #Se le da el tamanio a la ventana
# root.geometry('0x0')
#
#
#
#
# #LABEL PRINCIPAL
# label=tk.Label(root,text='Ingresa tu contrasena')
# label.pack(padx=1,pady=10)
#
# #Casilla entry-input
# entry=tk.Entry(root)
# #Tamaniocasilla input
# entry.pack(padx=10, pady=10)
#
#
# def mostrar_input():
#     texto=entry.get()
#     label_resultado.config(text=f"Tu nombre es {texto}")
#
# #Creamos un button
# button=tk.Button(root,text="Mostrar",command=mostrar_input)
# button.pack(padx=10,pady=10)
#
#
# # Etiqueta para mostrar el resultado
# label_resultado = tk.Label(root, text="")
# label_resultado.pack(padx=10, pady=10)
# #Inicia el bucle de eventos(loop de la ventana)
#
# #Root.mainloop() ->Esto inicia el bucle principal de la aplicacion Tkinter.Mantiene la ventana abierta y lista para recibir interacciones del usuario hasta que se cierre
# #Es muy importante eso
# root.mainloop()