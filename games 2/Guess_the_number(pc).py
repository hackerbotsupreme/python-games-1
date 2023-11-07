# so we talk about hor the computer guessing our number  ,we can also do the complete 
# inverse of thet function  , we can come up with a secret number and we can have 
# the computer try to guess it .


# steps 
# so i have a secret number and i am not going to tell the computer what the ssecret number is .
# that basically means computer has a range of number s to work with a minimum to a maximum a low and a high. 
import random 


def guess(x):
    random_number=random.randint(1,x)
    guess=0# we are setting gueess to 0 bcz we dont accidentally want guess becomes equal to random_number and since random number is starting from 1 so it can never be 0 .
    
    
    while guess != random_number:
        guess= int(input(f'Guess a number between 1 and {x} :'))
        if guess < random_number :
            print('sorry guess again , too low ')
        elif guess < random_number :
            print('sorry , guess again , too  high ')
    print(f'yay , congrats you have guessed the number {random_number} correctly ')



def computer_guess(x):
    low=1 
    high=x
    feedback=''
    while feedback != "c"  :
        if  low != high:
            guess=random.randint(low,high)
        else:
            guess=low # could also be high b/c low = high 
        feedback=input(f'is {guess} too high (H), too low (L), or correct (C) ?? ').lower()
        if feedback == 'h':
            high=guess-1 
        elif feedback == 'l':
            low=guess+1 
    print(f'yay, the computer guessed your number correctly , {guess}')
            
guess(10) 
computer_guess(10) 


# one case to consider here is random.randint( ) will throe error it chooses  same value for high and low . 
# so what we can do here is 


# output
# Guess a number between 1 and 10 :2 
#sorry guess again , too low 
#Guess a number between 1 and 10 :6
#Guess a number between 1 and 10 :5
#yay , congrats you have guessed the number 5 correctly 
#is 2 too high (H), too low (L), or correct (C) ?? h
#is 1 too high (H), too low (L), or correct (C) ?? l
#Traceback (most recent call last):
#sorry guess again , too low
#Guess a number between 1 and 10 :6
#sorry guess again , too low
#Guess a number between 1 and 10 :7
#yay , congrats you have guessed the number 7 correctlyis 1 too high (H), too low (L), or correct (C) ?? l
#is 5 too high (H), too low (L), or correct (C) ?? l
#is 7 too high (H), too low (L), or correct (C) ?? cyay, the computer guessed your number correctly , 7