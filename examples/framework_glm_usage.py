from sentinelpricing import Framework, LookupTable

# Rates are for illustrative purposes only...
region_rates = [
    {"region": "USA", "rate": 5},
    {"region": "Americas", "rate": 3},
    {"region": "Europe", "rate": 2},
    {"region": "Asia", "rate": 3},
]

group_rates = [
    {"group_type": "single", "rate": 1},
    {"group_type": "couple", "rate": 0.8},
    {"group_type": "family", "rate": 0.9},
    {"group_type": "group", "rate": 1.5},
]

base_rates = [
    {"month": 1, "rate": 100},
    {"month": 2, "rate": 100},
    {"month": 3, "rate": 100},
    {"month": 4, "rate": 110},
    {"month": 5, "rate": 110},
    {"month": 6, "rate": 130},
    {"month": 7, "rate": 130},
    {"month": 8, "rate": 130},
    {"month": 9, "rate": 120},
    {"month": 10, "rate": 120},
    {"month": 11, "rate": 10},
    {"month": 12, "rate": 10},
]


class TravelGoldV1(Framework):
    def setup(self):

        with open("models/sale_prediction_model.pkl", "rb") as f:
            loaded_model = pickle.load(f)

        self.sales_prediction = loaded_model
        self.region_rate = LookupTable(region_rates)
        self.group_rate = LookupTable(group_rates)

    def calculation(self, quote):
        quote += self.base_rate(quote["month"])
        quote *= self.group_rate(quote["group"])
        quote *= self.region_rate(quote["region"])

        model_parameters = [
            quote["month"],
            quote["group"],
            quote["region"],
        ]

        if self.sales_prediction.predict(model_parameters) < 0.6:
            quote *= 0.9

        return quote
