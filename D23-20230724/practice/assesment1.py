# 1)to find the greatest number
num1=int(input("number 1 :\n"))
num2=int(input("number 2 :\n"))
num3=int(input("number 3 :\n"))

if num1>num2:
    if num1>num3:
        print(num1,"is the greatest number")
if num2>num1:
    if num2>num3:
        print(num2,"is the greatest number")
if num3>num1:
    if num3>num2:
        print(num3,"is the greatest number")
else:
    print("the entered input is invalid")
    