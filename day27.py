# 1. Rotate Digits Left 
# Definition: Left rotation moves the first digit to the end. 
# Task: Rotate the given number one position to the left. 
# Example Input: 12345 
# Example Output: 23451

num=int(input())
temp=num
digits=1
while temp>=10:
    digits=digits*10
    temp//=10
first=num//digits
rem=num%digits
rotated=(rem*10)+first
print(rotated)

# 2. Rotate Digits Right 
# Definition: Right rotation moves the last digit to the beginning. 
# Task: Rotate the given number one position to the right. 
# Example Input: 12345 
# Example Output: 51234

n=int(input())
temp=n
d=1
while temp>=10:
    d=d*10
    temp//=10
rem=n%10
first=n//10
rotated=(rem*d)+first
print(rotated)

# 3. Swap First and Last Digits 
# Definition: Exchange the first and last digits. 
# Task: Print the modified number. 
# Example Input: 58391 
# Example Output: 18395

n=int(input())
temp=n
d=1
while temp>=10:
    d=d*10
    temp//=10
first=n//d
rem=(n%d)//10
last=n%10
swap=last*d+rem*10+first
print(swap)


# 4. Replace Every Even Digit with 0 
# Definition: Every even digit becomes 0. 
# Task: Transform the number. 
# Example Input: 482763 
# Example Output: 000703

n=int(input())
temp=n
list=[]
while temp>0:
    rem=temp%10
    list=[rem]+list
    temp//=10
for i in range(len(list)):
    if list[i]%2==0:
        list[i]=0
    print(list[i],end='')


# 5. Replace Every Odd Digit with 9 
# Definition: Every odd digit becomes 9. 
# Task: Transform the number. 
# Example Input: 482763 
# Example Output: 492769

n=int(input())
temp=n 
list=[]
while temp>0:
    rem=temp%10
    list=[rem]+list
    temp//=10
for i in range(len(list)):
    if list[i]%2!=0:
        list[i]=9
    print(list[i],end='')


# 6. Reverse Only Even Digits 
# Definition: Reverse only even digits, keep odd digits fixed. 
# Task: Print transformed number. 
# Example Input: 284673 
# Example Output: 684273

n=int(input())
temp=n
list=[]
while temp>0:
    rem=temp%10
    list=[rem]+list
    temp//=10
l1=[]
for i in range(len(list)):
    if list[i]%2==0:
        l1=[list[i]]+l1
j=0
for i in range(len(list)):
    if list[i]%2==0:
        list[i]=l1[j]
        j+=1
print(list)
res=0
for i in list:
    res=res*10+i
print(res)


# 7. Reverse Only Odd Digits 
# Definition: Reverse only odd digits, keep even digits fixed. 
# Task: Print transformed number. 
# Example Input: 583921
# Example Output: 123985

n=int(input())
list=[]
while n>0:
    rem=n%10
    list=[rem]+list
    n//=10
l1=[]
print(list)
for i in range(len(list)):
    if list[i]%2!=0:
        l1=[list[i]]+l1
ind=0
for i in range(len(list)):
    if list[i]%2!=0:
        list[i]=l1[ind]
        ind+=1
# print(list)

res=0
for i in list:
    res=res*10+i
print(res)


# 8. Move All Zeros to the Front 
# Definition: Move every zero to the beginning. 
# Task: Transform the number. 
# Example Input: 5020301 
# Example Output: 0005231

n=int(input())
list=[]
while n>0:
    rem=n%10
    list=[rem]+list
    n//=10
l1=[]
c=0
for i in list:
    if list[i]==0:
        l1+=[0]
for i in list:
    if i!=0:
        l1+=[i]
for i in l1:
    print(i,end='')


# 9. Move All Zeros to the End 
# Definition: Move every zero to the end. 
# Task: Transform the number. 
# Example Input: 5020301 
# Example Output: 5231000 

n=int(input())
list=[]
l1=[]
c=0
while n>0:
    rem=n%10
    list=[rem]+list
    n//=10
for i in list:
    if i==0:
        c+=1
    else:
        l1+=[i]
res=0
for i in l1:
    res=res*10+i
print(res*(10**c))



# 10. Remove Every Alternate Digit 
# Definition: Keep only the 1st, 3rd, 5th... digits. 
# Task: Print resulting number. 
# Example Input: 98765432 
# Example Output: 9753 

n=int(input())
list=[]
while n>0:
    rem=n%10
    list=[rem]+list
    n//=10
l1=[]
for i in range(len(list)):
    if i%2==0:
        l1+=[list[i]]
res=0
for i in l1:
    res=res*10+i
print(res)


# 11. Duplicate Every Digit 
# Definition: Every digit appears twice consecutively. 
# Task: Print transformed number. 
# Example Input: 483 
# Example Output: 448833

n=int(input())
temp=n
rev=0
while n>0:
    rem=n%10
    rev=((rem*10+rem))+rev*100 
    n//=10
