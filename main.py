from utils import BMICalculator
from exception import HeightNullError, WeightNullError, HeightLessThanZeroError, WeightLessThanZeroError

bmi_table = [
    {"BMI Category": "Underweight", "BMI Range": 18.4, "Health risk": "below Malnutrition risk"},
    {"BMI Category": "Normal weight", "BMI Range": 24.9, "Health risk": "Low risk"},
    {"BMI Category": "Overweight", "BMI Range": 29.9,  "Health risk": "Enhanced risk"},
    {"BMI Category": "Moderately obese", "BMI Range": 34.9, "Health risk": "Medium risk"},
    {"BMI Category": "Severely obese", "BMI Range": 39.9, "Health risk": "High risk"},
    {"BMI Category": "Very severely obese", "BMI Range": 40, "Health risk": "Very high risk"}
]

input_data = [
    {"Gender": "Male", "HeightCm": 171, "WeightKg": None},
    {"Gender": "Male", "HeightCm": 161, "WeightKg": 85},
    {"Gender": "Male", "HeightCm": 180, "WeightKg": 77},
    {"Gender": "Female", "HeightCm": 166, "WeightKg": 62},
    {"Gender": "Female", "HeightCm": 150, "WeightKg": 70},
    {"Gender": "Female", "HeightCm": 167, "WeightKg": 82}
]


def add_bmi_category_health_risk(data_list, table):

    for data in data_list:
        try:
            obj = BMICalculator.create_from_raw_data(data)
            bmi = obj.calculate_bmi()
            category, health_risk = obj.bmi_category_health_risk(table)
            data["BMI"] = bmi
            data["BMI Category"] = category
            data["Health Risk"] = health_risk
        except (HeightNullError, WeightLessThanZeroError, WeightNullError, HeightLessThanZeroError) as exp:
            print(exp)
            data_list = []
    return data_list


def number_of_overweight(data_list, table):
    if data_list:
        added_list = add_bmi_category_health_risk(data_list, table)
        overweight_list = [person for person in added_list if person["BMI Category"] == "Overweight"]
        return len(overweight_list)


if __name__ == "__main__":

    added_list_with_bmi = add_bmi_category_health_risk(input_data, bmi_table)
    print(added_list_with_bmi)
    print(number_of_overweight(input_data, bmi_table))

