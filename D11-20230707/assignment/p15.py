# two more questions

def find_question():
    print("TWO MORE QUESTIONS!")
    print("think of something and i'll try to guess it!")
    question1=input("Question 1) does it stays inside or outside or both?\n")
    question2=input("Question 2) is it a living thing?\n")

    if question1==("inside") and question2==("yes"):
        print("then what else could you'll be thinking of besides a houseplant")
    if question1==("inside") and question2==("no"):
        print("then what else could you'll be thinking of besides a showercurtain")
    if question1==("outside") and question2==("yes"):
        print("then what else could you'llbe thinking of besides a bison")
    if question1==("outside") and question2==("no"):
        print("then what else could you'llbe thinking of besides a billboard")
    if question1==("both") and question2==("yes"):
        print("then what else could you'llbe thinking of besides a dog")
    if question1==("both") and question2==("no"):
        print("then what else could you'llbe thinking of besides a cellphone")

find_question()