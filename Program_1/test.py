import unittest
from unittest.mock import mock_open, patch
from main import program1


class TestProgram1(unittest.TestCase):
    #mock
    def test_basic_12345(self):
        m = mock_open(read_data='1\n2\n3\n4\n5')
        with patch('{}.open'.format(__name__), m, create=True):
            with open('example.txt') as h:
                program1(h)
        m().write.assert_called_once_with('\n15')

    #stub
    def test_empty_file(self):
        m = mock_open(read_data='')
        with patch('{}.open'.format(__name__), m, create=True):
            with open('example.txt') as h:
                with self.assertRaises(ValueError):
                    program1(h)

    #mock
    def test_single_number(self):
        m = mock_open(read_data='1')
        with patch('{}.open'.format(__name__), m, create=True):
            with open('example.txt') as h:
                program1(h)
        m().write.assert_called_once_with('\n1')


if __name__ == '__main__':
    unittest.main()
