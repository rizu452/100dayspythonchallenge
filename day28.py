# 1. Remove All Spaces 
# Definition: A space (' ') is a blank character between words. 
# Task: Remove all spaces from the given string. 
# Example Input: Python Programming 
# Example Output: PythonProgramming 

string=input()
s=''
for ch in string:
    if ch!=' ':
        s+=ch
print(s)


# 2. camelCase to snake_case 
# Definition: camelCase uses capitals after first word; snake_case uses underscores. 
# Task: Convert camelCase to snake_case. 
# Example Input: studentName 
# Example Output: student_name 

string=input()
s=''
for ch in string:
    if 'A'<=ch<='Z':
        l=ord(ch)+32
        s+='_'+chr(l)
    else:
        s+=ch
print(s)


# 3. snake_case to camelCase 
# Definition: snake_case uses underscores; camelCase capitalizes later words. 
# Task: Convert snake_case to camelCase. 
# Example Input: student_name 
# Example Output: studentName 

string=input()
s=''
i=0
while i <len(string):
    if string[i]=='_' and 'a'<=string[i+1]<='z':
        l=ord(string[i+1])-32
        s+=chr(l)
        i+=1
    else:
        s+=string[i]
    i+=1
print(s)

# 4. Uppercase to Lowercase 
# Definition: Uppercase letters are A-Z. 
# Task: Convert all uppercase letters to lowercase. 
# Example Input: HELLO WORLD 
# Example Output: hello world 

string=input()
s=''
for ch in string:
    if ch==' ':
        s+=' '
    else:
        s+=chr(ord(ch)+32)
print(s)


# 5. Lowercase to Uppercase 
# Definition: Lowercase letters are a-z. 
# Task: Convert all lowercase letters to uppercase. 
# Example Input: python 
# Example Output: PYTHON

string=input()
s=''
for ch in string:
    if ch==' ':
        s+=' '
    else:
        s+=chr(ord(ch)-32)
print(s)


# 6. Reverse Every Word 
# Definition: Reverse each word only. 
# Task: Reverse every word. 
# Example Input: Learn Python 
# Example Output: nraeL nohtyP 

sentence=input()
word=''
s=''
for ch in sentence:
    if ch!=' ':
        word=ch+word
    if ch==' ':
        s+=word+' '
        word=''
        continue
s+=word        
print(s)


# 7. Remove Duplicate Characters 
# Definition: Keep first occurrence only. 
# Task: Remove duplicate characters. 
# Example Input: programming
# Example Output: progamin 

word=input()
res=''
for ch in word:
    if ch in res:
        continue
    else:
        res+=ch
print(res)


# 8. Count Vowels and Consonants 
# Definition: Count vowels and consonants. 
# Task: Print both counts. 
# Example Input: Education 
# Example Output: Vowels:5 Consonants:4 

word=input()
vowels='aeiouAEIOU'
v=0
c=0
for ch in word:
    if ch in vowels:
        v+=1
    else:
        c+=1
print(f"vowels={v}")
print(f"consonants={c}")



# 9. Replace Multiple Spaces 
# Definition: Extra spaces should become one. 
# Task: Replace multiple spaces with one. 
# Example Input: Python is fun 
# Example Output: Python is fun 

sentence=input()
s=''
word=''
space=0
for ch in sentence:
    if ch!=' ':
        word+=ch
        space=0
    if ch==' ':
        space+=1
        if space>1:
            continue
        s+=word+' '
        word=''
    continue   
s+=word
print(s)


# 10. Capitalize Every Word 
# Definition: First letter uppercase. 
# Task: Convert to title case. 
# Example Input: welcome to python 
# Example Output: Welcome To Python 

sentence=input()
s=''
word=''
for ch in sentence:
    if ch!=' ':
        if word=='':
            word+=chr(ord(ch)-32)
            # print(word)
        else:
            word+=ch
    else:
        s+=word+' '
        word=''
s+=word
print(s)


