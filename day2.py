# 1. Longest Login Streak
# Concepts to Use: for loop, counting
# Example Data: logins = [1, 1, 0, 1, 1, 1, 0, 1]
# Task: 1 means logged in and 0 means missed day. Find the longest continuous login streak.
# Expected Output:
# Longest Streak = 3
# Write Your Solution Below:

logins=[1,1,0,1,1,1,1,0,1]
streak=0
max=0
for login in logins:
    if login==0:
        streak=0
        login+=1
        continue
    streak+=1
    login+=1
    if streak>max:
        max=streak
print("longest streak is :",max)

# 2. Password Strength Checker
# Concepts to Use: for loop, counting
# Example Data: password = "Abc123X"
# Task: Count uppercase letters, lowercase letters, and digits. Print Strong Password if it contains at
# least one uppercase letter, one lowercase letter, and one digit.
# Expected Output:
# Uppercase = 2
# Lowercase = 3
# Digits = 3
# Strong Password
# Write Your Solution Below:

password="Abc123X"
uppercase=0
lowercase=0
digits=0
for char in password:
    if 'A'<=char<='Z':
        uppercase+=1
    elif 'a'<=char<='z':
        lowercase+=1
    elif char.isdigit():
        digits+=1
if uppercase>0 and lowercase>0 and digits>0:
    print("strong password")
else:
    print("weak password")
print("uppercase=",uppercase)
print("lowercase=",lowercase)
print("digits=",digits)


# 3. Warehouse Stock Alert
# Concepts to Use: for loop, continue
# Example Data: stock = [25, 5, 0, 18, 3, 40]
# Task: Ignore products with stock 0. Count how many products need restocking (stock less than 10).
# Expected Output:
# Products To Restock = 2
# Write Your Solution Below:

stock=[25,5,0,18,3,40]
restock=0
for product in stock:
    if product==0:
        continue
    elif product<10:
        restock+=1
print("products to restock = ",restock)

# 4. Bus Seat Occupancy
# Concepts to Use: while loop
# Example Data: seats = [1, 0, 1, 1, 0, 0, 1]
# Task: 1 means occupied and 0 means empty. Calculate occupied seats, empty seats, and
# occupancy percentage.
# Expected Output:
# Occupied = 4
# Empty = 3
# Occupancy = 57.14%
# Write Your Solution Below:

seats=[1,0,1,1,0,0,1]
occupied=0
empty=0
o_percentage=1
ind=0
while ind<len(seats):
    ind1=seats[ind]
    ind+=1
    if ind1==0:
        empty+=1
        continue
    else:
        occupied+=1
o_percentage=(occupied/len(seats))*100
print("occupied = ",occupied)
print("empty = ",empty)
print(f"occupancy = {o_percentage:.2f}%")


# 5. Consecutive Failures Detector
# Concepts to Use: for loop, break
# Example Data: results = ['P', 'P', 'F', 'F', 'F', 'P']
# Task: Stop processing when 3 consecutive failures occur.
# Expected Output:
# 3 Consecutive Failures Found
# Write Your Solution Below:

results=['p','p','f','f','f','p']
count=0
for result in results:
    if result=='f':
        count+=1
        if count==3:
            print(f"{count} consecutive failures found")
            break
else:
    count=0


# 6. Product Return Analysis
# Concepts to Use: for loop
# Example Data: orders = [500, 800, -500, 1000, -800]
# Task: Positive values are sales and negative values are returns. Calculate total sales, total returns,
# and net revenue.
# Expected Output:
# Sales = 2300
# Returns = 1300
# Net Revenue = 1000
# Write Your Solution Below:

orders=[500,800,-500,1000,-800]
sales=0
returns=0
netrevenue=0
for order in orders:
    if order>0:
        sales+=order
    elif order<0:
        returns-=order
print("sales=",sales)
print("returns=",returns)
netrevenue=sales-returns
print("netrevenue",netrevenue)


# 7. Mobile Data Usage Tracker
# Concepts to Use: while loop
# Example Data: usage = [450, 600, 700, 550], limit = 2000
# Task: Process usage day by day and stop when the limit is exceeded.
# Expected Output:
# Limit Exceeded On Day 4
# Used = 2300 MB
# Write Your Solution Below:

usage=[450,600,700,550]
limit=2000
total=0
data=0
while data<len(usage):
    data1=usage[data]
    total+=data1
    data+=1
    if total>limit:
        print("limit exceed on day ",data)
        break
print("used data=",total)


# 8. Voting Machine Result
# Concepts to Use: for loop
# Example Data: votes = ['A', 'B', 'A', 'C', 'A', 'B', 'A']
# Task: Count votes for each candidate and find the winner.
# Expected Output:
# A = 4
# B = 2
# C = 1
# Winner = A
# Write Your Solution Below:

votes=['A','B','A','C','A','B','A','C','C','C','C']
Acount=0
Bcount=0
Ccount=0
for vote in votes:
    if vote=='A':
        Acount+=1
    elif vote=='B':
        Bcount+=1
    elif vote=='C':
        Ccount+=1
print(f"A = {Acount}")
print(f"B = {Bcount}")
print(f"C = {Ccount}")
if Acount>Bcount and Acount>Ccount:
    print("winner = A")
elif Bcount>Acount and Bcount>Ccount:
    print("winner=B")
else:
    print("winner = C")


# 9. Parking Lot Management
# Concepts to Use: for loop, counting
# Example Data: vehicles = ['C', 'B', 'C', 'T', 'B', 'C']
# Task: Count Cars, Bikes, and Trucks.
# Expected Output:
# Cars = 3
# Bikes = 2
# Trucks = 1

vehicles=['c','b','c','t','b','c']
cars=0
bikes=0
trucks=0
for vehicle in vehicles:
    if vehicle=='c':
        cars+=1
    elif vehicle=='b':
        bikes+=1
    else:
        trucks+=1
print("cars = ",cars)
print("bikes = ",bikes)
print("trucks = ",trucks)


# 10. Number Sequence Analyzer
# Concepts to Use: for loop
# Example Data: numbers = [12, 5, 8, 21, 14, 7]
# Task: Find number of even numbers, odd numbers, largest number, and smallest number.
# Expected Output:
# Even = 3
# Odd = 3
# Largest = 21
# Smallest = 5
# Write Your Solution Below:

numbers=[12,5,8,21,14,7]
even=0
odd=0
for num in numbers:
    if num%2==0:
        even+=1
    else:
        odd+=1
largest=max(numbers)
smallest=min(numbers)
print("even = ",even)
print("odd = ",odd)
print("largest=",largest)
print("smallest=",smallest)