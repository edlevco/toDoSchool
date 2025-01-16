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
input_font = ("Times New Roman", 17, "bold")

# Configure row and column weights
window.columnconfigure(0, weight=1, minsize = 70)  # Column 0 expands proportionally
window.columnconfigure(1, weight=3)  # Column 1 expands twice as much as column 0
window.rowconfigure(0, weight=1)     # Row 0 expands

def refresh_list_frame():
    # Clear the existing widgets in the list_frame
    for widget in list_frame.winfo_children():
        widget.destroy()

    # Fetch the updated list of names
    updated_list_names = list.returnAllLists()

    # Repopulate the frame with the updated lists
    for list_name in updated_list_names:
        label = tk.Label(
            list_frame,
            text=list_name.split(".")[0].capitalize(),
            fg=list_name.split(".")[1],
            highlightbackground="grey",
            highlightthickness=1,
            pady=5,
            anchor="w",
            font=("Times New Roman", 20),
            wraplength= 170,
            width = 1
            
        )
        label.pack(fill="x")



list_frame = tk.Frame(
    window,
    highlightbackground="grey",
    highlightthickness=2,
    bg = "lightgrey"
)
list_frame.grid(column = 0, row = 0, sticky="nesw")

refresh_list_frame()






# window.bind("<Button-1>", on_left_click)
window.bind("<Escape>", lambda e: window.quit())
window.resizable(False, False)

def del_list():

    def check_stat():
        remove_array = []
        for i, var in enumerate(check_vars):
            if var.get() == 1:
                remove_array.append(fresh_list_names[i])
        list.remove_list_array(remove_array)
        refresh_list_frame()
        dl_window.quit()
        dl_window.destroy()
                

    fresh_list_names = list.returnAllLists() # Return

    

    width = 250
    height = 350
    dl_window = tk.Toplevel()
    dl_window.title("Delete list..")
    dl_window.geometry(f"{width}x{height}")
    dl_window.resizable(False, False)


    label = tk.Label(
        dl_window,
        font = ("Times New Roman)", 19, "bold"),
        text = "Select Lists To Delete"
    )
    label.pack()


    check_vars = []

    # Create Checkbuttons
    for list_name in fresh_list_names:
        check_var = tk.IntVar()  # Unique IntVar for each Checkbutton
        check_vars.append(check_var)
        check_box = tk.Checkbutton(
            dl_window,
            font = input_font,
            fg = list_name.split(".")[1],
            text=list_name.split(".")[0],
            variable=check_var  # Link IntVar to the Checkbutton
        )
        check_box.pack()

    functions.create_cancel(height, dl_window)

    del_btn = tk.Button(dl_window, text = "Delete Selected", command = check_stat)
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
            refresh_list_frame()
            nl_window.quit()
            nl_window.destroy()

    # List of colors
    colors = ["white", "red", "blue", "green", "dark orange", "purple", "dark gray", "goldenrod"]
    width = 250
    height = 400
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
            font = input_font,
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

# crashes when method is called with help window
# help_menu = tk.Menu(mainMenu, tearoff=False)
# mainMenu.add_cascade(label="Help", menu=help_menu)

window.configure(menu=mainMenu)


# Run the main loop
window.mainloop()
