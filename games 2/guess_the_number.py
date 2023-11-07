# useful  info : whenever we import a  fnction , for our needed information we can go to its documention and find out what we need.
# steps 
# first we  have to get the random number  and make it between 1 and x 
# we need to guess the random number untill we guessed the correct number so that means we have to keep looping untill we are right 
# so what do we have so far  the computer is saying ok i got a random number between 1 and x and i can keep guessing untill i guess the right one 
# thats not fun 
# we want the computer to give us some clue bout what's right and what's wrong . so i am gonna use some if  statement to  tell us guess a little high or guess a little low  . 
# now remember that whaen  our guess  is equal to random_number then we gonna hit this if , elif statement but when this number become equal to random number then 
# we will print that i am right at the end of the loop 
# to do the above step we can go at the same indentation of the while loop then say the following. 
import random 


def guess(x):
    random_number=random.randint(1,x)
    guess=0# we are setting gueess to 0 bcz we dont accidentally want guess becomes equal to random_number and since random number is starting from 1 so it can never be 0 .
    
    
    while guess != random_number:
        guess= int(input(f'Guess a number between 1 and {x} :'))
        if guess < random_number :
            print('sorry guess again , too low ')
        elif guess < random_number :
            print('guess again , too  high ')
    print(f'yay , congrats you have guessed the number {random_number} correctly ')

guess(5)

# output 
# Guess a number between 1 and 10 :3
# yay , congrats you have guessed the number 3 correctly 
# Guess a number between 1 and 10 :2
# sorry guess again , too low 
# Guess a number between 1 and 10 :3
# yay , congrats you have guessed the number 3 correctly