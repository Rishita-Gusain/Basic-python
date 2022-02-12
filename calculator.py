def calculate(a,b): #function to calculate 
    a=int(a)
    b=int(b)
    if operator=="1":
        print(a+b)
    elif operator=="2":
        print(a-b)
    elif operator=="3":
        print(a*b)
    elif operator=="4":
        print(a/b)
    else:
        print("Invalid choice! Your choice is not matching with optionss")


print("Welcome! \n")
ques=input("Are you ready to play the game?\n") #user input
if ques=="yes":
    print("What you want to do? \n")
    print("1. + : Addition\n")
    print("2. - : Subtraction\n")
    print("3. * : Multiplication\n")
    print("4. / : Division\n")
    operator= input("Enter you choice: \n")
    print("Enter two numbers\n")
    a=input("Enter first digit\n")
    b=input("Enter second digit\n")
    calculate(a,b)
elif ques=="no":
    print("Thank you!")
else:
    print("Invalid choice")
#chances given to user
count=0
while(count<3):
    count=count+1
    choice= input("Do you want to continue the game? \n")
    if choice=="yes":
        print("What you want to do? \n")
        print("1. + : Addition\n")
        print("2. - : Subtraction\n")
        print("3. * : Multiplication\n")
        print("4. / : Division\n")
        operator= input("Enter you choice: \n")
        print("Enter two numbers\n")
        a=input("Enter first digit\n")
        b=input("Enter second digit\n")
        calculate(a,b)
    else:
        print("Thank You!")
