# # 1. Find the Largest of N Numbers Problem 
# # Definition: Find the greatest value from a sequence of numbers. T
# # ask: Read N, then read N numbers one by one and print the largest. 
# # Example Input: N=5 12 45 8 90 34 
# # Example Output: Largest = 90

def largestnumber():
    n=int(input("enter a number "))
    largest=0
    while n>0:
        num=int(input())
        if num>largest:
            largest=num
        n-=1
    print(f"largest = {largest}")
largestnumber()


# 2. Find the Smallest of N Numbers Problem 
# Definition: Find the smallest value from a sequence of numbers. 
# Task: Read N numbers and print the smallest. 
# Example Input: N=5 18 3 45 7 12 
# Example Output: Smallest = 3 

def smallestnumber():
    n= int(input())
    smallest=99
    while n>0:
        num=int(input())
        if num<smallest:
            smallest=num
        n-=1
    print(f"smallest = {smallest}")
smallestnumber()


# 3. Find the Second Largest Number Problem 
# Definition: Find the second highest value without sorting. 
# Task: Read N numbers and print the second largest. 
# Example Input: N=5 25 60 15 80 50 
# Example Output: Second Largest = 60 

def secondlargest():
    n=int(input())
    largest=0
    second_largest=0
    while n>0:
        num=int(input())
        if num>largest:
            second_largest=largest
            largest=num
        n-=1
    print(f"second largest = {second_largest}")
secondlargest()


# 4. Find the Second Smallest Number Problem 
# Definition: Find the second lowest value without sorting.
# Task: Read N numbers and print the second smallest. 
# Example Input: N=5 25 60 15 80 50 
# Example Output: Second Smallest = 25 

def secondsmallest():
    n=int(input())
    smallest=99
    second_smallest=0
    while n>0:
        num=int(input())
        if num<smallest:
            second_smallest=smallest
            smallest=num
        n-=1
    print(f"second smallest = {second_smallest}")
secondsmallest()


# 5. Count Positive, Negative and Zero Values Problem 
# Definition: Classify numbers based on their sign. 
# Task: Read N numbers and count positives, negatives and zeros. 
# Example Input: N=6 10-5 0 18-2 0 
# Example Output: Positive = 2 Negative = 2 Zero = 2 

def countnums():
    n=int(input())
    p_count=0
    n_count=0
    z_count=0
    while n>0:
        num=int(input())
        if num>0:
            p_count+=1
        elif num<0:
            n_count+=1
        else:
            z_count+=1
        n-=1
    print(f"positive = {p_count} negative = {n_count} zero = {z_count}")
countnums()

# 6. Find the Missing Number Problem 
# Definition: One number from 1 to N is missing. 
# Task: Read N and the remaining numbers, then find the missing number. 
# Example Input: N=6 1 2 3 5 6 
# Example Output: Missing Number = 4 

def findmissing():
    n=int(input())
    i=n
    sum=0
    while i>0:
        sum+=i
        i-=1
    print(sum)
    sum1=0
    while n-1>0:
        num=int(input())
        sum1+=num
        n-=1
    print(sum1)
    if sum!=sum1:
        missing=sum-sum1
    print(f"missing={missing}")
findmissing()

# 7. Check Whether a Number is Perfect Problem 
# Definition: A perfect number equals the sum of its proper factors. 
# Task: Determine whether the given number is perfect. 
# Example Input: 28 
# Example Output: Perfect Number 

def perfectnum():
    num=int(input())
    temp=num
    i=1
    sum=0
    while i<temp:
        if temp%i==0:
            sum+=i
        i+=1
    print(f"sum={sum}")
    if sum==num:
        print(f"{num} is a perfect number")
    else:
        print(f"{num} is not a perfect number")
perfectnum()


# 8. Find the GCD of Two Numbers Problem 
# Definition: The GCD is the greatest number that divides both numbers. 
# Task: Find the GCD using loops. Example Input: 24 36 
# Example Output: GCD = 12

def gcd():
    num1=int(input())
    num2=int(input())
    if num1>num2:
        smallest=num2
    else:
        smallest=num1
    i=smallest
    while i<=smallest:
        if num1%i==0 and num2%i==0:
            print(f"GCD = {i}")
            break
        i-=1
gcd()

# 9. Find the LCM of Two Numbers Problem 
# Definition: The LCM is the smallest number divisible by both numbers. 
# Task: Find the LCM using loops. Example Input: 12 18 
# Example Output: LCM = 36 

def lcm():
    n1=int(input("enter number1 "))
    n2=int(input("enter number2 "))
    if n1>n2:
        lcm=n1
    else:
        lcm=n2
    while True:
        if lcm%n1==0 and lcm%n2==0:
            break
            # print(n)
        lcm+=1
    print(lcm)
lcm()

# 10. Power Without Using ** Problem 
# Definition: Calculate a power using repeated multiplication. 
# Task: Read the base and exponent, then compute the result using a loop. 
# Example Input: Base = 3 Exponent = 4 
# Example Output: 81

def power():
    base=int(input())
    exponent=int(input())
    i=1
    power=1
    while i<=exponent:#2<4
        power*=base#1*3=3,3*3=9,9*3=27*
        i+=1#2
    print(f"power= {power}")
power()