#  Adding Values in a whileloop

print("i will add up the numbers you give me!")
sum=0
while True:
    a=int(input("number:"))
    if a!=0:
        sum=sum+a
        print("so far the total is",sum)
    elif a==0:
        print("the total is",sum)
        break   