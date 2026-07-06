# Mini Project: Smart Mobile Calculator
# Objective
# Develop a calculator similar to a mobile calculator using Python.
# Rules- Do not use built-in functions such as eval(), sum(), max(), min(), etc.- Write a separate user-defined function for each operation.- Every function must return its result.- Use a menu-driven program.- Continue until the user selects Exit.- Handle division by zero and invalid choices.
# Functions to Create
# addition(a,b)
# subtraction(a,b)
# multiplication(a,b)
# division(a,b)
# modulus(a,b)
# floor_division(a,b)
# power(a,b)
# ANS Feature
# Maintain a variable named ANS. After every calculation, store the returned result in ANS.
# The user should be able to choose either:
# 1. Enter a new number
# 2. Use Previous Answer (ANS)
# for both operands.
# Menu
# 1. Addition
# 2. Subtraction
# 3. Multiplication
# 4. Division
# 5. Modulus
# 6. Floor Division
# 7. Power
# 8. Clear ANS
# 9. Show ANS
# 10. Exit
# Expected Behaviour
# The output of one operation should be reusable as the input to another operation through ANS, just
# like a mobile calculator.
# Evaluation- Separate functions for each operation- Proper use of return values- Correct ANS implementation- Menu-driven program- Proper error handling- Good code readability and indentation
ans=0
ans1=[]
def showans(ans):
    # print(f"ans = {ans}")
    ans1.append(ans)
    return ans
print(showans(ans))
while True:
    def calculator():
        print("menu:\n1.addition\n2.subtraction\n3.multiplication\n4.division\n5.modulus\n6.floor division\n7.power\n8.clear ans\n9.exit")
    calculator()
    choice=int(input("enter your choice from menu : "))

    if choice==1:
        option=int(input("1.enter new number\n2.use previous ans"))
        if option==1:
            num1=int(input("enter a new number1 :"))
            num2=int(input("enter a new number2 :"))
        else:
            if option!=1 and option!=2:
                print("select valid option")
                break
            num1=ans1[-1]
            num2=int(input("enter another number"))
        def addition(num1,num2):
            ans=num1+num2
            showans(ans)
            return ans
        print(f"The addition of {num1} and {num2} is:",addition(num1,num2))

    if choice==2:
        option=int(input("1.enter new number\n2.use previous ans"))
        if option==1:
            num1=int(input("enter a new number1 :"))
            num2=int(input("enter a new number2 :"))
        else:
            if option!=1 and option!=2:
                print("select valid option")
                break
            num1=ans1[-1]
            num2=int(input("enter another number"))
        def subtraction(num1,num2):
            ans=num1-num2
            showans(ans)
            return ans
        print(f"the subtraction of {num1} and {num2} is:",subtraction(num1,num2))

    if choice==3:
        option=int(input("1.enter new number\n2.use previous ans"))
        if option==1:
            num1=int(input("enter a new number1 :"))
            num2=int(input("enter a new number2 :"))
        else:
            if option!=1 and option!=2:
                print("select valid option")
                break
            num1=ans1[-1]
            num2=int(input("enter another number"))
        def multiplication(num1,num2):
            ans=num1*num2
            showans(ans)
            return ans
        print(f"the multiplication of {num1} and {num2} is:",multiplication(num1,num2))

    if choice==4:
        option=int(input("1.enter new number\n2.use previous ans"))
        if option==1:
            num1=int(input("enter a new number1 :"))
            num2=int(input("enter a new number2 :"))
        else:
            if option!=1 and option!=2:
                print("select valid option")
                break
            num1=ans1[-1]
            num2=int(input("enter another number"))
        def division(num1,num2):
            ans=num1/num2
            showans(ans)
            return ans
        print(f"the division of {num1} and {num2} is:",division(num1,num2))

    if choice==5:
        option=int(input("1.enter new number\n2.use previous ans"))
        if option==1:
            num1=int(input("enter a new number1 :"))
            num2=int(input("enter a new number2 :"))
        else:
            if option!=1 and option!=2:
                print("select valid option")
                break
            num1=ans1[-1]
            num2=int(input("enter another number"))
        def modulus(num1,num2):
            ans=num1%num2
            showans(ans)
            return ans
        print(f"the modulus of {num1} and {num2} is:",modulus(num1,num2))

    if choice==6:
        option=int(input("1.enter new number\n2.use previous ans"))
        if option==1:
            num1=int(input("enter a new number1 :"))
            num2=int(input("enter a new number2 :"))
        else:
            if option!=1 and option!=2:
                print("select valid option")
                break
            num1=ans1[-1]
            num2=int(input("enter another number"))
        def floordivision(num1,num2):
            ans=num1//num2
            showans(ans)
            return ans
        print(f"the floor division of {num1} and {num2} is :",floordivision(num1,num2))

    if choice==7:
        option=int(input("1.enter new number\n2.use previous ans"))
        if option==1:
            num1=int(input("enter a new number1 :"))
            num2=int(input("enter a new number2 :"))
        else:
            if option!=1 and option!=2:
                print("select valid option")
                break
            num1=ans1[-1]
            num2=int(input("enter another number"))
        def power(num1,num2):
            ans=num1**num2
            showans(ans)
            return ans
        print(f"the power of {num1} to {num2} is:",power(num1,num2))    
        
    if choice==8:
        def clear():
            ans=0
            print(f"ans={ans}")
        clear()
    if choice==9:
        break
