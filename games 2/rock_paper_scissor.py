import  random
def play():
    user = input('What is your choice ?"r"for rock "p" for paper  "s"  for scissor \n')
    computer = random.choice (["r","p","s"])
    # creating moves in order to determine who wins 
    # we know that r > s , s>p, p>r 
    if user == computer :
        return 'tie '
    if  is_win(user , computer ):
        return 'you won '
    return ' you lost '
    
# here you will notice that i dont have an  if statement and the reason for that is if you have alreasy passed these two on above and after each of cases the function ends right here  or in this case  if you won it ends here the only way we can even reach this line line 11 if we did not go through any of these  which is the same . it just saves you an extra line of space instead of saying else. or if you insist you can write ... 
def is_win ( player , opponent ):
    # returns true  if the player wins 
    # we know that r > s , s>p, p>r 
    if ( player == "r" and opponent == "s") or ( player == "s" and opponent == "p") or ( player == "p" and opponent == "r"):
        return True 
    
print(play())    

        