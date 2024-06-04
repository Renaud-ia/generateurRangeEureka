class ErreurRequete(Exception):
    def __init__(self, message: str = ""):
        super().__init__(message)


class BearerNotValid(ErreurRequete):
    def __init__(self, message: str = ""):
        super().__init__(message)


