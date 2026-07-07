# 1. Find All Leaders in a List
# Task: An element is a leader if it is greater than every element to its right.
# Example Input:
# Input: [16, 17, 4, 3, 5, 2]
# Example Output:
# Output: [17, 5, 2]

# def leaders():
#     list=[16,17,4,3,5,2]
#     leader=[]
#     for i in range(len(list)):
#         is_leader=True
#         for j in range(i+1,len(list)): 
#             if list[j]>list[i]:
#                 leader+=[list[j]]
#                 is_leader=False
#     print(leader)
# leaders()

# 2. Rearrange Positive and Negative Numbers
# Task: Rearrange the list so positive and negative numbers appear alternately. If one type runs out,
# append the remaining elements.
# Example Input:
# Input: [1, -2, 3, -4, -5, 6, 7]
# Example Output:
# Output: [1, -2, 3, -4, 6, -5, 7]

def rearrangenums():
    list1=[1-2,3,-4,-5,6,7]
    list2=[]
    for i in range(len(list)):
        if list1[i]>0:
           if list1[i+1]<0:
              continue



# 3. Find the Majority Element
# Task: Return the element appearing more than n/2 times. If none exists, return None.
# Example Input:
# Input: [2, 2, 1, 2, 3, 2, 2]
# Example Output:
# Output: 2


# 4. Maximum Difference
# Task: Find the maximum value of arr[j] - arr[i] where j > i.
# Example Input:
# Input: [2, 3, 10, 6, 4, 8, 1]
# Example Output:
# Output: 8



# 5. Equilibrium Index
# Task: Find an index where the sum of elements on the left equals the sum on the right.
# Example Input:
# Input: [1, 3, 5, 2, 2]
# Example Output:
# Output: 2
