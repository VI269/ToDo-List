import json
import glob
import os

class Lists:
    path = ''
    def __init__(self, folderpath):
        self.path = folderpath
    
    def getDefaultList(self):
        with open(self.path+f"/default.json", 'r') as f:
            load = json.load(f) 
            return load

    def getList(self, name):
        try:
            with open(self.path+f"/{name}.json", 'r') as f:
                load = json.load(f) 
                return load
        except:
            return "List Not Found"
    
    def totalLists(self):
        return [f for f in glob.glob(self.path+"/*.json")]

    def totalListsSelf(self):
        return [glob.glob("/Lists/*.json")]
    
    def searchTask(self, task):
        taskFound = []
        for _task in self.getDefaultList().keys():
            if _task == task:
                taskFound.append(self.getDefaultList()[_task])
        
        for file in self.totalListsSelf().keys():
            for task in self.getList(file):
                if _task == task:
                    taskFound.append(file[_task])
        
        return taskFound
    
    def createList(self, name):
        with open(self.path+f"/{name}.json", 'w') as f:
            return

    def deleteList(self, name):
        try:
            os.remove(self.path+f"/{name}.json")
        except:
            return False
    
    def changeList(self, name, dictionary):
        try:
            with open(self.path+f"/{name}.json", 'w') as f:
                json.dump(dictionary,f)
        except:
            return False

test = Lists(os.path.dirname(os.path.abspath(__file__))+"/Lists")

print(test.totalListsSelf())

