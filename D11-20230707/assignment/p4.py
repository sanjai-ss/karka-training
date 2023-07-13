# more user input of data
print("please enter the following information so i can sell it for a profit!")
fname=(str(input("First name:")))
lname=(str(input("Last name:")))
grade=(int(input("Grade (9-12):")))
id=(int(input("Student ID:")))
login=(str(input("Login:")))
gpa=(float(input("GPA (0.0-4.0):")))

# print("your information:")
# print("{:>5} Login:{:<10}".format('',login))
# print("{:>5} ID:{:<10}".format('',id))
# print("{:>5} Name:{:<10}".format('',fname,lname))
# print("{:>5} GPA:{:<0}".format('',gpa))
# print("{:>5} Grade:{:<10}".format('',grade))


print(f"login information \n \t login:{login}\n \t id:{id}\n \t name:{fname,lname}\n \t gpa:{gpa}\n \t grade:{grade}")