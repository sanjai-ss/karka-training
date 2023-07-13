a=[71,62,53,44,35,23,17]
sum =0
for i in a:
    sum=i+sum
print(sum)
average =sum/len(a)
print(average)
if 40<average<60:
    print("medium")
if average <=90 :
    print("excellent")