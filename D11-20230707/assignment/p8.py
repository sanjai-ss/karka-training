# how old are you?
def is_eligible():
    name=(str(input("hey, what's your name?")))
    print("\n")
    age=(int(input(f"ok,{name}, how old are you?")))
    print("\n")
    if age<16:
        print("you can't drive",name)
    if age<18:
        print("you can't vote",name)
    if age<25:
        print("you can't rent a car",name)
    if age>=25:
        print("you can do anything that's legal",name)
        
is_eligible()
