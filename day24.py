# 1. Find the First Unique Word 
# Problem Definition: A unique word appears exactly once in a sentence. 
# Task: Read a sentence and print the first word that occurs only once. 
# Example Input: cat dog cat fish dog bird 
# Example Output: fish 

string=input()
dict_count={}
word=''
if string[-1]!=' ':
    string+=' '
for ch in string:
    if ch!=' ':
        word+=ch
    elif word !=' ':
        if word not in dict_count:
            dict_count[word]=1
        else:
            dict_count[word]+=1
        word=''
for word,count in dict_count.items():
    if count==1:
        print(f"{word}")
        break
# print(dict_count)



# 2. Student Marks Analyzer 
# Problem Definition: Store students and their marks in a dictionary. 
# Task: Read names and marks of N students. Print highest and lowest. 
# Example Input: 4 Rahul 85 Anu 92 Kiran 78 Meena 90 
# Example Output: Highest : Anu Lowest : Kiran 

n=int(input())
dict={}
highest=float('-inf')
lowest=float('inf')
for i in range(n):
    name=input()
    marks=int(input())
    dict[name]=marks
# print(dict)
for name,mark in dict.items():
    if mark>highest:
        highest=mark
        key=name
    if mark<lowest:
        lowest=mark
        key1=name
print(f"Highest : {key}")
print(f"Lowest : {key1}")




# 3. Find Missing Alphabets 
# Problem Definition: Determine which lowercase letters are absent. 
# Task: Read a string and print missing lowercase letters. 
# Example Input: abcdefxyz 
# Example Output: g h i j k l m n o p q r s t u v w 

string=input()
alphabet=''
for i in range(97,123):
    alphabet+=chr(i)
    # print(alphabet,end=' ')
for alpha in alphabet:
        if alpha not in string:
            print(alpha,end=' ')


# 4. Find Common Words Between Two Sentences 
# Problem Definition: Some words may appear in both sentences. 
# Task: Read two sentences and print common words. 
# Example Input: python is easy learning python is fun 
# Example Output: python is 

sent1=input()+' '
sent2=input()+' '
dict1={}
word=''
for ch in sent1:
    if ch!=' ':
        word+=ch
    else:
        if word!=' ':
            if word not in dict1:
                dict1[word]=1
            dict1[word]+=1
        word=''
for ch in sent2:
    if ch!=' ':
        word+=ch
    else:
        if word in dict1:
            print(word,end=' ')
        word=''


# 5. Print Words in Descending Frequency 
# Problem Definition: Order words by frequency. 
# Task: Read a sentence and print frequencies.
# Example Input: red blue red green blue red 
# Example Output: red : 3 blue : 2 green : 1 

sentence=input()
dict={}
for word in sentence.split():
    if word not in dict:
        dict[word]=1
    else:
        dict[word]+=1
sorted_list=sorted(dict.items(), key=lambda items:items[1] ,reverse=True)
for word,count in sorted_list:
    print(f"{word} : {count}",end=' ')

# 6. Detect Duplicate Values 
# Problem Definition: Different keys may share the same value. 
# Task: Read a dictionary and print duplicate values. 
# Example Input: A 10 B 20 C 10 D 40 E 20 
# Example Output: 10 20 

n=int(input())
dict={}
for i in range(n):
    key=input()
    value=int(input())
    dict[key]=value
# print(dict)
dict1={}
for key,value in dict.items():
    if value not in dict1:
        dict1[value]=key
    else:
        print(f"{value}",end=' ')

# 7. Count Words Starting with Each Alphabet 
# Problem Definition: Group words by first letter. 
# Task: Read a sentence and count words by first letter. 
# Example Input: apple ant ball bat banana cat 
# Example Output: a : 2 b : 3 c : 1 

sentence=input()
dict={}
for word in  sentence.split():
    if word[0] not in dict:
        dict[word[0]]=1
    else:
        dict[word[0]]+=1
print(dict)

#8. Build a Character Position Dictionary 
#Problem Definition: Store positions of each character. 
#Task: Read a string and print positions. 
#Example Input: banana 
#Example Output: b : 0 a : 1 3 5 n : 2 4 

string=input()
dict={}
for i in range(len(string)):
    if string[i] not in dict:
        dict[string[i]]=str(i)
    else:
        dict[string[i]]+=" "+str(i)
print(dict)
    


#9. Find the Longest Word(s) 
#Problem Definition: More than one longest word may exist. 
#Task: Read a sentence and print every longest word.
#Example Input: python programming java development 
#Example Output: programming development 

sentence=input()
dict={}
h_count=0
for word in sentence.split():
    count=0
    if word not in dict:
        for ch in word:
            count+=1
        if count>h_count:
            h_count=count
        dict[word]=count
    else:
        continue
print(dict)
for word,count in dict.items():
    if count==h_count:
        print(f"{word}")


#10. Mini Inventory Manager 
#Problem Definition: Search products using a dictionary. 
#Task: Read products then search for one. 
#Example Input: 3 Pen 20 Book 15 Pencil 40 Book 
#Example Output: 15

n=int(input())
dict={}
for i in range(n):
    product=input("enter product ")
    cost=int(input("enter cost "))
    dict[product]=cost
search=input()
for product,cost in dict.items():
    if search==product:
        print(f"the cost of {search} is {cost}")