from exception import HeightNullError, WeightNullError, HeightLessThanZeroError, WeightLessThanZeroError


class BMICalculator:

    def __init__(self, gender, height, weight):
        self.gender = gender
        self.height = height
        self.weight = weight

        self.__input_data_validator()
        self.height = self.height / 100

    @classmethod
    def create_from_raw_data(cls, row):
        gender = row.get("Gender", None)
        height = row.get("HeightCm", None)
        weight = row.get("WeightKg", None)

        return cls(gender, height, weight)

    def calculate_bmi(self):
        return round(self.weight / (self.height ** 2), 2)

    def bmi_category_health_risk(self, table):
        bmi = self.calculate_bmi()
        for data in table:
            if bmi <= data.get("BMI Range"):
                return data.get("BMI Category"), data.get("Health risk")
            elif bmi >= table[-1].get("BMI Range"):
                return table[-1].get("BMI Category"), table[-1].get("Health risk")

    def __input_data_validator(self):
        if not self.height:
            raise HeightNullError
        if self.height <= 0:
            raise HeightLessThanZeroError
        if not self.weight:
            raise WeightNullError
        if self.weight <= 0:
            raise WeightLessThanZeroError
