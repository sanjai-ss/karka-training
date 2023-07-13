# BMI categories
import p7
value=p7.calculate_bmi()
def calculate_bmi(value):
    if value <18.5:
        print("BMI category: underweight")
    elif value>=18.5 and value<=24.9:
        print("BMI category: normal weight")
    elif value>=25.0 and value<=29.9:
        print("BMI category: overweight")
    elif value>=30.0:
        print("BMI category: obese")
print("your BMI is:",value)   
calculate_bmi(value)