from hashtable import HashTable
import pytest


@pytest.fixture
def hashtable():
    return HashTable(17, 3)


def test_hash_fun(hashtable):
    assert hashtable.hash_fun('aaa') == hashtable.hash_fun('aaa')
    assert hashtable.hash_fun('aaa') != hashtable.hash_fun('aa')
    assert hashtable.hash_fun('aab') == hashtable.hash_fun('aab')


def test_seek_slot(hashtable):
    assert hashtable.seek_slot('aaa') == 3
    assert hashtable.seek_slot('aa') == 2
    assert hashtable.seek_slot('aaba') == 4


def test_put(hashtable):
    assert hashtable.put('aaa') == 3
    assert hashtable.put('aa') == 2


def test_find(hashtable):
    assert hashtable.find('aaa b') is None
    assert hashtable.find('a') is None
