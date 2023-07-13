#how old are you specifically

def is_eligible():
    name=(str(input("hey, what's your name? (sorry i keep forgetting.)")))
    print("\n")
    age=(int(input(f"ok,{name}, how old are you?")))
    print("\n")
    if age<16:
        print("you can't drive",name)
    elif age<18:
        print("you can drive you can't vote",name)
    elif age<25:
        print("you can vote you can't rent a car",name)
    elif age>=25:
        print("you can do pretty much anything ",name)
        
is_eligible()
