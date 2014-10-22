import re
__author__ = 'hezuo'

class PhpClass():
    content = ''
    setters = list()

    def __init__(self, content):
        self.content = content

    def generateSetters(self):
        self.__getAllPrivateAttributes()

    def __getAllPrivateAttributes(self):
        attributes = Attributes();
        pattern = 'private[\\s]+[\n]*[$][\\w\\d]*[\\s]*;'
        attributes.attributesRaw = re.findall(pattern, self.content)
        attributes.getAllAttributes()
        print attributes.attributes




class Attributes():
    attributesRaw = list()
    attributes = list()

    def getAllAttributes(self):
        self.attributes = list()
        print self.attributesRaw

        for attr in self.attributesRaw:
            tmp = attr.replace(";", "")
            tmp = tmp.strip()
            tmp = tmp[7:]
            tmp = tmp.replace("\n", "")
            tmp = tmp.strip()
            self.attributes.append(tmp)

        return self.attributes


