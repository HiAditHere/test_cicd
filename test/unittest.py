import unittest
import os
import sys

project_root = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
sys.path.append(project_root)
class TestPipeline(unittest.TestCase):

    def sample(self):
        a = 3
        self.assertEqual(a,3)

if __name__ == '__main__':
    unittest.main()