import json, random

class KanjiData():
    def __init__(self, path):
        srcFile = open(path, "r")
        srcString = srcFile.read()
        srcFile.close()
        
        self.data = json.loads(srcString)

    def GetRandomCharacter(self):
        listLength = len(self.data)
        randIndex = random.randint(0, listLength-1)

        return self.data.items()[randIndex]
        
