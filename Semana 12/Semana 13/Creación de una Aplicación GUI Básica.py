import tkinter as tk
from tkinter import messagebox

def agregar_dato():
    dato = entry.get()
    if dato:
        lista.insert(tk.END, dato)
        entry.delete(0, tk.END)
    else:
        messagebox.showwarning("Entrada vacía", "Por favor, ingrese un dato antes de agregar.")

def limpiar_lista():
    lista.delete(0, tk.END)

# Crear la ventana principal
root = tk.Tk()
root.title("Aplicación GUI Básica")
root.geometry("400x300")

# Crear y posicionar los componentes
label = tk.Label(root, text="Ingrese un dato:")
label.pack(pady=5)

entry = tk.Entry(root, width=40)
entry.pack(pady=5)

btn_agregar = tk.Button(root, text="Agregar", command=agregar_dato)
btn_agregar.pack(pady=5)

lista = tk.Listbox(root, width=50, height=10)
lista.pack(pady=5)

btn_limpiar = tk.Button(root, text="Limpiar", command=limpiar_lista)
btn_limpiar.pack(pady=5)

# Ejecutar el bucle principal de la aplicación
root.mainloop()
