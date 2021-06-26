import unittest

from parameterized import parameterized

from app import get_doc_owner_name, add_new_shelf, check_document_existance


class AppTests(unittest.TestCase):

    def setUp(self):
        print('SetUp metod')

    def tearDown(self):
        print('TearDown metod')

    @parameterized.expand([
        ['2207 876234', 'Василий Гупкин'],
        ['11-2', 'Геннадий Покемонов'],
        ['10006', 'Аристарх Павлов'],
        ['1111', None]
    ])
    def test_get_doc_owner_name(self, number, result):
        self.assertEqual(get_doc_owner_name(number), result)

    @parameterized.expand([
        ['1', ('1', False)],
        ['3', ('3', False)],
        ['5', ('5', True)]
    ])
    def test_add_new_shelf(self, number, result):
        self.assertEqual(add_new_shelf(number), result)

    @parameterized.expand([
        ['2207 876234', True],
        ['11-2', True],
        ['10006', True]
    ])
    def test_check_document_existance(self, number, result):
        self.assertEqual(check_document_existance(number), result)


if __name__ == '__main__':
    unittest.main()
