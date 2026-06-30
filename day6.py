# Task 1: Student Grade Checker (Beginner)
# Topics to Use: if, elif, else
# Problem: A school wants to automatically assign grades based on student marks.
# A→90 and above, B→75–89, C→60–74, D→35–59, Fail→Below 35.
# Example Input: Enter marks: 82
# Expected Output: Grade: B

def Gradechecker():
    marks=int(input("enter marks of a student:"))
    if marks>=90:
        print(f"Grade of student for {marks} is A")
    elif marks>=75 and marks<89:
        print(f"Grade of student for {marks} is B")
    elif marks>=60 and marks<74:
        print(f"Grade of student for {marks} is C")
    elif marks>=35 and marks<59:
        print(f"Grade of student for {marks} is D")
    else:
        print(f"fail")
Gradechecker()

# --------------------------------------------------------------------------------------------------------------------------------------
# Task 2: ATM PIN Verification (Beginner)
# Topics: while, if-else
# Problem: Allow only 3 PIN attempts. Correct PIN: Login Successful. After 3 wrong
# attempts: Card Blocked.
# Example Input: 1111, 2345, 1234
# Expected Output: Login Successful

def atmpin():
    actualpin=input("enter actual pin:")
    limit=3
    for i in range(3):
        limit-=1
        pin=input("enter pin:")
        if pin!=actualpin:
            # limit-1
            print(f"wrong pin you have limit:{limit}")

        else:
            print("login success")
atmpin()

# ------------------------------------------------------------------------------------------------------------------------------------------------
# Task 3: Multiplication Tables (Beginner)
# Topics: for loop
# Problem: Print multiplication table up to 10.
# Example Input: 7
# Expected Output:
# 7 x 1 = 7
# 7 x 2 = 14
# ...
# 7 x 10 = 70

def multiplications():
    number=int(input("enter a number for its table:"))
for i in range(1,11):
    mult=number*i
    print(f"{number} x {i} = {mult}")
multiplications()

# -------------------------------------------------------------------------------------------------------------------------------------------------------------------
# Task 4: Number Guess Validation (Beginner)
# Topics: while, if
# Problem: Keep asking until number is between 1 and 100.
# Example Input: 150, -5, 45
# Expected Output: Invalid, Invalid, Valid Number

def numberguess():
    i=0
    # number=int(input("enter a number from 1 to 100"))
    while i>=0:
        number=int(input("enter a number from 1 to 100"))
        if number>0 and number<=100:
            print("valid")
            break
        else:
            print("invalid")
        i+=1
numberguess()

# ---------------------------------------------------------------------------------------------------------------------------------------
# Task 5: Number Pattern (Beginner)
# Topics: Nested for loops
# Problem: Print pattern:
# 1
# 12
# 123
# 1234
# 12345

def pattern():
    n=5
    for i in range(1,6):
        for j in range(1,i+1):
            print(j, end="")
        print()
pattern()

# --------------------------------------------------------------------------------------------------------------------------------------------------
# Task 6: Bus Seat Booking Display (Beginner)
# Topics: Nested loops
# Problem: Display seats:
# R1C1 R1C2 R1C3 R1C4 R1C5
# R2C1 R2C2 R2C3 R2C4 R2C5
# R3C1 R3C2 R3C3 R3C4 R3C5
# R4C1 R4C2 R4C3 R4C4 R4C5

def seatbooking():
    rows=int(input("enter number of rows:"))
    columns=int(input("enter number of columns:"))
    for i in range(1,rows+1):
        for j in range(1,columns+1):
            print(f"R{i}C{j}",end=" ")
        print()
seatbooking()

# ---------------------------------------------------------------------------------------------------------------------------------------

# Task 7: Restaurant Ordering System (Beginner)
# Topics: while, if-elif, menu-driven programming
# Menu: 1.Pizza 2.Burger 3.Sandwich 4.Exit
# Keep ordering until Exit. Display Total Items Ordered = X.
# Example Input: 1 2 2 3 4
# Expected Output: Pizza Ordered, Burger Ordered, Burger Ordered, Sandwich Ordered,
# Total Items Ordered = 4

