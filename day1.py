1. Grocery Store Billing with Discount
Concepts to Use: for loop, if
Example Data: prices = [500, 1200, 800, 1500]
Task: Calculate the total bill. If an item price is greater than 1000, give a 10% discount on that
item. Calculate the final bill after discount.
Expected Output:
Total Bill = 4000
Discount = 270
Final Bill = 3730
Write Your Solution Below:

data=[500,1200,800,1500]
total=0
disscount=0
for price in data:
    total+=price
    if price>1000:
        diss=price*(10/100)
        disscount+=diss
final=total-disscount
print("Total bill = ",total)
print("Disscount = ",disscount)
print("Final bill = ",final)


2. Employee Attendance Percentage
Concepts to Use: for loop, counting
Example Data: attendance = ['P', 'A', 'P', 'P', 'A', 'P']
Task: Calculate the total present days and attendance percentage.
Expected Output:
Present Days = 4
Attendance Percentage = 66.67

attendance=['P','A','P','P','A','P']
present=0
absent=0
for i in attendance:
    if i=='P':
        present+=1
percentage=(present/len(attendance))*100
print(f"present days = {present}")
print(f"Attendance percentage = {percentage:.2f}")


3. Online Shopping Cart
Concepts to Use: for loop, continue
Example Data: cart = [500, -1, 700, 1200, -1, 300]
Task: -1 means item removed from cart. Ignore removed items and calculate the total amount.
Expected Output:
Total Amount = 2700

cart=[500,-1,700,1200,-1,300]
total=0
for i in cart:
    if i==-1:
        continue
    total+=i
print("total amount = ",total)

4. Bank Transactions
Concepts to Use: for loop, break
Example Data: transactions = [5000, -2000, -3000, -4000]
balance = 6000
Task: Process transactions one by one. Stop if the balance becomes negative. Display the final
balance.
Expected Output:
Insufficient Balance
Final Balance = 1000

trans=[5000,-2000,-3000,-4000]
balance=6000
final=0
for i in trans:
    balance+=i
    if balance<0:
        break
print("insufficient balance")
final+=balance
print('final balance = ',final)


5. Cricket Tournament Analysis
Concepts to Use: for loop
Example Data: runs = [45, 80, 22, 95, 60]
Task: Find the total runs, highest score, and average score.
Expected Output:
Total = 302
Highest = 95
Average = 60.4

runs=[45,80,22,95,60]
total_runs=0
h_score=0
average=0
for i in runs:
    total_runs+=i
average=total_runs/len(runs)
h_score=max(runs)
print(f"total = {total_runs}")
print(f"highest = {h_score}")
print(f"average = {average}")


6. Electricity Consumption Billing
Concepts to Use: while loop
Example Data: units = [120, 150, 200, 180]
Task: Calculate the electricity bill using: First 100 units = 5/unit Remaining units = 8/unit
Expected Output:
Calculate Total Bill

units=[120,150,200,180]
i=0
while i<len(units):
    if units[i]<100:
        units[i]*=5
        print("total bill = ",units)
    if units[i]>100:
        unit1=units[i]-100
        unit2=unit1+100
        unit1*=8
        unit2*=5
        unit=unit1+unit2
    print("total bill = ",unit)
    i+=1


Concepts to Use: for loop, counting
Example Data: marks = [75, 30, 82, 40, 95, 28]
Task: Count how many students passed and failed. Pass mark = 35.
Expected Output:
Passed = 4
Failed = 2
Write Your Solution Below

marks=[75,30,82,40,95,28]
p_mark=35
pcount=0
fcount=0
for i in marks:
    if i>35:
        pcount+=1
    else:
        fcount+=1
print("passed = ",pcount)
print("failed = ",fcount)


8. Food Delivery Performance
Concepts to Use: for loop, continue
Example Data: ratings = [5, 4, 0, 3, 5, 0, 4]
Task: 0 means not rated. Ignore those ratings and calculate the average rating.
Expected Output:
Average Rating = 4.2
Write Your Solution Below:

ratings=[5,4,0,3,5,0,4]
count=0
average=0
for i in ratings:
    if i==0:
        continue
    count+=1
average=sum(ratings)/count
# count+=1
print("average = ",average)


9. ATM Cash Dispensing
Concepts to Use: while loop
Example Data: amount = 3700
Task: Calculate the minimum number of notes required using 2000, 500, 200, and 100
notes.
Expected Output:
2000 x 1
500 x 3
200 x 1
Write Your Solution Below:

amount=3700
while amount>0:
    if amount>=2000:
        n=amount//2000
        amount=amount%2000
        print("2000*",n)
    elif amount>=500:
        n=amount//500
        amount=amount%500
        print("500*",n)
    elif amount>=200:
        n=amount//200
        amount=amount%200
        print("200*",n)


10. Sales Report Generator
Concepts to Use: for loop, break, continue
Example Data: sales = [5000, 7000, -1, 9000, 0, 8000]
Task: -1 means holiday (skip it). 0 means system crash (stop processing). Calculate total sales
before crash.
Expected Output:
Total Sales = 21000
Write Your Solution Below:

sales=[5000,7000,-1,9000,0,8000]
total=0
for i in sales:
    if i==-1:
        continue
    elif i==0:
        break
    total+=i
print(total)