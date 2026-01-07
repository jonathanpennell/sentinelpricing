"""Framework Inheritance

This module demonstrates an example implementation of an insurance quote
calculation framework using the 'sentinelpricing' package. It defines several
versions of a motor insurance pricing model (MotorV1 through MotorV4) that
calculate a premium based on a base rate and an additional rate for customers
over 50 years old.


Example Usage: The module provides two example quote dictionaries:
    - 'quote_under_50' for a 25-year-old
    - 'quote_over_50' for a 75-year-old It then generates quotes by
        invoking the 'quote' class method on each MotorV version, printing
        the final quote values and summaries.

This example serves as a guide to how inheritance can save you time and energy,
whilst also ensuring that your frameworks/rates are consistent across multiple
versions.
"""

from sentinelpricing import Framework, Rate


class MotorV1(Framework):
    """MotorV1 (Framework):
    - Implements the basic pricing strategy.
    - In the 'setup' method, it initializes:
        - base_rate = 100
        - over_50_rate = 50
    - The 'calculation' method:
        - Adds the base_rate to the given quote.
        - Checks if the 'age' field in the quote dictionary is greater than 50;
          if so, it adds the over_50_rate.
        - Returns the modified quote.
    """

    name = "MotorV1"

    def setup(self):
        self.base_rate = 100
        self.over_50_rate = 50

    def calculation(self, quote):
        quote += self.base_rate
        if quote["age"] > 50:
            quote += self.over_50_rate
        return quote


class MotorV2(MotorV1):
    """MotorV2 (MotorV1):
    - Inherits from MotorV1 and overrides the 'setup' method.
    - Updates the base_rate to 110 while keeping the over_50_rate
        unchanged.
    """

    name = "MotorV2"

    def setup(self):
        self.base_rate = 110
        self.over_50_rate = 50


class MotorV3(MotorV2):
    """MotorV3 (MotorV2):
    - Further extends MotorV2 by overriding the 'setup' method.
    - Sets the base_rate to 120 with the same over_50_rate.
    """

    name = "MotorV3"

    def setup(self):
        self.base_rate = 120
        self.over_50_rate = 50


class MotorV4(MotorV3):
    """MotorV4 (MotorV4):
    - Intended to demonstrate the use of a Rate object from the package.
    - In the 'setup' method:
        - Sets base_rate to a Rate object labeled "Base Rate" with a value
            of 130.
        - Sets over_50_rate to a Rate object labeled "Over 50's Adjustment"
            with a value of 50.
    """

    name = "MotorV4"

    def setup(self):
        self.base_rate = Rate("Base Rate", 130)
        self.over_50_rate = Rate("Over 50's Adjustment", 50)


quote_under_50 = {"age": 25}

quote_over_50 = {"age": 75}

q1 = MotorV1.quote(quote_under_50)
q2 = MotorV2.quote(quote_under_50)
q3 = MotorV3.quote(quote_under_50)
q4 = MotorV4.quote(quote_under_50)
q5 = MotorV4.quote(quote_over_50)

print("Quote One:".ljust(12), q1)
print("Quote Two:".ljust(12), q2)
print("Quote Three:".ljust(12), q3)
print("Quote Four:".ljust(12), q4)
print("Quote Five:".ljust(12), q5)

print("~" * 70, sep="")

for q in q1, q2, q3, q4, q5:
    print(q.summary())
    print("~" * 70)
