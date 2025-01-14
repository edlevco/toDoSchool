import tkinter as tk
from tkinter import ttk

root = tk.Tk()

# Create a ttk.Style instance
style = ttk.Style()

# Define a custom style for the button
style.configure("Custom.TButton", background="blue", foreground="white", font=("Arial", 12))

# Create a frame to hold the button
frame = ttk.Frame(root, padding=10)
frame.pack()

# Apply the custom style to a ttk.Button
button = ttk.Button(frame, text="Click Me", style="Custom.TButton")
button.pack(pady=10)

# Set the window background color
root.configure(bg="gray")

root.mainloop()
