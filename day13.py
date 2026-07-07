# 1. Count Total Keys
# Task:
# Write a function that returns the total number of keys in a dictionary.
# Example Input:
# {"a":10,"b":20,"c":30}
# Example Output:
# 3

# def totalkeys(**dictionary):
#     count=0
#     for i in dictionary:
#         count+=1
#     print(count)
# totalkeys(a=10,b=20,c=30)

# 2. Find the Key with the Largest Value
# Task:
# Return the key whose value is the largest.
# Example Input:
# {"Math":78,"Science":92,"English":85}
# Example Output:
# Science

# def largestvalue(**marks):
#     largest=0
#     subject=""
#     for mark in marks:
#         if marks[mark]>largest:
#             largest=marks[mark]
#             subject=mark
#     print(subject)
# largestvalue(math=78,science=92,english=85)


# 3. Find the Key with the Smallest Value
# Task:
# Return the key whose value is the smallest.
# Example Input:
# {"Math":78,"Science":92,"English":65}
# Example Output:
# English

# def smallestmark(**marks):
#     smallest=100
#     subject=""
#     for mark in marks:
#         if marks[mark]<smallest:
#             smallest=marks[mark]
#             subject=mark
#     print(subject)
# smallestmark(math=78,science=92,english=65)


# 4. Sum of All Values
# Task:
# Return the sum of all values in the dictionary.
# Example Input:
# {"Pen":20,"Book":150,"Bag":500}
# Example Output:
# 670

# def sumofvalues(**values):
#     sum=0
#     for value in values:
#         sum+=values[value]
#     print(sum)
# sumofvalues(pen=20,book=150,bag=500)


# 5. Count Even Values
# Task:
# Return how many values in the dictionary are even.
# Example Input:
# {"a":10,"b":7,"c":16,"d":5}
# Example Output:
# 2

# def evencount(**values):
#     count=0
#     for value in values:
#         if values[value]%2==0:
#             count+=1
#     print(count)
# evencount(a=10,b=7,c=16,d=5)


# 6. Count Values Greater Than a Target
# Task:
# Given a target number, count how many dictionary values are greater than it.
# Example Input:
# Dictionary={"A":45,"B":80,"C":65,"D":90}
# Target=70
# Example Output:
# 2

# def greatestvalue(**values):
#     count=0
#     target=int(input("enter target"))
#     for value in values:
#         if values[value]>target:
#             count+=1
#     print(count)
# greatestvalue(a=45,b=80,c=65,d=90)


# 7. Create a Dictionary of Squares
# Task:
# Given a list of numbers, create a dictionary where the number is the key and its square is the value.
# Example Input:
# [2,3,4,5]
# Example Output:
# {2:4,3:9,4:16,5:25}

# def dectsqr(*values):
#     sqr=0
#     dict={}
#     for value in values:
#         sqr=value*value
#         dict[value]=sqr
#     print(dict)
# dectsqr(2,3,4,5)


# 8. Count Positive Values
# Task:
# Return the number of positive values in the dictionary.
# Example Input:
# {"a":-5,"b":10,"c":0,"d":8}
# Example Output:
# 2

# def countpositive(**values):
#     count=0
#     for value in values:
#         if values[value]>0:
#             count+=1
#     print(count)
# countpositive(a=-5,b=10,c=0,d=8)


# 9. Find the Average of All Values
# Task:
# Return the average of all values in the dictionary.
# Example Input:
# {"A":10,"B":20,"C":30}
# Example Output:
# 20.0

# def averageofvalues(**values):
#     sum=0
#     count=0
#     for value in values:
#         sum+=values[value]
#         count+=1
#     avg=sum/count
#     print(avg)
# averageofvalues(a=10,b=20,c=30)


# 10. Reverse Key and Value
# Task:
# Create a new dictionary where the values become keys and the keys become values.
# Example Input:
# {"A":1,"B":2,"C":3}
# Example Output:
# {1:"A",2:"B",3:"C"}

# def reversekey(**values):
#     rev={}
#     for value in values:
#         rev[values[value]]=value
#     print(rev)
# reversekey(a=1,b=2,c=3)