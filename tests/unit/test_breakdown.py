import unittest

from sentinelpricing import Breakdown

TEST_QUOTE_ID = 123


def test_init_breakdown():
    assert len(Breakdown(TEST_QUOTE_ID)) == 1


def test_breakdown_append():
    b = Breakdown(TEST_QUOTE_ID)
    b.append("Note")
    assert len(b) == 2


def test_breakdown_repr():
    b = Breakdown(TEST_QUOTE_ID)
    assert isinstance(repr(b), str)
