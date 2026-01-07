from sentinelpricing import Framework, Quote


def test_multiple_inheritance():
    class A(Framework):
        def setup(self):
            self.x = 1
            print("x")

        def calculation(self):
            return 1

    class B(A):
        def setup(self):
            self.y = 2
            print("y")

        def calculation(self):
            return 1

    class C(B):
        def setup(self):
            self.z = 3
            print("z")

        def calculation(self):
            return 1

    a = A()
    assert len(a._setup_methods) == 0
    b = B()
    assert len(b._setup_methods) == 1
    c = C()
    assert len(c._setup_methods) == 2

    assert hasattr(c, "z"), "Has no Z attr"
    assert hasattr(c, "y"), "Has no Y attr"
    assert hasattr(c, "x"), "Has no X attr"

    assert (c.x, c.y, c.z) == (1, 2, 3)


def test_framework_quote():

    def calculate(self, quote):
        quote += 100
        if quote["age"] < 20:
            quote += 500
        return quote

    Motor = type(
        "Motor", (Framework,), {"setup": lambda x: x, "calculation": calculate}
    )

    motor = Motor()

    over_20 = motor.quote({"age": 21})
    under_20 = motor.quote({"age": 19})

    assert isinstance(over_20, Quote)
    assert isinstance(under_20, Quote)

    assert over_20 == 100
    assert under_20 == 600
