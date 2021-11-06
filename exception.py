class HeightNullError(Exception):

    def __init__(self):
        self.msg = "Value of height cannot be Null"

    def __str__(self):
        return self.msg


class WeightNullError(Exception):

    def __init__(self):
        self.msg = "Value of weight cannot be Null"

    def __str__(self):
        return self.msg


class HeightLessThanZeroError(Exception):

    def __init__(self):
        self.msg = "Value of height cannot be zero or less than zero"

    def __str__(self):
        return self.msg


class WeightLessThanZeroError(Exception):

    def __init__(self):
        self.msg = "Value of weight cannot be zero or less than zero"

    def __str__(self):
        return self.msg

