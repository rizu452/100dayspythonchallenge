# 1. Count Numbers Whose Last Digit is Greater Than First Digit 
# Problem Definition: Every number has a first digit and a last digit. Compare them. 
# Task: Read N numbers. Count how many have the last digit greater than the first digit. 
# Example Input: 5 123 482 91 3456 78 
# Example Output: 2

n=int(input())
count=0
for i in range(n):
    nums=int(input())
    temp=nums
    for i in range(temp):
        digit=temp%10
        # temp//=10
    while temp>=10:
        temp//=10
    if digit>temp:
        count+=1
print(count)
        

# 2. Print Common Factors of Two Numbers 
# Problem Definition: A common factor divides both numbers exactly. 
# Task: Read two numbers and print all their common factors. 
# Example Input: 24 36 
# Example Output: 1 2 3 4 6 12

n1=int(input())
n2=int(input())
if n1>n2:
    smallest=n2
else:
    smallest=n1
for i in range(1,smallest+1):
    if n1%i==0 and n2%i==0:
        print(i,end=" ")


# 3. Count Numbers Having Exactly Three Digits 
# Problem Definition: A three-digit number lies between 100 and 999. 
# Task: Read N numbers and count how many are exactly three digits. 
# Example Input: 5 23 456 890 1000 145 
# Example Output: 3

n=int(input())
count3=0
for i in range(n):
    nums=int(input())
    temp=nums
    count=0
    while temp>0:
        digit=temp%10
        count+=1
        temp//=10
    if count==3:
        count3+=1
print(count3)


# 4. Print Numbers Whose Digit Sum is Even
# Problem Definition: The sum of the digits can be used as a condition. 
# Task: Read N. Print all numbers from 1 to N whose digit sum is even. 
# Example Input: 15 
# Example Output: 2 4 6 8 11 13 15

n=int(input())
i=1
while i<=n:
    sum=0
    temp=i
    while temp>0:
        digit=temp%10
        sum+=digit
        temp//=10
    if sum%2==0:
        print(i,end=" ")
    i+=1

# 5. Count Factors That Are Even 
# Problem Definition: Not every factor is even. 
# Task: Read a number and count how many of its factors are even. 
# Example Input: 24 Example Output: 6 

n=int(input())
count=0
for i in range(1,n+1):
    if n%i==0:
        if i%2==0:
            count+=1
print(count)

# 6. Reverse Only Even Numbers 
# Problem Definition: Different inputs may require different processing. 
# Task: Read N numbers. Reverse only even numbers and print odd numbers unchanged. 
# Example Input: 4 123 246 789 820 
# Example Output: 123 642 789 28 

def evenonly(*numbers):
    for i in range(len(numbers)):
        if numbers[i]%2!=0:
            print(numbers[i])
            continue
        temp=numbers[i]
        rev=0
        while temp!=0:
            rem=temp%10
            rev=rev*10+rem
            temp//=10
        print(rev)
evenonly(123,246,789,820)

# 7. Find the Smallest Multiple of 7 Greater Than N 
# Problem Definition: Search until the required condition is met. 
# Task: Read N and print the smallest multiple of 7 greater than N. 
# Example Input: 50 Example Output: 56

n=int(input())
while n>0:
    if n%7==0:
        print(n)
        break
    n+=1


# 8. Count Numbers Having Equal Even and Odd Digits 
# Problem Definition: Compare the number of even and odd digits. 
# Task: Read N numbers and count how many have equal even and odd digits. 
# Example Input: 4 1234 2468 1357 4521 Example Output: 2 

def countevenodd(*num):
    count=0
    for i in range(len(num)):
        even=0
        odd=0
        temp=num[i]
        while temp>0:
            rem=temp%10
            if rem%2==0:
                even+=1
            else:
                odd+=1
            temp//=10
        if even==odd:
            count+=1
    print(count)
countevenodd(1234,2468,1357,4521)


# 9. Print Factors Between 5 and 20 
# Problem Definition: Filter factors within a range. 
# Task: Read a number and print only the factors between 5 and 20. 
# Example Input: 120 
# Example Output: 5 6 8 10 12 15 20 

number=int(input())
n1=int(input())
n2=int(input())
while n1<=n2:
    if number%n1==0:
        print(n1,end=" ")
    n1+=1


# 10. Read Numbers Until Their Sum Exceeds 100 
# Problem Definition: A loop can stop based on the running total. 
# Task: Keep reading numbers until the sum exceeds 100. Print the final sum. 
# Example Input: 20 35 18 40 
# Example Output: 113

n=1
sum=0
while n>0:
    num=int(input())
    sum+=num
    if sum>100:
        break
    n+=1
print(sum)