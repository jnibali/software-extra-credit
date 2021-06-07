import unittest
import sentence_reverse

class testCaseAdd(unittest.TestCase):
    def test_volume(self):
        self.assertEqual(sentence_reverse.reverse("My name is V Tadimeti"),"Tadimeti V is name My")
       
#tests for additon, then subtraction, then multiply, and then division
#select right options in terminal when testing

if __name__ == '__main__':
    unittest.main()