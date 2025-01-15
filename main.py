import tkinter as tk
from tkinter import ttk
import list
import functions



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

def del_list():

    def check_stat():
        remove_array = []
        for i, var in enumerate(check_vars):
            if var.get() == 1:
                remove_array.append(fresh_list_names[i])
        list.remove_list_array(remove_array)
        dl_window.quit()
        dl_window.destroy()
                

    fresh_list_names = list.returnAllLists() # Return
    list_names = [name.split(".")[0] for name in fresh_list_names]
    
    
    width = 250
    height = 350
    dl_window = tk.Toplevel()
    dl_window.title("Delete list..")
    dl_window.geometry(f"{width}x{height}")


    check_vars = []

    # Create Checkbuttons
    for list_name in list_names:
        check_var = tk.IntVar()  # Unique IntVar for each Checkbutton
        check_vars.append(check_var)
        check_box = tk.Checkbutton(
            dl_window,
            text=list_name,
            variable=check_var  # Link IntVar to the Checkbutton
        )
        check_box.pack()

    functions.create_cancel(height, dl_window)

    del_btn = tk.Button(dl_window, text = "Create", command = check_stat)
    del_btn.place(x = width - 10, y = height - 10, anchor="se")


    dl_window.mainloop()

    




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

    def create_list():
        if preview.get() and preview:
            color = color_var.get()
            name = preview.get()
            new_list = list.List(name, color)
            nl_window.quit()
            nl_window.destroy()

    # List of colors
    colors = ["white", "red", "blue", "green", "dark orange", "purple", "dark gray", "goldenrod"]
    width = 250
    height = 350
    # Variables
    color_var = tk.StringVar(value=colors[0])  # Default selection
    preview = tk.StringVar()  # Initial preview text


    nl_window = functions.create_window(width, height)

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

    functions.create_cancel(height, nl_window)

    create_btn = tk.Button(nl_window, text = "Create", command = create_list)
    create_btn.place(x = width - 10, y = height - 10, anchor="se")

    nl_window.mainloop()


mainMenu = tk.Menu(window)

file_menu = tk.Menu(mainMenu, tearoff=False)
file_menu.add_command(label="New List", command=new_list)
file_menu.add_separator()
file_menu.add_command(label="Delete List", command=del_list)
mainMenu.add_cascade(label="List", menu=file_menu)

help_menu = tk.Menu(mainMenu, tearoff=False)
mainMenu.add_cascade(label="Help", menu=help_menu)

window.configure(menu=mainMenu)


# Run the main loop
window.mainloop()
