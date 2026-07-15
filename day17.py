# 1. Print Numbers from 1 to N 
# Definition: Loops allow a program to repeat the same task multiple times. 
# Task: Read a number N and print all numbers from 1 to N using a loop. 
# Example Input: N = 5 
# Example Output: 1 2 3 4 5

def numbersequence():
    num=int(input("enter a number "))
    i=1
    while i<=num:
        print(i,end=" ")
        i+=1
numbersequence()



# 2. Print Numbers from N to 1 
# Definition: Reverse counting is useful in many programming problems. 
# Task: Read a number N and print numbers from N to 1 using a loop. 
# Example Input: N = 5 
# Example Output: 5 4 3 2 1

def reverseseuence():
    num=int(input("enter a number "))
    i=num
    while i>0:
        print(i,end=" ")
        i-=1
reverseseuence()


# 3. Sum of First N Natural Numbers 
# Definition: Natural numbers start from 1. 
# Task: Find the sum of numbers from 1 to N using a loop. 
# Example Input: N = 5 
# Example Output: 15

def sumofnaturalnum():
    num=int(input("enter a number "))
    sum=0
    i=1
    while i<=num:
        sum+=i
        i+=1
    print(sum)
sumofnaturalnum()


# 4. Factorial of a Number 
# Definition: The factorial of a number is the product of all positive integers from 1 to that number. 
# Task: Calculate the factorial using a loop. 
# Example Input: N = 5 
# Example Output: 120

def factorial():
    num=int(input("enter a number "))
    product=1
    i=1
    while i<=num:
        product*=i
        i+=1
    print(product)
factorial()


# 5. Multiplication Table 
# Definition: A multiplication table shows the multiples of a number. 
# Task: Print the multiplication table of a given number up to 10. 
# Example Input: N = 3 
# Example Output: 3 x 1 = 3 ... 3 x 10 = 30


def multiplication():
    num=int(input("enter a num "))
    product=1
    i=1
    while i<=10:
        product=num*i
        print(f"{num} x {i} = {product}")
        i+=1
multiplication()


# 6. Count Digits 
# Definition: Every number contains one or more digits. 
# Task: Count the total number of digits using a loop.
# Example Input: 45892 
# Example Output: 5

def countdigits():
    num=int(input("enter a number "))
    temp=num
    count=0
    while temp>0:
        count+=1
        temp=temp//10
    print(count)
countdigits()


# 7. Reverse a Number 
# Definition: Reversing digits is a common number problem. 
# Task: Reverse the given number using a loop. 
# Example Input: 1234 
# Example Output: 4321

def reversenumber():
    num=int(input("enter a number "))
    rev=0
    temp=num
    while temp>0:
        digit=temp%10
        rev=rev*10+digit
        temp=temp//10
    print(rev)
reversenumber()


# 8. Sum of Digits 
# Definition: Add all digits present in the number. 
# Task: Calculate the sum of digits using a loop. 
# Example Input: 572 
# Example Output: 14


def sumofdigits():
    num=int(input("enter a number "))
    sum=0
    temp=num
    while temp>0:
        digit=temp%10
        sum+=digit
        temp=temp//10
    print(sum)
sumofdigits()


# 9. Product of Digits 
# Definition: Multiply all digits present in the number. 
# Task: Calculate the product of digits using a loop. 
# Example Input: 572 
# Example Output: 70

def productofdigits():
    num=int(input("enter a number "))
    product=1
    temp=num
    while temp>0:
        digit=temp%10
        product*=digit
        temp=temp//10
    print(product)
productofdigits()


# 10. Count Even and Odd Digits 
# Definition: Separate digits based on whether they are even or odd. 
# Task: Count even digits and odd digits using a loop. 
# Example Input: 583920 
# Example Output: Even Digits = 3 Odd Digits = 3

def countevenodd():
    num=int(input("enter anumber : "))
    e_count=0
    o_count=0
    temp=num
    while temp>0:
        digit=temp%10
        if digit%2==0:
            e_count+=1
        else:
            o_count+=1
        temp//=10
    print(f"even digits={e_count} , odd digits={o_count} ")
countevenodd()