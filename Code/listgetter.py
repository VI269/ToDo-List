import json
import glob

class Lists:
    path = ''
    def __init__(self, folderpath):
        self.path = folderpath
    
    def getDefaultList(self):
        return json.load(open(self.path+"/default.json", 'r'))
    
    def getList(self, name):
        try:
            return json.load(open(self.path+f"/{name}.json", 'r')) 
        except:
            return "List Not Found"
    
    def totalLists(self):
        return [f for f in glob.glob(self.path+"/*.json")]
    
    def searchTask(self, task):
        taskFound = []
        for _task in self.getDefaultList():
            if _task == task:
                taskFound.append(_task)
        
        for file in self.totalLists():
            for task in self.getList(file):
                if _task == task:
                    taskFound.append(_task)
        
        return taskFound