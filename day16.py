# 1. Swap Two Numbers Without Third Variable Definition: Exchange values of two variables without using an extra variable. Task: Swap using arithmetic operators and bitwise XOR. 
# Example Input: A=15, B=25 
# Example Output: A=25, B=15

def swapping():
    a=int(input("enter a number "))
    b=int(input("enter a number "))
    a=a^b
    b=a^b
    a=a^b
    print(f"a={a}")
    print(f"b={b}")
swapping()




# 2. Convert Seconds Into Hours, Minutes and Seconds 
# Definition: Convert total seconds into time units. 
# Task: Find hours, minutes and remaining seconds. 
# Example Input: Total seconds=7384 
# Example Output: Hours=2, Minutes=3, Seconds=4

def time():
    t_seconds=int(input("enter total seconds "))
    hours=t_seconds//3600
    minutes=t_seconds%3600//60
    seconds=t_seconds%3600%60
    print(f"hours={hours}")
    print(f"minutes={minutes}")
    print(f"seconds={seconds}")
time()




#  Temperature Conversion System 
# Definition: Convert temperature values between Celsius and Fahrenheit. 
# Task: Convert Celsius to Fahrenheit and Fahrenheit to Celsius. 
# Example Input: Celsius=30 
# Example Output: Fahrenheit=86

def temp_conversion():
    temp=int(input("enter temperature "))
    convert=int(input("1.celsius \n2.fahrenheit \n"))
    if convert==1:
        celsius=(temp-32)/1.8
        print(f"celsius={celsius}")
    elif convert==2:
        fahrenheit=(temp*1.8)+32
        print(f"farenheit={fahrenheit}")
temp_conversion()




# 4. Calculate Compound Amount 
# Definition: Compound interest calculates interest on both the original amount and previously earned interest. 
# Task: Calculate final amount using the compound interest formula. 
# Formula: Amount = P × (1 + R/100)^T 
# Where: P = Principal amount 
# R = Rate of interest 
# T = Time period 
# Example Input: Principal = 10000 Rate = 10 Time = 2 years 
# Example Output: Final Amount = 12100
    
def compoundinterset():
    principal=int(input("enter principal amount "))
    rate=int(input("enter rate of interest "))
    time=float(input("enter time "))
    CI=principal*(1+rate/100)**2
    print(f"final amount={CI:.0f}")
compoundinterset()




# 5. Split Bill Among Friends 
# Definition: Divide a total bill equally among people. 
# Task: Find each person's share and remaining amount.
# Example Input: Bill=2455, Friends=5 
# Example Output: Each pays=491, Remaining=0

def sharebill():
    bill=int(input("enter total bill "))
    friends=int(input("enter number of friends"))
    if bill>0 and bill>friends:
        pay=bill//friends
        remaining=bill%friends
        print(f"each pays={pay}")
        print(f"remaining={remaining}")
    else:
        print("enter correct bill")
sharebill()





# 6. Convert Distance Units 
# Definition: Convert kilometers into smaller units. 
# Task: Convert km into meters, centimeters and millimeters. 
# Example Input: Distance=5 km 
# Example Output: Meters=5000, Centimeters=500000, Millimeters=5000000


def distanceconvert():
    distance=int(input("enter distance in km  "))
    meters=distance*1000
    centimeters=meters*100
    millimeters=centimeters*10
    print(f"meters={meters},centimeters={centimeters},millimeters={millimeters}")
distanceconvert()




# 7. Digital Storage Conversion 
# Definition: Convert storage units from GB to smaller units. 
# Task: Convert GB into MB, KB and Bytes. 
# Example Input: Storage=2 GB 
# Example Output: MB=2048, KB=2097152, Bytes=2147483648

def digitalconversion():
    gb=int(input("enter gb "))
    mb=1024*gb
    kb=mb*1024
    bytes=1024*kb
    print(f"mb={mb},kb={kb},bytes={bytes}")
digitalconversion()



# 8. Minimum Currency Notes 
# Definition: Find the number of currency notes required for an amount. 
# Task: Use 500, 200, 100 and 50 denomination notes. 
# Example Input: Amount=1850 
# Example Output: 500 notes=3, 200 notes=1, 100 notes=1, 50 notes=1

def currencynotes():
    amount=int(input("enter total amount"))
    if amount>=500:
        f_h=amount//500
    # print(fivehundred)
        amount=amount%500
    if amount>=200:
        t_h=amount//200
    # print(twohundred)
        amount=amount%200
    if amount>=100:
        hundred=amount//100
    # print(hundred)
        amount=amount%100
    if amount>=50:
        fifty=amount//50
    
    print(f"500 notes={f_h}, 200 notes={t_h}, 100 notes={hundred}, 50 notes={fifty}")
currencynotes()



# 9. Salary Calculation System 
# Definition: Calculate final salary after adding bonus and deducting tax. 
# Task: Calculate the final salary. 
# Example Input: Salary=40000, Bonus=5000, Tax=10% 
# Example Output: Final Salary=40500

def salcalculation():
    sal=int(input("enter your salary "))
    bonus=int(input("enter bonus amount "))
    tax=int(input("enter tax "))
    total_sal=sal+(bonus*(10/100))
    print(total_sal)
salcalculation()



# 10. Travel Time Calculator 
# Definition: Calculate travel duration using distance and speed. 
# Task: Find time for two journeys and total time. Formula: Time = Distance / Speed 
# Example Input: Distance1=120, Speed1=60, Distance2=100, Speed2=50 
# Example Output: Journey1=2 hours, Journey2=2 hours, Total=4 hours

def traveltime():
    distance1=int(input("enter distance1 "))
    speed1=int(input("enter speed1 "))
    journey1=distance1/speed1
    distance2=int(input("enter distance2 "))
    speed2=int(input("enter speed2 "))
    journey2=distance2/speed2
    total=journey1+journey2
    print(f"journey1={journey1:.0f}, journey2={journey2:.0f}, total={total:.0f}")
traveltime()