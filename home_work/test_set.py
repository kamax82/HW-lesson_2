import pytest


def test_set_isdisjoint(fix_for_set):
    '''Checking whether sets do not have the same elements'''
    other_set = set('hello')
    assert fix_for_set.isdisjoint(other_set) == True


def test_set_intersection(fix_for_set):
    '''Checking counting of particular values'''
    set_2 = set([3, 5, 6, 7, 10, 11])
    inersected = fix_for_set.intersection(set_2)
    assert len(inersected) == 2


def test_set_add(fix_for_set):
    '''Checking adding an element'''
    fix_for_set.add('hello')
    assert len(fix_for_set) == 11 and ('hello' in fix_for_set) == True


def test_set_discard(fix_for_set):
    '''Checking removing a value from set'''
    fix_for_set.discard(6)
    assert (6 not in  fix_for_set) == True


@pytest.mark.parametrize('new_values_for_set', ['o','t','u','s'])
def test_set_len(fix_for_set, new_values_for_set):
    '''Checking length of set'''
    fix_for_set.add(new_values_for_set)
    assert len(fix_for_set) == len(new_values_for_set)+10