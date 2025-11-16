import tkinter as tk
from tkinter import messagebox

# Create main window
root = tk.Tk()
root.title("Student Information")
root.geometry("300x200")

# Label for Name
name_label = tk.Label(root, text="Enter your Name:")
name_label.pack(pady=5)

# Entry field for Name
name_entry = tk.Entry(root, width=30)
name_entry.pack(pady=5)

# Label for Class
class_label = tk.Label(root, text="Enter your Class:")
class_label.pack(pady=5)

# Entry field for Class
class_entry = tk.Entry(root, width=30)
class_entry.pack(pady=5)

# Function for Submit button
def submit_info():
    name = name_entry.get()
    student_class = class_entry.get()
    if name and student_class:
        messagebox.showinfo("Information", f"Name: {name}\nClass: {student_class}")
    else:
        messagebox.showwarning("Input Error", "Please fill in all fields!")

# Function for Cancel button
def cancel_info():
    name_entry.delete(0, tk.END)
    class_entry.delete(0, tk.END)

# Buttons
submit_button = tk.Button(root, text="Submit", command=submit_info)
submit_button.pack(pady=5)

cancel_button = tk.Button(root, text="Cancel", command=cancel_info)
cancel_button.pack(pady=5)

# Run the GUI loop
root.mainloop()
