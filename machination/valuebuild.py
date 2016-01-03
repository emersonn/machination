"""
Value Builder
Emerson Matson

Allows building of a value from visiting states. Assumes all states are
Accept states.
"""

from machination.machinery import Machination
from machination.machinery import State


class ValueState(State):
    # TODO(Maybe abstract this out with String and Value. They both use a List.)
    def __init__(self, name, handler, visit):
        """Creates a new ValueState.

        Args:
            name, handler: See parent class.
            visit: Value to add to the current value.
        """

        def value_response(acc):
            acc.append(visit)

        super(ValueState, self).__init__(name, handler, value_response)


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
