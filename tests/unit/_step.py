import operator

from sentinelpricing import Step


def test_step_init():
    s = Step(100, operator.add, 100, "CONST")
    assert isinstance(s, Step)
