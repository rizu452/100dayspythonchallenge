# Basic Unique Number Problems in Python
# 1. Sum of First and Last Digit
# Task: Given a number, find the sum of its first digit and last digit.
# Example Input: Number = 58392
# Example Output: First digit = 5, Last digit = 2, Sum = 7

# def sumoffirstandlast(number):
#     sum=0
#     i=0
#     number=str(number)
#     while i<len(number):
#         # print(number[i])
#         if i==0 or i==len(number)-1:
#             sum=sum+int(number[i])
#         i+=1
#     print(f"first digit={int(number[0])},last digit={int(number[i-1])},sum={sum}")
# sumoffirstandlast(58392)

# 2. Count Digits Greater Than 5
# Task: Count digits in a number that are greater than 5.
# Example Input: Number = 836921
# Example Output: Digits greater than 5 = 4

# def countdigits(number):
#     count=0
#     number=str(number)
#     i=0
#     while i<len(number):
#         if int(number[i])>5:
#             count+=1
#         i+=1
#     print(f"count={count}")
# countdigits(836921)


# 3. Product of Digits at Odd Positions
# Task: Find product of digits present at odd positions from right side.
# Example Input: Number = 58294
# Example Output: Product = 64

# def productofodddigits(number):
#     product=1
#     number=str(number)
#     i=-1
#     while i>=-len(number):
#         if i%2!=0:
#             print(i)
#             product*=int(number[i])
#         i-=1
#     print(f"product={product}")
# productofodddigits(58294)

# 4. Largest Digit Difference
# Task: Find difference between largest and smallest digit.
# Example Input: Number = 58392
# Example Output: Largest = 9, Smallest = 2, Difference = 7

# def largestdigit(number):
#     difference=0
#     number=str(number)
#     i=0
#     largest=0
#     smallest=int(number[0])
#     while i<len(number):
#         if int(number[i])>largest :
#             largest=int(number[i])
#         elif int(number[i])<smallest:
#             smallest=int(number[i])
#         i+=1
#         difference=largest-smallest
#     print(largest)
#     print(smallest)
#     print(difference)
# largestdigit(58392)



# 5. Count Even and Odd Digits
# Task: Count even and odd digits in a number.
# Example Input: Number = 58392
# Example Output: Even digits = 2, Odd digits = 3


# def evenoddcount(number):
#     even=0
#     odd=0
#     i=0
#     number=str(number)
#     while i<len(number):
#         if int(number[i])%2==0:
#             even+=1
#         else:
#             odd+=1
#         i+=1
#     print(even)
#     print(odd)
# evenoddcount(58392)


# 6. Reverse Number Without Changing Middle Digit
# Task: Reverse first and last digits while keeping middle digits unchanged.
# Example Input: Number = 12345
# Example Output: Result = 52341


# def reversedigit(number):
#     list=[]
#     for i in str(number):
#         list=list+[i]
#     print(list)
#     for i in list:
#         list[0],list[-1]=list[-1],list[0]
#     print(list)
#     number=""
#     for i in list:
#         number+=i
#     number=int(number)
#     print(number)
# reversedigit(12345)


# 7. Digit Sum Until Single Digit
# Task: Add digits repeatedly until one digit remains.
# Example Input: Number = 9876
# Example Output: Final Result = 3

# def digitsum(number):
#     sum=0
#     for i in str(number):
#         sum+=int(i)
#     print(sum)
#     # sum=str(sum)
#     sum1=0
#     for i in str(sum):
#         sum1+=int(i)
#     print(sum1)
# digitsum(9876)


# 8. Second Largest Digit
# Task: Find the second largest digit in a number.
# Example Input: Number = 58392
# Example Output: Largest = 9, Second largest = 8

# def secondlargest(number):
#     number=str(number)
#     largest=0
#     secondlargst=0
#     for i in number:
#         if int(i)>largest:
#             secondlargest=largest
#             largest=int(i)
#             # secondlargest=largest
#     print(secondlargest)
# secondlargest(58392)


# 9. Replace Zero Digits
# Task: Replace all zero digits with 9.
# Example Input: Number = 102030
# Example Output: Result = 192939

# def replace(number):
#     number=str(number)
#     i=0
#     i1=9
#     number1=""
#     for i in number:
#         if int(i)==0:
#             i=int(i)+i1
#             number1+=str(i)
#         else:
#             number1+=i
#     print(int(number1))
# replace(102030)

# 10. Digit Position Finder
# Task: Find position of a digit in a number from right side.
# Example Input: Number = 58392, Digit = 3
# Example Output: Position = 3

# def position(number):
#     number=str(number)
#     count=1
#     digit=int(input())
#     i=-1
#     while i>=-len(str(number)):
#         if int(number[i])==digit:
#             print(count)
#         else:
#             count+=1
#         i-=1
# position(58392)