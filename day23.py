# 1. Count Frequency of Each Character 
# Problem Definition: A dictionary can store how many times each character appears. 
# Task: Read a string and print the frequency of every character. 
# Example Input: programming 
# Example Output: p : 1 r : 2 o : 1 g : 2 a : 1 m : 2 i : 1 n : 1 

n=input()
dict={}
for ch in n:
    if ch not in dict:
        dict[ch]=1
    else:
        dict[ch]+=1
print(dict)

# 2. Find the First Repeating Character 
# Problem Definition: The first repeating character appears more than once. 
# Task: Read a string and print the first repeating character. 
# Example Input: datastructure 
# Example Output: a 

n=input()
# h_count=0
for i in range(len(n)):
    count=1
    for j in range(i+1,len(n)):
        if  n[i]==n[j]:
            count+=1
    if count>1:
        print(n[i])
        break


# 3. Group Students by Grade 
# Problem Definition: Store multiple values under the same category. 
# Task: Read student names and grades. Print students grouped by grade. 
# Example Input: 5 Rahul A Anu B Kiran A Meena C Ajay B 
# Example Output: A : Rahul Kiran B : Anu Ajay C : Meena 

n=int(input())
dict={}
for i in range(n):
    key=input()
    value=input()
    dict[key]=value
# print(dict)
dict1={}
for name,grade in dict.items():
    if grade not in dict1:
        dict1[grade]=name
    else:
        dict1[grade]+=' '+name
print(dict1)

# 4. Find the Most Frequent Word 
# Problem Definition: Words may repeat. 
# Task: Read a sentence and print the word with the highest frequency. 
# Example Input: python is easy python is powerful python 
# Example Output: python

string=input()
dict={}
word=''
h_count=0
for ch in string:
    if ch != ' ':
        word+=ch
    elif word != ' ':
        if word not in dict:
            dict[word]=1
        else:
            dict[word]+=1
        word=''
for word,count in dict.items():
    if count>h_count:
        h_count=count
        h_word=word
print(h_word)
# print(dict)
    
# 5. Merge Two Dictionaries 
# Problem Definition: Add values for duplicate keys. 
# Task: Read two dictionaries and merge them. 
# Example Input: A 10, B 20 B 30, C 40 
# Example Output: A : 10 B : 50 C : 40 

dict1={'A':10,'B':20}
dict2={'B':30,'C':40}
for key,value in dict2.items():
    if key not in dict1:
        dict1[key]=value
    else:
        dict1[key]+=value
print(dict1)


# 6. Find Employees Having the Same Salary 
# Problem Definition: Different keys can share the same value. 
# Task: Read employee names and salaries. Print employees having identical salaries. 
# Example Input: Rahul 30000 Anu 25000 Kiran 30000 Meena 40000 
# Example Output: 30000 : Rahul Kiran 

dict={'rahul':30000,'anu':25000,'kiran':30000,'meena':40000}
dict1={}
count=0
for name,sal in dict.items():
    if sal not in dict1:
        dict1[sal]=name
    else:
        dict1[sal]+=' '+name
        count+=1
for sal,name in dict1.items():
    if " " in name:
        print(f"{sal} : {name}")


# 7. Build an Inverted Dictionary 
# Problem Definition: Swap every key with its value. 
# Task: Read a dictionary and create its inverse. 
# Example Input: A : Apple B : Ball C : Cat 
# Example Output: Apple : A Ball : B Cat : C 

data={'a':'apple','b':'ball','c':'cat'}
reverse={}
for letter,word in data.items():
    if word not in reverse:
        reverse[word]=letter
for word in reverse:
    letter=reverse[word]
    print(f"{word}:{letter}",end=' ')
# print(reverse)

# 8. Count the Frequency of Each Number 
# Problem Definition: Count integers using a dictionary. 
# Task: Read N integers and print frequencies. 
# Example Input: 8 4 2 4 1 2 4 5 1 
# Example Output: 1 : 2 2 : 2 4 : 3 5 : 1 

n=int(input())
dictcount={}
for i in range(n):
    num=int(input())
    if num not in dictcount:
        dictcount[num]=1
    else:
        dictcount[num]+=1
for num,count in sorted(dictcount.items()):
        print(f"{num}:{count}",end=' ')

# 9. Find Keys Having the Maximum Value 
# Problem Definition: More than one key can have the maximum value. 
# Task: Read a dictionary and print all keys with the maximum value. 
# Example Input: Math : 95 Science : 90 English : 95 
# Example Output: Math English 

n=int(input())
dict={}
for i in range(n):
    subject=input()
    marks=int(input())
    dict[subject]=marks
# # print(dict)
h_marks=0
for subject,i in dict.items():
    if i>=h_marks:
        h_marks=i
        print(subject,end=' ')


# 10. Build a Phone Directory 
# Problem Definition: Search efficiently using a dictionary. 
# Task: Store names and phone numbers, then search by name. 
# Example Input: 3 Rahul 9876543210 Anu 9123456789 Kiran 9988776655 
# Anu 
# Example Output: 9123456789


n=int(input())
dict={}
for i in range(n):
    name=input()
    phone=int(input())
    dict[name]=phone
# print(dict)
name1=input()
for name,phone in dict.items():
    if name1==name:
        print(phone)