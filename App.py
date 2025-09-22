import tkinter as tk
from tkinter import messagebox, simpledialog

class TodoApp:
    def __init__(self, root):
        self.root = root
        self.root.title("To-Do List")
        self.root.geometry("400x400")
        self.root.resizable(False, False)

        # Title
        tk.Label(root, text="My To-Do List", font=("Arial", 16, "bold")).pack(pady=10)

        # Task list
        self.tasks_listbox = tk.Listbox(root, width=40, height=10, font=("Arial", 12), selectmode=tk.SINGLE)
        self.tasks_listbox.pack(pady=10)

        # Buttons
        button_frame = tk.Frame(root)
        button_frame.pack(pady=10)

        tk.Button(button_frame, text="Add Task", width=10, command=self.add_task).grid(row=0, column=0, padx=5)
        tk.Button(button_frame, text="Edit Task", width=10, command=self.edit_task).grid(row=0, column=1, padx=5)
        tk.Button(button_frame, text="Delete Task", width=10, command=self.delete_task).grid(row=0, column=2, padx=5)

    def add_task(self):
        task = simpledialog.askstring("Add Task", "Enter a new task:")
        if task:
            self.tasks_listbox.insert(tk.END, task)

    def edit_task(self):
        try:
            selected_index = self.tasks_listbox.curselection()[0]
            old_task = self.tasks_listbox.get(selected_index)
            new_task = simpledialog.askstring("Edit Task", "Update the task:", initialvalue=old_task)
            if new_task:
                self.tasks_listbox.delete(selected_index)
                self.tasks_listbox.insert(selected_index, new_task)
        except IndexError:
            messagebox.showwarning("No selection", "Please select a task to edit.")

    def delete_task(self):
        try:
            selected_index = self.tasks_listbox.curselection()[0]
            self.tasks_listbox.delete(selected_index)
        except IndexError:
            messagebox.showwarning("No selection", "Please select a task to delete.")

# Run app
if __name__ == "__main__":
    root = tk.Tk()
    app = TodoApp(root)
    root.mainloop()
