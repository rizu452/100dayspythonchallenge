# Problem 1: Find the Largest Digit in a Number 
# Task: Given a positive integer, find its largest digit using recursion. 
# Example Input: 583921 
# Example Output: Output: 9

# def largest(num,l=0):
#     if num==0:
#         return l
#     else:
#         rem=num%10
#         if rem>l:
#             l=rem
        
#         return largest(num//10,l)
# print(largest(583921))
# # print(largest(60328417))

# Problem 2: Count Occurrences of a Digit 
# Task: Given a number and a digit, count how many times the digit appears using recursion. 
# Example Input: I
# nput: Number = 7878787 Digit = 7 
# Example Output: Output: 4

# def occurrences(num,c=0):
#     if num==0:
#         return c
#     else:
#         # rem=num%10
#         # if rem==target:
#         #     c+=1
#         return occurrences(num//10,c+1 if num%10==target else c)
# target=int(input('enter a number :'))
# print(occurrences(7878787))

# Problem 3: Check if a Number is a Palindrome 
# Task: Determine whether a given integer is a palindrome using recursion (without converting it to a string). 
# Example Input: 
# Input: 12321 
# Example Output: Output: Palindrome

# def palindrome(num,org,rev=0):
#     if num==0:
#         return 'palindrome' if rev==org else 'not a palindrome'
#     else:
#         digit=num%10
#         rev=rev*10+digit
#         return palindrome(num//10,org,rev)

# print(palindrome(12321,12321))
# print(palindrome(12345,12345))
# print(palindrome(10301,10301))
# print(palindrome(7,7))

# Problem 4: Print Digits from Left to Right 
# Task: Print each digit of a number from left to right using recursion. 
# Example Input: 
# Input: 4825 
# Example Output: 
# Output: 4 8 2 5

# def digitprint(num,rev=0):
#     if num==0:
#         return rev
#     else:
#         return digitprint(num//10),print(num%10,end=' ')

# digitprint(4825)
    

# Problem 5: Find the Product of Digits 
# Task: Find the product of all digits in a number using recursion. 
# Example Input: 
# Input: 2345 
# Example Output: 
# Output: 120

def product(num,prd=1):
    if num==0:
        return prd
    else:
        prd*=num%10
        return product(num//10,prd)
    
print(product(2345))