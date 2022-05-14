import time
import unittest
from Common.SetUp.SetUpFile import Set_Up_Class

class Mac_Mini_Test_Class(unittest.TestCase, Set_Up_Class):
    def SetUp(self):
        self.generalSetUp()

    def tearDown(self):
        time.sleep(1)
        self.driver.close()