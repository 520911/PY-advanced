import create_ya_folder as cyf
import unittest


class YaTests(unittest.TestCase):

    def test_create_ya_folder(self):
        self.assertEqual(cyf.create_ya_folder('test'), 201)

    def test_create_ya_folder_409(self):
        self.assertEqual(cyf.create_ya_folder('test'), 409)


if __name__ == '__main__':
    unittest.main()
