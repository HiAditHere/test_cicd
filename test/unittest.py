import unittest
import os
import sys

project_root = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
sys.path.append(project_root)
class TestPipeline(unittest.TestCase):

    def test_sample(self):
        a = 2
        self.assertEqual(a,3)