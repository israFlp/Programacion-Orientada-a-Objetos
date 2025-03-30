import tkinter as tk
from tkinter import ttk, messagebox


class TodoApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Lista de Tareas")
        self.root.geometry("500x400")

        # Estilo
        self.style = ttk.Style()
        self.style.configure('TButton', font=('Arial', 10))
        self.style.configure('Completed.TLabel', foreground='gray', font=('Arial', 10, 'overstrike'))

        # Frame principal
        self.main_frame = ttk.Frame(root, padding="10")
        self.main_frame.pack(fill=tk.BOTH, expand=True)

        # Entrada de tarea
        self.task_entry = ttk.Entry(self.main_frame, font=('Arial', 12))
        self.task_entry.pack(fill=tk.X, pady=(0, 10))
        self.task_entry.bind('<Return>', lambda e: self.add_task())

        # Botones
        self.button_frame = ttk.Frame(self.main_frame)
        self.button_frame.pack(fill=tk.X, pady=(0, 10))

        self.add_button = ttk.Button(
            self.button_frame,
            text="Añadir Tarea",
            command=self.add_task
        )
        self.add_button.pack(side=tk.LEFT, expand=True, fill=tk.X, padx=(0, 5))

        self.complete_button = ttk.Button(
            self.button_frame,
            text="Marcar como Completada",
            command=self.mark_completed
        )
        self.complete_button.pack(side=tk.LEFT, expand=True, fill=tk.X, padx=(0, 5))

        self.delete_button = ttk.Button(
            self.button_frame,
            text="Eliminar Tarea",
            command=self.delete_task
        )
        self.delete_button.pack(side=tk.LEFT, expand=True, fill=tk.X)

        # Lista de tareas
        self.tasks_frame = ttk.Frame(self.main_frame)
        self.tasks_frame.pack(fill=tk.BOTH, expand=True)

        self.scrollbar = ttk.Scrollbar(self.tasks_frame)
        self.scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

        self.task_list = tk.Listbox(
            self.tasks_frame,
            yscrollcommand=self.scrollbar.set,
            font=('Arial', 12),
            selectbackground='#a6a6a6',
            selectmode=tk.SINGLE
        )
        self.task_list.pack(fill=tk.BOTH, expand=True)
        self.scrollbar.config(command=self.task_list.yview)

        # Evento de doble clic para marcar como completada
        self.task_list.bind('<Double-Button-1>', lambda e: self.mark_completed())

        # Almacén de tareas (texto y estado)
        self.tasks = []

    def add_task(self):
        task_text = self.task_entry.get().strip()
        if task_text:
            self.tasks.append({'text': task_text, 'completed': False})
            self.update_task_list()
            self.task_entry.delete(0, tk.END)
        else:
            messagebox.showwarning("Advertencia", "Por favor ingresa una tarea válida.")

    def mark_completed(self):
        selected = self.task_list.curselection()
        if selected:
            index = selected[0]
            self.tasks[index]['completed'] = not self.tasks[index]['completed']
            self.update_task_list()

    def delete_task(self):
        selected = self.task_list.curselection()
        if selected:
            index = selected[0]
            del self.tasks[index]
            self.update_task_list()

    def update_task_list(self):
        self.task_list.delete(0, tk.END)
        for task in self.tasks:
            text = task['text']
            if task['completed']:
                self.task_list.insert(tk.END, text)
                self.task_list.itemconfig(tk.END, {'fg': 'gray'})
            else:
                self.task_list.insert(tk.END, text)
                self.task_list.itemconfig(tk.END, {'fg': 'black'})


if __name__ == "__main__":
    root = tk.Tk()
    app = TodoApp(root)
    root.mainloop()