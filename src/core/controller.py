from core.observable import Observable


class Controller(Observable):

    def __init__(self, context, events=None):
        super().__init__(events)
        self.context = context