# 11. Print Only Digits 
# Definition: Digits are 0-9. 
# Task: Extract digits. 
# Example Input: AB12CD345 
# Example Output: 12345 

string=input()
s=''
for ch in string:
    if '0'<=ch<='9':
        s+=ch
print(s)



# 12. Print Only Alphabets 
# Definition: Letters only. 
# Task: Remove digits and symbols. 
# Example Input: Pyt#123hon! 
# Example Output: Python 

string=input()
s=''
for ch in string:
    if 'A'<=ch<='Z' or 'a'<=ch<='z':
        s+=ch
print(s)



# 13. Count Words 
# Definition: Words separated by spaces. 
# Task: Count words. 
# Example Input: Python is easy to learn 
# Example Output: 5 

sentence=input()
count=0
for i in range(len(sentence)):
    if sentence[i]!=' ':
        if i==0 or sentence[i-1]==' ':
            count+=1
print(count)



# 14. Check Anagram 
# Definition: Same letters, different order.
# Task: Check anagram. 
# Example Input: listen / silent 
# Example Output: Anagram 

s1=input()
s2=input()
is_anagram=True
if len(s1)==len(s2):
    d1={}
    d2={}
    for ch in s1:
        if ch in d1:
            d1[ch]+=1
        else:
                d1[ch]=1
# print(d1)
    for ch in s2:
        if ch in d2:
            d2[ch]+=1
        else:
            d2[ch]=1
for ch in d1:
    if ch not in d2 or d1[ch]!=d2[ch]:
        is_anagram=False
        break
else:
    is_anagram=False
if is_anagram:
    print('anagram')
else:
    print('not anagram')
        

# 15. Find Longest Word 
# Definition: Longest word has most characters. 
# Task: Print longest word. 
# Example Input: I love programming language 
# Example Output: programming

sentence=input()
word=''
c=0
dict={}
for ch in sentence:
    if ch != ' ':
        word+=ch
        c+=1
    else:
        if word not in dict:
            dict[word]=c
        else:
            continue
        word=''
        c=0
if word!='':
    dict[word]=c
print(dict)
h_count=0
longest=''
for word,count in dict.items():
    if count>h_count:
        h_count=count
        longest=word
print(longest)

# 16. Remove All Digits 
# Definition: Digits are numeric chars. 
# Task: Remove all digits. 
# Example Input: Room12Block5 
# Example Output: RoomBlock 

string=input()
s=''
for ch in string:
    if 'A'<=ch<='Z' or 'a'<=ch<='z':
        s+=ch
print(s)

# 17. Move Digits to End 
# Definition: Keep letter order. 
# Task: Move digits to end. 
# Example Input: A1B2C34 
# Example Output: ABC1234 

string=input()
n=''
a=''
for ch in string:
    if '0'<=ch<='9':
        n+=ch
    else:
        a+=ch
print(a+n)


# 18. Toggle Case 
# Definition: Swap upper/lower. 
# Task: Toggle every letter. 
# Example Input: PyThOn 
# Example Output: pYtHoN 

string=input()
s=''
for ch in string:
    if 65<=ord(ch)<=95:
        s+=chr(ord(ch)+32)
    else:
        s+=chr(ord(ch)-32)
print(s)


# 19. Palindrome 
# Definition: Reads same both ways. 
# Task: Check palindrome. 
# Example Input: madam 
# Example Output: Palindrome 

string=input()
rev=''
for ch in string:
    rev=ch+rev
# print(rev)
if string==rev:
    print('palindrome')
else:
    print('not palindrome')



# 20. Compress Characters 
# Definition: Consecutive repeats become char+count. 
# Task: Compress string. 
# Example Input: aaabbccccdd 
# Example Output: a3b2c4d2

string=input()
dict={}
for ch in string:
    if ch in dict:
        dict[ch]+=1
    else:
        dict[ch]=1
# print(dict)
for key,value in dict.items():
    print(f'{key}{value}',end='')


