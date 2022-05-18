from nativedictionary import NativeDictionary
import pytest


@pytest.fixture
def nativedictionary():
    return NativeDictionary(17)


def test_hash_fun(nativedictionary):
    assert nativedictionary.hash_fun('a') == 1
    assert nativedictionary.hash_fun('aa') == 2
    assert nativedictionary.hash_fun('aaa') == 3


def test_is_key(nativedictionary):
    nativedictionary.put('b', 1)
    assert nativedictionary.is_key('a') is False
    assert nativedictionary.is_key('b') is True


def test_put(nativedictionary):
    nativedictionary.put('a', 100)
    nativedictionary.put('aa', 125)
    nativedictionary.put('aaa', 150)
    assert nativedictionary.values[1] == 'a'
    assert nativedictionary.slots[1] == 100
    assert nativedictionary.values[2] == 'aa'
    assert nativedictionary.slots[2] == 125
    assert nativedictionary.values[3] == 'aaa'
    assert nativedictionary.slots[3] == 150
    nativedictionary.put('aaa', 175)
    assert nativedictionary.values[3] == 'aaa'
    assert nativedictionary.slots[3] == 175


def test_get(nativedictionary):
    nativedictionary.put('a', 100)
    nativedictionary.put('aa', 125)
    nativedictionary.put('aaa', 150)
    assert nativedictionary.get('') is None
    assert nativedictionary.get('aaaa') is None
    assert nativedictionary.get('b') is None
    assert nativedictionary.get('a') == 100
    assert nativedictionary.get('aa') == 125
    assert nativedictionary.get('aaa') == 150
