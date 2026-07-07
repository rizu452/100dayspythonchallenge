# 1. Count Even Numbers
# Write a function that returns the number of even numbers in a list.
# Example
# Input: [2, 5, 8, 11, 14]
# Output: 3

# def counteven(*numbers):
#     count=0
#     for num in numbers:
#         if num%2==0:
#             count+=1
#     return count
# print(counteven(2,5,8,11,14,15,32,66,88))

# 2. Find the Largest Element
# Return the largest element in a list.
# Example
# Input: [12, 45, 7, 89, 23]
# Output: 89

# def largestelement(*numbers):
#     largest=0
#     for num in numbers:
#         if num>largest:
#             largest=num
#     return largest
# print(largestelement(12,45,7,89,23))

# 3. Find the Smallest Element
# Return the smallest element in a list.
# Example
# Input: [12, 45, 7, 89, 23]
# Output: 7

# def smallestelement(*numbers):
#     smallest=numbers[0]
#     for num in numbers:
#         if num<smallest:
#             smallest=num
#     return smallest
# print(smallestelement(12,45,7,89,23))

# 4. Reverse a List
# Return the list in reverse order.
# Example
# Input: [1, 2, 3, 4, 5]
# Output: [5, 4, 3, 2, 1]

# def reverselist():
#     list=[1,2,3,4,5]
#     list1=[]
#     for i in list:
#         list1=[i]+list1
#     print(list1)
# reverselist()


# 5. Sum of All Elements
# Return the sum of all numbers in the list.
# Example
# Input: [4, 8, 10]
# Output: 22

# def sumofelements(*numbers):
#     sum=0
#     for num in numbers:
#         sum+=num
#     print(sum)
# sumofelements(4,8,10)


# 6. Count Occurrences
# Count how many times a target appears.
# Example
# Input: List=[1,2,3,2,4,2], Target=2
# Output: 3

# def occurrences():
#     numbers=[1,2,3,2,4,2]
#     target=int(input("enter a target number"))
#     count=0
#     for num in numbers:
#         if num==target:
#             count+=1 
#     print(count)
# occurrences()

# 7. Remove Duplicates
# Remove duplicates while preserving order.
# Example
# Input: [1,2,2,3,1,4]
# Output: [1,2,3,4]

# def remvdup():
#     list=[1,2,2,3,1,4]
#     list1=[]
#     for i in list:
#         if i in list1:
#             continue
#         else:
#             list1=list1+[i]
#     print(list1)
# remvdup()

# 8. Find the Average
# Return the average of all numbers.
# Example
# Input: [10,20,30,40]
# Output: 25.0

# def average(*numbers):
#     sum=0
#     count=0
#     for num in numbers:
#         sum+=num
#         count+=1
#     avg=sum/count
#     print(avg)
# average(10,20,30,40)

# 9. Create a List of Squares
# Return a new list containing the square of every element.
# Example
# Input: [2,3,4,5]
# Output: [4,9,16,25]

# def listofsqrs():
#     list=[2,3,4,5]
#     list1=[]
#     for i in list:
#         sqr=i*i
#         list1=list1+[sqr]
#     print(list1)
# listofsqrs()

# 10. Count Positive Numbers
# Return the number of positive numbers.
# Example
# Input: [-2,5,0,7,-1,9]
# Output:3

# def cntpositive(*numbers):
#     count=0
#     for num in numbers:
#         if num>0:
#             count+=1
#     print(count)
# cntpositive(-2,5,0,7,-1,9)


