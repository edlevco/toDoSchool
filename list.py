import os
import json
from datetime import datetime

class List:

    def __init__ (self, list_name):
        self.list_name = list_name
        self.list_file = list_name+".json"
        self.initialize_list()

    def initialize_list (self):
        if not os.path.exists(self.list_file):
            with open(self.list_file, "w") as f:
                json.dump({"tasks": {}}, f, indent = 4)

    def add_task(self):
        data = self.load_list()
        
        name = input("Enter task name: ")
        description = input("Enter task description: ")
        status = self.getValidInt("""
                                (1) Not Started
                                (2) In Progress

""", 1, 2)

        date = self.getValidDate("Enter tasks due date (yyyy-mm-dd): ")
    
        data["tasks"][name] = {
            "description": description,
            "status": status,
            "date": date,
        }

        self.save_list(data)

    def load_list(self):
        with open(self.list_file, "r") as f:
            return json.load(f)
    
    def save_list(self, data):
        with open(self.list_file, "w") as f:
                json.dump(data, f, indent = 4)
    
    def print_list(self):
        data = self.load_list()
        print(f"List name: {self.list_name}")


    def print_all_names(self):
        data = self.load_list()
        for name, i in data["tasks"]["name"]:
            print(f"{i}) {name}")
            


    def remove_item(self, name):
        pass


    def getValidInt(self, prompt, min, max):
        while True:
            try:
                num = int(input(prompt))

                if num <= max and num >= min:
                    return num
                else:
                    print("Integer out of range: Try again: ")

            except ValueError:
                print("Invalid Integer: Try again: ")

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



                


        




