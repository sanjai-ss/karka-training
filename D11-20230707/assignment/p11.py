# space boxing

def calculate_weight():
    weight=(float(input("please enter your current earth weight:")))
    print("\n")
    print("i have information for the following planets: \n 1.venus\t 2. mars\t 3.jupiter\n 4.saturn\t 5.uranus\t 6.neptune")
    print("\n")
    planet=(int(input("which planet are you visiting?")))
    print("\n")
    if planet==1:
        print("your weight would be",weight*0.78,"kilo's on that planet.")
    if planet==2:
        print("your weight would be",weight*0.39,"kilo's on that planet.")
    if planet==3:
        print("your weight would be",weight*2.65,"kilo's on that planet.")
    if planet==4:
        print("your weight would be",weight*1.17,"kilo's on that planet.")
    if planet==5:
        print("your weight would be",weight*1.05,"kilo's on that planet.")
    if planet==6:
        print("your weight would be",weight*1.23,"kilo's on that planet.")
        
calculate_weight()
    