import os 
from listgetter import Lists

path = os.path.dirname(os.path.abspath(__file__))+"/Lists"
list_controller = Lists(path)
lis = ''

def getList():
    inp = input("List > ")
    return inp

def getTask():
    inp = input("Task > ")
    return inp

def search(task):
    return list_controller.searchTask(task)

def getCmd():
    inp = input("Command > ")
    return inp

def change_list(inp):
    lis = inp

def main():
    cmd = getCmd().lower()
    if cmd == "list":
        change_list(getList())
    
    elif cmd == 'search':
        print(search(getTask()))

if __name__ == '__main__':
    main()

