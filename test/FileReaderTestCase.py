from phputil.FileReader import FileReader

__author__ = 'hezuo'
import unittest


class FileReaderTestCase(unittest.TestCase):
    def testReadFile(self):
        filepath = "/home/hezuo/repo/phputil/test/input/MyClass.php"
        fr = FileReader(filepath)
        fr.readFile()
        assert fr.content != ''

    def testReadFileFailed(self):
        filepath = "/home/hezuo/repo/phputil/test/input/MyClass.phpa"
        fr = FileReader(filepath)
        fr.readFile()
        assert fr.content == ''