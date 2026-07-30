# 1. Longest Repeating Character Block 
# Definition A repeating character block is a sequence of consecutive identical characters. 
# Task Read a string and print: The character having the longest consecutive block. The length of that block. 
# Example Input aaabccccddbb 
# Example Output Character = c Length = 4

# string=input()
# h_count=0
# dict={}
# for i in range(len(string)-1):
#     if string[i]==string[i+1]:
#         if string[i] not in dict:
#             dict[string[i]]=2
#         else:
#             dict[string[i]]+=1
#     elif string[i]!=string[i+1]:
#         continue
# # print(dict)
# for ch,count in dict.items():
#     if count>h_count:
#         h_count=count
#         key=ch
# print(f'character = {key} lengh = {h_count}')

# 2. Characters Between Two Letters 
# Definition The characters between two occurrences are those lying strictly between them. 
# Task Read a string and a character. Print the number of characters between the first and last occurrence of that character. If the character appears fewer than two times, print -1. 
# Example Input programming g 
# Example Output 5

# string=input()
# ch=input()
# ch_count=0
# count=0
# for i in range(len(string)):
#     if string[i]==ch:
#         first=i
#         count+=1
#         for j in range(i+1,len(string)):
#                 # print(string[j])
#             if string[j]==ch:
#                 last=j
#                 count+=1
#             if string[j]!=ch:
#                 ch_count+=1
# if count<2:
#     print('-1')
# else:
#     print(ch_count)

# 3. Word With Maximum Vowels 
# Definition The vowel count of a word is the number of vowels present in it. 
# Task Read a sentence and print the word containing the maximum number of vowels. If there is a tie, print the first one. 
# Example Input education makes learning enjoyable 
# Example Output education 

# sentence=input()
# h_count=0
# dict={}
# for word in sentence.split():
#     count=0
#     if word not in dict:
#         for ch in word:
#             if ch in 'aeiouAEIOU':
#                 count+=1
#         dict[word]=count
# for word,count in dict.items():
#     if count>h_count:
#         h_count=count
#         key=word
#     elif count==0 :
#         key=sentence.split()[0]
# print(f'{key}')

# 4. Consecutive Alphabet Check 
# Definition Two letters are consecutive if their ASCII values differ by exactly 1. 
# Task Read a string and determine whether every adjacent pair of characters is consecutive. 
# Example Input abcde 
# Example Output Yes 
# def consecutive():
#     s=input()
#     sum=0
#     act_sum=0
#     for i in range(len(s)-1):
#         if ord(s[i])+1==ord(s[i+1]):
#             return True

#     return False
# result=consecutive()
# if result:
#     print('yes')
# else:
#     print('not true')


# 5. Reverse Every Word 
# Definition Each word is reversed individua ly while keeping the order of words unchanged. 
# Task Read a sentence and print the modified sentence. 
# Example Input learn python today 
# Example Output nrael nohtyp yadot 

# sentence=input()
# s1=""
# for word in sentence.split():
#     rev=''
#     for ch in word:
#         rev=ch+rev
#     s1+=' '+rev
# print(s1)

# 6. Most Frequent Vowel 
# Definition The most frequent vowel is the vowel that appears the greatest number of times. 
# Task Read a string and print the vowel with the highest frequency. If there are no vowels, print No Vowels. 
# Example Input communication 
# Example Output o 

# string=input()
# dict={}
# h_count=0
# for i in range(len(string)):
#     if string[i] in 'aeiouAEIOUU':
#         if string[i] not in dict:
#             dict[string[i]]=1
#         else:
#             dict[string[i]]+=1
# print(dict)
# for vowel,count in dict.items():
#     if count>h_count:
#         h_count=count
#         key=vowel
# print(key)

# 7. Equal Vowels and Consonants 
# Definition A string is balanced if it contains the same number of vowels and consonants. 
# Task Read a string containing only alphabets. Print whether it is balanced. 
# Example Input code 
# Example Output Balanced 

# string=input()
# v=0
# c=0
# for ch in string:
#     if ch in 'aeiouuAEIOU':
#         v+=1
#     else:
#         c+=1
# if v==c:
#     print('balanced')
# else:
#     print('not balanced')

# 8. Mirror Half Check 
# Definition The first half of the string should match the reverse of the second half. 
# Task Read an even-length string and determine whether it satisfies this condition. 
# Example Input abccba 
# Example Output Yes 

s=input()
s1=''
s2=''
if len(s)%2==0:
    mid=len(s)//2
    for i in range(mid):
        s1+=s[i]
    for j in range(mid,len(s)):
        s2=s[j]+s2
    if s1==s2:
        print('mirror')
    else:
        print('not mirror')
else:
    print('-1')


# 9. Count Valid Identifier Characters Definition A valid identifier character is: A-Z a-z 0-9 _ (underscore) 
# Task Read a string and count how many valid identifier characters it contains. 
# Example Input user_name@123 
# Example Output 12 

# string=input()

# count=0
# for ch in string:
#     if 'A'<=ch<='Z' or 'a'<=ch<='z' or '0'<=ch<='9' or ch=='_':
#         count+=1
# print(count)


# 10. Smallest Window Containing All Vowels 
# Definition A window is a continuous part of a string. 
# Task Read a string and find the length of the smalest substring that contains a, e, i, o, u at least once each. If no such substring exists, print -1. 
# Example Input aeiobcdfgu 
# Example Output 10

# string=input()
# count=0
# s=''
# for ch in string:
#     if 'a' in s and 'e' in s and 'i' in s and 'o' in s and 'u' in s:
#         break
#     else:
#         s+=ch
#         count+=1
# print(s)
# print(count)