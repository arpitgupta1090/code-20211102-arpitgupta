class BMICalculator:

    def __init__(self, gender, height, weight):
        self.gender = gender
        self.height = height / 100
        self.weight = weight

    @classmethod
    def create_from_raw_data(cls, row):
        gender = row.get("Gender", None)
        height = row.get("HeightCm", None)
        weight = row.get("WeightKg", None)

        return cls(gender, height, weight)

    def calculate_bmi(self):
        return round(self.weight / (self.height ** 2), 2)
