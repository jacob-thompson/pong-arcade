import unittest

import pygame

class TestPong(unittest.TestCase):
    def test_pygame_works(self):
        pygame.init()
        self.assertTrue(pygame.get_init())

if __name__ == '__main__':
    unittest.main()