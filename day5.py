# 1. Find Common Elements Between Two Lists
# Given:
# a=[4,7,2,9,1]
# b=[8,2,1,6,4]
# Explanation: Compare each element of first list with every element of second list using nested
# loops. Print common values and avoid duplicates.
# Expected Output:
# 4
# 2
# 1

# a=[4,7,2,9,1]
# b=[8,2,1,6,4]
# for i in range(len(a)):
#     for j in range(len(b)):
#         if a[i]==b[j]:
#             print(a[i])
#         else:
#             continue

# 2. Find First Pair with Target Sum
# Given:
# arr=[2,5,7,9,1,4]
# target=11
# Explanation: Compare each element with all remaining elements and stop immediately after finding
# first matching pair.
# Expected Output:
# 2 9

# arr=[2,5,7,9,1,4]
# target=11
# for i in arr:
#     for j in arr:
#         if i+j==target:
#             print(f"{i}  {j}")
#         break


# 3. Frequency Count Without count()
# Given:
# arr=["apple","banana","apple","orange","banana","apple"]
# Explanation: Count occurrences manually using nested loops without dictionary or count().
# Expected Output:
# apple : 3
# banana : 2
# orange : 1

# arr=['apple','banana','apple','orange','banana','apple']
# a=[]
# for i in range(len(arr)):
#     if arr[i] in a:
#         continue
#     count=0
#     for j in range(len(arr)):
#         # print(arr[i],arr[j])
#         if arr[i]==arr[j]:
#             count+=1
#     print(f"{arr[i]} = {count}")
#     a.append(arr[i])


# 4. Find Duplicate Strings
# Given:
# names=["Raj","John","Raj","Mike","John","Raj"]
# Explanation: Traverse and identify repeated strings. Print duplicates once only.
# Expected Output:
# Raj
# John

# arr=['raj','john','raj','mike','john','raj']
# a=[]
# for i in range(len(arr)):
#     if arr[i] in a:
#         # print(f"{arr[i]}"
#         continue
#     count=0
#     for j in range(len(arr)):
#         if arr[i]==arr[j]:
#             # a.append(arr[i])
#             count+=1
#     a.append(arr[i])
#     # print(f"{arr[i]} = {count}")
#     if count>1:
#         print(f"{arr[i]}")


# 5. Matrix Equality Check
# Given:
# m1=[[1,2,3],[4,5,6]]
# m2=[[1,2,3],[4,5,6]]
# Explanation: Compare every row and column value.
# Expected Output:
# Matrices are equal

# m1=[[1,2,3],[4,5,6]]
# m2=[[1,2,3],[4,5,6]]
# for i in range(len(m1)):
#     for j in range(len(m1[i])):
#         if m1[i][j]==m2[i][j]:
#             pass
# print("matrices are equal")


# 6. Find Missing Elements Between Two Lists
# Given:
# a=[1,2,3,4,5,6]
# b=[2,4,6]
# Explanation: Print values from first list that do not exist in second list.
# Expected Output:
# 1
# 3
# 5

# a=[1,2,3,4,5,6]
# b=[2,4,6]
# for i in range(len(a)):
#         if a[i] in b:
#             continue
#         print(f"{a[i]}")


# 7. Longest Matching Consecutive Characters
# Given:
# s1="ABCDXYZEF"
# s2="XYZABCDPQ"
# Explanation: Find longest consecutive matching sequence using nested loops.
# Expected Output:
# 4

# s1="ABCDXYZEF"
# s2="XYZABCDPQ"
# count=0
# for i in range(len(s1)):
#     for j in range(len(s2)):
#         if i<len(s1) and j<len(s2):
#             if s1[i]==s2[i]:
#                 count+=1
#     print(f"{count}")

