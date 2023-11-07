import random 
#  as i know that i wanna choose randomluy from the words list so that's why i am going to import random 
# also i want the word list that i just made words.py so i'm gonna say 
from words import words
import string 
def get_valid_word(words):
    word=random.choice(words) # randomly chooses something from the list 
    while '-' in word or ' ' in word:
        word= random.choice(words)
    return word #<-- we are going to uppercase all our leetters  , so this should actually be : return word.upper() 
def hangman():
    word=get_valid_word(words)
    word_letters= set(word) # this will keep track of the words that already been guessed 
    alphabet  = set(string.ascii_uppercase)
    used_letters= set()# it will keep track of the words the user has already guessed 
    
    
    # getting user input 
    while len(word_letters)> 0:
        # letters used 
        print('you have used these lettters', ' '.join(used_letters ))
        # what current word is 
        word_list =[letter if letter in used_letters else '-'for letter in word]
        print('current word:', ' '.join(word_list ))
        
        user_letter= input('Guess a letter:').upper()
        if user_input in alphabet - used_letters :
            used_letters.add(user_letter)
            if user_letter in word_letters:
                word_letters.remove(user_letter)

                
        elif user_letter in used_letters:
            print('you have already used ,please try again ')
        else:
            print('invalid charecter , please try again ')

    # gets  here when len(word_letters ) == 0 
    
user_input= input('type something: ')
print(user_input)
