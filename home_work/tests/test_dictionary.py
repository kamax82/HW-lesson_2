import pytest


def test_dict_clear(fix_for_dict):
    '''Dictionary cleanup'''
    fix_for_dict.clear()
    assert len(fix_for_dict) == 0


def test_dict_copy(fix_for_dict):
    '''Try to copy and check the result'''
    copy = fix_for_dict.copy()
    assert fix_for_dict == copy


def test_dict_pop(fix_for_dict):
    '''Remove element by certain key and check the value of the element'''
    element = fix_for_dict.pop(5)
    assert element == 50


def test_dict_items(fix_for_dict):
    '''Convert dictionary into tuple and check certain element'''
    tuple_elbment = (7, 70)
    assert tuple_elbment == list(fix_for_dict.items())[7]


@pytest.mark.parametrize('tries', [1, 2, 3])
def test_dict_update(fix_for_dict, tries):
    '''Updating dictionary by adding new kay: value'''
    upd = {'year': 2020}
    fix_for_dict.update(upd)
    assert fix_for_dict['year'] == 2020
