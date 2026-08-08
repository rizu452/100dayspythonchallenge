import random
user_count=0
python_count=0
score=int(input('enter the score to win the game'))
while user_count<score and python_count<score:
    user=input('select rock or paper or scissors :')
    choice=['rock','paper','scissors']
    dice=random.choice(choice)
    print(f'python choosed {dice}')
    if user=='rock' and dice=='paper':
        python_count+=1
        print(f'python got point {python_count}')
    elif user=='paper' and dice=='scissors':
        python_count+=1
        print(f'python got point {python_count}')
    elif user=='scissors' and dice=='rock':
        python_count+=1
        print(f'python got point {python_count}')
    elif user==dice:
        print('each got tie')
    else:
        user_count+=1
        print(f'user got point {user_count}')
if user_count==score:
    print(f'user won first with {user_count}')
else:
    print(f'python won first with {python_count}')