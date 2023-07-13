# choose your own adventure
def find_choices():
    print("WELCOME TO MITCHELL'S TINY ADVENTURE!\n")
    place=input('you are in a creepy house! would you like to go "kitchen" or into the "upstairs"?\n')
           
    if place=="kitchen":
        things=input("there is along countertop with dirty dishes everywhere. off to one side there is,as you'd expect, a refrigerator.\nyou may open the 'refrigerator' or look into the 'cabinet'\n")
        if things=="refrigerator":
            ans=input('inside the refrigerator you see food and stuff. it looks pretty nasty. would you like to eat some of the food?("yes" or "no")\n')
            if ans=="yes":
                print("you had a very bad diarhoea")
            elif ans=="no":
                print("you die of starvation....eventually.")
        elif things=="cabinet":
            ans=input('inside the cabinet you see a banana,but seems it was rotten would you like to eat the banana?("yes" or "no")\n')
            if ans=="yes":
                print("you had a very bad diarhoea")
            elif ans=="no":
                print("you die of starvation....eventually.")
    elif place=="upstairs":
        things=input("there is a cupboard and there is a suitcase on the floor. you may look into the 'cupboard' or open the 'suitcase'\n")
        if things=="cupboard":
            ans=input('inside the cupboard  you see a cat.would you like to lift it in your hand?("yes" or "no")\n')
            if ans=="yes":
                print("oh..the cat scratched your hand")
            elif ans=="no":
                print("the cat ran away")
        elif things=="suitcase":
            ans=input('inside the suitcase you see a mystery box.would you like to open it?("yes" or "no")\n')
            if ans=="yes":
                print("you found an old watch ")
            elif ans=="no":
                print("the mystery box remained mystery")

find_choices()