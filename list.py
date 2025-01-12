import os
import json
from datetime import datetime
from termcolor import colored

class List:

    

    def __init__ (self, list_name):
        self.file_name = "all_lists.json"
        self.list_name = list_name
        self.initialize_list()

    def initialize_list (self):
        if not os.path.exists(self.file_name):
            with open(self.file_name, "w") as f:
                json.dump({"lists": {}}, f, indent = 4)

    def add_task(self):
        data = self.load_list()
        
        name = input("Enter task name: ")
        description = input("Enter task description: ")
        status = getValidInt("""
                                (1) Not Started
                                (2) In Progress

""", 1, 2)

        date = self.getValidDate("Enter tasks due date (yyyy-mm-dd): ")
    
        data["tasks"][self.list_name][name] = {
            "description": description,
            "status": status,
            "date": date,
        }
        self.save_list(data)

    def load_list(self):
        with open(self.file_name, "r") as f:
            return json.load(f)
    
    def save_list(self, data):
        with open(self.file_name, "w") as f:
                json.dump(data, f, indent = 4)
    
    def print_tasks(self):
        data = self.load_list()
        names = list(data["lists"][self.list_name].keys())
        print(f"List name: {self.list_name}")

        # Mapping of status to messages and colors
        status_map = {
            1: ("un-started", "red"),
            2: ("inprogress", "yellow")
        }

                # Iterate through the tasks
        for key, task in data["tasks"].items():
            print(f"Task: {key}")
            print(f"Description: {task['description']}")
            
            # Get the status
            task_status = task.get("status", 0)  # Default to 0 if "status" is missing
            message, color = status_map.get(task_status, ("unknown", "white"))
            print(colored(message, color))


    def print_all_names(self):
        data = self.load_list()
        for i, name in enumerate(data["tasks"][self.list_name].keys(), start = 1):
            print(f"{i}) {name}")
        
        return i
            

    def remove_item(self, index):
        data = self.load_list()
        all_items = list(data["tasks"].keys())

        key_to_remove = all_items[index-1]
        del data["tasks"][key_to_remove]  # Remove the key-value pair
        self.save_list(data)




    def getValidDate(self, prompt, date_format="%Y-%m-%d"):
        while True:
            try:
                user_input = input(prompt)
                valid_date = datetime.strptime(user_input, date_format)
                
                # Ensure the date is not in the past
                if valid_date < datetime.now():
                    print("The date cannot be in the past. Please enter a future date.")
                    continue
                
                # Return the date as a string for JSON compatibility
                return valid_date.strftime(date_format)
            except ValueError:
                print(f"Invalid date. Please enter in the format: {date_format}")

def getValidInt(prompt, min, max):
        while True:
            try:
                num = int(input(prompt))

                if num <= max and num >= min:
                    return num
                else:
                    print("Integer out of range: Try again: ")

            except ValueError:
                print("Invalid Integer: Try again: ")

def createNewList():
    json_files = [file for file in os.listdir("lists") if file.endswith('.json')]
    while True:
        list_name = (input("Enter the name of the new list: ")).lower()

        for file in json_files:
            if list_name == file.split('.')[0]:
                print(f"There is already a list with the name: {list_name}")
                return None
        
        return list_name
    
def printAllListNames():


    for index, file in enumerate(json_files, start=1):
        print(f"{index}) {file}")
    
    return index

def getListName(index):
    json_files = [file.split(".")[0] for file in os.listdir("lists") if file.endswith('.json')]
    return json_files[index-1]


                


        




