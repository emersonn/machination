"""
Value Tests
Emerson Matson

Run with nosetests.
"""

from machination.valuebuild import ValueState
from machination.valuebuild import ValueMachination

class TestEasy(object):
    def setup(self):
        states = []

        def one(args):
            return "two"

        def two(args):
            return None

        self.st_one = ValueState("one", one, 1)
        self.st_two = ValueState("two", two, 2)

        states.extend([
            self.st_one,
            self.st_two
        ])

        self.mach = ValueMachination(states, self.st_one)

    def test_run(self):
        rv = self.mach.run({
            'one': 'one',
            'two': 'two'
        })

        assert rv == 3

class TestMultiple(object):
    def setup(self):
        states = []

        def one(args):
            if args > 0:
                return "two"
            return "three"

        def two(args):
            if args == 0:
                return "three"
            return None

        def three(args):
            return None

        self.st_one = ValueState("one", one, 1)
        self.st_two = ValueState("two", two, 2)
        self.st_three = ValueState("three", three, 3)

        states.extend([
            self.st_one,
            self.st_two,
            self.st_three
        ])

        self.mach = ValueMachination(states, self.st_one)

    def test_run_once(self):
        rv = self.mach.run({
            'one': 0,
            'three': 3
        })

        assert rv == 4
