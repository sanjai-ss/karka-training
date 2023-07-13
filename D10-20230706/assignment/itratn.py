# to add and find average of num
List = [10,20,30,40,50,60]
sum = 0
for i,num in enumerate(List):
    sum=sum+num
print("sum of list=",sum)

print("average of list=",sum/len(List))

# to assign INR to numbers
List=[100,200,500,1000]
b=[]
for i,num in enumerate(List):
    
    a ="INR"+str(num)  
    b.append(a)
print(b)


# to find whether the num is odd or even
a=[1,2,3,4,5,6,7,8,9,10]
b=[]
c=[]
for i,num in enumerate(a):
    
    if(num%2==0):
        b.append(num)
    else:
        c.append(num)
print("even",b)
print("odd",c)

# to add marks and find before and after
marks = [62,95,84,53,71]
total_marks=0

for mark in marks:
    print("before",total_marks)
    total_marks=total_marks+mark
    print("after",total_marks)


