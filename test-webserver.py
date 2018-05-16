import unittest
from webserver import hello,different


class TestApp(unittest.TestCase):

    def test_hello_world(self):
        # print('hello_world')
        self.assertEqual(hello(), "Hello World!")

    def test_different(self):
        # print('A different world')
        self.assertEqual(different(), "A different world")


if __name__ == '__main__':
    unittest.main()

