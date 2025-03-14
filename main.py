import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
import list
import functions
from datetime import datetime

# Initialize the main window
window = tk.Tk()
window.title("TO-DO LIST")
width = 500
height = 700
left = int(window.winfo_screenwidth() / 2) - int(width / 2)
right = int(window.winfo_screenheight() / 2) - int(height / 2)
window.geometry(f"{width}x{height}+{left}+{right}")
input_font = ("Times New Roman", 17, "bold")

list_labels = []  # Keep track of the list labels


header = None
item_frame = None




# Configure row and column weights
window.columnconfigure(0, weight=1, minsize=110)  # Column 0 expands proportionally
window.columnconfigure(1, weight=3, minsize=180)  # Column 1 expands twice as much as column 0
window.rowconfigure(0, weight=1)  # Row 0 expands

def on_left_click(event):

    mouse_x = event.x_root
    mouse_y = event.y_root

    # Get the position of the list_frame relative to the root window
    frame_x = list_frame.winfo_rootx()
    frame_y = list_frame.winfo_rooty()

    # Now calculate the mouse position relative to the list_frame
    x = mouse_x - frame_x
    y = mouse_y - frame_y


    print(f"x: {x}")
    print(f"y: {y}")
    clicked_label = None
    last_label = list_labels[-1]

    if x < last_label.winfo_width() and y < last_label.winfo_height() + last_label.winfo_y():
        for label in list_labels:
            label_top = label.winfo_y()
            label_bottom = label_top + label.winfo_height()
            if y > label_top and y < label_bottom:
                clicked_label = label
            else:
                label.config(bg="#323232")
        show_tasks(clicked_label)


def show_tasks(label):


    global header
    global item_frame

    if header is not None:
        header.destroy()
    
    if item_frame is not None:
        item_frame.destroy()

    label.config(bg="black")
    button = tk.Button(
        task_frame,
        text = "+",
        fg = "black",
    )
    button.place(x = 5, y = 5)

    color = label["fg"]
    title = label["text"]

    header = tk.Label(
        task_frame,
        text = title,
        fg = color,
        font = ("sans-serif", 20)
    )
    header.pack()

    button.bind("<Button-1>", lambda e: create_task(title))

    for list_name in list.returnAllLists():
        if list_name.split(".")[0].lower() == title.lower():
            current_list = list.List(list_name.split(".")[0], list_name.split(".")[1], False)
    tasks = current_list.return_tasks()

    # Create a Frame that will expand to fill the space
    item_frame = tk.Frame(task_frame, bd=5, relief="solid", highlightbackground="blue", highlightcolor="blue")
    item_frame.pack(fill="both", expand=True)


    for task_key, task_data in tasks.items():
        label = tk.Label(
            item_frame,
            text = task_key
        )
        label.pack()
        
        
        
        







def create_task(label):

    def create_task():
        create_task = True
        try:
            datetime.strptime(date_var.get(), "%m-%d")
        except ValueError:
            messagebox.showerror("Error", "Enter Valid Date")
            create_task = False
        
        try: 
            datetime.strptime(time_var.get(), "%H:%M")
        except ValueError:
            messagebox.showerror("Error", "Enter Valid 25Hr Time")
            create_task = False

        if create_task:

            for title in list.returnAllLists():

                if title.split(".")[0].lower() == label.lower():

                    current = list.List(title.split(".")[0], title.split(".")[1], False)
                    current.add_task(task_var.get(), date_var.get(), time_var.get(), dropdown_var.get())
                    nt_window.quit()
                    nt_window.destroy()

                


    nt_window = tk.Toplevel()
    width = 500
    height = 300
    nt_window.geometry(f"{width}x{height}")
    nt_window.title("Task Creation")
    nt_window.focus()

    task_var = tk.StringVar()
    task_entry = tk.Entry(
        nt_window,
        textvariable = task_var)
    task_entry.pack()

    date_var = tk.StringVar()
    date_entry = tk.Entry(
        nt_window,
        textvariable = date_var
    )
    date_entry.pack()

    time_var = tk.StringVar()
    time_entry = tk.Entry(
        nt_window,
        textvariable = time_var
    )
    time_entry.pack()

    
        # Create a Tkinter variable to hold the selected option
    dropdown_var = tk.StringVar()
    dropdown_var.set("Not Started")  # Set the default value

    status = ["Not Started", "In Progress"]

    # Create the dropdown menu (OptionMenu)
    dropdown = tk.OptionMenu(nt_window, dropdown_var, *status)
    dropdown.pack()





    create_btn = tk.Button(nt_window, text="Create", command=create_task)
    create_btn.place(x=width - 10, y=height - 10, anchor="se")

    functions.create_cancel(height, nt_window)

    nt_window.mainloop()


def refresh_list_frame():
    """Refresh the list of labels displayed."""
    # First, clear all the labels from the UI (destroy existing widgets)
    for label in list_labels:
        label.destroy()
    list_labels.clear()  # Reset the list_labels array

    # Fetch the updated list of names from the `list` module
    updated_list_names = list.returnAllLists()

    # Repopulate the frame with updated lists
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
            bg = "#323232",
            wraplength=170,
            width=1
        )
        label.pack(fill="x")
        list_labels.append(label)  # Add the label to the list_labels array

    return list_labels


list_frame = tk.Frame(
    window,
    highlightbackground="grey",
    highlightthickness=2,
    bg="lightgrey"
)
list_frame.grid(column=0, row=0, sticky="nesw")

task_frame = tk.Frame(
    window,
    highlightbackground= "grey",
    highlightthickness=2
)
task_frame.grid(column=1, row=0, sticky="nesw")

# Initial population of list_labels
list_labels = refresh_list_frame()
show_tasks(list_labels[0])

window.bind("<Button-1>", on_left_click)
window.bind("<Escape>", lambda e: window.quit())
window.resizable(False, False)



def del_list():
    def check_stat():
        remove_array = []
        for i, var in enumerate(check_vars):
            if var.get() == 1:
                remove_array.append(fresh_list_names[i])

        list.remove_list_array(remove_array)

        # Refresh the list after deletion
        refresh_list_frame()
        dl_window.quit()
        dl_window.destroy()

    fresh_list_names = list.returnAllLists()  # Return current list of names

    width = 250
    height = 350
    dl_window = tk.Toplevel()
    dl_window.title("Delete list..")
    dl_window.geometry(f"{width}x{height}")
    dl_window.resizable(False, False)

    label = tk.Label(
        dl_window,
        font=("Times New Roman)", 19, "bold"),
        text="Select Lists To Delete"
    )
    label.pack()

    check_vars = []

    # Create Checkbuttons for each list
    for list_name in fresh_list_names:
        check_var = tk.IntVar()  # Unique IntVar for each Checkbutton
        check_vars.append(check_var)
        check_box = tk.Checkbutton(
            dl_window,
            font=input_font,
            fg=list_name.split(".")[1],
            text=list_name.split(".")[0],
            variable=check_var  # Link IntVar to the Checkbutton
        )
        check_box.pack()

    functions.create_cancel(height, dl_window)

    del_btn = tk.Button(dl_window, text="Delete Selected", command=check_stat)
    del_btn.place(x=width - 10, y=height - 10, anchor="se")

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
            if len(preview.get()) > 15 and " " not in preview.get():
                messagebox.showerror("Error", "List can't be more than 15 characters!")
            else:
                new_list = list.List(name.capitalize(), color, True)
                # Refresh the list after creation
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
            font=input_font,
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

    create_btn = tk.Button(nl_window, text="Create", command=create_list)
    create_btn.place(x=width - 10, y=height - 10, anchor="se")

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
