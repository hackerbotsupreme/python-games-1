# random password generator program 
# steps 
# ask the user if they want to genetrate a password or not 
# if yes , ask for the password length 
# generate  and print password 
# if no ,  exit the program 
import string 
import random 


charecters= list( string.ascii_letters + string.digits + '!@#$%^&*()' )



def generate_password():
    password_length=int(input('how long the password you would like to be :')) 

    
    random.shuffle(charecters)

    password=[]

    for x in range(password_length):
        password.append(random.choice(charecters))

    random.shuffle(password)

    
    
    password=''.join(password)
    print(password)

    
    
option=input('do you want to generate a password ? (Yes/No)  :')

if option=='Yes':
    generate_password()
elif option=='No':
    print('program ended')
    quit()
else:
    print('invalid input, please enter Yes or No ')
    quit()
    
# remember that quit() function tells to quit from the total function not from the loop okkkkkkkkkkkkkkkk
# output
# PS C:\Users\rekha\OneDrive\Desktop\games> & C:/Users/rekha/AppData/Local/Microsoft/WindowsApps/python3.10.exe c:/Users/rekha/OneDrive/Desktop/games/Rndom_password_generator.py
#do you want to generate a password ? (Yes/No)  :Yes
#hoe long the password you would like to be :17
#vgizYX5YW9wHQyCdX
#PS C:\Users\rekha\OneDrive\Desktop\games> & C:/Users/rekha/AppData/Local/Microsoft/WindowsApps/python3.10.exe c:/Users/rekha/OneDrive/Desktop/games/Rndom_password_generator.py
#do you want to generate a password ? (Yes/No)  :yes
#invalid input, please enter Yes or No 
#PS C:\Users\rekha\OneDrive\Desktop\games> & C:/Users/rekha/AppData/Local/Microsoft/WindowsApps/python3.10.exe c:/Users/rekha/OneDrive/Desktop/games/Rndom_password_generator.py
#do you want to generate a password ? (Yes/No)  :Yes
#hoe long the password you would like to be :23
#VLQsV9ht#oLtJNs5TwBm!Eh
#PS C:\Users\rekha\OneDrive\Desktop\games> & C:/Users/rekha/AppData/Local/Microsoft/WindowsApps/python3.10.exe c:/Users/rekha/OneDrive/Desktop/games/Rndom_password_generator.py
#do you want to generate a password ? (Yes/No)  :No
#program ended
#PS C:\Users\rekha\OneDrive\Desktop\games> 
