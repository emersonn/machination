from machination.machinery import State


class AppendState(State):
    def __init__(self, name, handler, visit):
        """Creates a new AppendState.

        Args:
            name, handler: See parent class.
            visit: Object to append to the response when this State is visited.
        """

        def response(acc):
            acc.append(visit)

        super(AppendState, self).__init__(name, handler, response)
