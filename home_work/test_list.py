import pytest


def test_list_insert(fix_for_list):
    '''Insert "hello' in third position in the list and checking result'''
    fix_for_list.insert(2,'hello')
    assert fix_for_list[0] == 1 and fix_for_list[2] == 'hello' and fix_for_list[3] == 3


def test_list_count(fix_for_list):
    '''Checking counting of particular values'''
    fix_for_list.insert(7, 2)
    assert fix_for_list.count(2) == 2


def test_list_reverse(fix_for_list):
    '''Checking reverse orders'''
    fix_for_list.reverse()
    assert fix_for_list[0] == 10 and fix_for_list[-1] == 1

def test_list_remove(fix_for_list):
    '''Checking removing a value from list'''
    fix_for_list.remove(5)
    assert fix_for_list.count(5) == 0

@pytest.mark.parametrize('loop', [100,200,300])
def test_list_extend(fix_for_list, loop):
    '''Checking list extension by calling the last key. Every pass adding additional parameter'''
    to_extand = [i for i in range(11,21)]
    to_extand.append(loop)
    fix_for_list.extend(to_extand)
    assert fix_for_list[-1] == loop
