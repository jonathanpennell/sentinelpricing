from sentinelpricing import Framework, TestCase


def test_testcase_quote():
    class A(Framework):
        def setup(self):
            self.x = 1
            print("x")

        def calculation(self, quote):
            return quote + self.x

    class B(A):
        def setup(self):
            self.y = 2
            print("y")

        def calculation(self, quote):
            return quote + self.y

    class C(B):
        def setup(self):
            self.z = 3
            print("z")

        def calculation(self, quote):
            return quote + self.z

    testcase = TestCase({"age": 100})

    for framework in A(), B(), C():
        testcase.quote(framework)

    assert len(testcase.quotes) == 3
