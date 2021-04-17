import unittest


class TestCC(unittest.TestCase):
    def test1(self):
        self.assertEqual(2, 2, msg='2=2')


if __name__ == '__main__':
    unittest.main()
