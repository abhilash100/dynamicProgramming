import unittest
import sys
import os

PACKAGE_PARENT = '..'
SCRIPT_DIR = os.path.dirname(os.path.realpath(os.path.join(os.getcwd(), os.path.expanduser(__file__))))
sys.path.append(os.path.normpath(os.path.join(SCRIPT_DIR, PACKAGE_PARENT)))

from dp_common.mode import Mode
from generic.jump_game import JumpGame


class JumpGameTest(unittest.TestCase):
    def test_jump_game1(self):
        jump_game = JumpGame()
        self.assertEqual(jump_game.jump_game1([2,3,1,1,4]), True)
        self.assertEqual(jump_game.jump_game1([3,2,1,0,4]), False)
        self.assertEqual(jump_game.jump_game1([2,0,0]), True)
        self.assertEqual(jump_game.jump_game1([0]), True)

        self.assertEqual(jump_game.jump_game1_memo([2, 3, 1, 1, 4]), True)
        self.assertEqual(jump_game.jump_game1_memo([3, 2, 1, 0, 4]), False)
        self.assertEqual(jump_game.jump_game1_memo([2, 0, 0]), True)
        self.assertEqual(jump_game.jump_game1_memo([0]), True)

        self.assertEqual(jump_game.jump_game1_tab([2,3,1,1,4]), True)
        self.assertEqual(jump_game.jump_game1_tab([3,2,1,0,4]), False)
        self.assertEqual(jump_game.jump_game1_tab([2,0,0]), True)
        self.assertEqual(jump_game.jump_game1_tab([0]), True)

    def test_jump_game2(self):
        jump_game = JumpGame()

        self.assertEqual(jump_game.jump_game2([2,3,1,1,4]), 2)
        self.assertEqual(jump_game.jump_game2([2,3,0,1,4]), 2)
        self.assertEqual(jump_game.jump_game2([5,6,4,4,6,9,4,4,7,4,4,8,2,6,8,1,5,9,6,5,2]), 3)

        self.assertEqual(jump_game.jump_game2_memo([2,3,1,1,4]), 2)
        self.assertEqual(jump_game.jump_game2_memo([2,3,0,1,4]), 2)
        self.assertEqual(jump_game.jump_game2_memo([5,6,4,4,6,9,4,4,7,4,4,8,2,6,8,1,5,9,6,5,2]), 3)

        self.assertEqual(jump_game.jump_game2_tab([2,3,1,1,4]), 2)
        self.assertEqual(jump_game.jump_game2_tab([2,3,0,1,4]), 2)
        self.assertEqual(jump_game.jump_game2_tab([5,6,4,4,6,9,4,4,7,4,4,8,2,6,8,1,5,9,6,5,2]), 3)



if __name__ == '__main__':
    unittest.main()
