def add (a,b):
    return a+b 
def subtract(a,b):
    return a-b 
def multiply (a,b):
    return a*b 
def divide (a,b):
    if b != 0:
        return a/b 
    else:
        return "error:division by zero"
        

print("select operation: +, -, *, /")
choice = input("enter choice:")
num1 = float(input("enter first number:"))
num2 =float(input("enter second number:"))

if choice == '+':
    print("result:", add(num1, num2))
elif choice == '-':
    print("result:", subtract(num1 , num2))
elif choice =='*':
    print("result:", multiply(num1 ,num2))
elif choice =='/':
    print("result:", divide(num1, num2))
    


