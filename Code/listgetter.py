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
        start = [f for f in glob.glob(self.path+"/*.json")]
        out = []
        for lis in start:
            out.append((lis.split('/')[-1])[:-5])
        return out
    
    def searchTask(self, task):
        tasks_found = []
        for defTask, defProg in self.getDefaultList().items():
            if defTask == task:
                tasks_found.append(defProg)
        
        for lists in self.totalLists():
            for tas, prog in self.getList(lists).items():
                if tas == task:
                    tasks_found.append(prog)
        
        return None if tasks_found == [] else tasks_found
    
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
    
    def changeTo(self, task, completion, listed):
        try:
            lis = self.getList(listed)
            lis[task] = completion
            self.changeList(listed, lis)
            return
        except:
            return False

