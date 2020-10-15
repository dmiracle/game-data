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

    def test_random_hindrances(self):
        for _ in range(100):
            d, n = self.test_char.get_random_hindrances()
            Ms = sum(v == 'M' for v in d.values())
            ms = sum(v == 'm' for v in d.values())
            self.assertTrue(n == ms + 2 * Ms)

    def test_add_edge(self):
        print(self.test_char.edges)
        print(self.test_char.get_random_edge())
        print(self.test_char.get_random_edges(4))
        self.test_char.generate_random_character()
        print(self.test_char)

if __name__ == '__main__':
    unittest.main()