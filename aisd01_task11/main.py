from bloomfilter import BloomFilter
import pytest


@pytest.fixture
def bf():
    return BloomFilter(32)


def test_hash1(bf):
    mask = bin(bf.hash1("0123456789"))[2:]
    print(f'{mask:>032}', bf.hash1("0123456789"))
    print(bf.hash1("0123456789") & bf.hash1("0123456789"))


def test_hash2(bf):
    mask = bin(bf.hash1("0123456789"))[2:]
    print(f'{mask:>032}', bf.hash2("0123456789"))
    print(bf.hash1("0123456789") & bf.hash2("0123456789"))


def test_add(bf):
    bf.add("0123456789")
    print(bf.filter)


def test_is_value(bf):
    assert not bf.is_value("0123456789")
    bf.add("0123456789")
    assert bf.is_value("0123456789")
