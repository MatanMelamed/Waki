class Stat:
    def __init__(self, name, value):
        self.name = name
        self.value = value

    def __gt__(self, other):
        return False


class StatsManager:
    _available_stats = {}

    def __init__(self):
        pass


