# 1. Merge Two Sorted Lists
# Given two lists already sorted in ascending order, create a new sorted list by comparing elements
# one by one. Do not use sort(), append(), extend(), or slicing.
# Input
# List1=[1,4,7,10]
# List2=[2,3,8,9]
# Output
# [1,2,3,4,7,8,9,10]

# def Mergesortedlist():
#     list1=[1,4,7,10]                #7
#     list2=[2,3,8,9]                 #8
#     list3=[]
#     for i in list1:
#         for j in list2:
#             #print(i,j)
#             if i in list3 :
#                 continue
#             elif j in list3:
#                 continue
#             elif i < j:
#                 list3+=[i]              #10
#                 break
#             elif j<i:                   #9
#                 list3+=[j]
#             else:
#                 list3+=[i]
#     for i in list1:
#         if i not in list3:
#             list3+=[i]
#     for j in list2:
#         if j not in list3:
#             list3+=[j]
#     print(list3)
# Mergesortedlist()

# 2. Find the Second Largest Number
# Given a list of integers, find the second largest distinct number without using sort(), max(), or min().
# Input
# [12,45,67,23,89,54]
# Output
# 67

# def second_largest():
#     list=[12,45,67,23,89,54]
#     highest=0
#     for i in list:
#         if i >highest:
#             secondlargest=highest
#             highest=i
#     print(f"second largest is {secondlargest}")
# second_largest()


# 3. Tuple Frequency Counter
# Given a tuple, count how many times each element appears and store the result in a dictionary. Do
# not use count().
# Input
# (2,5,2,8,5,5)
# Output
# {2:2, 5:3, 8:1}

# def tuplefrequencycounter():
#     tup=(2,5,2,8,5,5)
#     freq={}
#     for i in tup:
#         if i in freq:
#             freq[i]+=1
#         else:
#             freq[i]=1
#     for key,value in freq.items():
#         print(f"{key} : {value}")
# tuplefrequencycounter()

# 4. Dictionary Value Sum
# Given a dictionary whose values are integers, calculate the total of all values manually. Do not use
# sum().
# Input
# {'A':10,'B':20,'C':30}
# Output
# 60

# def dectionarysum():
#     data={'A':10,'B':20,'C':30}
#     sum=0
#     for i in data:
#         sum+=data[i]
#     print("sum is : ",sum)
# dectionarysum()

# 5. Unique Elements from Two Lists
# Print elements that occur in only one list. Do not use sets.
# Input
# List1=[1,2,3,4]
# List2=[3,4,5,6]
# Output
# 1 2 5 6

# def uniqueelements():
#     list1=[1,2,3,4]
#     list2=[3,4,5,6]
#     for i in list1:
#         if i not in list2:
#             print(i,end=' ')
#     for j in list2:
#         if j not in list1:
#             print(j,end=' ')
# uniqueelements()

# 6. Student Marks Analysis
# Store student names and marks in a dictionary. Find the highest scorer, lowest scorer, and average
# marks manually.
# Input
# {'John':78,'Rahul':92,'Priya':85,'Anu':65}
# Output
# Highest: Rahul-92
# Lowest: Anu-65
# Average: 80

# def student_analysis():
#     data={'john':78,'rahul':92,'priya':85,'anu':65}
#     highest = 0
#     lowest = list(data.values())[0]
#     h_name = ""
#     l_name = ""
#     total = 0
#     for name, marks in data.items():
#         if marks > highest:
#             highest = marks
#             h_name = name
#         if marks < lowest:
#             lowest = marks
#             l_name = name
#         total += marks
#     average = total / len(data)
#     print("Highest:", h_name, "-", highest)
#     print("Lowest:", l_name, "-", lowest)
#     print("Average:", average)
# student_analysis()

# 7. Remove Duplicate Tuples
# Given a list of tuples, print only unique tuples while keeping the original order. Do not use set().
# Input
# [(1,2),(3,4),(1,2),(5,6),(3,4)]
# Output
# [(1,2),(3,4),(5,6)]


# def duplicate():
#     data=[(1,2),(3,4),(1,2),(5,6),(3,4)]
#     data2=[]
#     for i in data:
#         # print(i,end='')
#         if i in data2:
#             continue
#         else:
#             data2+=[i]
#         print(i)
# duplicate()

# 8. Word Frequency Counter
# Given a list of words, count occurrences of each word and store them in a dictionary. Do not use
# count() or Counter.
# Input
# ['apple','banana','apple','orange','banana','apple']
# Output
# {'apple':3,'banana':2,'orange':1}

# data=['apple','banana','apple','orange','banana','apple']
# data1=[]
# for i in range(len(data)):
#     if data[i] in data1:
#         count+=1
#         continue
#     count=0
#     for j in range(len(data)):
#         # data1=data[i]
#         if data[i]==data[j]:
#             count+=1
#     data1+=[data[i]]
#     print(data[i] ,":" ,count)



# 9. Check Whether One Set is a Subset
# Determine whether every element of the first set exists in the second set without using issubset().
# Input
# Set1={2,4}
# Set2={1,2,3,4,5}
# Output
# Subset

# def subset():
#     set1={2,4,6}
#     set2={1,2,3,4,5}
#     for i in set1:
#         if i  not in set2:
#             print("not subset")
#             return
#     print("subset")
# subset()


# 10. Inventory Management System
# Create a menu-driven dictionary program. Keys are product names and values are quantities.
# Implement Add, Update, Delete, Search, Display, and Exit options.
# Example Input/Output
# Choice:1 Add Pen 50
# Choice:1 Add Book 20
# Choice:2 Update Pen 75
# Choice:4 Search Pen -> Pen:75
# Choice:5 -> Pen:75 Book:20
# Choice:3 Delete Book
# Choice:5 -> Pen:75
# Choice:6 -> Program exited

def inventorymanagementsystem():
    dictionary={}
    while True:
        print("\n1.Add")
        print("2.update")
        print("3.delete")
        print("4.search")
        print("5.display")
        print("6.exit")
        choice=int(input("select from menu : "))
        if choice==1:
            item=input()
            quantity=int(input())
            dictionary[item]=quantity
            print(f"{dictionary}")
        if choice==2:
            item=input("")
            quantity=int(input())
            if item in dictionary:
                dictionary[item]=quantity
            print(f"{dictionary}")
        if choice==3:
            item=input()
            if item in dictionary:
                del dictionary[item]
                print(f"{dictionary}")
            else:
                print(f"item not found")
        if choice==4:
            item=input()
            if item in dictionary:
                print(f"{item}->{item}:{quantity}")
            else:
                print("item not found")
        if choice==5:
            item=input()
            if item in dictionary:
                print(f"{item}->{item}:{quantity}")
            else:
                print("item not found")
        if choice==6:
            print("program ended")
            break
        else:
            print("invalid choice")
inventorymanagementsystem()