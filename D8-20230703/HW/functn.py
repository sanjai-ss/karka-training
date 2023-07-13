first = int(input("enter the first number"))
operator = input("enter the operator(+,-,*,/,%,**)")
third = int(input("enter the third number"))

def perform_arithmetic_operation(first, operator, third):
    if operator == "+":
        result = first + third
    elif operator == "-":
        result = first - third
    elif operator == "*":
        result = first * third
    elif operator == "/":
        result = first / third
    elif operator == "%":
        result = first % third
    elif operator == "**":
        result = first ** third
    else:
        return "invalid operator"
    
    return result         

answer = perform_arithmetic_operation(first, operator, third)
print("Answer=",answer)                 

    