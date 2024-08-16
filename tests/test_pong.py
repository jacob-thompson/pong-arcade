import unittest

import pygame

class TestPong(unittest.TestCase):
    def test_pygame_works(self):
        pygame.display.init()
        pygame.font.init()
        #pygame.mixer.init()

        self.assertTrue(pygame.display.get_init())
        self.assertTrue(pygame.font.get_init())
        #self.assertTrue(pygame.mixer.get_init() != None)

        pygame.display.quit()
        pygame.font.quit()
        #pygame.mixer.quit()

        # unittest modules seem to be unable to access
        ## audio devices, so pygame.mixer module
        ## can not be tested in this manner

if __name__ == '__main__':
    unittest.main()