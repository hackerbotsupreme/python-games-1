# funtionality ofthe program .
# so what this will do os that it takes a string , and it replaces some words in that string with anther word 
# so this is very easy and straightforward .
def replace_the_word():
    string = ' Hi guys , i am tomi and hi , hi,hi , hi ,hi'
    #lets collect this from the user 
    word_to_replace= input('enter the word to replace :')# word to replace
    word_replacement= input('enter the word replacement :')# word to replace with
    print(string.replace(word_to_replace,word_replacement))
replace_the_word()#calling the function


#enter the word to replace :hi
#enter the word replacement :bye
# Hi guys , i am tomi and bye , bye,bye , bye ,bye
#PS C:\Users\rekha\OneDrive\Desktop\games> 