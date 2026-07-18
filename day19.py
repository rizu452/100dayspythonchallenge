# 1. Count Even and Odd Numbers from 1 to N Problem 
# Definition: A program can classify numbers as even or odd. 
# Task: Read N. Count even and odd numbers from 1 to N. 
# Example Input: 10 
# Example Output: Even Numbers = 5 Odd Numbers = 5

def evenodd():
    n=int(input())
    e_count=0
    o_count=0
    while n>0:
        if n%2==0:
            e_count+=1
        else:
            o_count+=1
        n-=1
    print(f"even={e_count} odd={o_count}")
evenodd()

# 2. Sum of Numbers Divisible by 3 Problem 
# Definition: Process only numbers that satisfy a condition. 
# Task: Read N. Find the sum of numbers divisible by 3. 
# Example Input: 10 
# Example Output: 18

def sumofnumbers():
    n=int(input())
    sum=0
    while n>0:
        if n%3==0:
            sum+=n
        n-=1
    print(f"{sum}")
sumofnumbers()


# 3. Print Leap Years in a Range Problem 
# Definition: Leap years follow specific rules. 
# Task: Read start year and end year. Print all leap years. 
# Example Input: 2000 2020 
# Example Output: 2000 2004 2008 2012 2016 2020

def leapyear():
    from_year=int(input("enter a year to start from "))
    to_year=int(input("enter a year to search upto "))
    while from_year<=to_year:
        if (from_year%4==0 and from_year%100!=0) or from_year%400==0:
            print(from_year)
        from_year+=1
leapyear()
        


# 4. Count Multiples of 5 and 7 Problem 
# Definition: Numbers may satisfy multiple divisibility rules. 
# Task: Read N. Count multiples of 5, 7 and both. 
# Example Input: 50 
# Example Output: 5=10 7=7 Both=1

def multiples():
    n=int(input())
    f_count=0
    s_count=0
    both=0
    i=1
    while i<=n:
        if i%5==0 and i%7==0:
            f_count+=1
            s_count+=1
            both+=1
        elif i%5==0:
            f_count+=1
        elif i%7==0:
            s_count+=1
        i+=1
    print(f"5={f_count} 7={s_count} both={both}")
multiples()


# 5. Print All Factors and Their Count Problem Definition: 
# Factors divide a number exactly. 
# Task: Print all factors and total count. 
# Example Input: 12 
# Example Output: 1 2 3 4 6 12 
# Total Factors = 6

def allfactorscount():
    n=int(input())
    count=0
    i=1
    while i<=n:
        if n%i==0:
            count+=1
            print(i,end=" ")
        i+=1
    print(f"\nTotal factors = {count}")
allfactorscount()


# 6. Largest Digit Problem 
# Definition: Find the greatest digit. 
# Task: Read a number and print the largest digit. 
# Example Input: 583920 
# Example Output: Largest Digit = 9

def largestdigit():
    n=int(input())
    largest=0
    while n>0:
        digit=n%10
        if digit>largest:
            largest=digit
        n=n//10
    print(f"largest digit = {largest}")
largestdigit()


# 7. Smallest Digit Problem 
# Definition: Find the smallest digit. 
# Task: Read a number and print the smallest digit. 
# Example Input: 583920 
# Example Output: Smallest Digit = 0

def smallestdigit():
    n=int(input())
    smallest=9
    while n>0:
        digit=n%10
        if digit<smallest:
            smallest=digit
        n=n//10
    print(f"smallest digit = {smallest}")
smallestdigit()


# 8. Count Digits Greater Than 5 Problem 
# Definition: Count digits meeting a condition. 
# Task: Read a number and count digits > 5. 
# Example Input: 589762 
# Example Output: 4

def countdigits():
    n=int(input())
    count=0
    while n>0:
        digit=n%10
        if digit>5:
            count+=1
        n//=10
    print(f"count={count}")
countdigits()


# 9. Sum Only Even Digits Problem 
# Definition: Add only even digits. 
# Task: Read a number and print the sum of even digits. 
# Example Input: 58294 
# Example Output: 14

def sumeven():
    n=int(input())
    sum=0
    while n>0:
        digit=n%10
        if digit%2==0:
            sum+=digit
        n//=10
    print(sum)
sumeven()


# 10. Divisible by 3 but Not 5 Problem 
# Definition: Filter numbers using two conditions. 
# Task: Read N and print numbers divisible by 3 but not 5. 
# Example Input: 30 
# Example Output: 3 6 9 12 18 21 24 27

def divisible():
    n=int(input())
    i=1
    while i<=n:
        if i%3==0 and i%5!=0:
            print(i,end=" ")
        i+=1
divisible()
