import tkinter as tk
from tkinter import ttk, messagebox


class TaskManagerApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Gestor de Tareas")
        self.root.geometry("500x400")

        # Configurar atajos de teclado
        self.root.bind('<Escape>', lambda e: self.root.quit())
        self.root.bind('<Delete>', lambda e: self.delete_task())
        self.root.bind('d', lambda e: self.delete_task())
        self.root.bind('c', lambda e: self.complete_task())

        self.create_widgets()
        self.load_tasks()

    def create_widgets(self):
        # Frame principal
        main_frame = ttk.Frame(self.root, padding="10")
        main_frame.pack(fill=tk.BOTH, expand=True)

        # Entrada de tarea
        ttk.Label(main_frame, text="Nueva Tarea:").pack(anchor=tk.W)
        self.task_entry = ttk.Entry(main_frame, width=50)
        self.task_entry.pack(fill=tk.X, pady=5)
        self.task_entry.bind('<Return>', lambda e: self.add_task())

        # Botones
        button_frame = ttk.Frame(main_frame)
        button_frame.pack(fill=tk.X, pady=10)

        ttk.Button(
            button_frame,
            text="Añadir (Enter)",
            command=self.add_task
        ).pack(side=tk.LEFT, padx=5)

        ttk.Button(
            button_frame,
            text="Completar (C)",
            command=self.complete_task
        ).pack(side=tk.LEFT, padx=5)

        ttk.Button(
            button_frame,
            text="Eliminar (D/Delete)",
            command=self.delete_task
        ).pack(side=tk.LEFT, padx=5)

        # Lista de tareas
        ttk.Label(main_frame, text="Tareas:").pack(anchor=tk.W)
        self.task_list = tk.Listbox(
            main_frame,
            height=15,
            selectbackground="#a6a6a6",
            selectmode=tk.SINGLE
        )
        self.task_list.pack(fill=tk.BOTH, expand=True)

        # Barra de desplazamiento
        scrollbar = ttk.Scrollbar(self.task_list)
        scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
        self.task_list.config(yscrollcommand=scrollbar.set)
        scrollbar.config(command=self.task_list.yview)

        # Info atajos
        ttk.Label(
            main_frame,
            text="Atajos: Enter=Añadir, C=Completar, D/Delete=Eliminar, Esc=Salir",
            font=('Helvetica', 8)
        ).pack(anchor=tk.W, pady=5)

    def add_task(self):
        task_text = self.task_entry.get().strip()
        if task_text:
            self.task_list.insert(tk.END, task_text)
            self.task_entry.delete(0, tk.END)
            self.save_tasks()
        else:
            messagebox.showwarning("Advertencia", "Por favor ingrese una tarea.")

    def complete_task(self):
        selected = self.task_list.curselection()
        if selected:
            index = selected[0]
            task_text = self.task_list.get(index)

            # Verificar si ya está marcada
            if task_text.startswith("✓ "):
                # Quitar marca
                new_text = task_text[2:]
                self.task_list.delete(index)
                self.task_list.insert(index, new_text)
            else:
                # Añadir marca
                new_text = f"✓ {task_text}"
                self.task_list.delete(index)
                self.task_list.insert(index, new_text)
                self.task_list.itemconfig(index, {'fg': 'gray'})

            self.save_tasks()

    def delete_task(self):
        selected = self.task_list.curselection()
        if selected:
            self.task_list.delete(selected[0])
            self.save_tasks()

    def save_tasks(self):
        with open("tasks.txt", "w") as f:
            tasks = self.task_list.get(0, tk.END)
            for task in tasks:
                f.write(task + "\n")

    def load_tasks(self):
        try:
            with open("tasks.txt", "r") as f:
                tasks = f.readlines()
                for task in tasks:
                    task = task.strip()
                    if task.startswith("✓ "):
                        self.task_list.insert(tk.END, task)
                        self.task_list.itemconfig(tk.END, {'fg': 'gray'})
                    else:
                        self.task_list.insert(tk.END, task)
        except FileNotFoundError:
            pass


if __name__ == "__main__":
    root = tk.Tk()
    app = TaskManagerApp(root)
    root.mainloop()