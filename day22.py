# 1. Count Numbers Divisible by the Sum of Their Digits 
# Problem Definition: Some numbers are divisible by the sum of their own digits. 
# Task: Read N. Count how many numbers from 1 to N are divisible by the sum of their digits. 
# Example Input: 20 
# Example Output: 13

n=int(input())
count=0
for i in range(1,n+1):
    temp=i
    sum=0
    while temp!=0:
        rem=temp%10
        sum+=rem
        temp//=10
    if i%sum==0:
        count+=1
print(count)


# 2. Print Numbers Whose First and Last Digits Are the Same 
# Problem Definition: A number may begin and end with the same digit. 
# Task: Read N. Print all numbers from 1 to N whose first and last digits are the same. 
# Example Input: 25 
# Example Output: 1 2 3 4 5 6 7 8 9 11 22

n=int(input())
for i in range(1,n+1):
    temp=i
    rem=temp%10
    last=rem
    first=0
    while temp>10:
        rem=temp%10
        temp//=10
    first=temp
    if first==last:
        print(i)


# 3. Count Numbers Having More Factors Than 4 
# Problem Definition: Some numbers have many factors. 
# Task: Read N. Count how many numbers from 1 to N have more than 4 factors. 
# Example Input: 15 
# Example Output: 5

n=int(input())
count=0
for i in range(1,n+1):
    f_count=0
    for j in range(1,i+1):
        if i%j==0:
            f_count+=1
    # print(f_count)
    if f_count>4:
        count+=1
print(count)


# 4. Print Numbers Whose Product of Digits is Even 
# Problem Definition: The product of a number's digits can classify it. 
# Task: Read N. Print all numbers from 1 to N whose product of digits is even. 
# Example Input: 15
# Example Output: 2 4 6 8 12 14 15

n=int(input())
for i in range(1,n+1):
    temp=i
    prd=1
    while temp>0:
        rem=temp%10
        prd*=rem
        temp//=10
    if prd%2==0:
        print(i,end=" ")


# 5. Count Numbers Ending with an Even Digit 
# Problem Definition: The last digit determines whether a number ends evenly. 
# Task: Read N. Count how many numbers from 1 to N end with an even digit. 
# Example Input: 20 
# Example Output: 10

n=int(input())
count=0
for i in range(1,n+1):
    temp=i
    rem=temp%10
    if rem==0 or rem%2==0:
        count+=1
print(count)


# 6. Find the Greatest Common Factor of Three Numbers 
# Problem Definition: A common factor can exist among three numbers. 
# Task: Read three numbers and print their greatest common factor. 
# Example Input: 24 36 60 
# Example Output: 12

n1=int(input())
n2=int(input())
n3=int(input())
smallest=0
if n1<n2 and n1<n3:
    smallest=n1
elif n2<n3 and n2<n1:
    smallest=n2
else:
    smallest=n3
for i in range(smallest,0,-1):
    if n1%i==0 and n2%i==0 and n3%i==0:
        print(i)
        break



# 7. Print Numbers Whose Digit Sum is Greater Than 10 
# Problem Definition: The sum of digits can be compared against a limit. 
# Task: Read N. Print all numbers from 1 to N whose digit sum is greater than 10. 
# Example Input: 30 Example Output: 29 30 

n=int(input())
for i in range(1,n+1):
    temp=i
    sum=0
    while temp>0:
        rem=temp%10
        sum+=rem
        temp//=10
    if sum>10:
        print(i)


# 8. Count Numbers That Have Exactly Two Even Digits 
# Problem Definition: Compare even and odd digits. 
# Task: Read N numbers and count how many contain exactly two even digits. 
# Example Input: 4 248 357 4821406 
# Example Output: 3 

n=int(input())
e_count=0
for i in range(n):
    nums=int(input())
    count=0
    temp=nums
    while temp>0:
        rem=temp%10
        if rem%2==0:
            count+=1
        temp//=10
    if count==2:
        e_count+=1
print(e_count)
        

# 9. Print Factors That Are Multiples of 3 
# Problem Definition: Filter factors divisible by 3. 
# Task: Read a number and print all factors that are multiples of 3. 
# Example Input: 36 
# Example Output: 3 6 9 12 18 36 

n=int(input())
for i in range(1,n+1):
    if n%i==0:
        if i%3==0:
            print(i)

# 10. Read Numbers Until the Product Exceeds 500 
# Problem Definition: A loop can stop based on the running product. 
# Task: Keep reading numbers until the product exceeds 500 and print the final product. 
# Example Input: 2 5 8 7 
# Example Output: 560

prd=1
while True:
    num=int(input())
    prd*=num
    if prd>500:
        print(prd)
        break