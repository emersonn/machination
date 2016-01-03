from machination.stringbuild import StringMachination as StrMach
from machination.stringbuild import StringState as StrState


class TestEasy(object):
    def setup(self):
        states = []

        def first(args):
            return "second"

        def second(args):
            return None

        self.first_st = StrState("first", first, "dogs")
        self.second_st = StrState("second", second, "cats")

        states.extend([
            self.first_st,
            self.second_st
        ])

        self.mach = StrMach(states, self.first_st)

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

    def test_add_state(self):
        def third(args):
            return None

        self.mach.add_state(
            StrState("third", third, "bigdogs")
        )

        assert "third" in self.mach.states

    def test_new_start(self):
        self.mach.set_start(
            self.second_st
        )

        assert self.mach.start == self.second_st.name


class TestMultipleRun(object):
    def setup(self):
        states = []

        def one(args):
            args = int(args)
            if args > 0:
                return "two"
            return "three"

        def two(args):
            args = int(args)
            if args == 0:
                return "three"
            return None

        def three(args):
            return None

        self.first_st = StrState("one", one, "one")
        self.second_st = StrState("two", two, "two")
        self.third_st = StrState("three", three, "three")

        states.extend([
            self.first_st,
            self.second_st,
            self.third_st
        ])

        self.mach = StrMach(states, self.first_st)

    def test_run_one(self):
        rv = self.mach.run({
            'one': '1',
            'two': '0',
            'three': '3'
        }, " ")

        assert rv == "one two three"
