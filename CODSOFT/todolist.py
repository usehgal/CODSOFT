import tkinter as tk
from tkinter import messagebox

class TodoApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Todo List Application")
        
        self.tasks = []
        self.task_widgets = []  # To store the widgets for each task (label, edit button, delete button).
        
        self.task_input = tk.Entry(root, font=("Arial", 16), width=50)
        self.task_input.pack(pady=10)
        
        self.add_button = tk.Button(root, text="Add Task", font=("Arial", 14), command=self.add_task)
        self.add_button.pack(pady=5)
        
        self.task_list_frame = tk.Frame(root)
        self.task_list_frame.pack()

        self.load_tasks()
        
    def add_task(self):
        task = self.task_input.get()
        if task:
            self.tasks.append(task)
            self.task_input.delete(0, tk.END)
            self.save_tasks()
            self.display_tasks()
        else:
            messagebox.showwarning("Warning", "Please enter a task.")

    def edit_task(self, task_index):
        edited_task = self.tasks[task_index]
        new_task = self.task_input.get()
        if new_task:
            self.tasks[task_index] = new_task
            self.task_input.delete(0, tk.END)
            self.save_tasks()
            self.display_tasks()
        else:
            messagebox.showwarning("Warning", "Please enter a task to edit.")

    def delete_task(self, task_index):
        del self.tasks[task_index]
        self.save_tasks()
        self.display_tasks()

    def save_tasks(self):
        with open("tasks.txt", "w") as file:
            for task in self.tasks:
                file.write(task + "\n")

    def load_tasks(self):
        try:
            with open("tasks.txt", "r") as file:
                for line in file:
                    task = line.strip()
                    if task:
                        self.tasks.append(task)
        except FileNotFoundError:
            pass

        self.display_tasks()

    def display_tasks(self):
        for widget in self.task_widgets:
            widget.destroy()
        self.task_widgets.clear()

        for i, task in enumerate(self.tasks):
            task_label = tk.Label(self.task_list_frame, text=task, font=("Arial", 16))
            task_label.grid(row=i, column=0, pady=5, sticky="w")

            edit_button = tk.Button(self.task_list_frame, text="Edit", font=("Arial", 12),
                                    command=lambda index=i: self.edit_task(index))
            edit_button.grid(row=i, column=1, padx=5)

            delete_button = tk.Button(self.task_list_frame, text="Delete", font=("Arial", 12),
                                      command=lambda index=i: self.delete_task(index))
            delete_button.grid(row=i, column=2, padx=5)

            self.task_widgets.append(task_label)
            self.task_widgets.append(edit_button)
            self.task_widgets.append(delete_button)

if __name__ == "__main__":
    root = tk.Tk()
    todo_app = TodoApp(root)
    root.mainloop()
