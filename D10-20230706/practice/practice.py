a = [1,2,3,4,5]
b=[]
for i,num in enumerate(a):
    if num%2==0:
       c=num*2
       b.append(c)
print(b)
for i in a :
    if i%2==0:
        c=i*2
        b.append(c)
print(b)

for i in range(0,len(a)):
    if a[i]%2==0:
        c=i*2
        b.append(c)
print(b)

num = int(input("enter a number"))
def find_value(a):
    sum=0
    for i in range(0,a+1):
        sum= i+sum
    return sum
b = find_value(num)
print(b)

a = [0,0,1,2,3,4]
for i in a:
    if (i==0):
        a.remove(i)
        a.append(i)
print(a)

# to add marks and find before and after
marks = [62,95,84,53,71]
total_marks=0
enum_marks=enumerate(marks)
print(type(enum_marks))

for i,mark in enum_marks:
    print("entering iteration process for item#:",str(i))
    print("before_sum=",total_marks)
    total_marks=total_marks+mark
    print("before_sum=",total_marks)
    print("exiting iteration process for item#:",str(i))
    print("\n")

# to find the index of a number
List=[23,32,2,5,9,64,34]
index=int(input("type a number="))

def find_index(a):
    for i in range(0,a+1):
        if List[i]==index:
            

