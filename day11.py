# 1. Count Total Vowels
# Task: Write a function that takes a string and returns the total number of vowels (a, e, i, o, u).
# Example Input:
# programming
# Example Output:
# Total Vowels = 3

# def countvowel(string):
#     count=0
#     vowel=[]
#     vowels=["a","e","i","o","u","A","E","I","O","U"]
#     for i in string:
#         vowel+=i
#     # print(vowel)
#     for i in vowel:
#         if i in vowels:
#             count+=1
#         else:
#             continue
#     print(f"Total vowels = {count}")

# countvowel("programming")


# 2. Count Total Consonants
# Task: Write a function that takes a string and returns the total number of consonants.
# Example Input:
# python
# Example Output:
# Total Consonants = 5

# def consonants(string):
#     count=0
#     cons=[]
#     vowels=["a","e","i","o","u","A","E","I","O","U"]
#     for i in string:
#         cons+=i
#     for i in cons:
#         if i not in vowels:
#             count+=1
#         else:
#             continue
#     print(f"Total consonants = {count}")
# consonants("python")

# 3. Reverse a String
# Task: Write a function that takes a string and returns the string in reverse order.
# Example Input:
# computer
# Example Output:
# Reversed String = retupmoc

# def reversestring(string):
#     rev=""
#     for i in string:
#         rev=i+rev
#     print(f"Reversed string = {rev}")
# reversestring("computer")

# 4. Count Uppercase and Lowercase Letters
# Task: Write a function that takes a string and returns the number of uppercase and lowercase
# letters.
# Example Input:
# PyThOn
# Example Output:
# Uppercase = 3
# Lowercase = 3

# def upperlower(string):
#     upper=0
#     lower=0
#     for i in string:
#         if 65<=ord(i)<=90:
#             upper+=1
#         elif 97<=ord(i)<=122:
#             lower+=1
#         else:
#             continue
#     print(f"upper = {upper}")
#     print(f"lower = {lower}")
# upperlower("pYThOn1")


# 5. Count Digits in a String
# Task: Write a function that takes a string and returns how many digits are present.
# Example Input:
# abc12345xy
# Example Output:
# Digits = 5

# def countdigits(string):
#     count=0
#     for i in string:
#         if 65<=ord(i)<=90 or 97<=ord(i)<=122:
#             continue
#         else:
#             count+=1
#     print(f"digits = {count}")
# countdigits("abc12345xy")

# 6. Check Palindrome
# Task: Write a function that takes a string and checks whether it is a palindrome.
# Example Input:
# madam
# Example Output:
# Palindrome

# def palindrome(string):
#     rev=""
#     for i in string:
#         rev=i+rev
#     if rev==string:
#         print(f"{string} is a palindrome")
#     else:
#         print(f"{string} is not a palindrome")
# palindrome("refer")

# 7. Count Occurrences of a Character
# Task: Write a function that takes a string and a character and returns how many times that
# character appears.
# Example Input:
# banana
# a
# Example Output:
# Occurrences = 3

# def occurrence():
#     string=input("enter a string : ")
#     char=input("enter a char to count how many times it occurs in string : ")
#     list=[]
#     count=0
#     for i in string:
#         list+=i
#     for i in list:
#         if i==char:
#             count+=1
#     print(f"occurences = {count}")
#     # print(list)
# occurrence()

# 8. Find the Longest Word
# Task: Write a function that takes a sentence and returns the longest word.
# Example Input:
# Python is an amazing language
# Example Output:
# Longest Word = language

# def longest():
#     sentence=input("enter a sentence : ")
#     words=sentence.split()
#     longest=""
#     for word in words:
#         if len(word)>len(longest):
#             longest=word
#     print(f"longest word is {longest}")
# longest()

# 9. Remove All Spaces
# Task: Write a function that takes a sentence and returns the same sentence after removing all
# spaces.
# Example Input:
# Data Science is fun
# Example Output:
# DataScienceisfun

# def spaceremove():
#     sentence=input("enter a sentence : ")
#     words=sentence.split()
#     temp=""
#     for word in words:
#         temp+=word
#     print(f"{temp}")
# spaceremove()


# 10. Count Words in a Sentence
# Task: Write a function that takes a sentence and returns the total number of words.
# Example Input:
# Learning Python is very interesting
# Example Output:
# Total Words = 5


# def countwords():
#     sentence=input("enter a sentence : ")
#     words=sentence.split()
#     count=0
#     for word in words:
#         count+=1
#     print(count)
# countwords()

# --------------------------------------------ADVANCED QUESTIONS----------------------------------------------------------------------

# 1. Compress Consecutive Characters
# Task: Write a function that compresses consecutive repeated characters. Store each character
# followed by its count.
# Example Input:
# aaabbccccdaa
# Example Output:
# a3b2c4d1a2

# def consecutive(string):
#     count=1
#     # string=input("enter a sentence : ")
#     for i in range(len(string)-1):
#         if string[i]==string[i+1]:
#             count+=1
#         else:
#             print(string[i],count)
#             count=1
#     print(f"{string[i]}{count}")
# consecutive("aaabbccccdaa")

# 2. First Non-Repeating Character
# Task: Write a function that returns the first character that appears only once in the string.
# Example Input:
# aabbcddeff
# Example Output:
# First Non-Repeating Character = c

# def nonrepeat(string):
#     count=1
#     for i in range(len(string)):
#         count=0
#         for j in range(len(string)):
#             if string[i]==string[j]:
#                 count+=1
#         if count==1:
#             print(f"{string[i]}")
#             return
#     print("no non repeating character found")
# nonrepeat("aabbcddeff")

# 3. Longest Word in a Sentence
# Task: Write a function that finds the longest word without using split().
# Example Input:
# Python programming improves logical thinking
# Example Output:
# Longest Word = programming

# def longestword(sentence):
#     words=""
#     longest=""
#     for word in sentence:
#         if word!=" ":
#             words+=word
#         # print(words)
#         else:
#             if len(words)>len(longest):
#                 longest=words
#             words=""
#     if len(words)>len(longest):
#         longest=words
#     print(longest)
# longestword("python programming improves logical thinking")

# 4. Remove Duplicate Characters
# Task: Write a function that removes duplicate characters while keeping only their first occurrence.
# Example Input:
# programming
# Example Output:
# progamin

# def removeduplicate(string):
#     word=""
#     for i in range(len(string)):
#         count=0
#         for j in range(len(string)):
#             if i==j and string[i] not in word:
#                 word+=string[i]
#     print(word)
# removeduplicate("programming")

