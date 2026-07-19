# 1. Print Numbers Divisible by Both 3 and 5 Problem 
# Definition: Some numbers satisfy multiple conditions at the same time. 
# Task: Read N and print all numbers from 1 to N divisible by both 3 and 5. 
# Example Input: 50 
# Example Output: 15 30 45

num=int(input())
i=1
while i<=num:
    if i%3==0 and i%5==0:
        print(i,end=" ")
    i+=1


# 2. Count Numbers Ending with 5 Problem 
#     Definition: The last digit helps identify patterns. 
#     Task: Read N and count numbers from 1 to N ending with 5. 
#     Example Input: 35 
#     Example Output: 4

n=int(input())
count=0
while n>0:
    if n%10==5:
        count+=1
    n-=1
print(count)


# 3. Sum Numbers Whose Last Digit is Even Problem 
# Definition: Check only the last digit before adding. 
# Task: Read N and find the sum of numbers whose last digit is even. 
# Example Input: 10 
# Example Output: 30

n=int(input())
sum=0
while n>0:
    digit=n%10
    if digit%2==0:
        sum+=n
    n-=1
print(sum)


# 4. Print Numbers Whose Square is Less Than N Problem 
# Definition: Print numbers only if their square is less than N. 
# Task: Read N and print such numbers. 
# Example Input: 30 
# Example Output: 1 2 3 4 5

n=int(input())
i=1
while i<=n:
    if i**2<n:
        print(i,end=" ")
    i+=1


# 5. Count Numbers Divisible by 4 but Not by 6
# Problem Definition: Combine two divisibility conditions. 
# Task: Read N and count numbers divisible by 4 but not 6. 
# Example Input: 30 
# Example Output: 5

n=int(input())
count=0
while n>0:
    if n%4==0 and n%6!=0:
        count+=1
    n-=1
print(count)


# 6. Reverse Every Alternate Number 
# Problem Definition: Process alternate inputs differently. 
# Task: Read N numbers. Reverse only the 2nd, 4th, 6th... numbers. 
# Example Input: 4 123 456 789 654 
# Example Output: 123 654 789 456

n=int(input())
i=1
while i<=n:
    nums=int(input())
    if i%2==0:
        rev=0
        temp=nums
        while temp>0:
            digit=temp%10
            rev=rev*10+digit
            temp//=10
        print(rev)
    i+=1


# 7. First Number Divisible by Both 7 and 9 
# Problem Definition: Stop when the required number is found. 
# Task: Read N and print the first number greater than N divisible by both 7 and 9. 
# Example Input: 50 
# Example Output: 63

n=int(input())
while n>0:
    if n%7==0 and n%9==0:
        print(n)
        break
    n+=1
    

# 8. Count Numbers Having More Even Digits Than Odd Digits 
# Problem Definition: Compare even and odd digits in each number. 
# Task: Read N numbers and count such numbers. 
# Example Input: 3 2481 1357 8246 
# Example Output: 2

n=int(input())
count=0
while n>0:
    nums=int(input()) #2481 1357 8246
    even=0
    odd=0
    temp=nums
    while temp>0: #8246 824 82 8
        digit=temp%10 #6 4 2 8
        if digit%2==0: #t t t t
            even+=1 #1 2 3 4
        else:
            odd+=1
        temp//=10 #824 82 8 0
    if even>odd: #3>0 0>3-f 4>3-t
        count+=1 #1 2
    n-=1
print(count)


# 9. Print Factors Greater Than 5 
# Problem Definition: Filter factors using a condition.
# Task: Read a number and print only factors greater than 5. 
# Example Input: 60 
# Example Output: 6 10 12 15 20 30 60

n=int(input())
fact=1
i=1
while i<=n:
    if n%i==0 and i>5:
        print(i , end=" ")
    i+=1
 
# 10. Sum Until a Negative Number Appears 
# Problem Definition: Use a negative number as the stopping condition. 
# Task: Read numbers until a negative appears and print the sum. 
# Example Input: 10 20 15 8-1 
# Example Output: 53

n=1
sum=0
while n>0:
    num=int(input())
    if num>0:
        sum+=num
    else:
        break
    n+=1
print(sum)