from sentinelpricing import Quote, QuoteSet


def test_quoteset_init():
    quotes = [Quote({"age": i + 17, "lic": i + 17}) for i in range(25)]

    qs = QuoteSet(quotes)

    assert isinstance(qs, QuoteSet)


def test_quoteset_get():
    quotes = [Quote({"age": i + 17, "lic": i + 17}) for i in range(25)]

    qs = QuoteSet(quotes)

    qs.quotes.insert(15, Quote({"age": 0, "lic": 18}))

    assert qs[15]["age"] == 0


def test_quoteset_add():
    LEN = 5
    quotes = [Quote({"age": i + 17}) for i in range(LEN)]
    other_quotes = [Quote({"lic": i + 17}) for i in range(LEN)]

    qs = QuoteSet(quotes)
    other_qs = QuoteSet(other_quotes)

    combined = qs + other_qs

    assert isinstance(combined, QuoteSet)
    assert len(combined) == LEN * 2
    print(combined[0])
    print("age" in combined[0])
    assert "age" in combined[0]
    assert "age" not in combined[5]
    assert "lic" not in combined[0]
    assert "lic" in combined[5]


def test_quoteset_max():
    quotes = [Quote({"age": i + 17, "lic": i + 17, "i": i}) for i in range(25)]

    quotes = [q + (q["i"] * 5) for q in quotes]

    qs = QuoteSet(quotes)

    assert qs.max() == 24 * 5


def test_quoteset_max_by():
    quotes = [Quote({"age": i + 17, "lic": i + 17, "i": i}) for i in range(25)]

    quotes = [q + (q["i"] * 5) for q in quotes]

    qs = QuoteSet(quotes)

    assert qs.max(by="age") == {k + 17: k * 5 for k in range(25)}


def test_quoteset_max_where():
    quotes = [Quote({"age": i + 17, "lic": i + 17, "i": i}) for i in range(25)]

    quotes = [q + (q["i"] * 5) for q in quotes]

    qs = QuoteSet(quotes)
    max_where = qs.max(where=lambda x: x["age"] < 25)
    expected = 5 * (24 - 17)
    assert max_where == expected


def test_quoteset_max_by_where():
    quotes = [Quote({"age": i + 17, "lic": i + 17, "i": i}) for i in range(25)]

    quotes = [q + (q["i"] * 5) for q in quotes]

    qs = QuoteSet(quotes)
    max_where = qs.max(by="age", where=lambda x: x["age"] < 20)
    expected = {k + 17: k * 5 for k in range(0, 20 - 17)}
    assert max_where == expected
