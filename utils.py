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

    def bmi_category_health_risk(self, table):
        bmi = self.calculate_bmi()
        for data in table:
            if bmi <= data.get("BMI Range"):
                return data.get("BMI Category"), data.get("Health risk")
            elif bmi >= table[-1].get("BMI Range"):
                return table[-1].get("BMI Category"), table[-1].get("Health risk")

