import tkinter as tk
from tkinter import filedialog, messagebox

root = tk.Tk()
root.title("My Notepad")
root.geometry("700x500")

def new_file():
    text_area.delete("1.0", tk.END)
    root.title("Untitled - My Notepad")

def open_file():
    file_path = filedialog.askopenfilename(
        filetypes=[("Text Files", "*.txt"), ("All Files", "*.*")]
    )

    if file_path:
        with open(file_path, "r", encoding="utf-8") as file:
            text_area.delete("1.0", tk.END)
            text_area.insert("1.0", file.read())

        root.title(file_path + " - My Notepad")

def save_file():
    file_path = filedialog.asksaveasfilename(
        defaultextension=".txt",
        filetypes=[("Text Files", "*.txt"), ("All Files", "*.*")]
    )

    if file_path:
        with open(file_path, "w", encoding="utf-8") as file:
            file.write(text_area.get("1.0", tk.END))

        messagebox.showinfo("Saved", "File saved successfully!")

def exit_app():
    root.destroy()

menu_bar = tk.Menu(root)

file_menu = tk.Menu(menu_bar, tearoff=0)
file_menu.add_command(label="New", command=new_file)
file_menu.add_command(label="Open", command=open_file)
file_menu.add_command(label="Save", command=save_file)
file_menu.add_separator()
file_menu.add_command(label="Exit", command=exit_app)

menu_bar.add_cascade(label="File", menu=file_menu)

edit_menu = tk.Menu(menu_bar, tearoff=0)
edit_menu.add_command(
    label="Cut",
    command=lambda: text_area.event_generate("<<Cut>>")
)
edit_menu.add_command(
    label="Copy",
    command=lambda: text_area.event_generate("<<Copy>>")
)
edit_menu.add_command(
    label="Paste",
    command=lambda: text_area.event_generate("<<Paste>>")
)

menu_bar.add_cascade(label="Edit", menu=edit_menu)

root.config(menu=menu_bar)

text_area = tk.Text(root, font=("Arial", 12), undo=True)
text_area.pack(expand=True, fill="both")

root.mainloop()