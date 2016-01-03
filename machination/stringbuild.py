"""
String Builder
Emerson Matson

Subclasses Machination to allow generate a String
response from the finite state machine. Assumes all states are accept states.
"""

from machination.machinery import Machination

from machination.appendbuild import AppendState


class StringState(AppendState):
    pass


class StringMachination(Machination):
    def run(self, data, joiner=""):
        """Runs the StringMachination.

        Args:
            data: See parent class.

        Returns:
            str: String of concatenated visits.
        """

        result = []

        super(StringMachination, self).run(data, result)

        return joiner.join(result)
