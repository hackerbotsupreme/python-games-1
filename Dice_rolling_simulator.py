# Dice_rollong_simulator program 
# steps 
# Roll the dice? (Yes/No)
# import random then fuction to roll the dice 
# create a dictionary that will have the drawings of the dice 

import random



def roll_dice():
    dice_drawing = {
        1: (
            "-----",
            "|   |",
            "| o |",
            "|   |",
            "-----",
        ),
        2: (
            "-----",
            "|o  |",
            "|   |",
            "|  o|",
            "-----",
        ),
        3: (
            "-----",
            "|o  |",
            "| o |",
            "|  o|",
            "-----",
        ),
        4: (
            "-----",
            "|o o|",
            "|   |",
            "|o o|",
            "-----",
        ),
        5: (
            "-----",
            "|o o|",
            "| o |",
            "|o o|",
            "-----",
        ),
        6: (
            "-----",
            "|o o|",
            "|o o|",
            "|o o|",
            "-----",
        ),

    }
   
    roll=input('roll the dice ? (Yes/No )')
    while roll.lower()== "yes".lower():
        dice1=random.randint(1,6)
        dice2=random.randint(1,6)
        print('dice rolled :{} and {}'.format(dice1,dice2) )# what is the difference between decimel and floating poiint numbers ?
        print('\n'.join(dice_drawing[dice1]))#  there is no inherent difference between a "decimal number" and a "floating-point number." Both terms can be used interchangeably to refer to numbers with a fractional part. 
        print('\n'.join(dice_drawing[dice2]))# The float data type in Python represents floating-point numbers and adheres to the IEEE 754 standard. It has a finite precision, which means that certain decimal numbers cannot 
        roll= input('roll again?((Yes/No )')
roll_dice()

# output untill now
#dice rolled :1 and 1
#roll again?((Yes/No )yes
#dice rolled :5 and 2
#roll again?((Yes/No )yes
#dice rolled :4 and 2
#roll again?((Yes/No )yes
#dice rolled :3 and 1
#roll again?((Yes/No )


# then we gonna add the pictures and gonna add the lines from -- 
#13 to 54 , 67 and 68
# output
#roll the dice ? (Yes/No )yes
#dice rolled :1 and 1
#-----
#|   |
#| o |
#|   |
#-----
#-----
#|   |
#| o |
#|   |
#-----
#roll again?((Yes/No )yes
#dice rolled :3 and 3
#-----
#|o  |
#| o |
#|  o|
#-----
#-----
#|o  |
#| o |
#|  o|
#-----
#roll again?((Yes/No )yes
#dice rolled :6 and 2
#-----
#|o o|
#|o o|
#|o o|
#-----
#-----
#|o  |
#|   |
#|  o|
#-----
#roll again?((Yes/No )cls
#PS C:\Users\rekha\OneDrive\Desktop\games>