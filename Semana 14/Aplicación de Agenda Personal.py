import tkinter as tk
from tkinter import ttk, messagebox
from tkcalendar import DateEntry  # Necesitas instalar tkcalendar: pip install tkcalendar

class AgendaPersonal:
    def __init__(self, root):
        self.root = root
        self.root.title("Agenda Personal")

        # Frame para la lista de eventos
        self.frame_lista = ttk.Frame(root)
        self.frame_lista.pack(padx=10, pady=10, fill=tk.BOTH, expand=True)

        # TreeView para mostrar los eventos
        self.tree = ttk.Treeview(self.frame_lista, columns=("Fecha", "Hora", "Descripción"), show="headings")
        self.tree.heading("Fecha", text="Fecha")
        self.tree.heading("Hora", text="Hora")
        self.tree.heading("Descripción", text="Descripción")
        self.tree.pack(fill=tk.BOTH, expand=True)

        # Frame para la entrada de datos
        self.frame_entrada = ttk.Frame(root)
        self.frame_entrada.pack(padx=10, pady=10, fill=tk.X)

        # Etiquetas y campos de entrada
        ttk.Label(self.frame_entrada, text="Fecha:").grid(row=0, column=0, padx=5, pady=5)
        self.fecha_entry = DateEntry(self.frame_entrada, date_pattern='yyyy-mm-dd')
        self.fecha_entry.grid(row=0, column=1, padx=5, pady=5)

        ttk.Label(self.frame_entrada, text="Hora:").grid(row=0, column=2, padx=5, pady=5)
        self.hora_entry = ttk.Entry(self.frame_entrada)
        self.hora_entry.grid(row=0, column=3, padx=5, pady=5)

        ttk.Label(self.frame_entrada, text="Descripción:").grid(row=0, column=4, padx=5, pady=5)
        self.descripcion_entry = ttk.Entry(self.frame_entrada)
        self.descripcion_entry.grid(row=0, column=5, padx=5, pady=5)

        # Frame para los botones
        self.frame_botones = ttk.Frame(root)
        self.frame_botones.pack(padx=10, pady=10, fill=tk.X)

        # Botones
        ttk.Button(self.frame_botones, text="Agregar Evento", command=self.agregar_evento).pack(side=tk.LEFT, padx=5)
        ttk.Button(self.frame_botones, text="Eliminar Evento Seleccionado", command=self.eliminar_evento).pack(side=tk.LEFT, padx=5)
        ttk.Button(self.frame_botones, text="Salir", command=root.quit).pack(side=tk.RIGHT, padx=5)

    def agregar_evento(self):
        # Obtener los valores de los campos de entrada
        fecha = self.fecha_entry.get()
        hora = self.hora_entry.get()
        descripcion = self.descripcion_entry.get()

        # Validar que todos los campos estén llenos
        if fecha and hora and descripcion:
            # Insertar el evento en el TreeView
            self.tree.insert("", tk.END, values=(fecha, hora, descripcion))
            # Limpiar los campos de entrada
            self.fecha_entry.set_date(None)
            self.hora_entry.delete(0, tk.END)
            self.descripcion_entry.delete(0, tk.END)
        else:
            messagebox.showwarning("Campos Vacíos", "Por favor, complete todos los campos.")

    def eliminar_evento(self):
        # Obtener el evento seleccionado
        seleccionado = self.tree.selection()
        if seleccionado:
            # Mostrar un diálogo de confirmación
            confirmar = messagebox.askyesno("Eliminar Evento", "¿Estás seguro de que deseas eliminar este evento?")
            if confirmar:
                # Eliminar el evento seleccionado
                self.tree.delete(seleccionado)
        else:
            messagebox.showwarning("Nada Seleccionado", "Por favor, seleccione un evento para eliminar.")

if __name__ == "__main__":
    root = tk.Tk()
    app = AgendaPersonal(root)
    root.mainloop()