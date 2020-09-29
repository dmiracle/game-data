import unittest
import sys
import os

sys.path.append(os.path.dirname(__file__))

from character import Character
class TestCharacter(unittest.TestCase):
    
    test_char = Character("Alice")

    def test_constructor(self):
        self.assertTrue(self.test_char.name)
        self.assertTrue(self.test_char.uid)

    def test_init_props(self):
        self.test_char.get_random_hindrances()
        self.assertTrue(self.test_char.get_random_hindrances())

if __name__ == '__main__':
    unittest.main()