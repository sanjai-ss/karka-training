# month name

month=int(input("month no:"))
def month_name(): 
    if month==1:
        return ("january")
    elif month==2:
        return ("february")
    elif month==3:
        return ("march")
    elif month==4:
        return ("april")
    elif month==5:
        return ("may")
    elif month==6:
        return ("june")
    elif month==7:
        return ("july")
    elif month==8:
        return ("august")
    elif month==9:
        return ("september")
    elif month==10:
        return ("october")
    elif month==11:
        return ("november")
    elif month==12:
        return ("december")
    else:
        return ("error")
    
value=month_name()
print(value)