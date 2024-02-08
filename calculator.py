def add(x,y):
    return (x+y)

def sub(x,y):
    return(x-y)

def multiply(x,y):
    return(x*y)
 
def divide(x,y):
    if y == 0:
        return "Error! no. is try to be divisible by 0 "
    else:
        return x/y
    

def calculator():
    print("Welcome to the simple calculator")
    print("Select operation ")
    print("1. add")
    print("2. sub")
    print("3. multiply")
    print("4. divide")

    choice = input("enter your choice(1/2/3/4):")

    if choice in ('1', '2', '3', '4'):
        num1= float(input("enter the first number : "))
        num2 = float(input("enter the second number: "))

        if choice == '1':
         print("result", add(num1, num2))

        elif choice =='2':
         print("result", sub(num1, num2))

        elif choice == '3':
         print("result", multiply(num1, num2))

        elif choice == '4':
         print("result", divide(num1, num2))

    else:
       print("Invalid number, please enter the valid choice")

    again = input("do you want to perform again calculation(yes/no)")
    if again.lower() == 'yes':
       calculator()

    else:
       print("Thank you for using the calculator ")

calculator()


    
