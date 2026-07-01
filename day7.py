# 1. Electricity Bill Using Slab Rates
# Task: Write a Python program to calculate the electricity bill based on the following conditions:
# * First 100 units → ₹5 per unit
# * Next 100 units → ₹7 per unit
# * Above 200 units → ₹10 per unit
# Things to use:
# * Variables
# * Input/output
# * If-elif-else
# * Arithmetic operators
# Example Input:
# Enter units: 250
# Example Output:
# Electricity bill = 1700

# def electricitybill():
#     units=int(input("enter units :"))
#     if units<=100:
#         amount=units*5
#         print(f"electicity bill = {amount}")
#     elif units<=200:
#         amount=units*7
#         print(f"electicity bill = {amount}")
#     else:
#         amount=units*10
#         print(f"electricity bill ={amount}")
# electricitybill()

# ------------------------------------------------------------------------------------------------------------------------------------
# 2. Check Whether a Number is Armstrong Number
# Task:
# Write a Python program to check whether a given number is an Armstrong number.
# Things to use:
# * While loop
# * Modulus (%)
# * Integer division (//)
# * If statement
# Example Input:
# Enter number: 153
# Example Output:
# 153 is an Armstrong number

# def amstrong(number):
#     count=0
#     temp=number
#     while temp>0:
#         count+=1
#         temp//=10
#         # print(count)
#     temp=number
#     sum=0
#     while temp>0:
#         digit=temp%10
#         sum+=digit**count
#         temp//=10
#     if number==sum:
#         print(f"{number} is amstrong")
#     else:
#         print(f"{number} is not an amstrong")
# amstrong(153)

# -----------------------------------------------------------------------------------------------------------------------------------------


# 3. Reverse a Number and Check Palindrome
# Task:
# Write a Python program to reverse a number and determine whether it is a palindrome number.
# Things to use:
# * While loop
# * Variables
# * Modulus (%)
# * If statement
# Example Input:
# Enter number: 1221
# Example Output:
# Reversed number = 1221
# Palindrome number

# def palindrome(number):
#     temp=number
#     rev=0
#     while temp>0:
#         digit=temp%10
#         rev=rev*10+digit
#         temp=temp//10
#     print(rev)
#     if rev==number:
#         print(f"{number} is a palindrome")
#     else:
#         print(f"{number} is not a palindrome")
# palindrome(1221)    

# --------------------------------------------------------------------------------------------------------------------------------------------------------------------
# 4. Count Even and Odd Digits in a Number
# Task:
# Write a Python program to count the number of even digits and odd digits in a given number.
# Things to use:
# * While loop
# * Modulus operator
# * If condition
# Example Input:
# Enter number: 256843
# Example Output:
# Even digits = 4
# Odd digits = 2


# def evenodd(number):
#     temp=number
#     ecount=0
#     ocount=0
#     while temp>0:
#         digit=temp%10
#         temp=temp//10
#         if digit>0 and digit%2==0:
#             ecount+=1
#             # print(f"even digits={ecount}")
#         else:
#             ocount+=1
#     print(f"even digits={ecount}")
#     print(f"odd digits are:{ocount}")
# evenodd(256843)

# ---------------------------------------------------------------------------------------------------------------------------------------------------------------------

# 5. ATM Cash Withdrawal System
# Task:
# Write a Python program to simulate an ATM withdrawal system with the following conditions:
# * User enters account balance and withdrawal amount
# * Withdrawal amount should be a multiple of 100
# * Withdrawal amount should not exceed account balance
# * Display updated balance if transaction is successful; otherwise show an appropriate message
# Things to use:
# * Variables
# * If-elif-else
# * Arithmetic operators
# * Multiple conditions
# Example Input:
# Enter account balance: 10000
# Enter withdrawal amount: 2500
# Example Output:
# Transaction Successful
# Remaining balance = 7500

# def atm():
#     balance=int(input("enetr account balance : "))
#     withdraw=int(input("enter withdrawl amount : "))
#     if withdraw>balance:
#         print("withdrawal amount should not exceed amount balanace")
#     elif withdraw%100!=0:
#         print("withdraw amount should be multiple of 100")
#     else:
#         balance-=withdraw
#         print("transaction successful")
#         print(f"Remaining amount is {balance}")
# atm()

# -------------------------------------------------------------------------------------------------------------------------------------------------------------
# 6. Strong Number Checker
# Task:
# Write a Python program to check whether a given number is a Strong number.
# A Strong number is a number whose sum of factorials of its digits equals the original number.
# Example:
# 145 = 1! + 4! + 5!
# Things to use:
# * While loop
# * Nested loop
# * Variables
# * Factorial logic
# * Modulus (%) and integer division (//)
# Example Input:
# Enter number: 145
# Example Output:
# 145 is a Strong number

