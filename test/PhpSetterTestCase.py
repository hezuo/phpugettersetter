import unittest
from phputil.FileReader import FileReader
from phputil.phpclass import PhpClass

__author__ = 'hezuo'

class PhpSetterTestCase(unittest.TestCase):
    def testGetAllAttributes(self):
        filepath = "/home/hezuo/repo/phputil/test/input/MyClass.php"
        fr = FileReader(filepath)
        phpClass = PhpClass(fr.readFile())
        phpClass .generateSetters()

        assert phpClass .content != ''