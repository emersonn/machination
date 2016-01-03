from machination.stringbuild import StringMachination as StrMach
from machination.stringbuild import StringState as StrState


def TestEasy(object):
    def setup(self):
        states = []

        def first(args):
            return "second"

        first_st = StrState("first", first, "dogs")

        def second(args):
            return None

        states.append(
            first_st,
            StrState("second", second, "cats")
        )

        self.mach = StrMach(states, first_st)
