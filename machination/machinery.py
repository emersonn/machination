"""
Machination
Emerson Matson

Functional finite state machine classes. Allows the user to model finite
state machines in order to generate a response. Does not read strings, but
interprets data specific to each state.
"""


# TODO(Define accept states.)
class State(object):
    def __init__(self, name, handler, response=lambda *i, **j: None):
        """Creates a new State.

        Args:
            name: str describing the State.
            handler: function to execute when asked to evaluate a str.
                Should take a string as an argument, and give the name
                    of another state as the return.
            response: function to execute before evaluation. Can be used
                as an accumulation of states that have been visited. Takes
                any object as an argument that is passed through in the
                Machination.
        """

        self.name = name
        self.handler = handler
        self.response = response

    def evaluate(self, data, acc=None):
        """Evaluates the State with the given data.

        Args:
            data: str to evaluate for the handler.
            acc: Any object to be used by the response function.
        """

        self.response(acc)
        return self.handler(data)


class Machination(object):
    def __init__(self, given_states, start):
        """Creates a Machination.

        Args:
            states: List of State objects.
            start: State object that acts as the start state.
        """

        # TODO(Check for duplicate states.)
        self.states = {}
        for state in given_states:
            self.states[state.name] = state

        self.start = start.name

    def add_state(state):
        """Adds a new state to the Machination.

        Args:
            state: State object to add. Must not be a duplicate, otherwise
                IllegalArgumentException.
        """

        if state.name in self.states:
            raise IllegalArgumentException()

        self.states[state.name] = state

    def set_start(state):
        """Sets the start state of the Machination.

        Args:
            state: State object to set as the start. Must exist in the
                Machination, otherwise IllegalArgumentException.
        """

        if state.name not in self.states:
            raise IllegalArgumentException()

        self.start = state.name

    def run(self, data, acc=None):
        """Run the current Machination on the given data.

        Args:
            data: Dictionary from str to str to run the machine on.
                Key is the name of the state with the value being the
                    argument to the handler function.
            acc: The object to pass through to the response of each State.
        """

        self._run(data, self.states[self.start], acc)

    def _run(self, data, current, acc):
        """Internal function for running the machine.

        Relevant Args:
            current: Current State object.
        """

        # NOTE: This should only happen if there is no start state OR if
        #   there is some state which points to a None state.
        if current:
            evaluation = current.evaluate(data[current.name], acc)
            if evaluation in self.states:
                self._run(data, self.states[evaluation], acc)
