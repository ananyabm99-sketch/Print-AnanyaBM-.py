'''while (True):
    print("Simple calculator")
    print("1.Addition")
    print("2.Subtraction")
    print("3.Multiplication")
    print("4.Division")
    print("5.quit")
    choice = input("Enter your choice : 1/2/3/4/5 :\n")
    if choice in ['1','2','3','4','5']:
        if choice in ['1','2','3','4']:
            num1 = int(input("Enter first number: \n"))
            num2 = int(input("enter second number: \n"))
            if choice == '1':
                print("The sum is :",num1+num2)
            elif choice == '2':
                print("The difference is :",num1 - num2)
            elif choice == '3':
                print("The product is :",num1 * num2)
            else :
                if num2 == 0:
                     print("Error: division by zero is not allowed. ")
                else:
                     print("The quotient is :",num1/num2)
        else:
            print("quitting...........")
            break
    
    else:
        print("Invalid Input,please try again!")'''

def add(a,b):
    return a+b
def sub(a,b):
    return a-b
def multi(a,b):
    return a*b
def divide(a,b):
    return a/b
operators = {
    "+":add,
    "-":sub,
    "*":multi,
    "/":divide,
}
print(operators["*"](a=2,b=3))
num = int(input("Enter a number: \n"))