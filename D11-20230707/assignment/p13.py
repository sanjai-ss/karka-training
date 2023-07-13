# two question quiz
def find_object():
    print("TWO QUESTIONS!")
    print("think of an object, andi'll try to guess it.")
    print("\n")
    question1=(str(input("Question 1) is it animal, vegetable, or mineral?\n")))
    print("\n")
    question2=(str(input("Question 2) is it bigger than a breadbox?\n")))
    print("\n")
    if question1=="animal":
        if question2=="yes":
            ans="moose"
        elif question2=="no":
            ans="squirrel"
    if question1=="vegetable":
        if question2=="yes":
            ans="watermelon"
        elif question2=="no":
            ans="carrot"
    if question1=="mineral":
        if question2=="yes":
           ans="camaro"
        elif question2=="no":
           ans="paper clip"
    print(f"my guess is that you are thinking of a {ans}.\ni would ask you if i'm right, but i don't actually care.")
find_object()
