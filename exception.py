class HeightNullError(Exception):

    def __init__(self):
        self.msg = "Value of height cannnot be Null"

    def __str__(self):
        return self.msg


class WeightNullError(Exception):

    def __init__(self):
        self.msg = "Value of weight cannnot be Null"

    def __str__(self):
        return self.msg


class HeightLessThanZeroError(Exception):

    def __init__(self):
        self.msg = "Value of height cannnot be zero or less than zero"

    def __str__(self):
        return self.msg


class WeightLessThanZeroError(Exception):

    def __init__(self):
        self.msg = "Value of weight cannnot be zero or less than zero"

    def __str__(self):
        return self.msg

