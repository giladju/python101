import os
import flask
import unittest
import tempfile

class FlaskrTestCase(unittest.TestCase):

  def test_message(self):
    flask.app.testing = True
    self.route("/")
    rv = self.app.route('/')
    assert b'Hello World' in rv.data

if __name__ == '__main__':
    unittest.main()