res=0
while rev>0:
    r=rev%10
    res=res*10+r
    rev//=10
print(res)



# 12. Insert 0 Between Every Pair of Digits 
# Definition: Insert one zero between consecutive digits. 
# Task: Transform the number. Example Input: 5678 
# Example Output: 5060708 

n=int(input())
rev=0
while n>0:
    rem=n%10
    rev=rem+rev*100  #8   7+800=807  80700+6=80706 8070600+5=8070605
    n//=10
res=0
while rev>0:
    r=rev%10
    res=res*10+r
    rev//=10
print(res)



# 13. Mirror the Number 
# Definition: Append the reverse to itself. 
# Task: Print mirrored number. 
# Example Input: 357 
# Example Output: 357753 

n=int(input())
temp=n
rev=0
c=0
while temp>0:
    r=temp%10
    c+=1
    rev=rev*10+r
    temp//=10
res=(n*10**c)+rev
print(res)



# 14. Compress Consecutive Digits 
# Definition: Replace repeated consecutive digits with digit+count.
# Task: Compress the number. 
# Example Input: 11122333344 
# Example Output: 13224342 

n=int(input())
prev=-1
c=0
list=[]
while n>0:
    r=n%10
    if r==prev:
        c+=1
    else:
        if prev!=-1:
            list=[prev*10+c]+list
        prev=r
        c=1
    n//=10
list=[prev*10+c]+list
res=0
for i in list:
    res=i+res*100
print(res)


# 15. Expand the Number 
# Definition: Write each digit according to its place value. 
# Task: Print expanded form. 
# Example Input: 5078 
# Example Output: 5000 + 70 + 8 

n=int(input())
d=1
res=0
list=[]
while n>0:
    r=n%10
    res=r*d
    list=[res]+list
    n//=10
    d*=10
for i in list:
    print(f"{i}+",end=' ')



# 16. Print Digits in Wave Order 
# Definition: First,last,second,second-last... 
# Task: Rearrange digits. 
# Example Input: 123456 
# Example Output: 162534

n=int(input())
list=[]
while n>0:
    r=n%10
    list=[r]+list
    n//=10
first=0
last=len(list)-1
l1=[]
while first<=last:
    l1+=[list[first]]
    if first!=last:
        l1+=[list[last]]
    first+=1
    last-=1
print(l1)


# 17. Reverse Digits in Pairs 
# Definition: Reverse every two consecutive digits. 
# Task: Transform the number. 
# Example Input: 123456 
# Example Output: 214365 

n=int(input())
rev=0
while n>=10:
    r=n%100
    rev=(r+10-1)+rev*100
    n//=100
res=0
print(rev)
while rev>=10:
    r=rev%100
    print(r)
    res=r+res*100
    rev//=100
print(res)


# 18. Replace Every Digit with Its Complement to 9 
# Definition: Replace d with 9-d. Task: Transform the number. 
# Example Input: 2845 
# Example Output: 7154 

n=int(input())
rev=0
while n>0:
    r=n%10
    rev=rev*10+(9-r)
    n//=10
res=0
while rev>0:
    r=rev%10
    res=res*10+r
    rev//=10
print(res)



# 19. Sort Even and Odd Digits Separately 
# Definition: Sort evens among evens and odds among odds. 
# Task: Print modified number. 
# Example Input: 86427531 
# Example Output: 24613578

n=int(input())
temp=n
e=[]
o=[]
list=[]
while n>0:
    r=n%10
    list=[r]+list
    n//=10
# print(l)
while temp>0:
    r=temp%10
    if r%2==0:
        e+=[r]
    else:
        o+=[r]
    temp//=10
l=len(e)
for i in range(len(e)):
    for j in range(l-i-1):
        if e[j]>e[j+1]:
            e[j],e[j+1]=e[j+1],e[j]
for i in range(len(o)):
    for j in range(len(o)-i-1):
        if o[j]>o[j+1]:
            o[j],o[j+1]=o[j+1],o[j]
even=0
odd=0
res=[]
for i in list:
    if i%2==0:
        res=res+[e[even]]
        even+=1
    else:
        res=res+[o[odd]]
        odd+=1
res1=0
for i in res:
    res1=res1*10+i
print(res1)
# print(e)
# print(o)
# print(res)


# 20. Interleave Two Halves 
# Definition: Split into equal halves and alternate digits. 
# Task: Rearrange digits. 
# Example Input: 12345678 
# Example Output: 15263748

n=int(input())
list=[]
while n>0:
    r=n%10
    list=[r]+list
    n//=10
l=len(list)
mid=len(list)//2
l1=[]
l2=[]
for i in range(mid):
    l1+=[list[i]]
for i in range(mid,len(list)):
    l2+=[list[i]]
res=[]
for i in range(mid):
    res+=[l1[i]]
    res+=[l2[i]]
result=0
for i in res:
    result=result*10+i
print(result)