# def strongnumber(number):
#     temp=number
#     strong=0
#     while temp>0:
#         fact=1
#         digit=temp%10
#         while digit>0:
#             fact*=digit
#             digit-=1
            
#         temp//=10
#         strong+=fact
#     if strong==number:
#         print(f"{number} is a strong number")
#     else:
#         print("not a strong number")
# strongnumber(145)

# ----------------------------------------------------------------------------------------------------------------------------------------

# 7. Sum of Squares Series
# Task:
# Write a Python program to find the sum of the following series:
# 1² + 2² + 3² + ... + n²
# Things to use:
# * For loop
# * Variables
# * Arithmetic operators
# Example Input:
# Enter n: 5
# Example Output:
# Sum = 55

# def squares():
#     n=int(input("enter a number"))
#     sum=0
#     for i in range(1,n+1):
#         sqr=i*i
#         sum+=sqr
#     print(f"sum = {sum}")
# squares()

# -------------------------------------------------------------------------------------------------------------------------------------------

# Find Frequency of Digits in a Number
# Task:
# Write a Python program to count the frequency of each digit in a given number.
# Things to use:
# * While loop
# * Dictionary or list
# * Modulus operator
# * Loops
# Example Input:
# Enter number: 22334452
# Example Output:
# 2 occurs 3 times
# 3 occurs 2 times
# 4 occurs 2 times
# 5 occurs 1 time

# def frequency(number):
#     temp = number
#     a = []
#     while temp > 0:
#         count = 0
#         digit = temp % 10
#         if digit not in a:
#             temp1 = number
#             while temp1 > 0:
#                 if temp1 % 10 == digit:
#                     count += 1
#                 temp1 //= 10
#             print(f"{digit} occurs {count} times")
#             a.append(digit)
#         temp //= 10
# frequency(22334452)

# 9. Find Prime Numbers in a Given Range
# Task:
# Write a Python program to display all prime numbers between two given numbers.
# Things to use:
# * Nested loops
# * If condition
# * Range function
# Example Input:
# Enter start number: 10
# Enter end number: 30
# Example Output:
# Prime numbers:
# 11
# 13
# 17
# 19
# 23
# 29

# def prime():
#     start=int(input("enter start number :"))
#     end=int(input("enter end number :"))
#     for i in range(start,end+1):
#         if i<2:
#             continue
#         j=2
#         while j<i:
#             if i%j==0:
#                 break
#             j+=1
#         if j==i:
#             print(f" {i}")
# prime()

# 10. Employee Payroll System with Bonus Calculation
# Task:
# Write a Python program to accept details of 5 employees (name, basic salary, and years of experience).
# Calculate:
# * HRA = 15% of basic salary
# * TA = 10% of basic salary
# * Bonus:
#   * Experience ≥ 5 years → 20% of salary
#   * Experience < 5 years → 10% of salary
# * Gross Salary = Basic + HRA + TA + Bonus
# Display:
# * Gross salary of each employee
# * Employee with highest gross salary
# Things to use:
# * Lists
# * Loops
# * Conditions
# * Variables
# * Percentage calculations
# Example Input:
# Employee Name: Ravi
# Basic Salary: 30000
# Experience: 6
# Employee Name: Priya
# Basic Salary: 40000
# Experience: 4
# Example Output:
# Ravi Gross Salary = 43500
# Priya Gross Salary = 54000
# Highest Gross Salary Employee: Priya
# Gross Salary = 54000

def payroll():
    names = []
    gross_salaries = []
    for i in range(5):
        print(f"\nEnter Details of Employee {i+1}")
        name = input("Employee Name: ")
        basic_salary = float(input("Basic Salary: "))
        experience = int(input("Years of Experience: "))
        hra = basic_salary * 15 / 100
        ta = basic_salary * 10 / 100
        if experience >= 5:
            bonus = basic_salary * 20 / 100
        else:
            bonus = basic_salary * 10 / 100
        gross_salary = basic_salary + hra + ta + bonus
        names.append(name)
        gross_salaries.append(gross_salary)
        print(f"{name} Gross Salary = {gross_salary}")
    highest_salary = gross_salaries[0]
    highest_employee = names[0]
    for i in range(1, len(gross_salaries)):
        if gross_salaries[i] > highest_salary:
            highest_salary = gross_salaries[i]
            highest_employee = names[i]
    print("\nHighest Gross Salary Employee:", highest_employee)
    print("Gross Salary =", highest_salary)
payroll()