def ordering():
    # enter=int(input("enter a number from menu :"))
    i=1
    orders=[]
    while i>0:
        enter=int(input("enter a number from menu :"))
        if enter==1:
            # print("pizza ordered")
            orders.append("pizza ordered")
            i+=1
        elif enter==2:
            # print("burger ordered")
            orders.append("burger ordered")
            i+=1
        elif enter==3:
            # print("sandwidtch ordered")
            orders.append("sandwich ordered")
            i+=1
        elif enter==4:
            break
        else:
            print("invalid order ,order items available from menu")
    print(orders)
ordering()

# ----------------------------------------------------------------------------------------------------------------------------------------------------------------------

# Task 8: Cinema Seat Booking (Intermediate)
# Topics: Nested loops, if, break, continue
# Problem: Theatre has 5 rows and 6 seats. If seat already booked print Already Booked
# else Seat Booked Successfully. Continue until 5 seats booked.
# Example: (2,4),(2,4),(3,5)
# Output: Seat Booked Successfully, Already Booked, Seat Booked Successfully.

# Create a theatre with 5 rows and 6 seats
# 0 = Empty
# 1 = Booked
def seatbooking():
    rows = 5
    cols = 6
    seats = []
    for i in range(rows):
        row = []
        for j in range(cols):
            row.append(0)
        seats.append(row)
    booked = 0
    while booked < 5:
        row = int(input("Enter Row (1-5): "))
        seat = int(input("Enter Seat (1-6): "))
        row = row - 1
        seat = seat - 1
        if seats[row][seat] == 1:
            print("Already Booked")
            continue
        seats[row][seat] = 1
        booked += 1
        print("Seat Booked Successfully")
    print("\n5 Seats Booked Successfully.")
    print("\nFinal Seat Status:")
    for i in range(rows):
        print(seats[i])
seatbooking()

# ----------------------------------------------------------------------------------------------------------------------------------------

# Task 9: Employee Attendance Report (Intermediate)
# Topics: Cross nested loops, if-else
# Problem: 3 departments, 5 employees each. Attendance: 1=Present, 0=Absent.
# Display department-wise Present and Absent counts.

def attendance():
    departments=3
    employees=5
    for i in range(1,4):
        pcount=0
        acount=0
        for j in range(1,6):
            atten=int(input("enter attendance in 0 or 1 : "))
            if atten==1:
                pcount+=1
            else:
                acount+=1
        print(f"department {i} : present count = {pcount} and absent count = {acount} ")
attendance()

# ------------------------------------------------------------------------------------------------------------------------------------------

# Task 10: Bank Transaction Simulator (Intermediate - Interview Level)
# Topics: while, nested loops, if-elif, cross nested loops, break, continue
# Menu: Deposit, Withdraw, Balance, Mini Statement, Exit.
# Rules: Login with PIN (3 attempts), continue until Exit, withdrawal cannot exceed
# balance, maintain transaction count, display total deposits and withdrawals.
# Example Input: PIN1234, Deposit5000, Withdraw1200, Balance, Mini Statement, Exit.
# Expected Output: Deposit Successful, Withdrawal Successful, Balance=3800,
# Transactions=2, Thank You.

def Atm():
    attempts = 3
    atmpin = input("Enter actual PIN: ")

    for i in range(3):
        pin = input("Enter PIN: ")

        if pin == atmpin:
            print("Login Successful")
            break
        else:
            attempts -= 1
            print(f"Login Failed. You have {attempts} attempts left.")

    if pin == atmpin:
        transactions = 0
        balance = int(input("Enter your balance: "))

        while True:
            enter = int(input("\nSelect an option:\n1. Deposit\n2. Withdraw\n3. Balance\n4. Exit\nEnter choice: "))

            if enter == 1:
                deposit = int(input("Enter amount to deposit: "))
                balance += deposit
                transactions += 1
                print("Deposit Successful")

            elif enter == 2:
                withdraw = int(input("Enter amount to withdraw: "))
                if withdraw > balance:
                    print(f"Insufficient Balance. Current balance is {balance}")
                else:
                    balance -= withdraw
                    print("Withdraw Successful")
                transactions += 1

            elif enter == 3:
                print("Current Balance =", balance)

            elif enter == 4:
                print("Thank You!")
                print("Total Transactions =", transactions)
                break

            else:
                print("Invalid Choice")

    else:
        print("Your 3 attempts are over.")


Atm()