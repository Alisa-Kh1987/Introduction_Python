class Archive:
    _instance = None

    def __new__(cls, number: int, string: str):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
            cls._instance.numbers = []
            cls._instance.strings = []
        else:
            cls._instance.numbers.append(cls._instance.number)
            cls._instance.strings.append(cls._instance.string)
        return cls._instance

    def __init__(self, number: int, string: str):
        self.number = number
        self.string = string

    def __str__(self):
        return f'{self.number}, {self.string} ({self.numbers}, {self.strings})'