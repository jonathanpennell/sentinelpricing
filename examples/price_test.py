import random

from itertools import chain
from typing import Dict

from sentinelpricing import Framework, LookupTable, PriceTest, TestSuite


def generate_random_testcase() -> Dict[str, float]:
    """Generate Random Testcase

    Creates a dictionary of keys "age" and "lic" with random values.
    """

    return {
        "age": round(random.gammavariate(5, 45 / 5)),
        "lic": 9 - round(random.expovariate(0.8)),
    }


# Creates a list of dictionaries, compatible with the lookup table
# These are the current rates we want to analyse
age_rates = [
    {"age": a, "rate": 1.5 * max((17 / a), 0.8)}
    for a in chain(
        [
            17,
        ],
        range(20, 80, 15),
    )
]

# Creates a list of dictionaries, compatible with the lookup table
# These are the current rates we want to analyse
lic_rates = [{"lic": l, "rate": max(1 - (l * 0.2), 0.8)} for l in range(0, 8)]

price_test_rates = [{"age": i, "rate": 0.9 + (i * 0.5)} for i in range(1, 6)]

# Here we create the random testcases, in reality though you would likely be
# loading these from a csv file or similar.
testcases = TestSuite([generate_random_testcase() for _ in range(10_000)])


class Motor(Framework):
    def setup(self):

        self.base_rate = 1000

        self.age_rates = LookupTable(age_rates)
        self.lic_rates = LookupTable(lic_rates)
        self.price_test = PriceTest("age", LookupTable(price_test_rates))

    def calculation(self, quote):
        quote += self.base_rate
        quote *= self.age_rates[quote["age"]]
        quote *= self.lic_rates[quote["lic"]]

        quote *= self.price_test[quote]

        return quote


qs = Motor.quote_many(testcases)

if hasattr(qs, "price_test"):
    for k in qs.price_test:
        print(repr(qs.price_test.buckets[k]))
    qs.avg(by=qs.price_test.bin)
