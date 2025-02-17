import tkinter as tk
from tkinter import messagebox

# Create the main window
window = tk.Tk()
window.geometry("400x400")

import tkinter as tk


def show_error():
    messagebox.showerror("Error", "An unexpected error occurred!")

# Create the main window
root = tk.Tk()
root.title("Error Example")
root.geometry("300x200")

# Add a button to trigger the error
error_button = tk.Button(root, text="Show Error", command=show_error)
error_button.pack(pady=50)

root.mainloop()


# Run the GUI application
window.mainloop()
