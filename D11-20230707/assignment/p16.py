# gender game
def gender_game():
    gender=input("what is your gender(male or female)?:")
    fname=input("first name:")
    lname=input("last name:")
    age=input("age:")
    if gender=="female":
        married=input(f"are you married,{fname}(yes or no)?")
        if married=="yes":
            print(f"then i shall call you mrs. {lname}.")
        elif married=="no":
            print(f"then i shall call you mrs. {fname+lname}.")
    if gender=="male"and age>="20":
        print(f"mr.{lname}")
    if gender=="male"and age<"20":
        print(fname+lname)
    
gender_game()
