from itertools import chain

from sentinelpricing import Framework, LookupTable, TestCase


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


class MotorV1(Framework):
    def setup(self):
        self.age = LookupTable(age_rates, name="age")
        self.lic = LookupTable(lic_rates, name="license years")

    def calculation(self, quote):
        age_rate = self.age[quote["age"]]
        lic_rate = self.lic[quote["lic"]]

        quote += 400
        quote *= age_rate
        quote *= lic_rate

        quote += 4000

        if quote > 3_000:
            quote.override(
                final_price=3000, message="Quote over allowed amount."
            )

        return quote


q = MotorV1.quote({"age": 20, "lic": 3})

print(q.breakdown)
