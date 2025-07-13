import tkinter as tk
from tkinter import messagebox

class TodoApp:
    def __init__(self, root):
        self.root = root
        self.root.title("To-Do List ")
        self.tasks = []  # List of (task_text, BooleanVar)
        self.checkbuttons = []

        self.entry = tk.Entry(root, width=30, font=("Arial", 14))
        self.entry.pack(pady=10)

        btn_frame = tk.Frame(root)
        btn_frame.pack(pady=5)
        self.add_btn = tk.Button(btn_frame, text="Add Task", command=self.add_task)
        self.add_btn.pack(side=tk.LEFT, padx=5)
        self.edit_btn = tk.Button(btn_frame, text="Edit Task", command=self.edit_task)
        self.edit_btn.pack(side=tk.LEFT, padx=5)
        self.delete_btn = tk.Button(btn_frame, text="Delete Task", command=self.delete_task)
        self.delete_btn.pack(side=tk.LEFT, padx=5)

        self.tasks_frame = tk.Frame(root)
        self.tasks_frame.pack(pady=10)

        self.selected_index = None

    def add_task(self):
        text = self.entry.get().strip()
        if not text:
            messagebox.showwarning("Warning", "Please enter a task.")
            return
        var = tk.BooleanVar()
        cb = tk.Checkbutton(self.tasks_frame, text=text, variable=var, anchor='w', width=30, command=self.on_select)
        cb.pack(anchor='w')
        cb.bind("<Button-1>", lambda e, idx=len(self.tasks): self.set_selected(idx))
        self.tasks.append((text, var))
        self.checkbuttons.append(cb)
        self.entry.delete(0, tk.END)
        self.selected_index = None

    def edit_task(self):
        idx = self.selected_index
        if idx is None or idx >= len(self.tasks):
            messagebox.showwarning("Warning", "Please select a task to edit (by clicking its checkbox label).")
            return
        new_text = self.entry.get().strip()
        if not new_text:
            messagebox.showwarning("Warning", "Task cannot be empty.")
            return
        var = self.tasks[idx][1]
        self.checkbuttons[idx].config(text=new_text)
        self.tasks[idx] = (new_text, var)
        self.entry.delete(0, tk.END)
        self.selected_index = None

    def delete_task(self):
        idx = self.selected_index
        if idx is None or idx >= len(self.tasks):
            messagebox.showwarning("Warning", "Please select a task to delete (by clicking its checkbox label).")
            return
        self.checkbuttons[idx].destroy()
        del self.tasks[idx]
        del self.checkbuttons[idx]
        self.selected_index = None

    def set_selected(self, idx):
        self.selected_index = idx
        self.entry.delete(0, tk.END)
        self.entry.insert(0, self.tasks[idx][0])

    def on_select(self):
        # Optional: You can handle check/uncheck events here if needed
        pass

root = tk.Tk()
app = TodoApp(root)
root.mainloop()
