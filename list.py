import os
import json
from datetime import datetime
from termcolor import colored

FILE_NAME = "all_lists.json"

class List:

    def __init__ (self, list_name, color, new):
        self.list_name = list_name
        self.color = color
        self.initialize_list()
        if new:
            self.make_key()

    def return_tasks(self):
        data = self.load_list()

        return data["lists"][self.list_name+"."+self.color]

    def initialize_list (self):
        if not os.path.exists(FILE_NAME):
            with open(FILE_NAME, "w") as f:
                json.dump({"lists": {}}, f, indent = 4)

    def make_key(self):
        data = self.load_list()
        data["lists"][self.list_name+"."+self.color] = {
        }
        self.save_list(data)

    def add_task(self, name, date, time, progress):
        data = self.load_list()
        
        data["lists"][self.list_name+"."+self.color][name] = {
            "date": date,
            "time": time,
            "status": progress,
        }
        self.save_list(data)

    def load_list(self):
        with open(FILE_NAME, "r") as f:
            return json.load(f)
    
    def save_list(self, data):
        with open(FILE_NAME, "w") as f:
                json.dump(data, f, indent = 4)
    
    def print_all_names(self):
        data = self.load_list()
        for i, name in enumerate(data["tasks"][self.list_name].keys(), start = 1):
            print(f"{i}) {name}")
        
        return i
            

    def getListName(index):
        json_files = [file.split(".")[0] for file in os.listdir("lists") if file.endswith('.json')]
        return json_files[index-1]

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

def returnAllLists():
        with open("all_lists.json", "r") as f:
            data = json.load(f)
            return list(data["lists"].keys())
        
def remove_item(self, index):
    data = self.load_list()
    all_items = list(data["lists"].keys())

    key_to_remove = all_items[index]
    del data["lists"][key_to_remove]  # Remove the key-value pair
    self.save_list(data)
    

def remove_list_array(all_names):
    with open("all_lists.json", "r") as f:
        data = json.load(f)

        for name in all_names:
            del data["lists"][name]
    
    with open(FILE_NAME, "w") as f:
        json.dump(data, f, indent = 4)
    
    
        

        




                


        




