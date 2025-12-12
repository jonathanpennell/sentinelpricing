class Step:
    """Step

    Form part of a quote Breakdown. Represents an operation carried out on a
    quote.
    """

    def __init__(self, name, oper, other, result):

        self.name = name
        self.oper = oper
        self.other = other
        self.result = result

    @classmethod
    def headers(cls):
        return f"{'Total': <8} :: {"Name":<72}" + f" - {"Operation": <30} - {"Other"}"

    def __repr__(self):
        return (
            f"{round(self.result, 5): <9} :: {self.name:<72}"
            + f" - {repr(self.oper): <30} - {self.other}"
        )
