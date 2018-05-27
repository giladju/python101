import unittest
from webserver import hello,different


class TestApp(unittest.TestCase):

    def test_hello_world(self):
        self.assertEqual(hello(), "Hello World!")

    def test_different(self):
        self.assertEqual(different(), "A different world")

    # def test_get_message_id(self):
    #     self.assertTrue(message(), is int, "Is integer")


if __name__ == '__main__':
    unittest.main()

