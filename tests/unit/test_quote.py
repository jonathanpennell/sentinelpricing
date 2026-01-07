import uuid
from operator import add, sub, mul, truediv

from sentinelpricing import Quote, Rate, Note, TestCase


def test_init_with_dict():
    data = {"a": 1, "b": 2}
    q = Quote(data)
    assert q.quotedata == data
    assert isinstance(q.id, uuid.UUID)


def test_init_with_testcase():
    data = {"x": 10}
    tc = TestCase(data)
    q = Quote(tc)
    assert q.quotedata == data


def test_repr():
    data = {"val": 5}
    q = Quote(data)
    q += 100
    rep = repr(q)
    assert str(q.id) in rep
    assert "Quote" in rep


def test_getitem_quotedata():
    data = {"key": "value"}
    q = Quote(data)
    assert q["key"] == "value"


def test_getitem_error():
    data = {"a": 1}
    q = Quote(data)
    assert q.get("b", None) is None


def test_add_operation_constant():
    data = {"a": 1}
    q = Quote(data)
    original = q.breakdown.final_price
    q = q + 50
    assert q.breakdown.final_price == add(original, 50)
    assert len(q.breakdown.steps) == 2

    step = q.breakdown.steps[0]
    assert step.name == "ORIG"
    assert step.b == 0
    assert step.result == 0

    step = q.breakdown.steps[1]
    assert step.name == "CONST"
    assert step.oper == add
    assert step.b == 50
    assert step.result == 50


def test_radd_operation_constant():
    data = {"a": 1}
    q = Quote(data)
    original = q.breakdown.final_price
    q = 25 + q
    assert q.breakdown.final_price == add(original, 25)
    assert len(q.breakdown.steps) == 2


def test_sub_operation_constant():
    data = {"a": 1}
    q = Quote(data)
    original = q.breakdown.final_price
    q = q - 30
    assert q.breakdown.final_price == sub(original, 30)
    assert len(q.breakdown.steps) == 2


def test_rsub_operation_constant():
    data = {"a": 1}
    q = Quote(data)
    original = q.breakdown.final_price
    q = 30 - q
    # Note: __rsub__ is implemented the same as __sub__
    assert q.breakdown.final_price == sub(original, 30)
    assert len(q.breakdown.steps) == 2


def test_mul_operation_constant():
    data = {"a": 1}
    q = Quote(data)
    original = q.breakdown.final_price
    q = q * 3
    assert q.breakdown.final_price == mul(original, 3)
    assert len(q.breakdown.steps) == 2


def test_rmul_operation_constant():
    data = {"a": 1}
    q = Quote(data)
    original = q.breakdown.final_price
    q = 3 * q
    assert q.breakdown.final_price == mul(original, 3)
    assert len(q.breakdown.steps) == 2


def test_truediv_operation_constant():
    data = {"a": 1}
    q = Quote(data)
    original = q.breakdown.final_price
    q = q / 4
    assert q.breakdown.final_price == truediv(original, 4)
    assert len(q.breakdown.steps) == 2


def test_rtruediv_operation_constant():
    data = {"a": 1}
    q = Quote(data)
    original = q.breakdown.final_price
    q = 4 / q
    assert q.breakdown.final_price == truediv(original, 4)
    assert len(q.breakdown.steps) == 2


def test_add_with_rate():
    data = {"a": 1}
    q = Quote(data)
    q += 100
    rate = Rate("DISCOUNT", 20)
    q = q + rate
    assert q.breakdown.final_price == add(100, 20)
    step = q.breakdown.steps[-1]
    assert step.name == "DISCOUNT"
    assert step.b == 20


def test_add_quote_merge():
    data = {"a": 1}
    q1 = Quote(data)
    q2 = Quote(data)

    q1 += 100
    q2 += 200

    result = q1 + q2
    # When adding two Quotes, the operation is a merge (no change).
    assert result is q1
    assert q1.breakdown.final_price == 100


def test_eq():
    data = {"a": 1}
    q1 = Quote(data)
    q2 = Quote(data)
    q3 = Quote(data)

    q1 += 100
    q2 += 100
    q3 += 150

    assert q1 == q2
    assert q1 == 100
    assert q3 != 100


def test_lt():
    data = {"a": 1}
    q1 = Quote(data)
    q2 = Quote(data)

    q1 += 100
    q2 += 150

    assert q1 < q2
    assert q1 < 150


def test_gt_le_ge():
    data = {"a": 1}
    q1 = Quote(data)
    q2 = Quote(data)
    q3 = Quote(data)

    q1 += 100
    q2 += 100
    q3 += 50

    assert q1 == q2
    assert not q1 < q2
    assert not q1 > q2
    assert q1 > q3
    assert q3 < q1


def test_note():
    data = {"a": 1}
    q = Quote(data)
    q.note("Test note")
    last = q.breakdown.steps[-1]
    assert isinstance(last, Note)
    assert last.text == "Test note"


def test_final_price_property():
    data = {"a": 1}
    q = Quote(data)
    q += 75
    assert q.final_price == 75
