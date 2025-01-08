import list
from termcolor import colored


def __main__():
    print(colored("Welcome to your schoolTool", "cyan"))

    running = True

    while running:

        mainOption = list.getValidInt("Main Window:\n(1) Make New List\n(2) Delete List\n(3) Change List Name\n(4) Enter List", 1, 4)

        if mainOption == 1:
            newListName = list.createNewList()
            if newListName:
                currentList = list.List(newListName)
        if mainOption == 4:
            max = list.printAllListNames()
            listChoice = list.getValidInt("Which List do you want to enter?", 1, max )
            currentList = list.List(list.getListName(listChoice))
            


        inList = True
        while inList:
            inListOptions = list.getValidInt(f"{currentList.list_name}:\n(1) Add New Item\n(2) Complete Item\n(3) View List", 1, 3)

            if inListOptions == 1:
                currentList.add_task()
            if inListOptions == 2:
                max = currentList.print_all_names()
                removeIndex = list.getValidInt("Which item do you want to remove? ", 1, max)
                currentList.remove_item(removeIndex)


            currentList.print_list()

                



        
        
        

    




__main__()