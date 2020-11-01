from models.utils.tools import is_int


class Stat:
    NAMES = {'dex': 'Dex', 'int': 'Int', 'str': 'Str', 'sta': 'Sta', 'critical chance': 'CC',
             'increased critical damage': 'ICD', 'speed': 'Speed', 'attack speed': 'A. Speed', 'def': 'Def',
             'attack': 'Attack', 'max. hp': 'Max. HP', 'max. mp': 'Max. MP', 'max .fp': 'Max .FP',
             'decreased casting time': 'DCT'}

    @classmethod
    def _parse_args(cls, *args, **kwargs):
        n = 'name'
        v = 'value'
        if len(args) > 1: return args
        if len(args) == 1:
            if n in kwargs:
                return [*args, kwargs[n]]
            elif v in kwargs:
                return [*args, kwargs[v]]
        if n in kwargs and v in kwargs:
            return [kwargs[n], kwargs[v]]
        return None

    def __new__(cls, *args, **kwargs):
        args = cls._parse_args(*args, **kwargs)
        n = args[0].lower()
        if (n not in Stat.NAMES.values() and n not in Stat.NAMES.keys()) \
                or not is_int(args[1]):
            return None

        return super().__new__(cls)

    def __init__(self, name, value):
        self.name = name if name.lower() not in Stat.NAMES.keys() else Stat.NAMES[name.lower()]
        self.value = value

    def __str__(self):
        return f'{self.name} > {self.value}'

    def __eq__(self, other):
        return self.name == other.name and self.value == other.value

    @classmethod
    def convert_str_to_stat(cls, str_stat):
        parsed_stat = str_stat.split(' > ')

        if len(parsed_stat) < 2 or ' > ' not in str_stat:
            return None

        return Stat(parsed_stat[0], parsed_stat[1])
