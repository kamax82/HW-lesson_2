import pytest


def test_string_split(fix_for_string):
    '''Split checking'''
    splitted = fix_for_string.split(' ')
    assert splitted[0] == 'Classical' and splitted[1] == 'hello' and splitted[2] == 'world'


def test_string_rfind(fix_for_string):
    '''Checking key of certain substring'''
    rfind = fix_for_string.rfind('ll')
    assert rfind == 12


def test_string_upper(fix_for_string):
    '''Checking detecting uppercase and not uppercase strings'''
    upper = fix_for_string.upper()
    assert (fix_for_string.isupper() == False) and (upper.isupper() == True)


def test_string_ljust(fix_for_string):
    '''Checking function ljust. It should return a given element as last in string'''
    supplemented = fix_for_string.ljust(30, "!")
    assert supplemented[29] == '!'


@pytest.mark.parametrize('exapmle', ['Boring'])
def test_string_replace(fix_for_string, exapmle):
    '''Checking string component replacement'''
    replaced = fix_for_string.replace('Classical', exapmle)
    assert replaced == 'Boring hello world'
