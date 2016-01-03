from machination.stringbuild import StringMachination as StrMach
from machination.stringbuild import StringState as StrState


class TestEasy(object):
    def setup(self):
        states = []

        def first(args):
            return "second"

        def second(args):
            return None

        first_st = StrState("first", first, "dogs")
        second_st = StrState("second", second, "cats")

        states.extend([
            first_st,
            second_st
        ])

        self.mach = StrMach(states, first_st)

    def test_run(self):
        rv = self.mach.run({
            'first': 'cat',
            'second': 'catter'
        })

        assert rv == "dogscats"

    def test_run_joiner(self):
        rv = self.mach.run({
            'first': 'cat',
            'second': 'catter'
        }, " ")

        assert rv == "dogs cats"
