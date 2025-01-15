
import tkinter as tk
from tkinter import ttk

def quit(window):
    window.quit()
    window.destroy()

def create_window(width, height):
    nl_window = tk.Toplevel()  # Use Toplevel for a secondary window
    nl_window.geometry(f"{width}x{height}")
    nl_window.title("Create a New List")
    nl_window.resizable(False, False)
    return nl_window

def create_cancel(height, window):
    cancel_btn = tk.Button(window, text = "Cancel", command = lambda: quit(window))
    cancel_btn.place(x = 10, y = height-10, anchor="sw")

    


