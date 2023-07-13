# a dumb calculator
def calculate_num():
    first=(float(input("what is your first number?")))
    second=(float(input("what is your second number?")))
    third=(float(input("what is your third number?")))

    value=first+second+third
    final_value=value/2
    return (f"{value}/2is....{final_value}")
    
a=calculate_num ()
print(a)