year = int(input("enter a year="))
def check_eligiblity(a):
    if a>=2021 and a<=2023:
        return("he is eligible")
    else:
        return("he is not eligible")
b = check_eligiblity(year)
print(b)