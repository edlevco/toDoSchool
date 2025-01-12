import list
import tkinter as tk
from tkinter import ttk




# Initialize the main window
window = tk.Tk()
window.title("TO-DO LIST")
width = 500
height = 700
window.geometry(f"{width}x{height}")

# Initialize variables
mainWindow = True
new_list_var = tk.StringVar()
entry = None
list_buttons = []  # To store button widgets for toggle
check_vars = []  # To store variables for checkboxes
edit_mode_active = False  # Flag for edit mode


def print_list():
    """Display all lists as buttons."""
    global list_buttons
    allLists = list.returnAllLists()
    for name in allLists:
        btn = tk.Button(window, text=name)
        btn.pack()
        list_buttons.append(btn)


def toggle_edit_mode():
    """Switch between normal mode and edit mode."""
    global edit_mode_active, check_vars, list_buttons

    if not edit_mode_active:
        # Enter edit mode
        edit_mode_active = True
        check_vars = []
        for btn in list_buttons:
            btn.destroy()  # Remove buttons
            var = tk.BooleanVar()  # Create a variable for the checkbox
            chk = tk.Checkbutton(window, text=btn['text'], variable=var)
            chk.pack()
            check_vars.append(var)

        # Add Delete and Cancel buttons
        delete_btn.pack(pady=10)
        cancel_btn.pack(pady=10)

    else:
        # Exit edit mode
        edit_mode_active = False
        for widget in window.winfo_children():
            if isinstance(widget, tk.Checkbutton):
                widget.destroy()  # Remove checkboxes

        delete_btn.pack_forget()
        cancel_btn.pack_forget()

        # Recreate list buttons
        list_buttons = []
        print_list()


def delete_selected():
    """Delete selected items."""
    selected_indices = [i for i, var in enumerate(check_vars) if var.get()]
    all_lists = list.returnAllLists()
    remaining_lists = [name for i, name in enumerate(all_lists) if i not in selected_indices]

    # Clear existing widgets and refresh
    for widget in window.winfo_children():
        widget.destroy()

    print("Remaining lists:", remaining_lists)  # Debugging
    initialize_main_window()


def initialize_main_window():
    """Setup the main window elements."""
    global list_buttons
    # Button to create a new list
    new_list_entry = tk.Entry(window, textvariable=new_list_var)
    new_list_entry.pack()

    new_list_btn = tk.Button(window, text="Create New List", command=print_entry)
    new_list_btn.pack()

    # Button to edit lists
    edit_list_btn = tk.Button(window, text="Edit Lists", command=toggle_edit_mode)
    edit_list_btn.pack()

    # Display all lists
    print_list()


def print_entry():
    """Add a new list."""
    if new_list_var.get():  # Check if the value is not empty
        btn = tk.Button(window, text=new_list_var.get())
        btn.pack()
        list_buttons.append(btn)


# Buttons for edit mode
delete_btn = tk.Button(window, text="Delete Selected", command=delete_selected)
cancel_btn = tk.Button(window, text="Cancel", command=toggle_edit_mode)

# Initialize the main window
initialize_main_window()

# Run the main loop
window.mainloop()
