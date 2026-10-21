
import tkinter as tk
from tkinter import ttk, messagebox

# Function to register student
def register_student():
    name = name_entry.get()
    roll_no = roll_entry.get()
    email = email_entry.get()
    course = course_combo.get()

    
    if name == "" or roll_no == "" or email == "" or course == "":
        messagebox.showerror("Error", "Please fill all the fields")
    else:
        messagebox.showinfo(
            "Registration Successful",
            f"Name: {name}\n"
            f"Roll Number: {roll_no}\n"
            f"Email: {email}\n"
            f"Course: {course}"
        )

        
        name_entry.delete(0, tk.END)
        roll_entry.delete(0, tk.END)
        email_entry.delete(0, tk.END)
        course_combo.set("")



root = tk.Tk()
root.title("Student Registration Form")
root.geometry("400x350")
root.resizable(False, False)


tk.Label(
    root,
    text="Student Registration Form",
    font=("Arial", 16, "bold")
).pack(pady=15)


frame = tk.Frame(root)
frame.pack(pady=10)


tk.Label(frame, text="Name:").grid(row=0, column=0, padx=10, pady=10, sticky="w")
name_entry = tk.Entry(frame, width=25)
name_entry.grid(row=0, column=1, padx=10, pady=10)


tk.Label(frame, text="Roll Number:").grid(row=1, column=0, padx=10, pady=10, sticky="w")
roll_entry = tk.Entry(frame, width=25)
roll_entry.grid(row=1, column=1, padx=10, pady=10)


tk.Label(frame, text="Email:").grid(row=2, column=0, padx=10, pady=10, sticky="w")
email_entry = tk.Entry(frame, width=25)
email_entry.grid(row=2, column=1, padx=10, pady=10)


tk.Label(frame, text="Course:").grid(row=3, column=0, padx=10, pady=10, sticky="w")

course_combo = ttk.Combobox(
    frame,
    values=["Computer Engineering", "Information Technology",
            "Mechanical Engineering", "Civil Engineering"],
    width=22,
    state="readonly"
)
course_combo.grid(row=3, column=1, padx=10, pady=10)


tk.Button(
    root,
    text="Register",
    command=register_student,
    bg="green",
    fg="white",
    font=("Arial", 11, "bold")
).pack(pady=15)


root.mainloop()

