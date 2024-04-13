import tkinter as tk
from tkinter import messagebox

def display_menu():
    print("1. Add task")
    print("2. View tasks")
    print("3. Mark task as done")
    print("4. Delete task")
    print("5. Exit")


def add_task():
    task_name = task_entry.get()
    if task_name:
        tasks_listbox.insert(tk.END, task_name)
        tasks[task_name] = "Pending"
        messagebox.showinfo("Success", "Task added successfully!")
        task_entry.delete(0, tk.END)
    else:
        messagebox.showerror("Error", "Please enter a task.")


def view_tasks():
    tasks_listbox.delete(0, tk.END)
    for task, status in tasks.items():
        tasks_listbox.insert(tk.END, f"{task} - {status}")


def mark_task_done():
    selected_task_index = tasks_listbox.curselection()
    if selected_task_index:
        selected_task = tasks_listbox.get(selected_task_index)
        tasks[selected_task.split(" - ")[0]] = "Done"
        tasks_listbox.delete(selected_task_index)
        tasks_listbox.insert(tk.END, selected_task.split(" - ")[0] + " - Done")
        messagebox.showinfo("Success", "Task marked as done!")
    else:
        messagebox.showerror("Error", "Please select a task.")


def delete_task():
    selected_task_index = tasks_listbox.curselection()
    if selected_task_index:
        selected_task = tasks_listbox.get(selected_task_index)
        del tasks[selected_task.split(" - ")[0]]
        tasks_listbox.delete(selected_task_index)
        messagebox.showinfo("Success", "Task deleted successfully!")
    else:
        messagebox.showerror("Error", "Please select a task.")


def exit_program():
    root.destroy()


root = tk.Tk()
root.title("Task Manager")

tasks = {}

menu_frame = tk.Frame(root)
menu_frame.pack()

add_button = tk.Button(menu_frame, text="Add task", command=add_task)
add_button.grid(row=0, column=0, padx=5, pady=5)

view_button = tk.Button(menu_frame, text="View tasks", command=view_tasks)
view_button.grid(row=0, column=1, padx=5, pady=5)

mark_done_button = tk.Button(menu_frame, text="Mark task as done", command=mark_task_done)
mark_done_button.grid(row=0, column=2, padx=5, pady=5)

delete_button = tk.Button(menu_frame, text="Delete task", command=delete_task)
delete_button.grid(row=0, column=3, padx=5, pady=5)

exit_button = tk.Button(menu_frame, text="Exit", command=exit_program)
exit_button.grid(row=0, column=4, padx=5, pady=5)

tasks_listbox = tk.Listbox(root)
tasks_listbox.pack(padx=10, pady=10)

task_entry = tk.Entry(root, width=50)
task_entry.pack(padx=10, pady=5)

root.mainloop()
