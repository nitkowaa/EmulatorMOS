import unittest
x = 0

def command(x):
    x = 0  #Placeholder for more actual method

class TestCommandsMethods(unittest.TestCase):


    def test_commandCMP(self):
        self.assertEqual('CMP',command(x))

if __name__ == '__main__':
    unittest.main()