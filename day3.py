# 1. Factors of a Number
# Concepts to Use: while loop, if
# What is it? A factor is a number that divides another number exactly without leaving a remainder.
# Example Data: num = 24
# Task: Print all factors of the given number.
# Expected Output: 1, 2, 3, 4, 6, 8, 12, 24
# Write Your Solution Below:

num=24
n=1
while n<=num:
    if num%n==0:
        print(n)
    n+=1


# 2. Count Factors
# Concepts to Use: while loop, counting
# What is it? Find how many factors a number has.
# Example Data: num = 24
# Task: Count the total number of factors.
# Expected Output: Total Factors = 8
# Write Your Solution Below:

num=int(input("enter a number"))
n=1
count=0
while n<=num:
    if num%n==0:
        count+=1
    n+=1
print(f"Total factors = {count}")


# 3. Common Factors of Two Numbers
# Concepts to Use: while loop, if
# What is it? Factors that are common to both numbers.
# Example Data: a = 12, b = 18
# Task: Print all common factors.
# Expected Output: 1, 2, 3, 6
# Write Your Solution Below:

a=int(input("enter a number"))
b=int(input("enter a number"))
n=1
while n<=a and n<=b:
    if a%n==0 and b%n==0:
        print(n)
    n+=1


# 4. Highest Common Factor (HCF)
# Concepts to Use: while loop, comparison
# What is it? The largest factor common to both numbers.
# Example Data: a = 12, b = 18
# Task: Find the HCF.
# Expected Output: HCF = 6
# Write Your Solution Below:

a=int(input("enter a"))
b=int(input("enter b"))
n=1
hcf=1
while n<=a and n<=b:
    if a%n==0 and b%n==0:
        hcf=n
    n+=1
print(hcf)


# 5. Least Common Multiple (LCM)
# Concepts to Use: while loop
# What is it? The smallest number that both numbers can divide exactly.
# Example Data: a = 12, b = 18
# Task: Find the LCM.
# Expected Output: LCM = 36
# Write Your Solution Below:

a=int(input("enter a"))
b=int(input("enter b"))
n=1
lcm=1
while n<=a and n<=b:
    if a%n==0 and b%n==0:
        lcm*=n
        print(n)
    n+=1
print(lcm)


# 6. Coprime Numbers
# Concepts to Use: while loop, HCF logic
# What is it? Two numbers are coprime if their HCF is 1.
# Example Data: a = 8, b = 15
# Task: Check whether the numbers are coprime.
# Expected Output: Coprime Numbers
# Write Your Solution Below:

a=int(input("enter a"))
b=int(input("enter b"))
n=1
hcf=0
while n<=a and n<=b:
    if a%n==0 and b%n==0:
        hcf=n
    n+=1
print("hcf = ",hcf)
if hcf==1:
    print("co primes")


# 7. Perfect Number
# Concepts to Use: while loop, factors
# What is it? A number whose factors (excluding itself) add up to the number.
# Example Data: num = 28
# Task: Check whether the number is perfect.
# Expected Output: Perfect Number
# Write Your Solution Below:

num=int(input("enter a number:"))
n=1
sum=0
while n<num:
    if num%n==0:
        sum+=n
    n+=1
if sum==num:
    print("perfect number")
else:
    print("not a perfect number")


# 8. Find Greatest Factor Other Than Itself
# Concepts to Use: while loop
# What is it? Find the largest factor excluding the number itself.
# Example Data: num = 36
# Task: Print the greatest factor other than the number.
# Expected Output: 18
# Write Your Solution Below:

num=int(input("enter a number :"))
n=1
gcf=0
while n<num:
    if num%n==0:
        gcf=n
    n+=1
print("GCF = ",gcf)


# 9. Factory Machine Synchronization
# Concepts to Use: LCM
# What is it? Machine A completes a cycle every 12 minutes and Machine B every 18 minutes.
# Example Data: machine1 = 12, machine2 = 18
# Task: Find after how many minutes both machines will complete a cycle together again.
# Expected Output: 36 Minutes
# Write Your Solution Below:

m1=int(input("enter a number:"))
m2=int(input("enter a number:"))
n=1
lcm=1
while n<=m1 and n<=m2:
    if m1%n==0 and m2%n==0:
        lcm*=n
    n+=1
print(lcm,"minutes")


# 10. Gift Box Distribution
# Concepts to Use: HCF
# What is it? You have 24 chocolates and 36 biscuits. Create the maximum number of identical gift
# boxes without leftovers.
# Example Data: chocolates = 24, biscuits = 36
# Task: Find the maximum number of gift boxes.
# Expected Output: 12 Gift Boxes
# Write Your Solution Below:

chocolates=int(input("enter a number:"))
biscuits=int(input("enter a number:"))
n=1
hcf=1
while n<=chocolates and n<=biscuits:
    if chocolates%n==0 and biscuits%n==0:
        hcf=n
    n+=1
print(hcf,"gift boxes")
