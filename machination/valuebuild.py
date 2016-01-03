"""
Value Builder
Emerson Matson

Allows building of a value from visiting states. Assumes all states are
Accept states.
"""

from machination.machinery import Machination

from machination.appendbuild import AppendState


class ValueState(AppendState):
    pass


class ValueMachination(Machination):
    def run(self, data):
        """Runs the StringMachination.

        Args:
            data: See parent class.

        Returns:
            int: Value of all visits.
        """

        result = []

        super(ValueMachination, self).run(data, result)

        # TODO(Make this into a pretty lambda function.)
        value = 0
        for val in result:
            value += val

        return value
