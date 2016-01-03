"""
String Builder
Emerson Matson

Subclasses Machination to allow generate a String response from the finite state
machine. Assumes all states are accept states.
"""

from machination.machinery import Machination
from machination.machinery import State

class StringState(State):
    def __init__(self, name, handler, visit):
        """Creates a new StringState.

        Args:
            name, handler: See parent class.
            visit: String to append to the response when this State is visited.
        """

        def response(acc):
            acc.append(visit)

        super(StringState, self).__init__(name, handler, response)

class StringMachination(Machination):
    def run(self, data):
        """Runs the StringMachination.

        Args:
            data: See parent class.

        Returns:
            str: String of concatenated visits.
        """

        result = []

        super(StringMachination, self).__init__(data, result)

        return "".join(result)
