import unittest

class TestPipeline(unittest.TestCase):

    def sample(self):
        a = 3
        self.assertEqual(a,3)

if __name__ == '__main__':
    unittest.main()