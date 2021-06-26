import pytest
from app import get_doc_owner_name, add_new_shelf, delete_doc


class TestApp:

    def setup_class(self):
        pass

    def teardown_class(self):
        pass

    def setup(self):
        print('setup')

    def teardown(self):
        print('teardown')

    @pytest.mark.parametrize('number, result', [('2207 876234', 'Василий Гупкин'),
                                                ('11-2', 'Геннадий Покемонов'),
                                                ('10006', 'Аристарх Павлов'),
                                                ('1111', None)])
    def test_get_doc_owner_name(self, number, result):
        print('Test for func - get_doc_owner_name')
        assert get_doc_owner_name(number) == result

    @pytest.mark.parametrize('number, result', [('1', ('1', False)),
                                                ('3', ('3', False)),
                                                ('4', ('4', True))])
    def test_add_new_shelf(self, number, result):
        print('Test for func - add_new_shelf')
        assert add_new_shelf(number) == result

    @pytest.mark.parametrize('number, result', [('2207 876234', ('2207 876234', True)),
                                                ('10006', ('10006', True)),
                                                ('1111', None)])
    def test_delete_doc(self, number, result):
        print('Test for func - delete_doc')
        assert delete_doc(number) == result
