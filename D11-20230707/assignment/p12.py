# a little quiz
def find_answer():
        a=0
        ready=(str(input("are you ready for a quiz?\n")))
        if ready=="yes":
            print("okay, here it comes!")
        print("\n")
        question1=(int(input("Q1) what is the capital of tamil nadu?\n\t 1)madurai\n\t 2)coimbatore\n\t 3)chennai\n")))
        print("\n")
        if question1 ==1:
            print("that's wrong!")
        if question1 ==2:
            print("that's wrong!")
        if question1 ==3:
            print("that's right!")
            a=a+1
        question2=(int(input('Q2) can you store the value "cat" in a variable of type int?\n\t 1)yes\n\t 2)no\n')))
        print("\n")
        if question2 ==1:
            print('sorry, "cat" is a string. ints can only store numbers.')
        if question2 ==2:
            print("that's right!")
            a=a+1
        question3=(int(input("Q3) what is the result of 9+6/3?\n\t 1)5 \n\t 2)11\n\t 3)15/3\n")))
        print("\n")
        if question3 ==1:
            print("that's wrong!")
        if question3 ==2:
            print("that's right!")
            a=a+1
        if question3 ==3:
            print("that's wrong!")
        return a

b=find_answer()
print(f"overall, you got {b} out of 3 correct.\nthanks for playing!")
