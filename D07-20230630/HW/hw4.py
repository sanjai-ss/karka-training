item1= int (input ("enter the amount" ))
item2 =int (input ("enter the amount" ))
item3=int (input ("enter the amount" ))
item4=int (input ("enter the amount" ))
total_amount = (item1+item2+item3+item4)
if total_amount >=500 and total_amount <=1000:
    print (total_amount,"you have owned a silver token")
if total_amount >1000:
    print (total_amount,"you have owned a golden token")
else:
    print(total_amount,"not valid")
