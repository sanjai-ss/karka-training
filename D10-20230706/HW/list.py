# List=[1,100,300,4]
# a=List[0]
# for i in List:
#         if i>a:
#             a=i
# print("largest number",a)

# List=[1,100,300,4]
# a=List[0]
# for i in List:
#         if i<a:
#             a=i
# print("smallest number",a)

# to find the index of a number
List = [1,100,300,4,5,6,7]
index=int(input("enter the element to find the index="))
def find_index(a,b):
    for i in range(0,len(a)):
        if a[i]==b:
            print(i)
a=find_index(List,index)
