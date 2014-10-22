__author__ = 'hezuo'
from os.path import exists

class FileReader:
    filepath = ''
    content = ''

    def __init__(self, filepath):
        self.filepath = filepath

    def readFile(self):
        self.content = ''
        if( exists(self.filepath) ):
            with open(self.filepath, 'r') as f:
                for line in f:
                    self.content += line
                f.closed
            return self.content
    def getAllAttributes(self):
        self.content




