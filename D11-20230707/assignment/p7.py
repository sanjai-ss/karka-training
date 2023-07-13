# bmi calculator
def calculate_bmi():
    height=(float(input("your height in m:")))
    weight=(float(input("your weight in kg:")))      

    # return (f"Your bmi is {weight/(height**2)}")
    return weight/(height)**2
# bmi=calculate_bmi()
# print(bmi)  