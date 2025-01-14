import tkinter as tk
from tkinter import ttk
import list

# Initialize the main window
window = tk.Tk()
window.title("TO-DO LIST")
width = 500
height = 700
left = int(window.winfo_screenwidth() / 2) - int(width / 2)
right = int(window.winfo_screenheight() / 2) - int(height / 2)
window.geometry(f"{width}x{height}+{left}+{right}")

window.bind("<Escape>", lambda e: window.quit())
window.resizable(False, False)

# Initialize variables
mainWindow = True
new_list_var = tk.StringVar()
entry = None
list_buttons = []  # To store button widgets for toggle
check_vars = []  # To store variables for checkboxes
edit_mode_active = False  # Flag for edit mode


def new_list():
    def on_color_change():
        """Callback for when the color selection changes."""
        selected_color = color_var.get()
        # Update the preview label by recreating it
        nonlocal color_label  # Access the existing color_label variable
        color_label.destroy()  # Remove the old label
        color_label = tk.Label(
            nl_window,
            textvariable=preview,
            fg=selected_color,
            font=("Helvetica", 25, "bold")
        )  # Create a new label with the updated color
        color_label.pack(pady=10)


    def quit():
        nl_window.quit()
        label = tk.Label(nl_window, text = "Click to quit...", fg = "red")
        label.place(x = 10, y = 298)

    def create_list():
        if preview.get() and preview:
            color = color_var.get()
            name = preview.get()
            new_list = list.List(name, color)


    # List of colors
    colors = ["white", "red", "blue", "green", "dark orange", "purple", "dark gray", "goldenrod"]

    # Variables
    color_var = tk.StringVar(value=colors[0])  # Default selection
    preview = tk.StringVar()  # Initial preview text


    # Create a new top-level window
    nl_window = tk.Toplevel()  # Use Toplevel for a secondary window
    nl_window.geometry("250x350")
    nl_window.title("Create a New List")
    nl_window.resizable(False, False)

    # Add a label and entry for the name
    label = tk.Label(nl_window, text="Enter List Name:")
    label.pack()
    entry = tk.Entry(nl_window, textvariable=preview)
    entry.focus()
    entry.pack()


# Create radio buttons for each color
    for color in colors:

        radio_btn = tk.Radiobutton(
            nl_window,
            text=color,  # Display the color name
            fg=color,
            variable=color_var,  # Link the radio button to the shared variable
            value=color,  # Set the value to the color name
            command=on_color_change,  # Callback when the button is selected
        )
        radio_btn.pack()
    

    color_label = tk.Label(nl_window, textvariable=preview, fg="white", font=("Helvetica", 25, "bold"))  # Default color
    color_label.pack(pady=10)

    cancel_btn = tk.Button(nl_window, text = "Cancel", command = quit)
    cancel_btn.place(x = 10, y = 320)

    cancel_btn = tk.Button(nl_window, text = "Create", command = create_list)
    cancel_btn.place(x = 165, y = 320)

    nl_window.mainloop()


mainMenu = tk.Menu(window)

file_menu = tk.Menu(mainMenu, tearoff=False)
file_menu.add_command(label="New List", command=new_list)
file_menu.add_separator()
file_menu.add_command(label="Delete List", command=lambda: print("delete list"))
mainMenu.add_cascade(label="File", menu=file_menu)

help_menu = tk.Menu(mainMenu, tearoff=False)
mainMenu.add_cascade(label="Help", menu=help_menu)

window.configure(menu=mainMenu)


def print_entry():
    """Add a new list."""
    if new_list_var.get():  # Check if the value is not empty
        btn = tk.Button(window, text=new_list_var.get())
        btn.pack()
        list_buttons.append(btn)


# Run the main loop
window.mainloop()
