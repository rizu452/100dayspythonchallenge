# 1. Digit Mirror Sum
# Task: Given a number, add digits from opposite ends and store the results. If one digit remains in
# the middle, keep it as it is.
# Example Input:
# Input: 48391
# Calculation:
# 4+1=5
# 8+9=17
# 3 stays as it is
# Example Output:
# Output: [5,17,3]
                                #1 2 3 4 5
# def mirrorsum(number):  
#     number = 48391
#     digits = []
#     output=[]
#     for i in str(number):
#         digits += [int(i)]
#     # print(digits)
#     left=0
#     right=len(digits)-1         # 4 8 3 9 1
#     while left<=right:           # 0<=4 , 1<=3 , 2<=2
#         if left==right:             #0!=4 ,1!3 , 2==2
#             output+=[digits[left]]    #
#             # print(output)
#         else:
#             sum=digits[left]+digits[right]  #4+1 , 8+9
#             output+=[sum]                   #5 ,17
#             # print(output)
#         left+=1                             # 1 2
#         right-=1                            #3  2
#     print(output)
# mirrorsum(48391)


# 2. Lonely Digit Finder
# Task: Find the digit that appears exactly once in a number.
# Example Input:
# Input: 122334455
# Example Output:
# Output: 1

# def lonelynumber(number):
#     temp=number
#     digits=[]
#     count=0
#     counting=[]
#     for i in str(temp):
#         digits+=[int(i)]
#     for i in digits:
#         if i in counting:
#             count+=1
#             continue
#         for j in digits:
#             if i==j:
#                 counting+=[i]
#             count+=1
#         if count==1:
#                 print(f"{i}")

# lonelynumber(1223344556)

# 3. Mountain Number Checker
# Task: Check whether digits strictly increase and then strictly decrease.
# Example Input:
# Input: 123454321
# Example Output:
# Output: True
# Input: 123456
# Output: False

# def mountainnumber(number):
#     digits=[]
#     for i in str(number):
#         digits+=[int(i)]
#     # print(digits)
#     i=0
#     while i<len(digits)-1:
#         if digits[i]<digits[i+1]:
#             i+=1
#         else:
#             break
#     # print("peak = ",i)
#         # elif digits[i]>digits[i+1]:
#         #     break
#     j=len(digits)-1
#     while j>0:
#         if digits[j]<digits[j-1]:
#             j-=1
#         else:
#             break
#     # print("reached = ",j)
#     if i == j and i != 0 and i != len(digits)-1:
#         print("Mountain Number")
#     else:
#         print("Not a Mountain Number")
# mountainnumber(12345)


# 4. Circular Digit Rotation Maximum
# Task: Generate all circular rotations of a number and return the largest rotation.
# Example Input:
# Input: 1973
# Rotations:
# 1973
# 9731
# 7319
# 3197
# Example Output:
# Output: 9731

# def digitrotation(number):
#     digits=[]
#     for i in str(number):
#         digits+=[int(i)]
#     # print(digits)
#     # temp=""
#     # digits1=[]
#     i=0
#     while i<len(digits):
#         temp=""
#         digits1=[]
#         for j in range(-1,len(digits)-1):
#             temp=temp+str(digits[j])
#             digits1+=[digits[j]]
#         temp=int(temp)
#         # print(digits1)
#         print(temp)
#         i+=1
#         digits=digits1
# digitrotation(1973)

# 5. Digit Distance Sum
# Task: Find the sum of absolute differences between neighboring digits.
# Example Input:
# Input: 82746
# |8-2| + |2-7| + |7-4| + |4-6|
# Example Output:
# Output: 18

# def digitdistance(number):
#     digits=[]
#     diff=0
#     sum=0
#     for i in str(number):
#         digits+=[int(i)]
#     for i in range(len(digits)-1):
#         diff=digits[i]-digits[i+1]
#         # print(diff)
#         if diff<0:
#             diff=-diff
#             # print(diff)
#         sum=sum+diff
#     print(sum)
# digitdistance(82746)


# 6. Hidden Pair Product
# Task: Multiply each pair of neighboring digits and combine the results into one number.
# Example Input:
# Input: 2345
# 2×3=6
# 3×4=12
# 4×5=20
# Example Output:
# Output: 61220

# def hiddenproduct(number):
#     # product=[]
#     digits=[]
#     final=""
#     for i in str(number):
#         digits+=[int(i)]
#     for i in range(len(digits)-1):
#         prdct=digits[i]*digits[i+1]
#         # product+=[prdct]
#         # print(product)
#     final=final+str(prdct)
#     final=int(final)
#     print(int(final))
# hiddenproduct(2345)


# 7. Digit Wave Number
# Task: Check whether digits form a wave pattern:
# 1st < 2nd
# 2nd > 3rd
# 3rd < 4th and so on
# Example Input:
# Input: 163849
# 1<6
# 6>3
# 3<8                           1 6 3 8 4 9
# 8>4
# 4<9
# Example Output:
# Output: True

# def wavenumber(number):
#     digits=[]
#     for i in str(number):
#         digits+=[int(i)]
#     i=0
#     number=True
#     while i<len(digits)-2:
#         if digits[i]<digits[i+1]>digits[i+2] or digits[i]>digits[i+1]<digits[i+2]:
#             # print(digits[i],digits[i+1])
#             pass
#         else:
#             number=False
#             break
#         i+=1
#     if number:
#         print("wave number")
#     else:
#         print("not wave number")
# wavenumber(163849)

# 8. Number DNA Match
# Task: Given two numbers of equal length, count how many digits match in the same positions.
# Example Input:
# Input:
# 123456
# 153406
# Example Output:
# Output: 4

# def dnanumber(number1,number2):
#     digits1=[]
#     digits2=[]
#     for i in str(number1):
#         digits1+=[int(i)]
#     for j in str(number2):
#         digits2+=[int(j)]
#     count=0
#     for i in range(len(digits1)):
#         # for j in range(len(digits2)):
#             if  digits1[i]==digits2[i]:
#                 count+=1
#             else:
#                 continue
#     print(count)
# dnanumber(123456,153406)


# 9. Prime Gap Digit Number
# Task: Find absolute differences between adjacent digits and check whether all differences are
# prime numbers.
# Example Input:
# Input: 1638
# Differences:
# |1-6|=5
# |6-3|=3
# |3-8|=5
# Example Output:
# Output: True


# def gapdigit(number):
#     digits=[]
#     for i in str(number):
#         digits+=[int(i)]
#     diff=0
#     for i in range(len(digits)-1):
#         diff=digits[i]-digits[(i+1)]
#         if diff<0:
#             diff=-diff
#         print(diff)
#         temp=2
#         prime=True
#         if diff<=1:
#             return False
#             break
#         while temp<diff:
#             if diff%temp==0:
#                 prime=False
#                 break
#             temp+=1
#         if not prime:
#             return False
# print(gapdigit(16388))


